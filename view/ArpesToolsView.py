# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/ArpesToolsView.ui'
#
# Created: Fri Sep 25 10:44:46 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ArpesToolsView(object):
    def setupUi(self, ArpesToolsView):
        ArpesToolsView.setObjectName("ArpesToolsView")
        ArpesToolsView.resize(84, 45)
        self.verticalLayout = QtGui.QVBoxLayout(ArpesToolsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.kSpaceCheckBox = QtGui.QCheckBox(ArpesToolsView)
        self.kSpaceCheckBox.setObjectName("kSpaceCheckBox")
        self.verticalLayout.addWidget(self.kSpaceCheckBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(ArpesToolsView)
        QtCore.QMetaObject.connectSlotsByName(ArpesToolsView)

    def retranslateUi(self, ArpesToolsView):
        ArpesToolsView.setWindowTitle(QtGui.QApplication.translate("ArpesToolsView", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.kSpaceCheckBox.setText(QtGui.QApplication.translate("ArpesToolsView", "k-space", None, QtGui.QApplication.UnicodeUTF8))

