# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/ArpesBuildView.ui'
#
# Created: Tue Nov  3 16:11:32 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ArpesBuildWindow(object):
    def setupUi(self, ArpesBuildWindow):
        ArpesBuildWindow.setObjectName("ArpesBuildWindow")
        ArpesBuildWindow.resize(1074, 608)
        self.centralwidget = QtGui.QWidget(ArpesBuildWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableOfEntries = QtGui.QTableView(self.centralwidget)
        self.tableOfEntries.setSortingEnabled(True)
        self.tableOfEntries.setObjectName("tableOfEntries")
        self.verticalLayout_2.addWidget(self.tableOfEntries)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 260))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plotWidget = QtGui.QWidget(self.widget)
        self.plotWidget.setMinimumSize(QtCore.QSize(320, 240))
        self.plotWidget.setMaximumSize(QtCore.QSize(320, 240))
        self.plotWidget.setObjectName("plotWidget")
        self.horizontalLayout_2.addWidget(self.plotWidget)
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loadFilesBtn = QtGui.QPushButton(self.groupBox)
        self.loadFilesBtn.setObjectName("loadFilesBtn")
        self.verticalLayout.addWidget(self.loadFilesBtn)
        self.exportFermiBtn = QtGui.QPushButton(self.groupBox)
        self.exportFermiBtn.setObjectName("exportFermiBtn")
        self.verticalLayout.addWidget(self.exportFermiBtn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.widget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(200, 99999))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.autoColumnChooser = QtGui.QComboBox(self.groupBox_2)
        self.autoColumnChooser.setObjectName("autoColumnChooser")
        self.verticalLayout_3.addWidget(self.autoColumnChooser)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.autoColumnInitialTxt = QtGui.QLineEdit(self.groupBox_2)
        self.autoColumnInitialTxt.setObjectName("autoColumnInitialTxt")
        self.verticalLayout_3.addWidget(self.autoColumnInitialTxt)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.autoColumnStepTxt = QtGui.QLineEdit(self.groupBox_2)
        self.autoColumnStepTxt.setObjectName("autoColumnStepTxt")
        self.verticalLayout_3.addWidget(self.autoColumnStepTxt)
        self.autoColumnInsertBtn = QtGui.QPushButton(self.groupBox_2)
        self.autoColumnInsertBtn.setObjectName("autoColumnInsertBtn")
        self.verticalLayout_3.addWidget(self.autoColumnInsertBtn)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.widget)
        ArpesBuildWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(ArpesBuildWindow)
        self.statusbar.setObjectName("statusbar")
        ArpesBuildWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ArpesBuildWindow)
        QtCore.QMetaObject.connectSlotsByName(ArpesBuildWindow)

    def retranslateUi(self, ArpesBuildWindow):
        ArpesBuildWindow.setWindowTitle(QtGui.QApplication.translate("ArpesBuildWindow", "Build", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ArpesBuildWindow", "Files", None, QtGui.QApplication.UnicodeUTF8))
        self.loadFilesBtn.setText(QtGui.QApplication.translate("ArpesBuildWindow", "Import files", None, QtGui.QApplication.UnicodeUTF8))
        self.exportFermiBtn.setText(QtGui.QApplication.translate("ArpesBuildWindow", "Export fermi surface", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ArpesBuildWindow", "Auto fill column", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ArpesBuildWindow", "Column", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ArpesBuildWindow", "Initial value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ArpesBuildWindow", "Step", None, QtGui.QApplication.UnicodeUTF8))
        self.autoColumnInsertBtn.setText(QtGui.QApplication.translate("ArpesBuildWindow", "Insert", None, QtGui.QApplication.UnicodeUTF8))

