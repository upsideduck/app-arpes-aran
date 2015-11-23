# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/Tools_ROIWidget.ui'
#
# Created: Tue Nov  3 16:11:32 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Tools_ROIWidget(object):
    def setupUi(self, Tools_ROIWidget):
        Tools_ROIWidget.setObjectName("Tools_ROIWidget")
        Tools_ROIWidget.resize(193, 171)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Tools_ROIWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtGui.QLabel(Tools_ROIWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horAddILROIBtn = QtGui.QPushButton(Tools_ROIWidget)
        self.horAddILROIBtn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.horAddILROIBtn.setObjectName("horAddILROIBtn")
        self.horizontalLayout_3.addWidget(self.horAddILROIBtn)
        self.horRemILROIBtn = QtGui.QPushButton(Tools_ROIWidget)
        self.horRemILROIBtn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.horRemILROIBtn.setObjectName("horRemILROIBtn")
        self.horizontalLayout_3.addWidget(self.horRemILROIBtn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(Tools_ROIWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verAddILROIBtn = QtGui.QPushButton(Tools_ROIWidget)
        self.verAddILROIBtn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.verAddILROIBtn.setObjectName("verAddILROIBtn")
        self.horizontalLayout.addWidget(self.verAddILROIBtn)
        self.verRemILROIBtn = QtGui.QPushButton(Tools_ROIWidget)
        self.verRemILROIBtn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.verRemILROIBtn.setObjectName("verRemILROIBtn")
        self.horizontalLayout.addWidget(self.verRemILROIBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.addBoxROIBtn = QtGui.QPushButton(Tools_ROIWidget)
        self.addBoxROIBtn.setObjectName("addBoxROIBtn")
        self.horizontalLayout_2.addWidget(self.addBoxROIBtn)
        self.remBoxROIBtn = QtGui.QPushButton(Tools_ROIWidget)
        self.remBoxROIBtn.setObjectName("remBoxROIBtn")
        self.horizontalLayout_2.addWidget(self.remBoxROIBtn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)

        self.retranslateUi(Tools_ROIWidget)
        QtCore.QMetaObject.connectSlotsByName(Tools_ROIWidget)

    def retranslateUi(self, Tools_ROIWidget):
        Tools_ROIWidget.setWindowTitle(QtGui.QApplication.translate("Tools_ROIWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Tools_ROIWidget", "Horizontal", None, QtGui.QApplication.UnicodeUTF8))
        self.horAddILROIBtn.setText(QtGui.QApplication.translate("Tools_ROIWidget", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.horRemILROIBtn.setText(QtGui.QApplication.translate("Tools_ROIWidget", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Tools_ROIWidget", "Vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.verAddILROIBtn.setText(QtGui.QApplication.translate("Tools_ROIWidget", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.verRemILROIBtn.setText(QtGui.QApplication.translate("Tools_ROIWidget", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.addBoxROIBtn.setText(QtGui.QApplication.translate("Tools_ROIWidget", "+ Box", None, QtGui.QApplication.UnicodeUTF8))
        self.remBoxROIBtn.setText(QtGui.QApplication.translate("Tools_ROIWidget", "- Box", None, QtGui.QApplication.UnicodeUTF8))

