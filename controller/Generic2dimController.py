#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from GenericMultiDimBaseController import *
from view.Generic2dimView import Ui_Generic2dimWindow

##############################################################
# Class: MainController
# This is the main controller of the program
# Initial view, models and genereal setup is executed here
#

class Generic2dimController(GenericMultiDimBaseController):

	def __init__(self, cData, parent=None):
		super(Generic2dimController, self ).__init__(cData,Ui_Generic2dimWindow(),parent)
		self.configure_views()
		parent.view.menubar = None

	def configure_views(self):	
		super(Generic2dimController,self).configure_views()
		self.init2DView()


	def init2DView(self):
		super(Generic2dimController,self).init2DView()
		self.DataPlot.plot2DData(self.cData.data, 
				self.cData.axis1, 
				self.cData.axis2, 
				self.cData.axis1name, 
				self.cData.axis2name)
		self.setup2DTools()
		self.view.dataView.setText(self.cData.root.NXentry[self.cData.entryId].tree)

	def on_kSpaceCheckBoxChanged(self,val):
		super(Generic2dimController,self).on_kSpaceCheckBoxChanged(val)
		if self.cData.kdata == None and val == QtCore.Qt.Checked:
			QtCore.QMetaObject.invokeMethod(self.mapWorker, 'makekMapFrom2D', QtCore.Qt.QueuedConnection)
		elif not self.cData.kdata == None and val == QtCore.Qt.Checked:
			self.cData.setkSpace()
		elif val == QtCore.Qt.Unchecked:
			self.cData.setAngleSpace()

	def on_mapWorkerDone(self,result):
		super(Generic2dimController,self).on_mapWorkerDone(result)
		self.cData.setkSpace()

	def onP_dataChanged(self):
		super(Generic2dimController,self).onP_dataChanged()
		self.DataPlot.plot2DData(self.cData.data, 
				self.cData.axis1, 
				self.cData.axis2, 
				self.cData.axis1name, 
				self.cData.axis2name)
		self.setup2DTools()
		 
		