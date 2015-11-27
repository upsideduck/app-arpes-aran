#!/usr/bin/python
# -*- coding: utf-8 -*-
from helper.constants import *
import sys
from PySide import QtCore, QtGui 
from view.mainView import Ui_MainWindow
from controller.ArpesBuildController import *
from controller.GenericPQGController import *
from controller.ARPESPQGController import *
from nexpy.api import nexus as nx
import numpy as np
from copy import *
import pdb

import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
import matplotlib.pyplot as plt
from view.matplotlibwidget import *
from model.ArpesData import *
from helper.SpectrumFile import *


##############################################################
# Class: MainController
# This is the main controller of the program
# Initial view, models and genereal setup is executed here
#

class MainController(QtGui.QMainWindow):

	windows = []

	def __init__(self, parent=None):
		super(MainController, self ).__init__(parent)
		self.view = Ui_MainWindow()
		self.view.setupUi(self)
		self.cData = None

		self.configure_views()

	def closeEvent(self,event):
		matplotlib.pyplot.close("all")
		for window in self.windows:		# Close all windows if main window is closed
			window.close()	

	def configure_views(self):	
		## Matplotlib widget
		# Do this first to be ready with default values
 		self.DataPlot = MatplotlibWidget(self.view)
		# create a layout inside the blank widget and add the matplotlib widget        
		layout = QtGui.QVBoxLayout(self.view.plotWidget)        
		layout.addWidget(self.DataPlot)	

		## Folder View
		# Setup folder model
		self.dirmodel = QtGui.QFileSystemModel()
		# Don't show files, just folders in folder view
		self.dirmodel.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllDirs)
		self.view.dirView.setModel(self.dirmodel)
		self.view.dirView.clicked[QtCore.QModelIndex].connect(self.on_clicked_folderselected) 
		self.selectionDirModel = self.view.dirView.selectionModel()
		# Don't show columns for size, file type, and last modified
		self.view.dirView.setHeaderHidden(True)
		self.view.dirView.hideColumn(1)
		self.view.dirView.hideColumn(2)
		self.view.dirView.hideColumn(3)
		self.view.dirView.setRootIndex(self.dirmodel.setRootPath(DATA_ROOT_FOLDER))

		## File View
		# Setup file model
		self.filemodel = QtGui.QFileSystemModel()
		# Don't show folders, just files
		self.filemodel.setNameFilters(["*.nxs","*sp2"])
		self.filemodel.setNameFilterDisables(False)
		self.filemodel.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Files)
		self.view.fileView.setModel(self.filemodel)
		#self.view.fileView.clicked[QtCore.QModelIndex].connect(self.clicked_fileselected)
		self.selectionFileModel = self.view.fileView.selectionModel()
		self.selectionFileModel.selectionChanged.connect(self.on_fileselected)
		self.view.fileView.setRootIndex(self.filemodel.setRootPath(DATA_ROOT_FOLDER))
		# Configure fileView
		self.view.fileView.header().resizeSection(0, 190)
		self.view.fileView.header().resizeSection(1, 80)
		self.view.fileView.header().resizeSection(3, 110)
		self.view.fileView.hideColumn(2)  # Hide extension column, all are nxs

		## Tools
		self.view.loadBtn.clicked.connect(self.on_loadBtnClicked)
		self.view.buildBtn.clicked.connect(self.on_buildBtnClicked)
		self.view.entriesBox.currentIndexChanged[int].connect(self.on_entriesBoxChanged)
		

	## Slots
	def on_clicked_folderselected(self, index):
		# Get selected path of folder view
		index = self.selectionDirModel.currentIndex()
		dir_path = self.dirmodel.filePath(index)
		self.filemodel.setRootPath(dir_path)
		self.view.fileView.setRootIndex(self.filemodel.index(dir_path))

	def on_fileselected(self, selected, deselected):
		if self.cData:
			del self.cData

		indexes = selected.indexes()
		# Get selected path of file view
		file_path = self.filemodel.filePath(indexes[0])
		self.cData = SpectrumFile.load(file_path)
		if self.cData == None:
			return
		self.updatePlot()
		self.updateEntryBox()
		self.view.dataView.setText(self.cData.root.NXentry[self.cData.entryId].tree)
		self.view.loadBtn.setEnabled(True)

	def on_loadBtnClicked(self):
		if isinstance(self.cData, ArpesData):	
			self.windows.append(ARPESPQGController(deepcopy(self.cData)))
		elif isinstance(self.cData, GenericData):
			self.windows.append(GenericPQGController(copy(self.cData)))
		else:
			print "Error: Do not recognize the data format"

		self.windows[-1].show()


	def on_buildBtnClicked(self):
		self.windows.append(ArpesBuildController(self))
		self.windows[-1].show()

	def on_entriesBoxChanged(self,index):
		newEntryId = self.view.entriesBox.itemData(index)
		self.cData.entryId = newEntryId
		self.view.dataView.setText(self.cData.root.NXentry[self.cData.entryId].tree)
		self.updatePlot()

	## Helper functions
	def updatePlot(self):
		if len(self.cData.data.shape) == 2:
			self.DataPlot.plot2DData(self.cData.data, 
				self.cData.axis1, 
				self.cData.axis2, 
				self.cData.axis1name, 
				self.cData.axis2name)
		elif len(self.cData.data.shape) == 3:
			self.DataPlot.plot2DData(self.cData.data[:,:,0], 
				self.cData.axis2, 
				self.cData.axis3, 
				self.cData.axis2name, 
				self.cData.axis3name)

	def updateEntryBox(self):
		self.view.entriesBox.currentIndexChanged[int].disconnect(self.on_entriesBoxChanged)
		self.view.entriesBox.clear()
		for i, m in enumerate(self.cData.root.entries):
			self.view.entriesBox.addItem(m, i)
		self.view.entriesBox.currentIndexChanged[int].connect(self.on_entriesBoxChanged)

def main():
	app = QtGui.QApplication(sys.argv)
	mController = MainController()
	mController.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()