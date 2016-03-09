from helper.constants import *
import numpy as np
from PySide import QtCore 


class GenericData(QtCore.QObject):

	nbDataChanged = QtCore.Signal()
	__data = None
	dataType = CONST_DATATYPE_GENERIC	# Original data
	root = None
	__entryId = 0

	# Setters and Getters
	# Data property
	def getData(self):
		return self.__data

	def setData(self, d):
		self.__data = d
		self.nbDataChanged.emit()

	def delData(self):
		print "delete Data"
		del self.__data

	# EntryId property
	def getEntryId(self):
		return self.__entryId

	def setEntryId(self, d):
		self.__entryId = d
		self.reinitializeData()

	def delEntryId(self):
		print "delete entryId"
		del self.__entryId

	

	# Currently loaded
	data = property(getData,setData,delData)
	entryId = property(getEntryId,setEntryId,delEntryId)
	axis1 = None
	axis2 = None
	axis3 = None
	axis1name = None
	axis2name = None
	axis3name = None
	title = None

	def __init__(self, nxRoot, entryId = 0):
		super(GenericData, self).__init__()

		self.root = nxRoot
		self.entryId = entryId

	def reinitializeData(self):
		pass

