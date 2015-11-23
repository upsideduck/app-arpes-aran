from PySide import QtCore, QtGui
from helper.constants import *
import numpy as np
import ext.pyqtgraph as pg

class standardPlot(QtGui.QWidget):

	cData = None
	levelMin = 0
	levelMax = 4000
	autoLevel = True
	nameAxisZ = ""
	roiList = [[],[],[]]

	def __init__(self, parent = None):
		super(standardPlot, self).__init__()
		self.initUI()
		self.currentIndex = 0
		self.zAxis = None


	def initUI(self):
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
		self.ROIPlotItemRightWidget.setMaximumWidth(150)
		self.ROIPlotItemRightWidget.setMinimumWidth(150)
		self.ROIPlotItemRightWidget.hide()
		grid.addWidget(self.ROIPlotItemRightWidget,0,1)
		self.ROIPlotItemBottomWidget.setMaximumHeight(150)
		self.ROIPlotItemBottomWidget.setMinimumHeight(150)
		self.ROIPlotItemBottomWidget.hide()
		grid.addWidget(self.ROIPlotItemBottomWidget, 1, 0)
		

		# Layout items into PQG widget
		self.view.addItem(self.mainPlotItem,row=1, col=1)
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

		self.image.scale(self.scaleAxisHorizontal,self.scaleAxisVertical)
		self.image.setPos(self.posOrigoAxisHorizontal,self.posOrigoAxisVertical)
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
	def addInfiniteLineROI(self,angle,plot):
		if plot == self.ROIPlotItemBottomWidget:
			initPos = (self.posOrigoAxisVertical + self.lengthAxisVertical*self.scaleAxisVertical/2)
			bounds = [self.posOrigoAxisVertical,self.posOrigoAxisVertical+self.lengthAxisVertical*self.scaleAxisVertical]
			roiListID = CONST_ROI_HOR_LIST
			updatePlot = self.on_updateHorRoiPlot
		elif plot == self.ROIPlotItemRightWidget:
			initPos = (self.posOrigoAxisHorizontal + self.lengthAxisHorizontal*self.scaleAxisHorizontal/2)
			bounds = [self.posOrigoAxisHorizontal,self.posOrigoAxisHorizontal+self.lengthAxisHorizontal*self.scaleAxisHorizontal]
			roiListID = CONST_ROI_VER_LIST
			updatePlot = self.on_updateVerRoiPlot
		else:
			return

		roi = pg.InfiniteLine(angle=angle, movable=True, pos=initPos, bounds=bounds)
		roi.setPen(QtGui.QPen(QtGui.QColor(255, 255, 0, 200)))
		roi.setZValue(1)
		self.roiList[roiListID].append(roi)
		self.mainPlotItem.addItem(roi)
		roi.sigPositionChanged.connect(updatePlot)
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
			if type(roi) is pg.InfiniteLine:
				roi.sigPositionChanged.disconnect()
			else:
				print "Could not remove ROI plot"
				return 
			self.roiList[CONST_ROI_HOR_LIST].remove(roi)
			self.mainPlotItem.removeItem(roi)
			roi = None
			self.on_updateHorRoiPlot()

		if roi in self.roiList[CONST_ROI_VER_LIST]:
			if type(roi) is pg.InfiniteLine:
				roi.sigPositionChanged.disconnect()
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
	def on_updateHorRoiPlot(self):
		self.ROIPlotItemBottom.clear()
		for roi in self.roiList[CONST_ROI_HOR_LIST]:
			if type(roi) is pg.InfiniteLine: 
				idx = int((roi.value()-self.posOrigoAxisVertical)/self.scaleAxisVertical)
				if idx >= self.lengthAxisVertical or idx < 0:
					return
				y = np.asarray(self.getProcessedImage()[:,idx])
				x = np.linspace(self.posOrigoAxisHorizontal,self.posOrigoAxisHorizontal+self.lengthAxisHorizontal*self.scaleAxisHorizontal,self.lengthAxisHorizontal)
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
			if type(roi) is pg.InfiniteLine: 
				idx = int((roi.value()-self.posOrigoAxisHorizontal)/self.scaleAxisHorizontal)
				if idx >= self.lengthAxisHorizontal or idx < 0:
					return
				y = np.asarray(self.getProcessedImage()[idx,:])
				x = np.linspace(self.posOrigoAxisVertical,self.posOrigoAxisVertical+self.lengthAxisVertical*self.scaleAxisVertical,self.lengthAxisVertical)
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

	## General interaction functions
	#
	#

	def addHorIlRoi(self):
		self.addInfiniteLineROI(0, self.ROIPlotItemBottomWidget)

	def remHorIlRoi(self):
		if len(self.roiList[CONST_ROI_HOR_LIST]) > 0:
			self.removeROI(self.roiList[CONST_ROI_HOR_LIST][0])

	def addVerIlRoi(self):
		self.addInfiniteLineROI(90, self.ROIPlotItemRightWidget)

	def remVerIlRoi(self):
		if len(self.roiList[CONST_ROI_VER_LIST]) > 0:
			self.removeROI(self.roiList[CONST_ROI_VER_LIST][0])

	def addBoxRoi(self):
		self.addRectROI()

	def remBoxRoi(self):
		if len(self.roiList[CONST_ROI_BOTH_LIST]) > 0:
			self.removeROI(self.roiList[CONST_ROI_BOTH_LIST][0])



		