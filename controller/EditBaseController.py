from helper.constants import *
from PySide import QtCore, QtGui 
from nexpy.api import nexus as nx
import numpy as np
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
import matplotlib.pyplot as plt
#from pylab import *
import view.matplotlibwidget as matplotlibwidget
from model.ArpesData import *


class EditBaseController(QtGui.QMainWindow):
	
	def __init__(self, cData, view, parent=None):
		super(EditBaseController, self ).__init__()
		self.view = view
		self.cData = cData		# Holds the data for the current open experiment
		self.cData.dataChanged.connect(self.onP_dataChanged)
		self.view.setupUi(self)
		self.windowTitle = self.windowTitle() + " - " + str(self.cData.root.entry1.title)
		self.setWindowTitle(self.windowTitle)
		

	def configure_views(self):	
		## Matplotlib widget
		# Do this first to be ready with default values
 		self.DataPlot = matplotlibwidget.MatplotlibWidget(self.view)
 		self.DataPlot.setFocusPolicy( QtCore.Qt.ClickFocus )
		self.DataPlot.setFocus()	
		self.DataPlot.mpl_connect('motion_notify_event', self.on_cursorPosition)	
		self.DataPlot.mpl_connect('figure_leave_event', self.on_cursorLeaveFigure)	
		# create a layout inside the blank widget and add the matplotlib widget        
		layout = QtGui.QVBoxLayout(self.view.plotWidget)        
		layout.addWidget(self.DataPlot)	

		## Plot tools
		# Colormaps
		initialCmapIndex = self.DataPlot.allcolormaps.index(self.DataPlot.cmap)
		for i, m in enumerate(self.DataPlot.allcolormaps):
			self.view.colormapChooser.addItem(m)
		self.view.colormapChooser.setCurrentIndex(initialCmapIndex)
		self.view.colormapChooser.currentIndexChanged[int].connect(self.on_colormapChooserChanged)
		# Interpolation
		initialInterpolationIndex = self.DataPlot.interpolationMethods.index(self.DataPlot.interpolation)
		for i, m in enumerate(self.DataPlot.interpolationMethods):
			self.view.interpolationChooser.addItem(m)
		self.view.interpolationChooser.setCurrentIndex(initialInterpolationIndex)
		self.view.interpolationChooser.currentIndexChanged[int].connect(self.on_interpolationChooserChanged)
		# Contrast controls
		self.view.checkAutoScale.stateChanged[int].connect(self.on_checkAutoScaleChanged)
		self.view.voffsetslider.valueChanged[int].connect(self.on_voffsetSliderMoved)
		self.view.vmaxslider.valueChanged[int].connect(self.on_vmaxSliderMoved)
		# Horizontal and vertical cut sliders
		self.view.horizontalSlider.valueChanged[int].connect(self.on_horiSliderMoved)
		self.view.verticalSlider.valueChanged[int].connect(self.on_vertSliderMoved)
		# k-space
		self.view.kSpaceCheckBox.stateChanged[int].connect(self.on_kSpaceCheckBoxChanged)
	

	def init2DView(self):
		self.view.plotTools.setEnabled(True)
		self.view.checkAutoScale.setEnabled(True)	# Should not be necessary, but seem like a bug

	def setup2DTools(self):
		self.view.voffsetslider.setRange(0,self.cData.vmax)
		self.view.voffsetslider.setValue(0)
		self.view.vmaxslider.setRange(self.cData.vmin,self.cData.vmax)
		self.view.vmaxslider.setValue(self.cData.vmax)
		self.DataPlot.vmin = self.cData.vmin
		self.DataPlot.vmax = self.cData.vmax
		self.view.horizontalSlider.setRange(0,len(self.DataPlot.axis1)-1)
		self.view.verticalSlider.setRange(0,len(self.DataPlot.axis2)-1)
		self.view.xaxisNameLbl.setText(self.DataPlot.axis1Name+":")
		self.view.yaxisNameLbl.setText(self.DataPlot.axis2Name+":")

	def viewHistograms(self):
		#Set up plot
		self.histFigure = plt.figure(CONST_HISTOGRAM_FIGURE)
		self.histFigure.canvas.set_window_title("Histograms")
		self.histAxes = [None] * 2
		self.histAxes[0] = self.histFigure.add_subplot(211)
		self.histAxes[0].set_yticklabels([])
		self.histAxes[1] = self.histFigure.add_subplot(212)
		self.histAxes[1].set_yticklabels([])
		self.histFigure.show()

	def updateHistograms(self, xdata, ydata, plot,title):
		if plot == 1:
			ax = self.histAxes[0]
		elif plot == 2:
			ax = self.histAxes[1]
		ax.clear()
		ax.set_yticklabels([])
		ax.set_title(title)
		ax.plot(xdata,ydata)
		self.histFigure.canvas.draw()

	def dataplotChanged(self):
		if plt.fignum_exists(CONST_HISTOGRAM_FIGURE):
			self.on_horiSliderMoved(self.view.horizontalSlider.value())
			self.on_vertSliderMoved(self.view.verticalSlider.value())
	
	## Slots
	def on_checkAutoScaleChanged(self,val):
		self.cData.axis1[0] =  self.cData.axis1[0] -1
		if val == QtCore.Qt.Checked:
			self.view.voffsetslider.setEnabled(False)
			self.view.vmaxslider.setEnabled(False)
			self.DataPlot.setAutoscale(True)
		elif val == QtCore.Qt.Unchecked:
			self.view.voffsetslider.setEnabled(True)
			self.view.vmaxslider.setEnabled(True)
			self.DataPlot.setAutoscale(False)

	def on_kSpaceCheckBoxChanged(self,val):
		if val == QtCore.Qt.Checked and self.cData.kdata == None:
			self.mapCreationThread = QtCore.QThread()  # no parent!
			self.mapWorker = MakeMapWorker(self.cData.root)
			self.mapWorker.moveToThread(self.mapCreationThread)
			self.mapWorker.finished.connect(self.mapCreationThread.quit)
			self.mapWorker.progress.connect(self.on_mapWorkerUpdateProgress)
			self.mapWorker.finished.connect(self.on_mapWorkerDone)	
			self.mapCreationThread.start()
			self.view.kSpaceCheckBox.setEnabled(False)
			#self.progresslabel = QtGui.QLabel()
			#self.view.statusBar.addWidget(self.progresslabel)

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
		self.view.kSpaceCheckBox.setEnabled(True)

	#@QtCore.Slot(float)
	def on_mapWorkerUpdateProgress(self, result):
		self.view.statusBar.showMessage("Calculating k-map: "+str(int(result*100))+"% done",2000)
	
	def on_interpolationChooserChanged(self,index):
		self.DataPlot.setInterpolation(self.DataPlot.interpolationMethods[int(index)])

	def on_voffsetSliderMoved(self, val):
		self.DataPlot.setVoffset(int(val))

	def on_vmaxSliderMoved(self, val):
		self.DataPlot.setVmax(int(val))

	def on_colormapChooserChanged(self,index):
		self.DataPlot.setColorMap(self.DataPlot.allcolormaps[int(index)])

	def on_cursorPosition(self, event):
		if self.cData:
			if event.xdata != None:
				self.view.xCoordinate.setText(str(round(event.xdata,4)))
			if event.ydata != None:
				self.view.yCoordinate.setText(str(round(event.ydata,4)))

	def on_cursorLeaveFigure(self, event):
		self.view.xCoordinate.setText(str(""))
		self.view.yCoordinate.setText(str(""))

	def on_horiSliderMoved(self, val):
		if not plt.fignum_exists(CONST_HISTOGRAM_FIGURE):
			self.viewHistograms()
		self.DataPlot.setAxhorpos(int(val))
		self.updateHistograms(self.DataPlot.axis2[::-1],self.DataPlot.data[:,int(val)],1,self.DataPlot.axis2Name)


	def on_vertSliderMoved(self, val):
		if not plt.fignum_exists(CONST_HISTOGRAM_FIGURE):
			self.viewHistograms()
		self.DataPlot.setAxverpos(int(val))
		self.updateHistograms(self.DataPlot.axis1,self.DataPlot.data[int(val),:],2,self.DataPlot.axis1Name)

	@QtCore.Slot()
	def onP_dataChanged(self):
		pass
