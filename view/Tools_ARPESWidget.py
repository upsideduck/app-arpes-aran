# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/ui/Tools_ARPESWidget.ui'
#
# Created: Wed May 18 16:16:08 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Tools_ARPESWidget(object):
    def setupUi(self, Tools_ARPESWidget):
        Tools_ARPESWidget.setObjectName("Tools_ARPESWidget")
        Tools_ARPESWidget.resize(122, 85)
        self.verticalLayout = QtGui.QVBoxLayout(Tools_ARPESWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(Tools_ARPESWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.kSpaceCheckBox = QtGui.QCheckBox(self.groupBox)
        self.kSpaceCheckBox.setObjectName("kSpaceCheckBox")
        self.verticalLayout_2.addWidget(self.kSpaceCheckBox)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Tools_ARPESWidget)
        QtCore.QMetaObject.connectSlotsByName(Tools_ARPESWidget)

    def retranslateUi(self, Tools_ARPESWidget):
        Tools_ARPESWidget.setWindowTitle(QtGui.QApplication.translate("Tools_ARPESWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Tools_ARPESWidget", "ARPES Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.kSpaceCheckBox.setText(QtGui.QApplication.translate("Tools_ARPESWidget", "kx-ky", None, QtGui.QApplication.UnicodeUTF8))

