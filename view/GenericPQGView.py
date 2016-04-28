# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/ui/GenericPQGViewMW.ui'
#
# Created: Thu Apr 28 15:08:13 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GenericPQGView(object):
    def setupUi(self, GenericPQGView):
        GenericPQGView.setObjectName("GenericPQGView")
        GenericPQGView.resize(1083, 782)
        self.centralwidget = QtGui.QWidget(GenericPQGView)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.leftColumSplitter = QtGui.QSplitter(self.centralwidget)
        self.leftColumSplitter.setEnabled(True)
        self.leftColumSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.leftColumSplitter.setObjectName("leftColumSplitter")
        self.metaDataSplitter = QtGui.QSplitter(self.leftColumSplitter)
        self.metaDataSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.metaDataSplitter.setObjectName("metaDataSplitter")
        self.plottoolsSplitter = QtGui.QSplitter(self.metaDataSplitter)
        self.plottoolsSplitter.setAutoFillBackground(True)
        self.plottoolsSplitter.setOrientation(QtCore.Qt.Vertical)
        self.plottoolsSplitter.setObjectName("plottoolsSplitter")
        self.widget = QtGui.QWidget(self.plottoolsSplitter)
        self.widget.setObjectName("widget")
        self.mainPlotLayout = QtGui.QGridLayout(self.widget)
        self.mainPlotLayout.setContentsMargins(0, 0, 0, 0)
        self.mainPlotLayout.setObjectName("mainPlotLayout")
        self.widget1 = QtGui.QWidget(self.plottoolsSplitter)
        self.widget1.setObjectName("widget1")
        self.toolsLayout = QtGui.QHBoxLayout(self.widget1)
        self.toolsLayout.setContentsMargins(0, 0, 0, 0)
        self.toolsLayout.setObjectName("toolsLayout")
        self.metaDataView = QtGui.QTextEdit(self.metaDataSplitter)
        self.metaDataView.setEnabled(False)
        self.metaDataView.setMinimumSize(QtCore.QSize(300, 0))
        self.metaDataView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.metaDataView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.metaDataView.setObjectName("metaDataView")
        self.gridLayout.addWidget(self.leftColumSplitter, 0, 0, 1, 1)
        GenericPQGView.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(GenericPQGView)
        self.statusbar.setObjectName("statusbar")
        GenericPQGView.setStatusBar(self.statusbar)

        self.retranslateUi(GenericPQGView)
        QtCore.QMetaObject.connectSlotsByName(GenericPQGView)

    def retranslateUi(self, GenericPQGView):
        GenericPQGView.setWindowTitle(QtGui.QApplication.translate("GenericPQGView", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))

