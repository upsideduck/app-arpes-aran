from PySide import QtCore, QtGui
from helper.constants import *
import numpy as np
import ext.pyqtgraph as pg
import ext.pyqtgraph.opengl as gl

class standardPlot(QtGui.QWidget):

	__angle=0

	# Setters and Getters
	# Angle property
	def getAngle(self):
		return self.__angle

	def setAngle(self, d):
		if self.__angle == 0 and d != 0:
			self.mainPlotItem.getAxis('bottom').setStyle(showValues=False)
			self.mainPlotItem.getAxis('left').setStyle(showValues=False)
			self.ROIPlotItemBottomWidget.getAxis('bottom').setStyle(showValues=False)
			self.ROIPlotItemRightWidget.getAxis('left').setStyle(showValues=False)
		if d == 0:
			self.mainPlotItem.getAxis('bottom').setStyle(showValues=True)
			self.mainPlotItem.getAxis('left').setStyle(showValues=True)
			self.ROIPlotItemBottomWidget.getAxis('bottom').setStyle(showValues=True)
			self.ROIPlotItemRightWidget.getAxis('left').setStyle(showValues=True)

		self.__angle = d
		
	def delAngle(self):
		del self.__angle


	angle = property(getAngle,setAngle,delAngle)

	def __init__(self, showHistogram = False, parent = None):
		super(standardPlot, self).__init__()
		
		self.currentIndex = 0
		self.zAxis = None
		self.cData = None
		self.levelMin = 0
		self.levelMax = 4000
		self.autoLevel = True
		self.nameAxisZ = ""
		self.roiList = [[],[],[]]

		self.initUI(showHistogram)


	def initUI(self, showHistogram):
		grid = QtGui.QGridLayout()
		self.setLayout(grid)
		self.view = pg.GraphicsLayoutWidget()
		grid.addWidget(self.view)

		# Init all items for widget
		self.mainPlotItem = pg.PlotItem()
		self.ROIPlotItemBottomWidget = pg.PlotWidget()
		self.ROIPlotItemBottom = self.ROIPlotItemBottomWidget.getPlotItem()
		self.ROIPlotItemRightWidget = pg.PlotWidget() 
		self.ROIPlotItemRight = self.ROIPlotItemRightWidget.getPlotItem()
		self.image = pg.ImageItem()
		self.hist = pg.HistogramLUTWidget()

		# Setup histogram
		self.hist.item.setImageItem(self.image)
		self.hist.item.autoHistogramRange()
		self.hist.item.axis.setStyle(showValues=False)
		self.hist.setMinimumWidth(80)
		self.hist.setMaximumWidth(80)

		# Setup ROI
		self.ROIPlotItemRightWidget.setMaximumWidth(100)
		self.ROIPlotItemRightWidget.setMinimumWidth(100)
		self.ROIPlotItemRightWidget.hide()
		grid.addWidget(self.ROIPlotItemRightWidget,0,1)
		self.ROIPlotItemBottomWidget.setMaximumHeight(100)
		self.ROIPlotItemBottomWidget.setMinimumHeight(100)
		self.ROIPlotItemBottomWidget.hide()
		grid.addWidget(self.ROIPlotItemBottomWidget, 1, 0)
		

		# Layout items into PQG widget
		self.view.addItem(self.mainPlotItem,row=1, col=1)
		if showHistogram:
			grid.addWidget(self.hist,0,2)
		self.mainPlotItem.addItem(self.image)
		grid.setColumnStretch(0,10)
		grid.setRowStretch(0,10)

		
	def setData(self, cData, zAxis=None, metaDataOutput=None):
		if cData != None:
			self.cData = cData
		else:
			return

		if zAxis:
			self.setZAxis(zAxis)
		elif len(self.cData.data.shape) > 2:
			self.thirdDim()
			self.setZAxis(2)
		else:
			self.setZAxis(None)

		self.updateImage()

		self.updateImageTransform()
		#self.image.scale(self.scaleAxisHorizontal,self.scaleAxisVertical)
		#self.image.setPos(self.posOrigoAxisHorizontal,self.posOrigoAxisVertical)
		self.mainPlotItem.setLabel('bottom',text=self.nameAxisHorizontal)
		self.mainPlotItem.setLabel('left',text=self.nameAxisVertical)
		self.ROIPlotItemRight.setLabel('bottom', text="I")
		self.mainPlotItem.invertY(False)
		ratio = (self.lengthAxisVertical/self.lengthAxisHorizontal)/(self.scaleAxisHorizontal/self.scaleAxisVertical)
		self.mainPlotItem.getViewBox().setAspectLocked(lock=True,ratio=ratio)

		if metaDataOutput:
			metaDataOutput.setText(self.cData.root.NXentry[self.cData.entryId].tree)



	def thirdDim(self):
		grid = self.layout()
		# Slider
		self.thirdDimSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
		self.thirdDimNameLbl = QtGui.QLabel()
		self.thirdDimValueQSBox = QtGui.QDoubleSpinBox()
		self.thirdDimValueQSBox.setDecimals(4)
		thirdDimLayout = QtGui.QHBoxLayout()
		thirdDimLayout.addWidget(self.thirdDimNameLbl)
		thirdDimLayout.addWidget(self.thirdDimSlider)
		thirdDimLayout.addWidget(self.thirdDimValueQSBox)

		# Autolevel
		self.autoLevelCheckBox = QtGui.QCheckBox("Auto Level")
		self.autoLevelCheckBox.stateChanged[int].connect(self.on_autoHistLevel)
		if self.autoLevel:
			self.autoLevelCheckBox.setCheckState(QtCore.Qt.Checked)
		autoLevelLayout = QtGui.QVBoxLayout()
		spacerAL = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
		autoLevelLayout.addWidget(self.hist)
		autoLevelLayout.addWidget(self.autoLevelCheckBox)
		autoLevelLayout.addItem(spacerAL)

		grid.addLayout(thirdDimLayout,2,0,1,3)
		grid.addLayout(autoLevelLayout,0,2)

	def updateImage(self):
		if not self.cData:
			return 

		image = self.getProcessedImage()
	
		self.image.updateImage(image)

		if self.autoLevel:
			self.hist.region.setRegion([self.levelMin,self.levelMax])

		if self.roiList[CONST_ROI_BOTH_LIST]:
			self.on_updateBothRoiPlot()
		else:
			if self.roiList[CONST_ROI_HOR_LIST]:
				self.on_updateHorRoiPlot()
			if self.roiList[CONST_ROI_VER_LIST]:
				self.on_updateVerRoiPlot()


	## ROI functions
	#
	#
	#
	def addSingleLineROI(self,plot):
		centerPoint = self.centerPoint()
		if plot == self.ROIPlotItemBottomWidget:
			initPos = ([self.posOrigoAxisHorizontal,centerPoint[1]],[self.posOrigoAxisHorizontal+self.lengthAxisHorizontal*self.scaleAxisHorizontal,centerPoint[1]])
			bounds = [self.posOrigoAxisVertical,self.posOrigoAxisVertical+self.lengthAxisVertical*self.scaleAxisVertical]
			roiListID = CONST_ROI_HOR_LIST
			updatePlot = self.on_updateHorRoiPlot
		elif plot == self.ROIPlotItemRightWidget:
			bounds = [self.posOrigoAxisHorizontal,self.posOrigoAxisHorizontal+self.lengthAxisHorizontal*self.scaleAxisHorizontal]
			#initPos=([self.posOrigoAxisVertical,centerPoint[0]],[self.posOrigoAxisVertical+self.lengthAxisVertical*self.scaleAxisVertical,centerPoint[0]])
			initPos=([centerPoint[0],self.posOrigoAxisVertical],[centerPoint[0],self.posOrigoAxisVertical+self.lengthAxisVertical*self.scaleAxisVertical])
			roiListID = CONST_ROI_VER_LIST
			updatePlot = self.on_updateVerRoiPlot
		else:
			return

		angle = 0
		roi = SingleLineROI(positions=initPos, scaleCenter=centerPoint)
		roi.setPen(QtGui.QPen(QtGui.QColor(255, 255, 0, 200)))
		roi.setZValue(1)
		self.roiList[roiListID].append(roi)
		self.mainPlotItem.addItem(roi)
		roi.sigRegionChanged.connect(updatePlot)
		plot.show()
		updatePlot()

	def addRectROI(self):
		width = self.lengthAxisHorizontal*self.scaleAxisHorizontal/5
		height = self.lengthAxisVertical*self.scaleAxisVertical/5

		roi = pg.RectROI([self.posOrigoAxisHorizontal+self.lengthAxisHorizontal*self.scaleAxisHorizontal/2-width/2,self.posOrigoAxisVertical+self.lengthAxisVertical*self.scaleAxisVertical/2-height/2],[width,height], centered=True, sideScalers=True)
		roi.setPen(QtGui.QPen(QtGui.QColor(255, 255, 0, 200)))
		roi.setZValue(1)
		self.roiList[CONST_ROI_BOTH_LIST].append(roi)
		self.mainPlotItem.addItem(roi)
		roi.sigRegionChanged.connect(self.on_updateBothRoiPlot)
		self.ROIPlotItemRightWidget.show()
		self.ROIPlotItemBottomWidget.show()
		self.on_updateBothRoiPlot()

	def removeROI(self,roi):
		if roi in self.roiList[CONST_ROI_HOR_LIST]:
			if type(roi) is SingleLineROI:
				roi.sigRegionChanged.disconnect()
			else:
				print "Could not remove ROI plot"
				return 
			self.roiList[CONST_ROI_HOR_LIST].remove(roi)
			self.mainPlotItem.removeItem(roi)
			roi = None
			self.on_updateHorRoiPlot()

		if roi in self.roiList[CONST_ROI_VER_LIST]:
			if type(roi) is SingleLineROI:
				roi.sigRegionChanged.disconnect()
			else:
				print "Could not remove ROI plot"
				return 
			self.roiList[CONST_ROI_VER_LIST].remove(roi)
			self.mainPlotItem.removeItem(roi)
			roi = None
			self.on_updateVerRoiPlot()

		if roi in self.roiList[CONST_ROI_BOTH_LIST]:
			if type(roi) is pg.RectROI:
				roi.sigRegionChanged.disconnect()
			else:
				print "Could not remove ROI plot"
				return 
			self.roiList[CONST_ROI_BOTH_LIST].remove(roi)
			self.mainPlotItem.removeItem(roi)
			roi = None
			self.on_updateBothRoiPlot()

		if len(self.roiList[CONST_ROI_HOR_LIST]) == 0 and len(self.roiList[CONST_ROI_BOTH_LIST]) == 0:
			self.ROIPlotItemBottomWidget.hide()

		if len(self.roiList[CONST_ROI_VER_LIST]) == 0 and len(self.roiList[CONST_ROI_BOTH_LIST]) == 0:
			self.ROIPlotItemRightWidget.hide()
		
	# Slots
	# 
	#


	def on_updateHorRoiPlot(self):
		self.ROIPlotItemBottom.clear()
		for roi in self.roiList[CONST_ROI_HOR_LIST]:
			if type(roi) is SingleLineROI: 
				pos = roi.pos()
				size = roi.size()

				xStart = self.posOrigoAxisHorizontal+pos[0]+(1-size[0])*self.lengthAxisHorizontal*self.scaleAxisHorizontal/2
				xEnd = xStart+self.lengthAxisHorizontal*self.scaleAxisHorizontal*size[0]
				y = roi.getArrayRegion(np.asarray(self.getProcessedImage()), self.image, axes=(0,1))
				x = np.linspace(xStart,xEnd,len(y))
				self.ROIPlotItemBottom.plot(x=x, y=y, clear=False, pen='k')
			else:
				return

		for roi in self.roiList[CONST_ROI_BOTH_LIST]:
			if type(roi) is pg.RectROI:
				selected = roi.getArrayRegion(np.asarray(self.getProcessedImage()), self.image,axes=(0,1))
				pos = roi.pos()
				size = roi.size()
				y = selected.mean(axis=1)
				x = np.linspace(pos[0],pos[0]+size[0],len(y))

				self.ROIPlotItemBottom.plot(y=y, x=x, clear=False, pen='r')
			else:
				return

	def on_updateVerRoiPlot(self):
		self.ROIPlotItemRight.clear()
		for roi in self.roiList[CONST_ROI_VER_LIST]:
			if type(roi) is SingleLineROI: 
				pos = roi.pos()
				size = roi.size()
				points = roi.listPoints()

				xStart = pos[1]+points[0][1]
				xEnd = xStart+self.lengthAxisVertical*self.scaleAxisVertical*size[1]
				y = roi.getArrayRegion(np.asarray(self.getProcessedImage()), self.image, axes=(0,1))
				x = np.linspace(xStart,xEnd,len(y))
				self.ROIPlotItemRight.plot(x=y, y=x, clear=False, pen='k')
			else:
				return

		for roi in self.roiList[CONST_ROI_BOTH_LIST]:
			if type(roi) is pg.RectROI:
				selected = roi.getArrayRegion(np.asarray(self.getProcessedImage()), self.image,axes=(0,1))
				pos = roi.pos()
				size = roi.size()
				y = selected.mean(axis=0)
				x = np.linspace(pos[1],pos[1]+size[1],len(y))
				self.ROIPlotItemRight.plot(y=x, x=y, clear=False, pen='r')
			else:
				return


	def on_updateBothRoiPlot(self):
		self.on_updateHorRoiPlot()
		self.on_updateVerRoiPlot()

	def on_thirdDimSliderMoved(self,val):
		self.setCurrentIndex(val)

		step = ((self.axisZarr[-1]-self.axisZarr[0])/(len(self.axisZarr)-1))
		current = self.thirdDimValueQSBox.value()-self.axisZarr[0]

		if int(current/step) != self.thirdDimSlider.value():
			self.thirdDimValueQSBox.setValue(self.axisZarr[val])

	def on_thirdDimQSBoxChanged(self, val):
		step = ((self.axisZarr[-1]-self.axisZarr[0])/(len(self.axisZarr)-1))
		current = val-self.axisZarr[0]
		
		if int(current/step) != self.thirdDimSlider.value():
			self.thirdDimSlider.setValue(int(current/step))

	def on_autoHistLevel(self,state):
		if state == QtCore.Qt.Checked:
			self.autoLevel = True
		elif state == QtCore.Qt.Unchecked:
			self.autoLevel = False
		else:
			pass
		self.updateImage()

	def getProcessedImage(self):
		image = np.asarray(self.cData.data)


		if len(image.shape) == 2:
			procImage = image
		elif len(image.shape) == 3:
			if self.zAxis == 0:
				procImage = image[self.currentIndex,:,:]
			elif self.zAxis == 1:
				procImage = image[:,self.currentIndex,:]
			elif self.zAxis == 2:
				procImage = image[:,:,self.currentIndex]
			else:
				return None
		else:
			return None 

		self.levelMin, self.levelMax = list(map(float, self.quickMinMax(procImage)))

		return procImage

	def setZAxis(self,index):
		self.zAxis = index
		if self.zAxis == 0:
			self.scaleAxisHorizontal = float((self.cData.axis2[-1]-self.cData.axis2[0])/len(self.cData.axis2))
			self.scaleAxisVertical = float(self.cData.axis3[-1]-self.cData.axis3[0])/len(self.cData.axis3)
			self.lengthAxisHorizontal = len(self.cData.axis2)
			self.lengthAxisVertical = len(self.cData.axis3)
			self.lengthAxisZ = len(self.cData.axis1)
			self.posOrigoAxisHorizontal = float(self.cData.axis2[0])
			self.posOrigoAxisVertical = float(self.cData.axis3[0])
			self.nameAxisHorizontal = self.cData.axis2name
			self.nameAxisVertical = self.cData.axis3name
			self.nameAxisZ = self.cData.axis1name
			self.axisZarr = np.asarray(self.cData.axis1)
		elif self.zAxis == 1:
			self.scaleAxisHorizontal = float((self.cData.axis1[-1]-self.cData.axis1[0])/len(self.cData.axis1))
			self.scaleAxisVertical = float(self.cData.axis3[-1]-self.cData.axis3[0])/len(self.cData.axis3)
			self.lengthAxisHorizontal = len(self.cData.axis1)
			self.lengthAxisVertical = len(self.cData.axis3)
			self.lengthAxisZ = len(self.cData.axis2)
			self.posOrigoAxisHorizontal = float(self.cData.axis1[0])
			self.posOrigoAxisVertical = float(self.cData.axis3[0])
			self.nameAxisHorizontal = self.cData.axis1name
			self.nameAxisVertical = self.cData.axis3name
			self.nameAxisZ = self.cData.axis2name
			self.axisZarr = np.asarray(self.cData.axis2)
		elif self.zAxis == 2:
			self.scaleAxisHorizontal = float((self.cData.axis1[-1]-self.cData.axis1[0])/len(self.cData.axis1))
			self.scaleAxisVertical = float(self.cData.axis2[-1]-self.cData.axis2[0])/len(self.cData.axis2)
			self.lengthAxisHorizontal = len(self.cData.axis1)
			self.lengthAxisVertical = len(self.cData.axis2)
			self.lengthAxisZ = len(self.cData.axis3)
			self.posOrigoAxisHorizontal = float(self.cData.axis1[0])
			self.posOrigoAxisVertical = float(self.cData.axis2[0])
			self.nameAxisHorizontal = self.cData.axis1name
			self.nameAxisVertical = self.cData.axis2name
			self.nameAxisZ = self.cData.axis3name
			self.axisZarr = np.asarray(self.cData.axis3)
		else: 
			self.scaleAxisHorizontal = float((self.cData.axis1[-1]-self.cData.axis1[0])/len(self.cData.axis1))
			self.scaleAxisVertical = float(self.cData.axis2[-1]-self.cData.axis2[0])/len(self.cData.axis2)
			self.lengthAxisHorizontal = len(self.cData.axis1)
			self.lengthAxisVertical = len(self.cData.axis2)
			self.posOrigoAxisHorizontal = float(self.cData.axis1[0])
			self.posOrigoAxisVertical = float(self.cData.axis2[0])
			self.nameAxisHorizontal = self.cData.axis1name
			self.nameAxisVertical = self.cData.axis2name
			return


		self.thirdDimSlider.setRange(0,self.lengthAxisZ-1)
		self.thirdDimSlider.valueChanged[int].connect(self.on_thirdDimSliderMoved)
		self.thirdDimNameLbl.setText(self.nameAxisZ)
		self.thirdDimValueQSBox.setRange(self.axisZarr[0],self.axisZarr[-1])
		self.thirdDimValueQSBox.setSingleStep((self.axisZarr[-1]-self.axisZarr[0])/(self.lengthAxisZ-1))
		self.thirdDimValueQSBox.valueChanged.connect(self.on_thirdDimQSBoxChanged)
		self.thirdDimValueQSBox.setValue(self.thirdDimSlider.value())


	def updateImageTransform(self):
		t = QtGui.QTransform()

		self.image.setTransformOriginPoint(self.lengthAxisHorizontal/2,self.lengthAxisVertical/2)
		t.translate(self.posOrigoAxisHorizontal,self.posOrigoAxisVertical)
		if self.zAxis:
			t.rotate(self.angle)
			t.scale(self.scaleAxisHorizontal,self.scaleAxisVertical)
		else:
			t.scale(self.scaleAxisHorizontal,self.scaleAxisVertical)
			t.rotate(self.angle)
		
		self.image.setTransform(t)

	def setCurrentIndex(self, index):
		self.currentIndex = np.clip(index, 0, self.cData.data.shape[self.zAxis]-1)
		self.updateImage()

	def quickMinMax(self, data):
		"""
		Estimate the min/max values of *data* by subsampling.
		"""
		while data.size > 1e6:
			ax = np.argmax(data.shape)
			sl = [slice(None)] * data.ndim
			sl[ax] = slice(None, None, 2)
			data = data[sl]
		return np.nanmin(data), np.nanmax(data)

	def centerPoint(self):
		return [self.posOrigoAxisHorizontal+self.lengthAxisHorizontal*self.scaleAxisHorizontal/2,self.posOrigoAxisVertical+self.lengthAxisVertical*self.scaleAxisVertical/2]

	## General interaction functions
	#
	#

	# ROI
	# 
	
	def addHorIlRoi(self):
		self.addSingleLineROI(self.ROIPlotItemBottomWidget)

	def remHorIlRoi(self):
		if len(self.roiList[CONST_ROI_HOR_LIST]) > 0:
			self.removeROI(self.roiList[CONST_ROI_HOR_LIST][0])

	def addVerIlRoi(self):
		self.addSingleLineROI(self.ROIPlotItemRightWidget)

	def remVerIlRoi(self):
		if len(self.roiList[CONST_ROI_VER_LIST]) > 0:
			self.removeROI(self.roiList[CONST_ROI_VER_LIST][0])

	def addBoxRoi(self):
		self.addRectROI()

	def remBoxRoi(self):
		if len(self.roiList[CONST_ROI_BOTH_LIST]) > 0:
			self.removeROI(self.roiList[CONST_ROI_BOTH_LIST][0])

	# Rotation
	# 
	 
	def setRotationAngle(self, val):
		#self.image.setRotation(val)
		self.angle = val
		self.updateImageTransform() 
		self.on_updateBothRoiPlot()

class glVolumePlot(QtGui.QWidget):
	
	def __init__(self):
		super(glVolumePlot, self).__init__()

		self.cData = None
		self.threshold = 255
		self.initUI()


	def initUI(self):
		grid = QtGui.QGridLayout()
		self.setLayout(grid)
		self.view = gl.GLViewWidget()
		grid.addWidget(self.view)

		self.view.opts['distance'] = 200
 
		g = gl.GLGridItem()
		g.scale(10, 10, 1)
		self.view.addItem(g)

		self.plotVolumeItem = gl.GLVolumeItem(None)
		self.view.addItem(self.plotVolumeItem)
		
		self.plotAxis = gl.GLAxisItem()
		self.view.addItem(self.plotAxis)


	def setData(self, cData, metaDataOutput=None):
		if cData != None:
			self.cData = cData
		else:
			return

		self.updateImage()
		
		size = self.cData.data.shape
		
		self.plotVolumeItem.translate(-size[0]/2,-size[1]/2,-size[2]/2)

		if metaDataOutput:
			metaDataOutput.setText(self.cData.root.NXentry[self.cData.entryId].tree)

	def updateImage(self):
		data = np.asarray(self.cData.data)
		d2 = np.empty(data.shape + (4,), dtype=np.ubyte)
		
		
		norm = data.max() / self.threshold
		data = data / norm
		
		d2[..., 0] = data
		d2[..., 1] = d2[..., 0]
		d2[..., 2] = d2[..., 1]
		#d2[..., 3] = 10
		
		#d2[..., 0] = positive * (255./positive.max())
		#d2[..., 1] = negative * (255./negative.max())
		#d2[..., 2] = d2[...,1]
		#d2[..., 3] = 10
		d2[..., 3] = data
		d2[..., 3] = (d2[..., 3].astype(float) / 255.) **2 * 255
		
		d2[:, 0, 0] = [255,0,0,100]
		d2[0, :, 0] = [0,255,0,100]
		d2[0, 0, :] = [0,0,255,100]
		
		#print d2[...,3]
		
		self.plotVolumeItem.setData(d2)
		
	def setThreshold(self, val):
		if type(val) is int:
			self.threshold = val
			self.updateImage()
		else:
			print "Error: Value not int"

class SingleLineROI(pg.ROI):
    """
    ROI subclass with two freely-moving handles defining a line.
    
    ============== =============================================================
    **Arguments**
    positions      (list of two length-2 sequences) The endpoints of the line 
                   segment. Note that, unlike the handle positions specified in 
                   other ROIs, these positions must be expressed in the normal
                   coordinate system of the ROI, rather than (0 to 1) relative
                   to the size of the ROI.
    \**args        All extra keyword arguments are passed to ROI()
    ============== =============================================================
    """
    
    def __init__(self, positions=(None, None), pos=None, handles=(None,None), scaleCenter=None, **args):
        if pos is None:
            pos = [0,0]

        if scaleCenter is None:
            scaleCenter = [0,0]

        pg.ROI.__init__(self, pos, [1,1], invertible=False, **args)
        #ROI.__init__(self, positions[0])
        if len(positions) > 2:
            raise Exception("LineSegmentROI must be defined by exactly 2 positions. For more points, use PolyLineROI.")
        
        for i, p in enumerate(positions):
            self.addScaleHandle(p, center=scaleCenter,item=handles[i])
                
        
    def listPoints(self):
        return [p['item'].pos() for p in self.handles]
            
    def paint(self, p, *args):
        p.setRenderHint(QtGui.QPainter.Antialiasing)
        p.setPen(self.currentPen)
        h1 = self.handles[0]['item'].pos()
        h2 = self.handles[1]['item'].pos()
        p.drawLine(h1, h2)
        
    def boundingRect(self):
        return self.shape().boundingRect()
    
    def shape(self):
        p = QtGui.QPainterPath()
    
        h1 = self.handles[0]['item'].pos()
        h2 = self.handles[1]['item'].pos()
        dh = h2-h1
        if dh.length() == 0:
            return p
        pxv = self.pixelVectors(dh)[1]
        if pxv is None:
            return p
            
        pxv *= 4
        
        p.moveTo(h1+pxv)
        p.lineTo(h2+pxv)
        p.lineTo(h2-pxv)
        p.lineTo(h1-pxv)
        p.lineTo(h1+pxv)
      
        return p
    
    def getArrayRegion(self, data, img, axes=(0,1)):
        """
        Use the position of this ROI relative to an imageItem to pull a slice 
        from an array.
        
        Since this pulls 1D data from a 2D coordinate system, the return value 
        will have ndim = data.ndim-1
        
        See ROI.getArrayRegion() for a description of the arguments.
        """
        
        imgPts = [self.mapToItem(img, h['item'].pos()) for h in self.handles]
        rgns = []
        for i in range(len(imgPts)-1):
            d = pg.Point(imgPts[i+1] - imgPts[i])
            o = pg.Point(imgPts[i])
            r = pg.affineSlice(data, shape=(int(d.length()),), vectors=[pg.Point(d.norm())], origin=o, axes=axes, order=1)
            rgns.append(r)
            
        return np.concatenate(rgns, axis=axes[0])

		