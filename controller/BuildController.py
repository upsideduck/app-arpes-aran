from helper.constants import *
from PySide import QtCore, QtGui 
from nexpy.api import nexus as nx
from view.buildView import Ui_BuildWindow
import numpy as np
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
import matplotlib.pyplot as plt
#from pylab import *
from view.matplotlibwidget import *
import operator
from helper.spectrum import Arpes2DSpectrum
from helper.spectrum import Arpes3DSpectrum
from model.ArpesData import *


class BuildController(QtGui.QMainWindow):
	
	def __init__(self, parent=None):
		super(BuildController, self ).__init__()
		self.view = Ui_BuildWindow()
		self.view.setupUi(self)
		self.configure_views()		

	def configure_views(self):  
		# the solvent data ...
		self.header = CONST_TALBEHEADERS
		# use numbers for numeric data to sort properly
		self.entryList = []

		# add the model to the view
		self.table_model = TableOfEntriesModel(self, self.entryList, self.header)
		self.view.tableOfEntries.setModel(self.table_model)

		# set up selection model for tableview model
		self.selection = self.view.tableOfEntries.selectionModel()
		self.selection.selectionChanged.connect(self.handleSelectionChanged)
		
		# auto column dropdown chooser
		for i in range(0,len(CONST_AUTOCOLUMNALT)):
			self.view.autoColumnChooser.addItem(CONST_AUTOCOLUMNALT[i])
		# self.view.autoColumnChooser.currentIndexChanged[int].connect(self.on_autoColumnChooserChanged)
		self.view.autoColumnInsertBtn.clicked.connect(self.on_autoColumnInsert)

		self.view.loadFilesBtn.clicked.connect(self.on_loadFiles)    
		self.view.exportFermiBtn.clicked.connect(self.on_exportFermiSurface)     

		## Matplotlib widget
		# Do this first to be ready with default values
		self.DataPlot = MatplotlibWidget(self.view)
		# create a layout inside the blank widget and add the matplotlib widget        
		layout = QtGui.QVBoxLayout(self.view.plotWidget)        
		layout.addWidget(self.DataPlot)    

	def handleSelectionChanged(self, selected, deselected):
		if len(selected.indexes()) == 0:
			## deselected
			return

		index = selected.indexes()[0]
		if index.column() == 0:

			loadeddata = nx.NXroot((self.table_model.entries[index.row()]).nxEntry)
			# Determine and set contrast values on dataplot
			# vmin_index = np.unravel_index(loadeddata.entry1.analyser.data.argmin(), loadeddata.entry1.analyser.data.shape)
			# vmin = int(loadeddata.entry1.analyser.data[vmin_index])
			# vmax_index = np.unravel_index(loadeddata.entry1.analyser.data.argmax(), loadeddata.entry1.analyser.data.shape)
			# vmax = int(loadeddata.entry1.analyser.data[vmax_index])
	
			self.cData = ArpesData(loadeddata)

			self.DataPlot.plot2DData(self.cData.data, 
				self.cData.axis1, 
				self.cData.axis2, 
				"", 
				"",
				self.cData.title)

	def on_loadFiles(self):
		files=QtGui.QFileDialog.getOpenFileNames(self,
		                'Select one or more files to open',
		                '/Users/johanadell/Box Sync/Dev/ARAN/src/data',
		                'Spectra (*.sp2)')

		self.importFilesThread = QtCore.QThread()  # no parent!
		self.filesWorker = ImportFilesWorker(files)
		self.filesWorker.moveToThread(self.importFilesThread)

		self.filesWorker.progress.connect(self.on_fileImported)
		self.filesWorker.finished.connect(self.on_filesWorkerDone)	
		self.filesWorker.finished.connect(self.importFilesThread.quit)
					
		self.importFilesThread.start()
		
		QtCore.QMetaObject.invokeMethod(self.filesWorker, 'processFiles', QtCore.Qt.QueuedConnection)

	def on_exportFermiSurface(self):
		listOfEntries = self.table_model.listOfEntries()
		if len(listOfEntries) > 0:
			filename = QtGui.QFileDialog.getSaveFileName(self, "Save file", "", ".nxs")
			if len(filename[0]) > 0:
				fermiSurfaceEntry = Arpes3DSpectrum.parseListOfEntriesToNx(listOfEntries)
				root = nx.NXroot(fermiSurfaceEntry.nxEntry)
				root.save(filename[0]+filename[1])

				print root.tree
			else:
				print "No filename"



		# Result is a touple with (progress in %, nxEntry of processed specturm)
	def on_fileImported(self,result):	
	    self.table_model.setData(QtCore.QModelIndex(),TableRowItem(nxEntry=result[1],wf=0))
	    print "File imported, "+str(result[0]*100)+"% finished"

	def on_filesWorkerDone(self):
		self.view.tableOfEntries.resizeColumnsToContents()
		print "Import Done!"

	def on_autoColumnInsert(self):
		try:
			indexOfColumn =  CONST_TALBEHEADERS.index(CONST_AUTOCOLUMNALT[self.view.autoColumnChooser.currentIndex()])
			initialValue = float(self.view.autoColumnInitialTxt.text())
			stepValue = float(self.view.autoColumnStepTxt.text())

			totalRows = self.table_model.rowCount()
			for row in range(0,totalRows):
				self.table_model.setData(self.table_model.index(row,indexOfColumn),initialValue+row*stepValue)
		except ValueError:
	 		print "Column not valid"
		

class TableOfEntriesModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, entry, header, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.entries = entry
        self.header = header

    def rowCount(self, parent = None):
        return len(self.entries)

    def columnCount(self, parent = None):
        return len(self.header)

    def data(self, index, role):

        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
			return None
        entry = self.entries[index.row()]

        if not isinstance(entry,TableRowItem):
        	return None

        row = [str(entry.nxEntry.title), 
            float(entry.nxEntry.analyser.angles[0]), 
            abs(float(entry.nxEntry.analyser.angles[0]) - float(entry.nxEntry.analyser.angles[-1])), 
            float(entry.nxEntry.instrument.manipulator.rangle), 
            float(entry.nxEntry.analyser.energies[-1]), 
            float(entry.nxEntry.analyser.energies[0]),
            float(entry.wf)]
        return row[index.column()]
    
    def listOfEntries(self):
    	rowCount = len(self.entries)
    	listOfEntries = []
    	for row in range(0,rowCount):
    		listOfEntries.append(self.entries[row].nxEntry)
    	return listOfEntries


    def setData(self, index, value, role = QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
            if index.row() < 0 and isinstance(value,TableRowItem):		#Add new data item
            	self.entries.append(value)
            else:
            	if index.column() == R_ANGLE_COLUMN_NR:
	            	self.entries[index.row()].nxEntry.instrument.manipulator.rangle = float(value) 

            self.dataChanged.emit(index, index)
            self.emit(QtCore.SIGNAL("layoutChanged()"))

            return True
        return False

    def entryObj(self,index):
    	return self.entries[index.row()]

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
        if col == 0:
            sortedList = sorted(self.entries,key=lambda entry: str(entry.nxEntry.title))
        elif col == 1:
            sortedList = sorted(self.entries,key=lambda entry: float(entry.nxEntry.analyser.angles[0]))
        elif col == 2:
            sortedList = sorted(self.entries,key=lambda entry: abs(float(entry.nxEntry.analyser.angles[0]) - float(entry.nxEntry.analyser.angles[-1])))
        elif col == 3:
            sortedList = sorted(self.entries,key=lambda entry: float(entry.nxEntry.instrument.manipulator.rangle))
        elif col == 4:
            sortedList = sorted(self.entries,key=lambda entry: float(entry.nxEntry.analyser.energies[-1]))
        elif col == 5:
            sortedList = sorted(self.entries,key=lambda entry: float(entry.nxEntry.analyser.energies[0]))
        elif col == 6:
            sortedList = sorted(self.entries,key=lambda entry: float(entry.wf))
        else:
            sortedList = self.entries
        
        self.entries = sortedList

        if order == QtCore.Qt.DescendingOrder:
            self.entries.reverse()
        self.emit(QtCore.SIGNAL("layoutChanged()"))


    def flags(self,index):
		if (index.column() == R_ANGLE_COLUMN_NR):
			return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
		else:
			return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

class TableRowItem():
    def __init__(self, nxEntry, wf):
        self.nxEntry = nxEntry
        self.wf = wf

class ImportFilesWorker(QtCore.QObject):

	progress = QtCore.Signal(tuple)
	finished = QtCore.Signal()


 	def __init__(self,files):
 		super(ImportFilesWorker, self).__init__()
 		self.files = files
 		self.totalIter = len(files[0])
		
	@QtCore.Slot()
	def processFiles(self):
		i = 0
		for filepath in self.files[0]:
			extension = filepath.split('.')[-1]
			if extension == "sp2":
				processedFile = self.processSp2File(filepath,i)
				i += 1
				self.progress.emit((float(i)/self.totalIter,processedFile.nxEntry))
			else:
				print "Not a valid file"
		self.finished.emit()


	def processSp2File(self,filepath,iteration):
		print "-----------------------------------"
		entry = None
		root = None
		entryid = "entry"+str(iteration)
		arpes2DSpectrum = Arpes2DSpectrum.parseSP2ToNx(filepath,rotation=float(0.0))
		print "-----------------------------------"
		return arpes2DSpectrum



