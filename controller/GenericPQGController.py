from helper.constants import *
from PySide import QtCore, QtGui 
from nexpy.api import nexus as nx
import numpy as np
from view.GenericPQGView import Ui_GenericPQGView
from view.pyqtgraphwidget import *
from view.CustomWidgets import Tools_ROIWidget

class GenericPQGController(QtGui.QMainWindow):

	def __init__(self, cData, parent=None):
		super(GenericPQGController, self ).__init__()
		self.view = Ui_GenericPQGView()
		self.view.setupUi(self)
		self.setWindowTitle("Generic View")
		self.cData = cData

		pg.setConfigOption('foreground', 'k')
		pg.setConfigOption('background', None)

		self.plotWidget = standardPlot()
		self.view.hLayout.addWidget(self.plotWidget)

		tools = Tools_ROIWidget(self)
		self.view.toolsLayout.addWidget(tools)
		self.plotWidget.setData(self.cData, metaDataOutput=self.view.dataView)
		

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
