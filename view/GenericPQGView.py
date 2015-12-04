# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/ui/GenericPQGView.ui'
#
# Created: Fri Dec  4 12:06:06 2015
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
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.toolsLayout = QtGui.QHBoxLayout()
        self.toolsLayout.setObjectName("toolsLayout")
        self.verticalLayout_2.addLayout(self.toolsLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.dataView = QtGui.QTextEdit(GenericPQGView)
        self.dataView.setEnabled(False)
        self.dataView.setMinimumSize(QtCore.QSize(300, 0))
        self.dataView.setMaximumSize(QtCore.QSize(300, 16777215))
        self.dataView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dataView.setObjectName("dataView")
        self.horizontalLayout.addWidget(self.dataView)

        self.retranslateUi(GenericPQGView)
        QtCore.QMetaObject.connectSlotsByName(GenericPQGView)

    def retranslateUi(self, GenericPQGView):
        GenericPQGView.setWindowTitle(QtGui.QApplication.translate("GenericPQGView", "GenericPQGView", None, QtGui.QApplication.UnicodeUTF8))

