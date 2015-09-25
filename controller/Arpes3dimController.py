#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from Generic3dimController import *
from view.Generic3dimView import Ui_Generic3dimWindow
from view.CustomWidgets import ArpesToolsWidget
from model.ArpesData import MakeMapWorker


##############################################################
# Class: Arpes2dimController
# 
# 
#

class Arpes3dimController(Generic3dimController):

	def __init__(self, cData,view=None, parent=None):
		if view == None:
			view = Ui_Generic3dimWindow()
		super(Arpes3dimController, self ).__init__(cData,view,parent)



	def configure_views(self):
		super(Arpes3dimController,self).configure_views()
		self.setWindowTitle("ARPES: "+self.windowTitle)
		tools = ArpesToolsWidget()
		self.view.toolsHorizontalLayout.addWidget(tools)
		self.arpesToolsView = tools.ui	
		# k-space
		self.arpesToolsView.kSpaceCheckBox.stateChanged[int].connect(self.on_kSpaceCheckBoxChanged)
		
	
	def on_kSpaceCheckBoxChanged(self,val):
		if val == QtCore.Qt.Checked and self.cData.kdata is None:
			self.mapCreationThread = QtCore.QThread()  # no parent!
			self.mapWorker = MakeMapWorker(self.cData.root)
			self.mapWorker.moveToThread(self.mapCreationThread)
			self.mapWorker.finished.connect(self.mapCreationThread.quit)
			self.mapWorker.progress.connect(self.on_mapWorkerUpdateProgress)
			self.mapWorker.finished.connect(self.on_mapWorkerDone)	
			self.mapCreationThread.start()
			self.arpesToolsView.kSpaceCheckBox.setEnabled(False)
			#self.progresslabel = QtGui.QLabel()
			#self.view.statusBar.addWidget(self.progresslabel)
		if self.cData.kdata is None and val == QtCore.Qt.Checked:
			QtCore.QMetaObject.invokeMethod(self.mapWorker, 'makekMapFrom3D', QtCore.Qt.QueuedConnection)
		elif not self.cData.kdata is None and val == QtCore.Qt.Checked:
			self.cData.setkSpace()	
		elif val == QtCore.Qt.Unchecked:
			self.cData.setAngleSpace()

	#@QtCore.Slot(tuple)
	def on_mapWorkerDone(self, result):
		self.cData.k = result[0]
		self.cData.krotation = result[1]
		self.cData.kdata = result[2]
		self.mapWorker.finished.disconnect(self.mapCreationThread.quit)
		self.mapWorker.progress.disconnect(self.on_mapWorkerUpdateProgress)
		self.mapWorker.finished.disconnect(self.on_mapWorkerDone)	
		self.mapCreationThread = None
		self.mapWorker = None
		self.arpesToolsView.kSpaceCheckBox.setEnabled(True)
		self.cData.setkSpace()

	#@QtCore.Slot(float)
	def on_mapWorkerUpdateProgress(self, result):
		self.view.statusBar.showMessage("Calculating k-map: "+str(int(result*100))+"% done",2000)