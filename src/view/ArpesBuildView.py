# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/ui/ArpesBuildView.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ArpesBuildWindow(object):
    def setupUi(self, ArpesBuildWindow):
        ArpesBuildWindow.setObjectName(_fromUtf8("ArpesBuildWindow"))
        ArpesBuildWindow.resize(1074, 608)
        self.centralwidget = QtGui.QWidget(ArpesBuildWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableOfEntries = QtGui.QTableView(self.centralwidget)
        self.tableOfEntries.setSortingEnabled(True)
        self.tableOfEntries.setObjectName(_fromUtf8("tableOfEntries"))
        self.verticalLayout_2.addWidget(self.tableOfEntries)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 260))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.plotWidget = QtGui.QWidget(self.widget)
        self.plotWidget.setMinimumSize(QtCore.QSize(320, 240))
        self.plotWidget.setMaximumSize(QtCore.QSize(320, 240))
        self.plotWidget.setObjectName(_fromUtf8("plotWidget"))
        self.horizontalLayout_2.addWidget(self.plotWidget)
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.loadFilesBtn = QtGui.QPushButton(self.groupBox)
        self.loadFilesBtn.setObjectName(_fromUtf8("loadFilesBtn"))
        self.verticalLayout.addWidget(self.loadFilesBtn)
        self.exportFermiBtn = QtGui.QPushButton(self.groupBox)
        self.exportFermiBtn.setObjectName(_fromUtf8("exportFermiBtn"))
        self.verticalLayout.addWidget(self.exportFermiBtn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.widget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(200, 99999))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.autoColumnChooser = QtGui.QComboBox(self.groupBox_2)
        self.autoColumnChooser.setObjectName(_fromUtf8("autoColumnChooser"))
        self.verticalLayout_3.addWidget(self.autoColumnChooser)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.autoColumnInitialTxt = QtGui.QLineEdit(self.groupBox_2)
        self.autoColumnInitialTxt.setObjectName(_fromUtf8("autoColumnInitialTxt"))
        self.verticalLayout_3.addWidget(self.autoColumnInitialTxt)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.autoColumnStepTxt = QtGui.QLineEdit(self.groupBox_2)
        self.autoColumnStepTxt.setObjectName(_fromUtf8("autoColumnStepTxt"))
        self.verticalLayout_3.addWidget(self.autoColumnStepTxt)
        self.autoColumnInsertBtn = QtGui.QPushButton(self.groupBox_2)
        self.autoColumnInsertBtn.setObjectName(_fromUtf8("autoColumnInsertBtn"))
        self.verticalLayout_3.addWidget(self.autoColumnInsertBtn)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.widget)
        ArpesBuildWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(ArpesBuildWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ArpesBuildWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ArpesBuildWindow)
        QtCore.QMetaObject.connectSlotsByName(ArpesBuildWindow)

    def retranslateUi(self, ArpesBuildWindow):
        ArpesBuildWindow.setWindowTitle(_translate("ArpesBuildWindow", "Build", None))
        self.groupBox.setTitle(_translate("ArpesBuildWindow", "Files", None))
        self.loadFilesBtn.setText(_translate("ArpesBuildWindow", "Import files", None))
        self.exportFermiBtn.setText(_translate("ArpesBuildWindow", "Export fermi surface", None))
        self.groupBox_2.setTitle(_translate("ArpesBuildWindow", "Auto fill column", None))
        self.label.setText(_translate("ArpesBuildWindow", "Column", None))
        self.label_2.setText(_translate("ArpesBuildWindow", "Initial value", None))
        self.label_3.setText(_translate("ArpesBuildWindow", "Step", None))
        self.autoColumnInsertBtn.setText(_translate("ArpesBuildWindow", "Insert", None))

