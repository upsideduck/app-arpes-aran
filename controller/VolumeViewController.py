from helper.config import *
from PyQt4 import QtCore, QtGui 
from ext.nexpy.api import nexus as nx
import numpy as np
from view.pyqtgraphwidget import *
from view.VolumeView import Ui_VolumeViewer


class VolumeViewController(QtGui.QWidget):

	def __init__(self, cData, parent=None):
		super(VolumeViewController, self ).__init__()
		self.view = Ui_VolumeViewer()
		self.view.setupUi(self)

		self.view.thresholdBtn.clicked.connect(self.on_thresholdBtn)
		self.view.thresholdLineEdit.setValidator(QtGui.QIntValidator())	

		self.cData = cData

		pg.setConfigOption('foreground', 'k')
		pg.setConfigOption('background', None)

		self.plotWidget = glVolumePlot()
		self.plotWidget.setData(self.cData)

		self.plotWidget.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	

		self.view.plotLayout.addWidget(self.plotWidget)

	def on_thresholdBtn(self):
		self.plotWidget.setThreshold(int(self.view.thresholdLineEdit.text()))