from helper.constants import *
import sys
from PySide import QtCore, QtGui 
from GenericMultiDimBaseController import *
from view.Generic3dimView import Ui_Generic3dimWindow
try:
	from mayavi import mlab
	STATUS_MAYAVI_AVAILABLE = True
except:
	STATUS_MAYAVI_AVAILABLE = False


##############################################################
# Class: MainController
# This is the main controller of the program
# Initial view, models and genereal setup is executed here
#

class Generic3dimController(GenericMultiDimBaseController):

	def __init__(self, cData, parent=None):
		super(Generic3dimController, self ).__init__(cData,Ui_Generic3dimWindow(),parent)
		self.configure_views()

	def configure_views(self):	
		super(Generic3dimController,self).configure_views()

		self.view.open3DDisplay.clicked.connect(self.open3DViewer)
		self.view.zaxisSlider.valueChanged[int].connect(self.on_d3SliderMoved)
		self.view.zaxisSlider.sliderReleased.connect(self.dataplotChanged)
		# 3D plot picker
		for i in range(0,len(CONST_3DPLOTTYPES)):
			self.view.d3PlotChooser.addItem(CONST_3DPLOTTYPES[i])
		self.view.d3PlotChooser.currentIndexChanged[int].connect(self.on_d3PlotTypeChanged)

		self.init3DView()



	def init3DView(self):
		super(Generic3dimController,self).init2DView()
		self.replotData(0,0)
		if STATUS_MAYAVI_AVAILABLE:
			self.view.open3DDisplay.setEnabled(True)
		else:
			self.view.open3DDisplay.setEnabled(False)
		self.view.d3PlotChooser.setCurrentIndex(0)
		self.setup2DTools()
		self.setup3DTools(self.cData.axis1name, self.cData.axis1)		# Default
		self.view.dataView.setText(self.cData.root.tree)

	def setup3DTools(self, zaxisname, zaxisdata):
		self.view.zaxisNameLbl.setText(zaxisname)
		self.view.zaxisValueLbl.setText(str(np.asarray(zaxisdata)[0]))
		self.view.zaxisSlider.setRange(0,len(zaxisdata)-1)
		self.view.zaxisSlider.setValue(0)

	def open3DViewer(self):
		s = np.asarray(self.cData.data) 
		src = mlab.pipeline.scalar_field(s, scale=[1,1,8])
		mlab.pipeline.iso_surface(src, opacity=0.4)
		mlab.pipeline.scalar_cut_plane(src,plane_orientation='y_axes',view_controls=False)
		mlab.pipeline.scalar_cut_plane(src,plane_orientation='z_axes',view_controls=False)
		mlab.pipeline.scalar_cut_plane(src,plane_orientation='x_axes',view_controls=True)
		

	def replotData(self, index, val):
		if index == CONST_3DPLOTTYPE_EAVSRA:
			self.DataPlot.plot2DData(self.cData.data[:,:,int(val)], 
				self.cData.axis2, 
				self.cData.axis3, 
				self.cData.axis2name, 
				self.cData.axis3name)
			self.view.zaxisValueLbl.setText(str(round(np.asarray(self.cData.axis1)[int(val)],4)))
		elif index == CONST_3DPLOTTYPE_EAVSE:
			self.DataPlot.plot2DData(self.cData.data[int(val),:,:],
				self.cData.axis1, 
				self.cData.axis2, 
				self.cData.axis1name, 
				self.cData.axis2name)
			self.view.zaxisValueLbl.setText(str(round(np.asarray(self.cData.axis3)[int(val)],4)))
		elif index == CONST_3DPLOTTYPE_RAVSE:
			self.DataPlot.plot2DData(self.cData.data[:,int(val),:],
				self.cData.axis1, 
				self.cData.axis3, 
				self.cData.axis1name, 
				self.cData.axis3name)
			self.view.zaxisValueLbl.setText(str(round(np.asarray(self.cData.axis2)[int(val)],4)))
		else:
			print "??"


	## Slots
	def on_kSpaceCheckBoxChanged(self,val):
		super(Generic3dimController,self).on_kSpaceCheckBoxChanged(val)
		if self.cData.kdata == None and val == QtCore.Qt.Checked:
			QtCore.QMetaObject.invokeMethod(self.mapWorker, 'makekMapFrom3D', QtCore.Qt.QueuedConnection)
		elif not self.cData.kdata == None and val == QtCore.Qt.Checked:
			self.cData.setkSpace()
		elif val == QtCore.Qt.Unchecked:
			self.cData.setAngleSpace()

	def on_mapWorkerDone(self,result):
		super(Generic3dimController,self).on_mapWorkerDone(result)
		self.cData.setkSpace()

	def on_d3SliderMoved(self, val):
		index = self.view.d3PlotChooser.currentIndex()
		self.replotData(index,val)

	def on_d3PlotTypeChanged(self,index):
		self.replotData(index,0)
		if index == 0:
			self.setup3DTools(self.cData.axis1name, self.cData.axis1)
		elif index == 1:
			self.setup3DTools(self.cData.axis3name, self.cData.axis3)
		elif index == 2:
			self.setup3DTools(self.cData.axis2name, self.cData.axis2)
		else:
			print "??"
		self.setup2DTools()


	def onP_dataChanged(self):
		super(Generic3dimController,self).onP_dataChanged()
		index = self.view.d3PlotChooser.currentIndex()
		val = self.view.zaxisSlider.value()
		self.replotData(index,val)
		if index == 0:
			self.view.zaxisNameLbl.setText(self.cData.axis1name)
			self.view.zaxisValueLbl.setText(str(round(np.asarray(self.cData.axis1)[self.view.zaxisSlider.value()],4)))
		elif index == 1:
			self.view.zaxisNameLbl.setText(self.cData.axis3name)
			self.view.zaxisValueLbl.setText(str(round(np.asarray(self.cData.axis3)[self.view.zaxisSlider.value()],4)))
		elif index == 2:
			self.view.zaxisNameLbl.setText(self.cData.axis2name)
			self.view.zaxisValueLbl.setText(str(round(np.asarray(self.cData.axis2)[self.view.zaxisSlider.value()],4)))
		else:
			print "??"
		self.setup2DTools()

			


