# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/ui/Tools_ARPESWidget.ui'
#
# Created: Tue Dec  8 11:41:17 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Tools_ARPESWidget(object):
    def setupUi(self, Tools_ARPESWidget):
        Tools_ARPESWidget.setObjectName("Tools_ARPESWidget")
        Tools_ARPESWidget.resize(84, 35)
        self.verticalLayout = QtGui.QVBoxLayout(Tools_ARPESWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.kSpaceCheckBox = QtGui.QCheckBox(Tools_ARPESWidget)
        self.kSpaceCheckBox.setObjectName("kSpaceCheckBox")
        self.verticalLayout.addWidget(self.kSpaceCheckBox)

        self.retranslateUi(Tools_ARPESWidget)
        QtCore.QMetaObject.connectSlotsByName(Tools_ARPESWidget)

    def retranslateUi(self, Tools_ARPESWidget):
        Tools_ARPESWidget.setWindowTitle(QtGui.QApplication.translate("Tools_ARPESWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.kSpaceCheckBox.setText(QtGui.QApplication.translate("Tools_ARPESWidget", "k-space", None, QtGui.QApplication.UnicodeUTF8))

