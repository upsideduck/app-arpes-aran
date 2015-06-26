# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/bandView.ui'
#
# Created: Fri Apr 24 14:45:30 2015
#      by: pyside-uic 0.2.14 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_BandWindow(object):
    def setupUi(self, BandWindow):
        BandWindow.setObjectName("BandWindow")
        BandWindow.resize(1400, 862)
        self.centralwidget = QtGui.QWidget(BandWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(-1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 1, 0, 1, 1)
        self.verticalSlider = QtGui.QSlider(self.centralwidget)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout_2.addWidget(self.verticalSlider, 0, 1, 1, 1)
        self.plotWidget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setMinimumSize(QtCore.QSize(640, 480))
        self.plotWidget.setCursor(QtCore.Qt.ArrowCursor)
        self.plotWidget.setObjectName("plotWidget")
        self.gridLayout_2.addWidget(self.plotWidget, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
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
        self.tools2D = QtGui.QWidget(self.d3tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tools2D.sizePolicy().hasHeightForWidth())
        self.tools2D.setSizePolicy(sizePolicy)
        self.tools2D.setMaximumSize(QtCore.QSize(16777215, 50))
        self.tools2D.setBaseSize(QtCore.QSize(0, 0))
        self.tools2D.setObjectName("tools2D")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tools2D)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.xaxisNameLbl = QtGui.QLabel(self.tools2D)
        self.xaxisNameLbl.setText("")
        self.xaxisNameLbl.setObjectName("xaxisNameLbl")
        self.horizontalLayout_3.addWidget(self.xaxisNameLbl)
        self.xCoordinate = QtGui.QLabel(self.tools2D)
        self.xCoordinate.setText("")
        self.xCoordinate.setObjectName("xCoordinate")
        self.horizontalLayout_3.addWidget(self.xCoordinate)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_4 = QtGui.QLabel(self.tools2D)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.interpolationChooser = QtGui.QComboBox(self.tools2D)
        self.interpolationChooser.setObjectName("interpolationChooser")
        self.horizontalLayout_3.addWidget(self.interpolationChooser)
        self.label_3 = QtGui.QLabel(self.tools2D)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.colormapChooser = QtGui.QComboBox(self.tools2D)
        self.colormapChooser.setObjectName("colormapChooser")
        self.horizontalLayout_3.addWidget(self.colormapChooser)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.yaxisNameLbl = QtGui.QLabel(self.tools2D)
        self.yaxisNameLbl.setText("")
        self.yaxisNameLbl.setObjectName("yaxisNameLbl")
        self.horizontalLayout_4.addWidget(self.yaxisNameLbl)
        self.yCoordinate = QtGui.QLabel(self.tools2D)
        self.yCoordinate.setText("")
        self.yCoordinate.setObjectName("yCoordinate")
        self.horizontalLayout_4.addWidget(self.yCoordinate)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.kSpaceCheckBox = QtGui.QCheckBox(self.tools2D)
        self.kSpaceCheckBox.setEnabled(True)
        self.kSpaceCheckBox.setObjectName("kSpaceCheckBox")
        self.horizontalLayout_4.addWidget(self.kSpaceCheckBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addWidget(self.tools2D)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkAutoScale = QtGui.QCheckBox(self.d3tab)
        self.checkAutoScale.setEnabled(False)
        self.checkAutoScale.setChecked(True)
        self.checkAutoScale.setTristate(False)
        self.checkAutoScale.setObjectName("checkAutoScale")
        self.horizontalLayout_2.addWidget(self.checkAutoScale)
        self.voffsetslider = QtGui.QSlider(self.d3tab)
        self.voffsetslider.setEnabled(False)
        self.voffsetslider.setMaximum(500000)
        self.voffsetslider.setOrientation(QtCore.Qt.Horizontal)
        self.voffsetslider.setObjectName("voffsetslider")
        self.horizontalLayout_2.addWidget(self.voffsetslider)
        self.label = QtGui.QLabel(self.d3tab)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.vmaxslider = QtGui.QSlider(self.d3tab)
        self.vmaxslider.setEnabled(False)
        self.vmaxslider.setMaximum(500000)
        self.vmaxslider.setOrientation(QtCore.Qt.Horizontal)
        self.vmaxslider.setObjectName("vmaxslider")
        self.horizontalLayout_2.addWidget(self.vmaxslider)
        self.label_2 = QtGui.QLabel(self.d3tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem2)
        self.plotTools.addTab(self.d3tab, "")
        self.verticalLayout.addWidget(self.plotTools)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.dataView = QtGui.QTextEdit(self.centralwidget)
        self.dataView.setEnabled(False)
        self.dataView.setMinimumSize(QtCore.QSize(300, 0))
        self.dataView.setMaximumSize(QtCore.QSize(300, 16777215))
        self.dataView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dataView.setObjectName("dataView")
        self.horizontalLayout.addWidget(self.dataView)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        BandWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 22))
        self.menubar.setObjectName("menubar")
        BandWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(BandWindow)
        self.statusBar.setObjectName("statusBar")
        BandWindow.setStatusBar(self.statusBar)

        self.retranslateUi(BandWindow)
        self.plotTools.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BandWindow)

    def retranslateUi(self, BandWindow):
        BandWindow.setWindowTitle(QtGui.QApplication.translate("BandWindow", "ARAN Band Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("BandWindow", "Interpolation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("BandWindow", "Color space", None, QtGui.QApplication.UnicodeUTF8))
        self.kSpaceCheckBox.setText(QtGui.QApplication.translate("BandWindow", "k-space", None, QtGui.QApplication.UnicodeUTF8))
        self.checkAutoScale.setText(QtGui.QApplication.translate("BandWindow", "Auto scale", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("BandWindow", "Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("BandWindow", "Max", None, QtGui.QApplication.UnicodeUTF8))
        self.plotTools.setTabText(self.plotTools.indexOf(self.d3tab), QtGui.QApplication.translate("BandWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))

