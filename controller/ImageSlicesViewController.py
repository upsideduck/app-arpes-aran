from helper.config import *
from PySide import QtCore, QtGui 
from ext.nexpy.api import nexus as nx
import numpy as np
from view.pyqtgraphwidget import *
from view.ImageSlicesView import Ui_ImageSlicesViewer


class ImageSlicesViewController(QtGui.QWidget):

	def __init__(self, cData, parent=None):
		super(ImageSlicesViewController, self ).__init__()
		self.view = Ui_ImageSlicesViewer()
		self.view.setupUi(self)

		self.view.testBtn.clicked.connect(self.on_testBtn)

		self.cData = cData

		pg.setConfigOption('foreground', 'k')
		pg.setConfigOption('background', None)

		self.plotWidget = glImageSlicesPlot()
		self.plotWidget.setData(self.cData)

		self.plotWidget.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	

		self.view.plotLayout.addWidget(self.plotWidget)

	def on_testBtn(self):
		print "test"