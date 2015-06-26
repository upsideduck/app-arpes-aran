from PySide import QtCore, QtGui 
from nexpy.api import nexus as nx
from buildView import Ui_BuildWindow
import numpy as np
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
import matplotlib.pyplot as plt
#from pylab import *
import matplotlibwidget
import operator
import nximporter
from ArpesData import *

###
# Initial values
###


class BuildController(QtGui.QMainWindow):
	
	def __init__(self, parent=None):
		super(BuildController, self ).__init__()
		self.view = Ui_BuildWindow()
		self.view.setupUi(self)
		self.configure_views()		

	def configure_views(self):  
		# the solvent data ...
		self.header = ['File name', 'E Angle', 'Width', 'P Angle', 'High[eV]', 'Low[eV]', 'Wf[eV]' ]
		# use numbers for numeric data to sort properly
		self.entryList = []

		# add the model to the view
		self.table_model = MyTableModel(self, self.entryList, self.header)
		self.view.tableOfEntries.setModel(self.table_model)

		self.selection = self.view.tableOfEntries.selectionModel()
		self.selection.selectionChanged.connect(self.handleSelectionChanged)
		
		self.view.loadFilesBtn.clicked.connect(self.loadFile)     

		## Matplotlib widget
		# Do this first to be ready with default values
		self.DataPlot = matplotlibwidget.MatplotlibWidget(self.view)
		# create a layout inside the blank widget and add the matplotlib widget        
		layout = QtGui.QVBoxLayout(self.view.plotWidget)        
		layout.addWidget(self.DataPlot)    

	def handleSelectionChanged(self, selected, deselected):
		if len(selected.indexes()) == 0:
			## deselected
			return

		index = selected.indexes()[0]
		if index.column() == 0:
			loadeddata = nx.NXroot(self.table_model.entryObj(index))
			# Determine and set contrast values on dataplot
			vmin_index = np.unravel_index(loadeddata.entry1.analyser.data.argmin(), loadeddata.entry1.analyser.data.shape)
			vmin = int(loadeddata.entry1.analyser.data[vmin_index])
			vmax_index = np.unravel_index(loadeddata.entry1.analyser.data.argmax(), loadeddata.entry1.analyser.data.shape)
			vmax = int(loadeddata.entry1.analyser.data[vmax_index])
	
			self.cData = ArpesData(loadeddata,vmin,vmax)

			self.DataPlot.plot2DData(self.cData.data, 
				self.cData.axis1, 
				self.cData.axis2, 
				"", 
				"",
				self.cData.title)

	def loadFile(self):
		files=QtGui.QFileDialog.getOpenFileNames(self,
		                'Select one or more files to open',
		                '/Users/johanadell/Dropbox/Work/Dev/ARAN/test',
		                'Spectra (*.sp2)')


		i = 0
		for thefile in files[0]:

		    print "-----------------------------------"
		    entry = None
		    root = None
		    entryid = "entry"+str(i)
		    sp2file = nximporter.sp2(thefile)
		    (result,entry) = sp2file.parse(rotation=0)
		    self.table_model.setData(QtCore.QModelIndex(),entry)
		    i += 1
		    #root = nx.NXroot(entry)
		    #root.save('test/'+entryid+'.nxs')
		    print "-----------------------------------"
		self.view.tableOfEntries.resizeColumnsToContents()

class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, entryList, header, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.entryList = entryList
        self.header = header

    def rowCount(self, parent):
        return len(self.entryList)

    def columnCount(self, parent):
        return len(self.header)

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None
        entity = self.entryList[index.row()]

        onelist = [str(entity.title), 
            float(entity.analyser.angles[0]), 
            abs(float(entity.analyser.angles[0]) - float(entity.analyser.angles[-1])), 
            float(entity.instrument.manipulator.rangle), 
            float(entity.analyser.energies[-1]), 
            float(entity.analyser.energies[0])]
        return onelist[index.column()]

    def setData(self, index, value, role = QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
            self.entryList.append(value)

            self.dataChanged.emit(index, index)
            self.emit(QtCore.SIGNAL("layoutChanged()"))

            return True
        return False

    def entryObj(self,index):
    	return self.entryList[index.row()]

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
        if col == 0:
            sortedList = sorted(self.entryList,key=lambda entry: str(entry.title))
        elif col == 1:
            sortedList = sorted(self.entryList,key=lambda entry: float(entry.analyser.angles[0]))
        elif col == 2:
            sortedList = sorted(self.entryList,key=lambda entry: abs(float(entry.analyser.angles[0]) - float(entry.analyser.angles[-1])))
        elif col == 3:
            sortedList = sorted(self.entryList,key=lambda entry: float(entry.instrument.manipulator.rangle))
        elif col == 4:
            sortedList = sorted(self.entryList,key=lambda entry: float(entry.analyser.energies[-1]))
        elif col == 5:
            sortedList = sorted(self.entryList,key=lambda entry: float(entry.analyser.energies[0]))
        else:
            sortedList = self.entryList
        
        self.entryList = sortedList

        if order == QtCore.Qt.DescendingOrder:
            self.entryList.reverse()
        self.emit(QtCore.SIGNAL("layoutChanged()"))

class TableRowItem():
    def __init__(self, nxEntity, wf):
        self.nxEntity = nxEntity
        self.wf = wf

