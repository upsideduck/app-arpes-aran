from helper.constants import *
import numpy as np
from PySide import QtCore 


class GenericData(QtCore.QObject):

	dataChanged = QtCore.Signal()
	__data = None

	# Setters and Getters
	# Data property
	def getData(self):
		return self.__data

	def setData(self, d):
		self.__data = d
		self.dataChanged.emit()

	def delData(self):
		print "delete Data"
		del self.__data

	

	# Currently loaded
	data = property(getData,setData,delData)
	axis1 = None
	axis2 = None
	axis3 = None
	axis1name = None
	axis2name = None
	axis3name = None
	title = None

	def __init__(self, nxRoot):
		super(GenericdData, self).__init__()

