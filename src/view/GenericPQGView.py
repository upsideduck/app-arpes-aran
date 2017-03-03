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
        GenericPQGView.resize(952, 772)
        self.centralwidget = QtGui.QWidget(GenericPQGView)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layoutWidget.sizePolicy().hasHeightForWidth())
        self.layoutWidget.setSizePolicy(sizePolicy)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.mainPlotLayout = QtGui.QGridLayout(self.layoutWidget)
        self.mainPlotLayout.setObjectName(_fromUtf8("mainPlotLayout"))
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.metadataTab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.metadataTab.sizePolicy().hasHeightForWidth())
        self.metadataTab.setSizePolicy(sizePolicy)
        self.metadataTab.setObjectName(_fromUtf8("metadataTab"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.metadataTab)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.metaDataView = QtGui.QTextEdit(self.metadataTab)
        self.metaDataView.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.metaDataView.sizePolicy().hasHeightForWidth())
        self.metaDataView.setSizePolicy(sizePolicy)
        self.metaDataView.setMinimumSize(QtCore.QSize(300, 0))
        self.metaDataView.setMaximumSize(QtCore.QSize(16677215, 16777215))
        self.metaDataView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.metaDataView.setObjectName(_fromUtf8("metaDataView"))
        self.horizontalLayout.addWidget(self.metaDataView)
        self.tabWidget.addTab(self.metadataTab, _fromUtf8(""))
        self.plottoolsTab = QtGui.QWidget()
        self.plottoolsTab.setObjectName(_fromUtf8("plottoolsTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.plottoolsTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.toolsLayout = QtGui.QVBoxLayout()
        self.toolsLayout.setObjectName(_fromUtf8("toolsLayout"))
        self.verticalLayout_2.addLayout(self.toolsLayout)
        self.tabWidget.addTab(self.plottoolsTab, _fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.splitter)
        GenericPQGView.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(GenericPQGView)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GenericPQGView.setStatusBar(self.statusbar)

        self.retranslateUi(GenericPQGView)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GenericPQGView)

    def retranslateUi(self, GenericPQGView):
        GenericPQGView.setWindowTitle(_translate("GenericPQGView", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.metadataTab), _translate("GenericPQGView", "Meta data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plottoolsTab), _translate("GenericPQGView", "Plot tools", None))

