from PySide import QtCore, QtGui
from helper.constants import *
import numpy as np
import ext.pyqtgraph as pg
from ext.pyqtgraph.dockarea import *
import ext.pyqtgraph.opengl as gl

class standardPlot(QtGui.QWidget):

	roiSelected = QtCore.Signal(pg.ROI)

	def __init__(self, showHistogram=False, showSlices=False, parent=None, ):
		super(standardPlot, self).__init__()

		self.currentIndex = 0
		self.zAxis = None
		self.cData = None
		self.levelMin = 0
		self.levelMax = 4000
		self.autoLevel = True
		self.nameAxisZ = ""
		self.roiList = [[], [], []]
		self.showHistogram = showHistogram
		self.showSlices = showSlices
		self.hSliceRoi = None
		self.vSliceRoi = None
		self.initUI()

	def initUI(self):
		grid = QtGui.QGridLayout()
		self.setLayout(grid)
		#self.view = pg.GraphicsLayoutWidget()
		self.view = DockArea()
		self.mainPlotDock = Dock("Plot", hideTitle=True)
		self.view.addDock(self.mainPlotDock, 'right')## place d3 at bottom edge of d1

		grid.addWidget(self.view)

		# Init all items for widget
		self.mainPlotWidget = pg.PlotWidget()
		self.ROIPlotItemBottomWidget = pg.PlotWidget()
		self.ROIPlotItemRightWidget = pg.PlotWidget()
		self.image = pg.ImageItem()
		self.hist = pg.HistogramLUTWidget()
		self.thirdDimToolsLayouts = []

		self.hSliceImage = pg.ImageItem()
		self.hSlicePlotWidget= pg.PlotWidget()
		self.hSlicePlotWidget.addItem(self.hSliceImage)
		self.vSliceImage = pg.ImageItem()
		self.vSlicePlotWidget = pg.PlotWidget()
		self.vSlicePlotWidget.addItem(self.vSliceImage)

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
		grid.addWidget(self.ROIPlotItemRightWidget, 0, 1)
		self.ROIPlotItemBottomWidget.setMaximumHeight(100)
		self.ROIPlotItemBottomWidget.setMinimumHeight(100)
		self.ROIPlotItemBottomWidget.hide()
		grid.addWidget(self.ROIPlotItemBottomWidget, 1, 0)

		# Layout items into PQG widget
		self.mainPlotDock.addWidget(self.mainPlotWidget)

		if self.showHistogram:
			grid.addWidget(self.hist, 0, 2)
		self.mainPlotWidget.addItem(self.image)

		grid.setColumnStretch(0, 10)
		grid.setRowStretch(0, 10)

	def setData(self, newData, zAxis=None, metaDataOutput=None):
		## Remove old data
		if self.cData and newData:
			self.cData.nbDataChanged.disconnect(self.on_dataChanged)
			self.cData = None
		
		## Remove any third dim layouts if shown previously
		if len(self.thirdDimToolsLayouts):
			self.removeThirdDimTools()
		
		## Add new data
		if newData != None:
			newData.nbDataChanged.connect(self.on_dataChanged)
			self.cData = newData
		else:
			return

		if self.cData.is3D():
			if zAxis == None:
				self.zAxis = 2
			self.addThirdDimTools()
		else:
			self.showSlices = False # Alwasy set false for none 3D data
			self.zAxis = None

		## Load metadata into placeholder
		if metaDataOutput:
			metaDataOutput.setText(self.cData.root.NXentry[self.cData.entryId].tree)

		## Update plot on data change
		self.on_dataChanged()

	def addThirdDimTools(self):
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

		# Slices controls
		if self.showSlices:
			self.thirdDimSlicesCheckBox =  QtGui.QCheckBox("Slices")
			thirdDimLayout.addWidget(self.thirdDimSlicesCheckBox)
			self.thirdDimSlicesCheckBox.stateChanged[int].connect(self.on_thirdDimSlicesCheckBox)
			
			self.hSlicePlotDock = Dock("Horizontal Slice", widget=self.hSlicePlotWidget, hideTitle=True)
			self.view.addDock(self.hSlicePlotDock, 'left')

			self.vSlicePlotDock = Dock("Vertical Slice", widget=self.vSlicePlotWidget, hideTitle=True)
			self.view.addDock(self.vSlicePlotDock, 'bottom', self.hSlicePlotDock) 
			self.vSlicePlotDock.hide()
			self.hSlicePlotDock.hide()

		
		# Autolevel
		if self.showHistogram:
			self.autoLevelCheckBox = QtGui.QCheckBox("Auto Level")
			self.autoLevelCheckBox.stateChanged[int].connect(self.on_autoHistLevel)
			if self.autoLevel:
				self.autoLevelCheckBox.setCheckState(QtCore.Qt.Checked)
			autoLevelLayout = QtGui.QVBoxLayout()
			spacerAL = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
			autoLevelLayout.addWidget(self.hist)
			autoLevelLayout.addWidget(self.autoLevelCheckBox)
			autoLevelLayout.addItem(spacerAL)
			grid.addLayout(autoLevelLayout, 0, 2)
			self.thirdDimToolsLayouts.append(autoLevelLayout)

		grid.addLayout(thirdDimLayout, 2, 0, 1, 3)
		self.thirdDimToolsLayouts.append(thirdDimLayout)

	def removeThirdDimTools(self):
		for layout in self.thirdDimToolsLayouts:
			for i in reversed(range(layout.count())):
				layout.itemAt(i).widget().setParent(None)
			self.thirdDimToolsLayouts.remove(layout)
			del layout

	def updateImage(self):
		if not self.cData:
			return

		image = self.getProcessedImage()
		self.image.updateImage(image)

		if self.autoLevel:
			self.hist.region.setRegion([self.levelMin, self.levelMax])

		if self.roiList[CONST_ROI_BOTH_LIST]:
			self.on_updateBothRoiPlot()
		else:
			if self.roiList[CONST_ROI_HOR_LIST]:
				self.on_updateHorRoiPlot()
			if self.roiList[CONST_ROI_VER_LIST]:
				self.on_updateVerRoiPlot()

	def updateImageAxes(self):

		# Not set on first run
		try:
			oldScaleh = self.scaleAxisHorizontal
			oldScalev = self.scaleAxisVertical
		except Exception, e:
			oldScaleh = 1
			oldScalev = 1



		######
		## Change all static parameters to image axis
		######
		if self.zAxis == 0:
			self.scaleAxisHorizontal = float((self.cData.axis2[-1] - self.cData.axis2[0]) / len(self.cData.axis2))
			self.scaleAxisVertical = float(self.cData.axis3[-1] - self.cData.axis3[0]) / len(self.cData.axis3)
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
			self.scaleAxisHorizontal = float((self.cData.axis1[-1] - self.cData.axis1[0]) / len(self.cData.axis1))
			self.scaleAxisVertical = float(self.cData.axis3[-1] - self.cData.axis3[0]) / len(self.cData.axis3)
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
			self.scaleAxisHorizontal = float((self.cData.axis1[-1] - self.cData.axis1[0]) / len(self.cData.axis1))
			self.scaleAxisVertical = float(self.cData.axis2[-1] - self.cData.axis2[0]) / len(self.cData.axis2)
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
			self.scaleAxisHorizontal = float((self.cData.axis1[-1] - self.cData.axis1[0]) / len(self.cData.axis1))
			self.scaleAxisVertical = float(self.cData.axis2[-1] - self.cData.axis2[0]) / len(self.cData.axis2)
			self.lengthAxisHorizontal = len(self.cData.axis1)
			self.lengthAxisVertical = len(self.cData.axis2)
			self.posOrigoAxisHorizontal = float(self.cData.axis1[0])
			self.posOrigoAxisVertical = float(self.cData.axis2[0])
			self.nameAxisHorizontal = self.cData.axis1name
			self.nameAxisVertical = self.cData.axis2name
		

		######
		## Update image to new position
		######	
		t = QtGui.QTransform()
		t.translate(self.posOrigoAxisHorizontal, self.posOrigoAxisVertical)
		t.scale(self.scaleAxisHorizontal, self.scaleAxisVertical)
		self.image.setTransform(t)
		self.mainPlotWidget.setLabel('bottom', text=self.nameAxisHorizontal)
		self.mainPlotWidget.setLabel('left', text=self.nameAxisVertical)
		self.ROIPlotItemRightWidget.getPlotItem().setLabel('bottom', text="I")
		self.mainPlotWidget.invertY(False)
		ratio = (self.lengthAxisVertical / self.lengthAxisHorizontal) / (
		self.scaleAxisHorizontal / self.scaleAxisVertical)
		self.mainPlotWidget.getViewBox().setAspectLocked(lock=True, ratio=ratio)

		######
		## Update thid dimenssion tools
		######
		if self.cData.is3D():
			self.thirdDimSlider.setRange(0, self.lengthAxisZ - 1)
			self.thirdDimSlider.valueChanged[int].connect(self.on_thirdDimSliderMoved)
			self.thirdDimNameLbl.setText(self.nameAxisZ)
			self.thirdDimValueQSBox.setRange(self.axisZarr[0], self.axisZarr[-1])
			self.thirdDimValueQSBox.setSingleStep((self.axisZarr[-1] - self.axisZarr[0]) / (self.lengthAxisZ - 1))
			self.thirdDimValueQSBox.valueChanged.connect(self.on_thirdDimQSBoxChanged)
			#self.thirdDimValueQSBox.setValue(self.thirdDimSlider.value())

		######
		## Update image slices to new position
		######			
		if self.showSlices and self.hSliceRoi and self.vSliceRoi:
			oldPnth = self.hSliceRoi.pos()
			oldPntv = self.vSliceRoi.pos()

			newScaleh = self.scaleAxisHorizontal/oldScaleh
			newScalev = self.scaleAxisVertical/oldScalev

			newPnth = (oldPnth.x()*newScaleh,oldPnth.y()*newScaleh)
			newPntv = (oldPntv.x()*newScaleh,oldPntv.y()*newScalev)
			self.hSliceRoi.scale(newScaleh,center=[0,0])
			self.vSliceRoi.scale(newScalev,center=[0,0])
			self.hSliceRoi.setPos(newPnth)
			self.vSliceRoi.setPos(newPntv)

			th = QtGui.QTransform()
			th.translate(self.posOrigoAxisHorizontal, self.axisZarr[0])
			th.scale(self.scaleAxisHorizontal, float(self.axisZarr[-1] - self.axisZarr[0]) / len(self.axisZarr))
			self.hSliceImage.setTransform(th)
			self.hSlicePlotWidget.setLabel('bottom', text=self.nameAxisHorizontal)
			self.hSlicePlotWidget.setLabel('left', text=self.nameAxisZ)
			self.on_hSliceRoiChange(self.hSliceRoi)

			tv = QtGui.QTransform()
			tv.translate(self.posOrigoAxisVertical, self.axisZarr[0])
			tv.scale(self.scaleAxisVertical, float(self.axisZarr[-1] - self.axisZarr[0]) / len(self.axisZarr))
			self.vSliceImage.setTransform(tv)
			self.vSlicePlotWidget.setLabel('bottom', text=self.nameAxisVertical)
			self.vSlicePlotWidget.setLabel('left', text=self.nameAxisZ)
			self.on_vSliceRoiChange(self.vSliceRoi)
		

		for roi in self.roiList[CONST_ROI_HOR_LIST]:
			oldPnth = roi.pos()
			newScaleh = self.scaleAxisHorizontal/oldScaleh
			newPnth = (oldPnth.x()*newScaleh,oldPnth.y()*newScaleh)
			roi.scale(newScaleh,center=[0,0])
			roi.setPos(newPnth)
		
		for roi in self.roiList[CONST_ROI_VER_LIST]:
			oldPntv = roi.pos()
			newScalev = self.scaleAxisVertical/oldScalev
			newPntv = (oldPntv.x()*newScaleh,oldPntv.y()*newScalev)
			roi.scale(newScalev,center=[0,0])
			roi.setPos(newPntv)
		
		for roi in self.roiList[CONST_ROI_BOTH_LIST]:
			oldPntv = roi.pos()
			newScalev = self.scaleAxisVertical/oldScalev
			newPntv = (oldPntv.x()*newScaleh,oldPntv.y()*newScalev)
			roi.scale(newScalev,center=[0,0])
			roi.setPos(newPntv)
		
				

	def getProcessedImage(self):
		image = np.asarray(self.cData.data)

		if len(image.shape) == 2:
			procImage = image
		elif len(image.shape) == 3:
			if self.zAxis == 0:
				procImage = image[self.currentIndex, :, :]
			elif self.zAxis == 1:
				procImage = image[:, self.currentIndex, :]
			elif self.zAxis == 2:
				procImage = image[:, :, self.currentIndex]
			else:
				return None
		else:
			return None

		self.levelMin, self.levelMax = list(map(float, self.quickMinMax(procImage)))

		return procImage

	def setCurrentIndex(self, index):
		self.currentIndex = np.clip(index, 0, self.cData.data.shape[self.zAxis] - 1)
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
		return [self.posOrigoAxisHorizontal + self.lengthAxisHorizontal * self.scaleAxisHorizontal / 2,
				self.posOrigoAxisVertical + self.lengthAxisVertical * self.scaleAxisVertical / 2]

	def hInitSlicePos(self):
		centerPoint = self.centerPoint()
		return ([self.posOrigoAxisHorizontal, centerPoint[1]],[self.posOrigoAxisHorizontal + self.lengthAxisHorizontal * self.scaleAxisHorizontal,centerPoint[1]])

	def vInitSlicePos(self):
		centerPoint = self.centerPoint()
		return ([centerPoint[0], self.posOrigoAxisVertical],[centerPoint[0], self.posOrigoAxisVertical + self.lengthAxisVertical * self.scaleAxisVertical])
	
	## ROI functions
	#
	#
	def addSingleLineROI(self, plot):
		centerPoint = self.centerPoint()
		if plot == self.ROIPlotItemBottomWidget:
			initPos = ([self.posOrigoAxisHorizontal, centerPoint[1]],
					   [self.posOrigoAxisHorizontal + self.lengthAxisHorizontal * self.scaleAxisHorizontal,
						centerPoint[1]])
			bounds = [self.posOrigoAxisVertical,
					  self.posOrigoAxisVertical + self.lengthAxisVertical * self.scaleAxisVertical]
			roiListID = CONST_ROI_HOR_LIST
			updatePlot = self.on_updateHorRoiPlot
		elif plot == self.ROIPlotItemRightWidget:
			bounds = [self.posOrigoAxisHorizontal,
					  self.posOrigoAxisHorizontal + self.lengthAxisHorizontal * self.scaleAxisHorizontal]
			# initPos=([self.posOrigoAxisVertical,centerPoint[0]],[self.posOrigoAxisVertical+self.lengthAxisVertical*self.scaleAxisVertical,centerPoint[0]])
			initPos = ([centerPoint[0], self.posOrigoAxisVertical],
					   [centerPoint[0], self.posOrigoAxisVertical + self.lengthAxisVertical * self.scaleAxisVertical])
			roiListID = CONST_ROI_VER_LIST
			updatePlot = self.on_updateVerRoiPlot
		else:
			return None

		angle = 0
		roi = SingleLineROI(positions=initPos, scaleCenter=centerPoint)
		roi.setPen(QtGui.QPen(QtGui.QColor(255, 255, 0, 200)))
		roi.setZValue(1)
		self.roiList[roiListID].append(roi)
		self.mainPlotWidget.addItem(roi)
		roi.sigRegionChanged.connect(updatePlot)
		roi.setAcceptedMouseButtons(QtCore.Qt.LeftButton)
		roi.sigClicked.connect(self.on_roiSelected)
		roi.sigRegionChangeStarted.connect(self.on_roiSelected)
		plot.show()
		updatePlot()
		return roi

	def addRectROI(self):
		width = self.lengthAxisHorizontal * self.scaleAxisHorizontal / 5
		height = self.lengthAxisVertical * self.scaleAxisVertical / 5

		roi = RectangularROI(pos=[self.posOrigoAxisHorizontal + self.lengthAxisHorizontal * self.scaleAxisHorizontal / 2 - width / 2,self.posOrigoAxisVertical + self.lengthAxisVertical * self.scaleAxisVertical / 2 - height / 2], size=[width, height], centered=True, sideScalers=True)
		roi.setPen(QtGui.QPen(QtGui.QColor(255, 255, 0, 200)))
		roi.setZValue(1)
		self.roiList[CONST_ROI_BOTH_LIST].append(roi)
		self.mainPlotWidget.addItem(roi)
		roi.sigRegionChanged.connect(self.on_updateBothRoiPlot)
		roi.setAcceptedMouseButtons(QtCore.Qt.LeftButton)
		roi.sigClicked.connect(self.on_roiSelected)
		roi.sigRegionChangeStarted.connect(self.on_roiSelected)
		self.ROIPlotItemRightWidget.show()
		self.ROIPlotItemBottomWidget.show()
		self.on_updateBothRoiPlot()
		return roi

	def removeROI(self, roi):
		if roi in self.roiList[CONST_ROI_HOR_LIST]:
			if type(roi) is SingleLineROI:
				roi.sigClicked.disconnect(self.on_roiSelected)
				roi.sigRegionChanged.disconnect()
				roi.sigRegionChangeStarted.disconnect()
			else:
				print "Could not remove ROI plot"
				return
			self.roiList[CONST_ROI_HOR_LIST].remove(roi)
			self.mainPlotWidget.removeItem(roi)
			roi = None
			self.on_updateHorRoiPlot()

		if roi in self.roiList[CONST_ROI_VER_LIST]:
			if type(roi) is SingleLineROI:
				roi.sigClicked.disconnect(self.on_roiSelected)
				roi.sigRegionChanged.disconnect()
				roi.sigRegionChangeStarted.disconnect()
			else:
				print "Could not remove ROI plot"
				return
			self.roiList[CONST_ROI_VER_LIST].remove(roi)
			self.mainPlotWidget.removeItem(roi)
			roi = None
			self.on_updateVerRoiPlot()

		if roi in self.roiList[CONST_ROI_BOTH_LIST]:
			if type(roi) is RectangularROI:
				roi.sigClicked.disconnect(self.on_roiSelected)
				roi.sigRegionChanged.disconnect()
				roi.sigRegionChangeStarted.disconnect()
			else:
				print "Could not remove ROI plot"
				return
			self.roiList[CONST_ROI_BOTH_LIST].remove(roi)
			self.mainPlotWidget.removeItem(roi)
			roi = None
			self.on_updateBothRoiPlot()

		if len(self.roiList[CONST_ROI_HOR_LIST]) == 0 and len(self.roiList[CONST_ROI_BOTH_LIST]) == 0:
			self.ROIPlotItemBottomWidget.hide()

		if len(self.roiList[CONST_ROI_VER_LIST]) == 0 and len(self.roiList[CONST_ROI_BOTH_LIST]) == 0:
			self.ROIPlotItemRightWidget.hide()

	def removeAllROIs(self):
		for l in self.roiList:
			for roi in l:
				self.removeROI(roi)

	## Slots
	# 
	#
	def on_updateHorRoiPlot(self):
		self.ROIPlotItemBottomWidget.getPlotItem().clear()
		for roi in self.roiList[CONST_ROI_HOR_LIST]:
			if type(roi) is SingleLineROI:
				pos = roi.pos()
				size = roi.size()
				#xStart = self.posOrigoAxisHorizontal + pos[0] + (1 - size[0]) * self.lengthAxisHorizontal * self.scaleAxisHorizontal / 2
				#xEnd = xStart + self.lengthAxisHorizontal * self.scaleAxisHorizontal * size[0]
				pts = [roi.mapToParent(h['item'].pos()) for h in roi.handles]

				y = roi.getArrayRegion(np.asarray(self.getProcessedImage()), self.image, axes=(0, 1))
				x = np.linspace(pts[0].x(), pts[1].x(), len(y))
				self.ROIPlotItemBottomWidget.getPlotItem().plot(x=x, y=y, clear=False, pen='k')
			else:
				return

		for roi in self.roiList[CONST_ROI_BOTH_LIST]:
			if type(roi) is RectangularROI:
				selected = roi.getArrayRegion(np.asarray(self.getProcessedImage()), self.image, axes=(0, 1))
				pos = roi.pos()
				size = roi.size()
				y = selected.mean(axis=1)
				x = np.linspace(pos[0], pos[0] + size[0], len(y))

				self.ROIPlotItemBottomWidget.getPlotItem().plot(y=y, x=x, clear=False, pen='r')
			else:
				return

	def on_updateVerRoiPlot(self):
		self.ROIPlotItemRightWidget.getPlotItem().clear()
		for roi in self.roiList[CONST_ROI_VER_LIST]:
			if type(roi) is SingleLineROI:
				pos = roi.pos()
				size = roi.size()
				points = roi.listPoints()

				#xStart = pos[1] + points[0][1]
				#xEnd = xStart + self.lengthAxisVertical * self.scaleAxisVertical * size[1]
				pts = [roi.mapToParent(h['item'].pos()) for h in roi.handles]

				y = roi.getArrayRegion(np.asarray(self.getProcessedImage()), self.image, axes=(0, 1))
				x = np.linspace(pts[0].y(), pts[1].y(), len(y))
				self.ROIPlotItemRightWidget.getPlotItem().plot(x=y, y=x, clear=False, pen='k')
			else:
				return

		for roi in self.roiList[CONST_ROI_BOTH_LIST]:
			if type(roi) is RectangularROI:
				selected = roi.getArrayRegion(np.asarray(self.getProcessedImage()), self.image, axes=(0, 1))
				pos = roi.pos()
				size = roi.size()
				y = selected.mean(axis=0)
				x = np.linspace(pos[1], pos[1] + size[1], len(y))
				self.ROIPlotItemRightWidget.getPlotItem().plot(y=x, x=y, clear=False, pen='r')
			else:
				return

	def on_updateBothRoiPlot(self):
		self.on_updateHorRoiPlot()
		self.on_updateVerRoiPlot()

	def on_roiSelected(self,roi):
		self.roiSelected.emit(roi)

	def on_thirdDimSliderMoved(self, val):
		self.setCurrentIndex(val)

		step = ((self.axisZarr[-1] - self.axisZarr[0]) / (len(self.axisZarr) - 1))
		current = self.thirdDimValueQSBox.value() - self.axisZarr[0]

		if int(current / step) != self.thirdDimSlider.value():
			self.thirdDimValueQSBox.setValue(self.axisZarr[val])

		try:
			self.hSliceZaxisLine.setValue(self.axisZarr[val])
			self.vSliceZaxisLine.setValue(self.axisZarr[val])
		except Exception, e:
			pass

	def on_thirdDimQSBoxChanged(self, val):
		step = ((self.axisZarr[-1] - self.axisZarr[0]) / (len(self.axisZarr) - 1))
		current = val - self.axisZarr[0]

		if int(current / step) != self.thirdDimSlider.value():
			self.thirdDimSlider.setValue(int(current / step))

	def on_autoHistLevel(self, state):
		if state == QtCore.Qt.Checked:
			self.autoLevel = True
		elif state == QtCore.Qt.Unchecked:
			self.autoLevel = False
		else:
			pass
		self.updateImage()

	def on_thirdDimSlicesCheckBox(self, state):
		if state == QtCore.Qt.Checked:

			self.hSliceRoi = SingleLineROI(positions=self.hInitSlicePos(), scaleCenter=self.centerPoint(), userRemovable=False)
			self.hSliceRoi.setAcceptedMouseButtons(QtCore.Qt.LeftButton)
			self.hSliceRoi.sigClicked.connect(self.on_roiSelected)
			self.hSliceRoi.sigRegionChangeStarted.connect(self.on_roiSelected)
			self.hSliceRoi.setPen(QtGui.QPen(QtGui.QColor(0, 255, 0, 200)))
			self.mainPlotWidget.addItem(self.hSliceRoi)
			self.hSliceRoi.sigRegionChanged.connect(self.on_hSliceRoiChange)
			self.on_hSliceRoiChange(self.hSliceRoi)
			self.hSliceZaxisLine = pg.InfiniteLine(angle=0)
			self.hSlicePlotWidget.addItem(self.hSliceZaxisLine)
			self.hSliceZaxisLine.setValue(self.thirdDimValueQSBox.value())
			self.hSlicePlotDock.show()

			self.vSliceRoi = SingleLineROI(positions=self.vInitSlicePos(), scaleCenter=self.centerPoint(), userRemovable=False)
			self.vSliceRoi.setAcceptedMouseButtons(QtCore.Qt.LeftButton)
			self.vSliceRoi.sigClicked.connect(self.on_roiSelected)
			self.vSliceRoi.sigRegionChangeStarted.connect(self.on_roiSelected)
			self.vSliceRoi.setPen(QtGui.QPen(QtGui.QColor(0, 255, 0, 200)))
			self.mainPlotWidget.addItem(self.vSliceRoi)
			self.vSliceRoi.sigRegionChanged.connect(self.on_vSliceRoiChange)
			self.on_vSliceRoiChange(self.vSliceRoi)
			self.vSliceZaxisLine = pg.InfiniteLine(angle=0)
			self.vSlicePlotWidget.addItem(self.vSliceZaxisLine)
			self.vSliceZaxisLine.setValue(self.thirdDimValueQSBox.value())
			self.vSlicePlotDock.show()

		elif state == QtCore.Qt.Unchecked:
			self.hSlicePlotDock.hide()
			self.mainPlotWidget.removeItem(self.hSliceRoi)
			self.hSlicePlotWidget.removeItem(self.hSliceZaxisLine)
			self.hSliceZaxisLine = None
			self.hSliceRoi.sigRegionChanged.disconnect(self.on_hSliceRoiChange)
			self.hSliceRoi.sigRegionChangeStarted.disconnect(self.on_roiSelected)
			self.hSliceRoi.sigClicked.disconnect(self.on_roiSelected)
			self.hSliceRoi = None
			
			self.vSlicePlotDock.hide()
			self.mainPlotWidget.removeItem(self.vSliceRoi)
			self.vSlicePlotWidget.removeItem(self.vSliceZaxisLine)
			self.vSliceZaxisLine = None
			self.vSliceRoi.sigRegionChanged.disconnect(self.on_vSliceRoiChange)
			self.vSliceRoi.sigRegionChangeStarted.disconnect(self.on_roiSelected)
			self.vSliceRoi.sigClicked.disconnect(self.on_roiSelected)
			self.vSliceRoi = None
		else:
			pass

	def on_hSliceRoiChange(self,roi):
		img = roi.getArrayRegion(np.asarray(self.cData.data), self.image, axes=(0,1))
		self.hSliceImage.setImage(img, autoLevels=True)

		pts = [roi.mapToParent(h['item'].pos()) for h in roi.handles]
		th = QtGui.QTransform()
		th.translate(pts[0].x(), self.axisZarr[0])
		scale = (pts[1].x()-pts[0].x())/img.shape[0]
		th.scale(scale, float(self.axisZarr[-1] - self.axisZarr[0]) / len(self.axisZarr))
		self.hSliceImage.setTransform(th)

	def on_vSliceRoiChange(self,roi):
		img = roi.getArrayRegion(np.asarray(self.cData.data), self.image, axes=(0,1))
		self.vSliceImage.setImage(img, autoLevels=True)

		pts = [roi.mapToParent(h['item'].pos()) for h in roi.handles]
		tv = QtGui.QTransform()
		tv.translate(pts[0].y(), self.axisZarr[0])
		scale = (pts[1].y()-pts[0].y())/img.shape[0]
		tv.scale(scale, float(self.axisZarr[-1] - self.axisZarr[0]) / len(self.axisZarr))
		self.vSliceImage.setTransform(tv)

	def on_dataChanged(self):
		self.updateImageAxes()
		self.updateImage()
		#if self.showSlices:
			#self.thirdDimSlicesCheckBox.setCheckState(QtCore.Qt.Unchecked)
		#self.removeAllROIs()




	## ROI
	# 
	#
	def addHorIlRoi(self):
		roi = self.addSingleLineROI(self.ROIPlotItemBottomWidget)
		self.on_roiSelected(roi)

	def remHorIlRoi(self):
		if len(self.roiList[CONST_ROI_HOR_LIST]) > 0:
			self.removeROI(self.roiList[CONST_ROI_HOR_LIST][0])

	def addVerIlRoi(self):
		roi = self.addSingleLineROI(self.ROIPlotItemRightWidget)
		self.on_roiSelected(roi)

	def remVerIlRoi(self):
		if len(self.roiList[CONST_ROI_VER_LIST]) > 0:
			self.removeROI(self.roiList[CONST_ROI_VER_LIST][0])

	def addBoxRoi(self):
		roi = self.addRectROI()
		self.on_roiSelected(roi)

	def remBoxRoi(self):
		if len(self.roiList[CONST_ROI_BOTH_LIST]) > 0:
			self.removeROI(self.roiList[CONST_ROI_BOTH_LIST][0])

	def remRoi(self,roi):
		self.removeROI(roi)


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

		self.plotVolumeItem.translate(-size[0] / 2, -size[1] / 2, -size[2] / 2)

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
		# d2[..., 3] = 10

		# d2[..., 0] = positive * (255./positive.max())
		# d2[..., 1] = negative * (255./negative.max())
		# d2[..., 2] = d2[...,1]
		# d2[..., 3] = 10
		d2[..., 3] = data
		d2[..., 3] = (d2[..., 3].astype(float) / 255.) ** 2 * 255

		d2[:, 0, 0] = [255, 0, 0, 100]
		d2[0, :, 0] = [0, 255, 0, 100]
		d2[0, 0, :] = [0, 0, 255, 100]

		# print d2[...,3]

		self.plotVolumeItem.setData(d2)

	def setThreshold(self, val):
		if type(val) is int:
			self.threshold = val
			self.updateImage()
		else:
			print "Error: Value not int"


class glImageSlicesPlot(QtGui.QWidget):
	def __init__(self):
		super(glImageSlicesPlot, self).__init__()

		self.cData = None
		self.initUI()

	def initUI(self):
		grid = QtGui.QGridLayout()
		self.setLayout(grid)
		self.view = gl.GLViewWidget()
		grid.addWidget(self.view)

		self.view.setBackgroundColor(100, 100, 100)
		self.view.opts['distance'] = 200

		self.v1 = gl.GLImageItem(None)
		self.v2 = gl.GLImageItem(None)
		self.v3 = gl.GLImageItem(None)
		self.view.addItem(self.v1)
		self.view.addItem(self.v2)
		self.view.addItem(self.v3)

		ax = gl.GLAxisItem()
		self.view.addItem(ax)

	def setData(self, cData, metaDataOutput=None):
		if cData != None:
			self.cData = cData
		else:
			return

		self.updateImage()

	def updateImage(self):
		shape = self.cData.data.shape

		## slice out three planes, convert to RGBA for OpenGL texture
		levels = (self.cData.data.min(), self.cData.data.max())
		tex1 = pg.makeRGBA(self.cData.data[shape[0] / 2], levels=levels)[0]  # yz plane
		tex2 = pg.makeRGBA(self.cData.data[:, shape[1] / 2], levels=levels)[0]  # xz plane
		tex3 = pg.makeRGBA(self.cData.data[:, :, shape[2] / 2], levels=levels)[0]  # xy plane
		# tex1[:,:,3] = 128
		# tex2[:,:,3] = 128
		# tex3[:,:,3] = 128

		## Create three image items from textures, add to view
		self.v1.setData(tex1)
		self.v1.translate(-shape[1] / 2, -shape[2] / 2, 0)
		self.v1.rotate(90, 0, 0, 1)
		self.v1.rotate(-90, 0, 1, 0)
		self.v2.setData(tex2)
		self.v2.translate(-shape[0] / 2, -shape[2] / 2, 0)
		self.v2.rotate(-90, 1, 0, 0)
		self.v3.setData(tex3)
		self.v3.translate(-shape[0] / 2, -shape[1] / 2, 0)




class SingleLineROI(pg.ROI):

	originalState = None
	userRemovable = True


	def __init__(self, positions=(None, None), pos=None, handles=(None, None), scaleCenter=None, userRemovable = True, **args):
		if pos is None:
			pos = [0, 0]
		if scaleCenter is None:
			scaleCenter = [0, 0]
		pg.ROI.__init__(self, pos, [1, 1], invertible=True, **args)
		# ROI.__init__(self, positions[0])
		if len(positions) > 2:
			raise Exception(
				"LineSegmentROI must be defined by exactly 2 positions. For more points, use PolyLineROI.")
		for i, p in enumerate(positions):
			self.addScaleRotateHandle(p, center=scaleCenter, item=handles[i])

		self.originalState = self.saveState()
		self.userRemovable = userRemovable


	def listPoints(self):
		return [p['item'].pos() for p in self.handles]


	def paint(self, p, *args):
		p.setRenderHint(QtGui.QPainter.Antialiasing)
		p.setPen(self.currentPen)
		h1 = self.handles[0]['item'].pos()
		h2 = self.handles[1]['item'].pos()
		p.drawLine(h1, h2)

	def refToImage(self,image):
		imgPts = [self.mapToItem(image, h['item'].pos()) for h in self.handles]
		return imgPts

	def updateLine(self, positions, handles=(None, None)):
		self.clearPoints()
		center = [(positions[0].x()+positions[1].x())/2,(positions[0].y()+positions[1].y())/2]
		for i, p in enumerate(positions):
			self.addScaleRotateHandle(p, center=center, item=handles[i])
   
	def clearPoints(self):
		"""
		Remove all handles and segments.
		"""
		while len(self.handles) > 0:
			self.removeHandle(self.handles[0]['item'])

	def boundingRect(self):
		return self.shape().boundingRect()


	def shape(self):
		p = QtGui.QPainterPath()

		h1 = self.handles[0]['item'].pos()
		h2 = self.handles[1]['item'].pos()
		dh = h2 - h1
		if dh.length() == 0:
			return p
		pxv = self.pixelVectors(dh)[1]
		if pxv is None:
			return p

		pxv *= 4

		p.moveTo(h1 + pxv)
		p.lineTo(h2 + pxv)
		p.lineTo(h2 - pxv)
		p.lineTo(h1 - pxv)
		p.lineTo(h1 + pxv)

		return p

	def checkPointMove(self, handle, pos, modifiers):
		"""When handles move, they must ask the ROI if the move is acceptable.
		By default, this always returns True. Subclasses may wish override.
		"""

		# imgPts = [self.mapToParent(h['item'].pos()) for h in self.handles]
		# print imgPts

		# if imgPts[0].x() < self.onPlot.posOrigoAxisHorizontal or imgPts[0].x() > self.onPlot.posOrigoAxisHorizontal + self.onPlot.lengthAxisHorizontal or imgPts[0].y() < self.onPlot.posOrigoAxisVertical or imgPts[0].y() > self.onPlot.posOrigoAxisVertical + self.onPlot.lengthAxisVertical:
		# 	return False
		# elif imgPts[1].x() < self.onPlot.posOrigoAxisHorizontal or imgPts[1].x() > self.onPlot.posOrigoAxisHorizontal + self.onPlot.lengthAxisHorizontal or imgPts[1].y() < self.onPlot.posOrigoAxisVertical or imgPts[1].y() > self.onPlot.posOrigoAxisVertical + self.onPlot.lengthAxisVertical:
		# 	return False
		# else:
		# 	return True
		return True

	
	def getArrayRegion(self, data, img, axes=(0, 1)):
		"""
		Use the position of this ROI relative to an imageItem to pull a slice
		from an array.

		Since this pulls 1D data from a 2D coordinate system, the return value
		will have ndim = data.ndim-1

		See ROI.getArrayRegion() for a description of the arguments.
		"""

		imgPts = [self.mapToItem(img, h['item'].pos()) for h in self.handles]
		rgns = []
		for i in range(len(imgPts) - 1):
			d = pg.Point(imgPts[i + 1] - imgPts[i])
			o = pg.Point(imgPts[i])
			r = pg.affineSlice(data, shape=(int(d.length()),), vectors=[pg.Point(d.norm())], origin=o, axes=axes, order=1)
			rgns.append(r)

		return np.concatenate(rgns, axis=axes[0])

	def reset(self):
		self.setState(self.originalState)

class RectangularROI(pg.RectROI):
	"""
	Rectangular ROI subclass with a single scale handle at the top-right corner.
	
	============== =============================================================
	**Arguments**
	pos            (length-2 sequence) The position of the ROI origin.
	               See ROI().
	size           (length-2 sequence) The size of the ROI. See ROI().
	centered       (bool) If True, scale handles affect the ROI relative to its
	               center, rather than its origin.
	sideScalers    (bool) If True, extra scale handles are added at the top and 
	               right edges.
	\**args        All extra keyword arguments are passed to ROI()
	============== =============================================================
	
	"""
	originalState = None
	userRemovable = True

	def __init__(self, pos, size, **args):
		#QtGui.QGraphicsRectItem.__init__(self, 0, 0, size[0], size[1])
		pg.RectROI.__init__(self, pos, size, **args)
		self.originalState = self.saveState()
		self.userRemovable = True

	def reset(self):
		self.setState(self.originalState)