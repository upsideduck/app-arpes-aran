from helper.constants import *
from PySide import QtCore, QtGui 
from ext.nexpy.api import nexus as nx
import numpy as np
from view.GenericPQGView import Ui_GenericPQGView
from view.pyqtgraphwidget import *
from view.CustomWidgets import Tools_ROIWidget
from view.CustomWidgets import Tools_ViewsWidget
from view.CustomWidgets import Tools_ARPESWidget
from controller.VolumeViewController import *
from controller.ImageSlicesViewController import *
from model.ArpesData import MakeMapWorker


class ARPESPQGController(QtGui.QMainWindow):

	__selectedRoi = None
	
	def getSelectedRoi(self):
		return self.__selectedRoi

	def setSelectedRoi(self, d):
		self.__selectedRoi = d
		print "set"

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

		roiTools = Tools_ROIWidget(self)		
		self.view.toolsLayout.addWidget(roiTools)
		self.plotWidget.roiSelected.connect(self.on_roiSelected)

		
		if len(self.cData.data.shape) == 3:
			viewsTools = Tools_ViewsWidget(self)
			self.view.toolsLayout.addWidget(viewsTools)

		self.plotWidget.setData(self.cData, metaDataOutput=self.view.metaDataView)
		

		self.arpesTools = Tools_ARPESWidget(self)
		self.view.toolsLayout.addWidget(self.arpesTools)

	def closeEvent(self,event):
		for window in self.windows:		# Close all windows if  window is closed
			window.close()	


	## ROI tools slots
	def on_btnAddHorIlRoi(self):
		self.plotWidget.addHorIlRoi()

	def on_btnRemHorIlRoi(self):
		self.plotWidget.remHorIlRoi()

	def on_btnAddVerIlRoi(self):
		self.plotWidget.addVerIlRoi()

	def on_btnRemVerIlRoi(self):
		self.plotWidget.remVerIlRoi()

	def on_btnAddBoxRoi(self):
		self.plotWidget.addBoxRoi()

	def on_btnRemBoxRoi(self):
		self.plotWidget.remBoxRoi()

	def on_roiSelected(self, roi):
		self.selectedRoi = roi

	## Views tools slots
	def on_openVolumeView(self):
		self.windows.append(VolumeViewController(self.cData))
		self.windows[-1].show()

	def on_openSlicesView(self):
		self.windows.append(ImageSlicesViewController(self.cData))
		self.windows[-1].show()

	## ARPES tools slots
	def on_cboxKSpaceChanged(self,val):
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
