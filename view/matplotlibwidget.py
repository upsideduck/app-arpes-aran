
from matplotlib.figure import Figure
import matplotlib.cm as cm
from PySide import QtCore, QtGui
from matplotlib.backend_bases import FigureManagerBase, key_press_handler
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
import numpy as np

class MatplotlibWidget(FigureCanvas):

	window = None
	data = None
	axis1 = None
	axis2 = None
	axis1Name = None
	axis2Name = None
	title = None
	cmap = 'rainbow'
	autoscale = True
	vmin = 0
	vmax = 1
	voffset = 0
	axhorpos = 0
	axverpos = 0
	interpolation = 'none'

	interpolationMethods = ['none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

	def __init__(self, window, parent=None,xlabel='',ylabel='',title=''):
		super(MatplotlibWidget, self).__init__(Figure())

		self.window = window

		# Define all available colormaps
		self.allcolormaps=[m for m in cm.datad if not m.endswith("_r")]
		self.allcolormaps.sort()

		self.setParent(parent)
		self.figure = Figure(facecolor='none')
		self.canvas = FigureCanvas(self.figure)
		self.axes = self.figure.add_subplot(111)

		self.axes.set_xlabel(xlabel)
		self.axes.set_ylabel(ylabel)
		self.axes.set_title(title)

	def plot2DData(self,data,axis1,axis2,axis1Name="",axis2Name="", title=""):
		self.data = data
		self.axis1 = np.asarray(axis1)
		self.axis2 = np.asarray(axis2)[::-1]		# Due to how plot is displaying, it vert axis needs to be reversed
		self.axis1Name = axis1Name
		self.axis2Name = axis2Name
		self.title = title

		self.__updatePlot()

	def setColorMap(self,cmap):
		self.cmap = cmap
		self.__updatePlot()
	
	def setInterpolation(self,interpolation):
		self.interpolation = interpolation
		self.__updatePlot()

	def setVoffset(self,voffset):
		self.voffset = voffset
		self.__updatePlot()

	def setVmax(self,vmax):
		self.vmax = vmax
		self.__updatePlot()

	def setAxhorpos(self,pos):
		self.axhorpos = pos
		self.__updatePlot()

	def setAxverpos(self,pos):
		self.axverpos = pos
		self.__updatePlot()

	def setAutoscale(self,autoscale):
		self.autoscale = autoscale
		self.__updatePlot()

	def updatePlot(self):
		self.__updatePlot()

	def __updatePlot(self):
		if self.data is None:
			return
		axises = [float(self.axis2[0]),float(self.axis2[-1]),float(self.axis1[0]),float(self.axis1[-1])]
		self.axes.clear()
		kargs = {}
		kargs['extent'] = axises
		kargs['interpolation'] = self.interpolation
		kargs['cmap'] = cm.get_cmap(self.cmap)
		kargs['aspect'] = 1/((abs(axises[1]-axises[0]))/(abs(axises[3]-axises[2]))/1.4)
		if self.autoscale == False:
			kargs['vmin'] = self.vmin + self.voffset
			kargs['vmax'] = self.vmax + self.voffset
		self.image = self.axes.imshow(self.data, **kargs)
		#self.figure.colorbar(self.image)
		self.axes.set_xlabel(self.axis2Name)
		#self.window.xaxisNameLbl.setText(self.axis1Name+":")
		self.axes.set_ylabel(self.axis1Name)
		#self.window.yaxisNameLbl.setText(self.axis2Name+":")
		self.axes.set_title(self.title)
		
		self.axes.axvline(x=float(self.axis1[self.axhorpos]),color='r',ls='solid')
		self.axes.axhline(y=float(self.axis2[self.axverpos]),color='r',ls='solid')
		self.draw()