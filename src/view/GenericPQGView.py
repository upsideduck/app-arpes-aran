# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/ui/GenericPQGViewMW.ui'
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

class Ui_GenericPQGView(object):
    def setupUi(self, GenericPQGView):
        GenericPQGView.setObjectName(_fromUtf8("GenericPQGView"))
        GenericPQGView.resize(859, 782)
        self.centralwidget = QtGui.QWidget(GenericPQGView)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.leftColumSplitter = QtGui.QSplitter(self.centralwidget)
        self.leftColumSplitter.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftColumSplitter.sizePolicy().hasHeightForWidth())
        self.leftColumSplitter.setSizePolicy(sizePolicy)
        self.leftColumSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.leftColumSplitter.setObjectName(_fromUtf8("leftColumSplitter"))
        self.metaDataSplitter = QtGui.QSplitter(self.leftColumSplitter)
        self.metaDataSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.metaDataSplitter.setObjectName(_fromUtf8("metaDataSplitter"))
        self.plottoolsSplitter = QtGui.QSplitter(self.metaDataSplitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plottoolsSplitter.sizePolicy().hasHeightForWidth())
        self.plottoolsSplitter.setSizePolicy(sizePolicy)
        self.plottoolsSplitter.setAutoFillBackground(True)
        self.plottoolsSplitter.setOrientation(QtCore.Qt.Vertical)
        self.plottoolsSplitter.setObjectName(_fromUtf8("plottoolsSplitter"))
        self.layoutWidget = QtGui.QWidget(self.plottoolsSplitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.mainPlotLayout = QtGui.QGridLayout(self.layoutWidget)
        self.mainPlotLayout.setObjectName(_fromUtf8("mainPlotLayout"))
        self.layoutWidget1 = QtGui.QWidget(self.plottoolsSplitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.toolsLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.toolsLayout.setObjectName(_fromUtf8("toolsLayout"))
        self.metaDataView = QtGui.QTextEdit(self.metaDataSplitter)
        self.metaDataView.setEnabled(False)
        self.metaDataView.setMinimumSize(QtCore.QSize(300, 0))
        self.metaDataView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.metaDataView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.metaDataView.setObjectName(_fromUtf8("metaDataView"))
        self.gridLayout.addWidget(self.leftColumSplitter, 0, 0, 1, 1)
        GenericPQGView.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(GenericPQGView)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GenericPQGView.setStatusBar(self.statusbar)

        self.retranslateUi(GenericPQGView)
        QtCore.QMetaObject.connectSlotsByName(GenericPQGView)

    def retranslateUi(self, GenericPQGView):
        GenericPQGView.setWindowTitle(_translate("GenericPQGView", "MainWindow", None))

