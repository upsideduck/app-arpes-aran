# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/ui/GenericPQGViewMW.ui'
#
# Created: Fri Feb 19 12:51:49 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GenericPQGView(object):
    def setupUi(self, GenericPQGView):
        GenericPQGView.setObjectName("GenericPQGView")
        GenericPQGView.resize(800, 600)
        self.centralwidget = QtGui.QWidget(GenericPQGView)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hLayout = QtGui.QGridLayout()
        self.hLayout.setObjectName("hLayout")
        self.verticalLayout_2.addLayout(self.hLayout)
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.toolsLayout = QtGui.QHBoxLayout()
        self.toolsLayout.setObjectName("toolsLayout")
        self.verticalLayout_2.addLayout(self.toolsLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.dataView = QtGui.QTextEdit(self.centralwidget)
        self.dataView.setEnabled(False)
        self.dataView.setMinimumSize(QtCore.QSize(300, 0))
        self.dataView.setMaximumSize(QtCore.QSize(300, 16777215))
        self.dataView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dataView.setObjectName("dataView")
        self.horizontalLayout.addWidget(self.dataView)
        GenericPQGView.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(GenericPQGView)
        self.statusbar.setObjectName("statusbar")
        GenericPQGView.setStatusBar(self.statusbar)

        self.retranslateUi(GenericPQGView)
        QtCore.QMetaObject.connectSlotsByName(GenericPQGView)

    def retranslateUi(self, GenericPQGView):
        GenericPQGView.setWindowTitle(QtGui.QApplication.translate("GenericPQGView", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))

