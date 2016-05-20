# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/ui/GenericPQGViewMW.ui'
#
# Created: Wed May 18 16:16:08 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GenericPQGView(object):
    def setupUi(self, GenericPQGView):
        GenericPQGView.setObjectName("GenericPQGView")
        GenericPQGView.resize(859, 782)
        self.centralwidget = QtGui.QWidget(GenericPQGView)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.leftColumSplitter = QtGui.QSplitter(self.centralwidget)
        self.leftColumSplitter.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftColumSplitter.sizePolicy().hasHeightForWidth())
        self.leftColumSplitter.setSizePolicy(sizePolicy)
        self.leftColumSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.leftColumSplitter.setObjectName("leftColumSplitter")
        self.metaDataSplitter = QtGui.QSplitter(self.leftColumSplitter)
        self.metaDataSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.metaDataSplitter.setObjectName("metaDataSplitter")
        self.plottoolsSplitter = QtGui.QSplitter(self.metaDataSplitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plottoolsSplitter.sizePolicy().hasHeightForWidth())
        self.plottoolsSplitter.setSizePolicy(sizePolicy)
        self.plottoolsSplitter.setAutoFillBackground(True)
        self.plottoolsSplitter.setOrientation(QtCore.Qt.Vertical)
        self.plottoolsSplitter.setObjectName("plottoolsSplitter")
        self.layoutWidget = QtGui.QWidget(self.plottoolsSplitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.mainPlotLayout = QtGui.QGridLayout(self.layoutWidget)
        self.mainPlotLayout.setContentsMargins(0, 0, 0, 0)
        self.mainPlotLayout.setObjectName("mainPlotLayout")
        self.layoutWidget1 = QtGui.QWidget(self.plottoolsSplitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.toolsLayout = QtGui.QHBoxLayout(self.layoutWidget1)
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

