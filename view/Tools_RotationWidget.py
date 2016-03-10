# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/ui/Tools_RotationWidget.ui'
#
# Created: Fri Feb 19 12:51:49 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Tools_RotationWidget(object):
    def setupUi(self, Tools_RotationWidget):
        Tools_RotationWidget.setObjectName("Tools_RotationWidget")
        Tools_RotationWidget.resize(116, 84)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Tools_RotationWidget.sizePolicy().hasHeightForWidth())
        Tools_RotationWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Tools_RotationWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(Tools_RotationWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rotationSpinBox = QtGui.QDoubleSpinBox(self.groupBox)
        self.rotationSpinBox.setDecimals(1)
        self.rotationSpinBox.setMaximum(360.0)
        self.rotationSpinBox.setSingleStep(0.1)
        self.rotationSpinBox.setObjectName("rotationSpinBox")
        self.horizontalLayout_2.addWidget(self.rotationSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox)

        self.retranslateUi(Tools_RotationWidget)
        QtCore.QMetaObject.connectSlotsByName(Tools_RotationWidget)

    def retranslateUi(self, Tools_RotationWidget):
        Tools_RotationWidget.setWindowTitle(QtGui.QApplication.translate("Tools_RotationWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Tools_RotationWidget", "Rotation (°)", None, QtGui.QApplication.UnicodeUTF8))

