import operator
from PySide.QtCore import *
from PySide.QtGui import *
from nexpy.api import nexus as nx
import nexus_template
import nximporter
import numpy as np


class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        # the solvent data ...
        self.header = ['File name', 'E Angle', 'Width', 'P Angle', 'High[eV]', 'Low[eV]' ]
        # use numbers for numeric data to sort properly
        self.entryList = []

        self.i = 0

        # set basic window stuff
        self.setGeometry(300, 200, 970, 450)
        self.setWindowTitle("Build fermisurface")

        # add the model to the view
        self.table_model = MyTableModel(self, self.entryList, self.header)
        self.table_view = QTableView()
        self.table_view.setModel(self.table_model)
        # enable sorting
        self.table_view.setSortingEnabled(True)

        # add the table to the layout
        layout = QVBoxLayout(self) 
        layout.addWidget(self.table_view)
        loadFileBtn = QPushButton("Load file", self)
        printModelBtn = QPushButton("Print model", self)
        loadFileBtn.clicked.connect(self.loadFile) 
        printModelBtn.clicked.connect(self.printModel)            

        # add some button to the layout
        action_layout = QHBoxLayout(self)
        action_layout.addStretch(1)
        action_layout.addWidget(loadFileBtn)
        action_layout.addWidget(printModelBtn)
        
        layout.addLayout(action_layout)
        self.setLayout(layout)

    def loadFile(self):
        fname=QFileDialog.getOpenFileName()

    

        print "-----------------------------------"
        entry = None
        root = None
        entryid = "entry"+str(self.i)
        sp2file = nximporter.sp2(fname[0])
        (result,entry) = sp2file.parse(rotation=0.25*self.i)
        
        listEntry = (str(entry.title), 
            float(entry.analyser.angles[0]), 
            abs(float(entry.analyser.angles[0]) - float(entry.analyser.angles[-1])), 
            float(entry.instrument.manipulator.rangle), 
            float(entry.analyser.energies[-1]), 
            float(entry.analyser.energies[0]),
            entry)

        self.table_model.setData(QModelIndex(),listEntry)
        self.i += 1
        #root = nx.NXroot(entry)
        #root.save('test/'+entryid+'.nxs')
        print "-----------------------------------"

    def printModel(self):

        for i in range(self.table_model.rowCount(self)):
            print i

class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, entryList, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.entryList = entryList
        self.header = header

    def rowCount(self, parent):
        return len(self.entryList)

    def columnCount(self, parent):
        return len(self.header)

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None

        return self.entryList[index.row()][index.column()]

    def setData(self, index, value, role = Qt.EditRole):
        if role == Qt.EditRole:
            self.emit(SIGNAL("layoutAboutToBeChanged()"))
            self.entryList.append(value)

            self.dataChanged.emit(index, index)
            self.emit(SIGNAL("layoutChanged()"))

            return True
        return False

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        
        self.entryList = sorted(self.entryList,
            key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.entryList.reverse()
        self.emit(SIGNAL("layoutChanged()"))


app = QApplication([])
win = MyWindow()
win.show()
app.exec_()