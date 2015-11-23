# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/GenericPQGView.ui'
#
# Created: Tue Nov  3 16:11:33 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GenericPQGView(object):
    def setupUi(self, GenericPQGView):
        GenericPQGView.setObjectName("GenericPQGView")
        GenericPQGView.resize(894, 920)
        self.horizontalLayout = QtGui.QHBoxLayout(GenericPQGView)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hLayout = QtGui.QGridLayout()
        self.hLayout.setObjectName("hLayout")
        self.verticalLayout_2.addLayout(self.hLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.plotTools = QtGui.QTabWidget(GenericPQGView)
        self.plotTools.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotTools.sizePolicy().hasHeightForWidth())
        self.plotTools.setSizePolicy(sizePolicy)
        self.plotTools.setMinimumSize(QtCore.QSize(0, 0))
        self.plotTools.setMaximumSize(QtCore.QSize(16777215, 900))
        self.plotTools.setObjectName("plotTools")
        self.toolsTab = QtGui.QWidget()
        self.toolsTab.setObjectName("toolsTab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.toolsTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.toolsLayout = QtGui.QHBoxLayout()
        self.toolsLayout.setObjectName("toolsLayout")
        self.verticalLayout_4.addLayout(self.toolsLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem1)
        self.plotTools.addTab(self.toolsTab, "")
        self.verticalLayout_2.addWidget(self.plotTools)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.dataView = QtGui.QTextEdit(GenericPQGView)
        self.dataView.setEnabled(False)
        self.dataView.setMinimumSize(QtCore.QSize(300, 0))
        self.dataView.setMaximumSize(QtCore.QSize(300, 16777215))
        self.dataView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dataView.setObjectName("dataView")
        self.horizontalLayout.addWidget(self.dataView)

        self.retranslateUi(GenericPQGView)
        self.plotTools.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GenericPQGView)

    def retranslateUi(self, GenericPQGView):
        GenericPQGView.setWindowTitle(QtGui.QApplication.translate("GenericPQGView", "GenericPQGView", None, QtGui.QApplication.UnicodeUTF8))
        self.plotTools.setTabText(self.plotTools.indexOf(self.toolsTab), QtGui.QApplication.translate("GenericPQGView", "Tools", None, QtGui.QApplication.UnicodeUTF8))

