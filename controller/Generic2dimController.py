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

	def __init__(self, cData, view=None, parent=None):
		if view == None:
			view = Ui_Generic2dimWindow()
		super(Generic2dimController, self ).__init__(cData,view,parent)
		parent.view.menubar = None

	def configure_views(self):	
		super(Generic2dimController,self).configure_views()
		self.init2DView()
		self.setWindowTitle("Generic: "+self.windowTitle)

	def init2DView(self):
		super(Generic2dimController,self).init2DView()
		self.DataPlot.plot2DData(self.cData.data, 
				self.cData.axis1, 
				self.cData.axis2, 
				self.cData.axis1name, 
				self.cData.axis2name)
		self.setup2DTools()
		self.view.dataView.setText(self.cData.root.NXentry[self.cData.entryId].tree)

	def onP_dataChanged(self):
		super(Generic2dimController,self).onP_dataChanged()
		self.DataPlot.plot2DData(self.cData.data, 
				self.cData.axis1, 
				self.cData.axis2, 
				self.cData.axis1name, 
				self.cData.axis2name)
		self.setup2DTools()
		 
		