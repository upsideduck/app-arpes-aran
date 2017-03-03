from helper.config import *
from PyQt4 import QtCore, QtGui 
from nexpy.api import nexus as nx
import numpy as np
from view.GenericPQGView import Ui_GenericPQGView
from view.pyqtgraphwidget import *
from view.CustomWidgets import Tools_ROIWidget
from view.CustomWidgets import Tools_ImageWidget
from view.CustomWidgets import Tools_ViewsWidget
from view.CustomWidgets import Tools_ARPESWidget
from controller.VolumeViewController import *
from controller.ImageSlicesViewController import *
from model.ArpesData import MakeMapWorker
from math import *

class ARPESPQGController(QtGui.QMainWindow):

	__selectedRoi = None
	
	def getSelectedRoi(self):
		return self.__selectedRoi

	def setSelectedRoi(self, d):
		self.__selectedRoi = d
		if d == None:
			self.enableSelectedROITools(False)
		else:
			self.enableSelectedROITools(True)
			self.updateRoiTools()

	def delSelectedRoi(self):
		print "delete selected roi"
		del self.__selectedRoi

	selectedRoi = property(getSelectedRoi,setSelectedRoi,delSelectedRoi)

	def __init__(self, cData, parent=None):
		super(ARPESPQGController, self ).__init__()
		self.view = Ui_GenericPQGView()
		self.view.setupUi(self)

		self.windows = []

		self.setWindowTitle("ARPES View")
		self.cData = cData

		pg.setConfigOption('foreground', 'k')
		pg.setConfigOption('background', None)

		self.plotWidget = standardPlot(showHistogram=True, showSlices=True)
		self.plotWidget.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
		self.view.mainPlotLayout.addWidget(self.plotWidget)

		self.imageTools = Tools_ImageWidget(self)
		self.view.toolsLayout.addWidget(self.imageTools)

		self.roiTools = Tools_ROIWidget(self)		
		self.view.toolsLayout.addWidget(self.roiTools)
		self.plotWidget.roiSelected.connect(self.on_roiSelected)


		if len(self.cData.data.shape) == 3:
			viewsTools = Tools_ViewsWidget(self)
			self.view.toolsLayout.addWidget(viewsTools)

		self.plotWidget.setData(self.cData, metaDataOutput=self.view.metaDataView)
		

		self.arpesTools = Tools_ARPESWidget(self)
		self.view.toolsLayout.addWidget(self.arpesTools)

		spacerItem = QtGui.QSpacerItem(40, 2000, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.view.toolsLayout.addItem(spacerItem)

	def closeEvent(self,event):
		for window in self.windows:		# Close all windows if  window is closed
			window.close()	


	## ROI tools slots
	# View part
	def on_btnAddHorIlRoi(self):
		self.plotWidget.addHorIlRoi()

	def on_btnAddVerIlRoi(self):
		self.plotWidget.addVerIlRoi()

	def on_btnAddBoxRoi(self):
		self.plotWidget.addBoxRoi()

	def on_btnRemRoi(self):
		self.plotWidget.remRoi(self.selectedRoi)
		self.selectedRoi = None

	def on_btnResetRoi(self):
		self.selectedRoi.reset()
		

	def on_screenAngleROICheckBox(self,val):
		self.updateRoiTools()

	# Controller part
	def on_roiSelected(self, roi):
		if self.selectedRoi:
			self.selectedRoi.sigRegionChanged.disconnect(self.updateRoiTools)
		self.selectedRoi = roi
		self.selectedRoi.sigRegionChanged.connect(self.updateRoiTools)
		self.updateRoiTools()


	def angle_trunc(self,a):
	    while a < 0.0:
	        a += pi * 2
	    return a

	def getAngleBetweenPoints(self,x_orig, y_orig, x_landmark, y_landmark):
	    deltaY = y_landmark - y_orig
	    deltaX = x_landmark - x_orig
	    return atan2(deltaY, deltaX)

	def currentROIAngle(self):
		if self.roiTools.ui.screenAngleROICheckBox.isChecked():
			imgPts = [self.selectedRoi.mapToItem(self.plotWidget.image,h['item'].pos()) for h in self.selectedRoi.handles]
			return self.getAngleBetweenPoints(imgPts[0].x(),imgPts[0].y(),imgPts[1].x(),imgPts[1].y())/2/pi*360
		else:
			return self.selectedRoi.angle()

	def ROIAngleToSet(self,val):
		if self.roiTools.ui.screenAngleROICheckBox.isChecked():
			pts = [self.selectedRoi.mapToParent(h['item'].pos()) for h in self.selectedRoi.handles]
			return self.getAngleBetweenPoints(pts[0].x(),pts[0].y(),pts[1].x(),pts[1].y())/2/pi*360
		else:
			return val


	def updateRoiTools(self):
		if self.selectedRoi == None:
			return
		self.roiTools.ui.anlgeROILbl.setText(str(round(self.currentROIAngle(),1)))
	
	def enableSelectedROITools(self,state = True):
		self.roiTools.ui.screenAngleROICheckBox.setEnabled(state)
		self.roiTools.ui.resetROIBtn.setEnabled(state)
		if self.selectedRoi:
			if not self.selectedRoi.userRemovable:
				self.roiTools.ui.removeROIBtn.setEnabled(False)
			else:
				self.roiTools.ui.removeROIBtn.setEnabled(state)
		else:
			self.roiTools.ui.removeROIBtn.setEnabled(state)


	## Views tools slots
	def on_openVolumeView(self):
		self.windows.append(VolumeViewController(self.cData))
		self.windows[-1].show()

	def on_openSlicesView(self):
		self.windows.append(ImageSlicesViewController(self.cData))
		self.windows[-1].show()

	## Image tools slots
	def on_imageRotationSliderMoved(self,val):
		angle = val/10.0
		self.plotWidget.rotation = angle
		
		self.imageTools.ui.imageRotationSB.valueChanged.disconnect(self.on_imageRotationSBChanged)
		self.imageTools.ui.imageRotationSB.setValue(angle)
		self.imageTools.ui.imageRotationSB.valueChanged[float].connect(self.on_imageRotationSBChanged)
		

	def on_imageRotationSBChanged(self,val):
		angle = val
	
		self.plotWidget.rotateImage(angle)
		
		self.imageTools.ui.imageRotationSlider.valueChanged.disconnect(self.on_imageRotationSliderMoved)
		self.imageTools.ui.imageRotationSlider.setValue(angle*10)
		self.imageTools.ui.imageRotationSlider.valueChanged[int].connect(self.on_imageRotationSliderMoved)

	def on_imageRotationSliderReleased(self):
		self.plotWidget.updateAuxiliaryPlots()

	## ARPES tools slots
	def on_cboxKSpaceChanged(self,val):

		self.selectedRoi = None
		if val == QtCore.Qt.Checked and self.cData.kdata is None:
			self.mapCreationThread = QtCore.QThread()  # no parent!
			self.mapWorker = MakeMapWorker(self.cData.root)
			self.mapWorker.moveToThread(self.mapCreationThread)
			self.mapWorker.finished.connect(self.mapCreationThread.quit)
			self.mapWorker.progress.connect(self.on_mapWorkerUpdateProgress)
			self.mapWorker.finished.connect(self.on_mapWorkerDone)	
			self.mapCreationThread.start()
			self.arpesTools.kSpaceCheckBox.setEnabled(False)
			#self.progresslabel = QtGui.QLabel()
			#self.view.statusBar.addWidget(self.progresslabel)
	

		if self.cData.kdata is None and val == QtCore.Qt.Checked:
			if self.cData.is3D():
				QtCore.QMetaObject.invokeMethod(self.mapWorker, 'makekMapFrom3D', QtCore.Qt.QueuedConnection)
			elif self.cData.is2D():
				self.mapWorker.makekMapFrom2D()
		elif not self.cData.kdata is None and val == QtCore.Qt.Checked:
			self.cData.setkSpace()	
		elif val == QtCore.Qt.Unchecked:
			self.cData.setAngleSpace()

	#@QtCore.Slot(tuple)
	def on_mapWorkerDone(self,result):
		self.cData.kx = result[0]
		self.cData.ky = result[1]
		self.cData.kdata = result[2]
		self.mapWorker.finished.disconnect(self.mapCreationThread.quit)
		self.mapWorker.progress.disconnect(self.on_mapWorkerUpdateProgress)
		self.mapWorker.finished.disconnect(self.on_mapWorkerDone)	
		#self.mapCreationThread = None
		#self.mapWorker = None
		self.arpesTools.kSpaceCheckBox.setEnabled(True)
		self.cData.setkSpace()
		self.view.statusbar.showMessage("Calculation of kxky is done",2000)

	#@QtCore.Slot(float)
	def on_mapWorkerUpdateProgress(self, result):
		self.view.statusbar.showMessage("Calculating kxky...",10000)
		#print result	
