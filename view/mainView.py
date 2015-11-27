# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/mainView.ui'
#
# Created: Wed Nov 25 15:45:48 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1714, 985)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(-1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(400, 0))
        self.widget.setMaximumSize(QtCore.QSize(400, 16777215))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtGui.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.dirView = QtGui.QTreeView(self.widget)
        self.dirView.setMaximumSize(QtCore.QSize(400, 200))
        self.dirView.setObjectName("dirView")
        self.gridLayout_3.addWidget(self.dirView, 0, 0, 1, 1)
        self.fileView = QtGui.QTreeView(self.widget)
        self.fileView.setAutoExpandDelay(0)
        self.fileView.setSortingEnabled(True)
        self.fileView.setObjectName("fileView")
        self.gridLayout_3.addWidget(self.fileView, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.plotWidget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setMinimumSize(QtCore.QSize(640, 480))
        self.plotWidget.setCursor(QtCore.Qt.ArrowCursor)
        self.plotWidget.setObjectName("plotWidget")
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
        self.plotTools.setObjectName("plotTools")
        self.d3tab = QtGui.QWidget()
        self.d3tab.setObjectName("d3tab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.d3tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.loadBtn = QtGui.QPushButton(self.d3tab)
        self.loadBtn.setEnabled(False)
        self.loadBtn.setObjectName("loadBtn")
        self.verticalLayout_4.addWidget(self.loadBtn)
        self.buildBtn = QtGui.QPushButton(self.d3tab)
        self.buildBtn.setEnabled(True)
        self.buildBtn.setObjectName("buildBtn")
        self.verticalLayout_4.addWidget(self.buildBtn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem)
        self.plotTools.addTab(self.d3tab, "")
        self.verticalLayout.addWidget(self.plotTools)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.entriesBox = QtGui.QComboBox(self.widget_2)
        self.entriesBox.setMinimumSize(QtCore.QSize(0, 0))
        self.entriesBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.entriesBox.setObjectName("entriesBox")
        self.verticalLayout_3.addWidget(self.entriesBox)
        self.dataView = QtGui.QTextEdit(self.widget_2)
        self.dataView.setEnabled(False)
        self.dataView.setMinimumSize(QtCore.QSize(0, 0))
        self.dataView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dataView.setObjectName("dataView")
        self.verticalLayout_3.addWidget(self.dataView)
        self.horizontalLayout.addWidget(self.widget_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1714, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.plotTools.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "ARAN Experiment Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.loadBtn.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.buildBtn.setText(QtGui.QApplication.translate("MainWindow", "Build", None, QtGui.QApplication.UnicodeUTF8))
        self.plotTools.setTabText(self.plotTools.indexOf(self.d3tab), QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))

