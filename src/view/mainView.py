# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/ui/mainView.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1714, 985)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(400, 0))
        self.widget.setMaximumSize(QtCore.QSize(400, 16777215))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.dirView = QtGui.QTreeView(self.widget)
        self.dirView.setMaximumSize(QtCore.QSize(400, 200))
        self.dirView.setObjectName(_fromUtf8("dirView"))
        self.gridLayout_3.addWidget(self.dirView, 0, 0, 1, 1)
        self.fileView = QtGui.QTreeView(self.widget)
        self.fileView.setAutoExpandDelay(0)
        self.fileView.setSortingEnabled(True)
        self.fileView.setObjectName(_fromUtf8("fileView"))
        self.gridLayout_3.addWidget(self.fileView, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plotWidget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setMinimumSize(QtCore.QSize(640, 480))
        self.plotWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.plotWidget.setObjectName(_fromUtf8("plotWidget"))
        self.verticalLayout.addWidget(self.plotWidget)
        self.plotTools = QtGui.QTabWidget(self.centralwidget)
        self.plotTools.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotTools.sizePolicy().hasHeightForWidth())
        self.plotTools.setSizePolicy(sizePolicy)
        self.plotTools.setMinimumSize(QtCore.QSize(0, 0))
        self.plotTools.setMaximumSize(QtCore.QSize(16777215, 900))
        self.plotTools.setObjectName(_fromUtf8("plotTools"))
        self.d3tab = QtGui.QWidget()
        self.d3tab.setObjectName(_fromUtf8("d3tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.d3tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.loadBtn = QtGui.QPushButton(self.d3tab)
        self.loadBtn.setEnabled(False)
        self.loadBtn.setObjectName(_fromUtf8("loadBtn"))
        self.verticalLayout_4.addWidget(self.loadBtn)
        self.buildBtn = QtGui.QPushButton(self.d3tab)
        self.buildBtn.setEnabled(True)
        self.buildBtn.setObjectName(_fromUtf8("buildBtn"))
        self.verticalLayout_4.addWidget(self.buildBtn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem)
        self.plotTools.addTab(self.d3tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.plotTools)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.entriesBox = QtGui.QComboBox(self.widget_2)
        self.entriesBox.setMinimumSize(QtCore.QSize(0, 0))
        self.entriesBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.entriesBox.setObjectName(_fromUtf8("entriesBox"))
        self.verticalLayout_3.addWidget(self.entriesBox)
        self.metaDataView = QtGui.QTextEdit(self.widget_2)
        self.metaDataView.setEnabled(False)
        self.metaDataView.setMinimumSize(QtCore.QSize(0, 0))
        self.metaDataView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.metaDataView.setObjectName(_fromUtf8("metaDataView"))
        self.verticalLayout_3.addWidget(self.metaDataView)
        self.horizontalLayout.addWidget(self.widget_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1714, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.plotTools.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ARAN Experiment Viewer", None))
        self.loadBtn.setText(_translate("MainWindow", "Load", None))
        self.buildBtn.setText(_translate("MainWindow", "Build", None))
        self.plotTools.setTabText(self.plotTools.indexOf(self.d3tab), _translate("MainWindow", "Tools", None))

