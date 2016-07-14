# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/ui/Tools_ARPESWidget.ui'
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

class Ui_Tools_ARPESWidget(object):
    def setupUi(self, Tools_ARPESWidget):
        Tools_ARPESWidget.setObjectName(_fromUtf8("Tools_ARPESWidget"))
        Tools_ARPESWidget.resize(122, 85)
        self.verticalLayout = QtGui.QVBoxLayout(Tools_ARPESWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Tools_ARPESWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.kSpaceCheckBox = QtGui.QCheckBox(self.groupBox)
        self.kSpaceCheckBox.setObjectName(_fromUtf8("kSpaceCheckBox"))
        self.verticalLayout_2.addWidget(self.kSpaceCheckBox)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Tools_ARPESWidget)
        QtCore.QMetaObject.connectSlotsByName(Tools_ARPESWidget)

    def retranslateUi(self, Tools_ARPESWidget):
        Tools_ARPESWidget.setWindowTitle(_translate("Tools_ARPESWidget", "Form", None))
        self.groupBox.setTitle(_translate("Tools_ARPESWidget", "ARPES Tools", None))
        self.kSpaceCheckBox.setText(_translate("Tools_ARPESWidget", "kx-ky", None))

