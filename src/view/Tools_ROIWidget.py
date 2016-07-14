# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/ui/Tools_ROIWidget2.ui'
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

class Ui_Tools_ROIWidget(object):
    def setupUi(self, Tools_ROIWidget):
        Tools_ROIWidget.setObjectName(_fromUtf8("Tools_ROIWidget"))
        Tools_ROIWidget.resize(283, 209)
        Tools_ROIWidget.setBaseSize(QtCore.QSize(283, 209))
        self.gridLayout = QtGui.QGridLayout(Tools_ROIWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Tools_ROIWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.horAddILROIBtn = QtGui.QPushButton(self.groupBox)
        self.horAddILROIBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horAddILROIBtn.setObjectName(_fromUtf8("horAddILROIBtn"))
        self.verticalLayout_2.addWidget(self.horAddILROIBtn)
        self.verAddILROIBtn = QtGui.QPushButton(self.groupBox)
        self.verAddILROIBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verAddILROIBtn.setObjectName(_fromUtf8("verAddILROIBtn"))
        self.verticalLayout_2.addWidget(self.verAddILROIBtn)
        self.addBoxROIBtn = QtGui.QPushButton(self.groupBox)
        self.addBoxROIBtn.setObjectName(_fromUtf8("addBoxROIBtn"))
        self.verticalLayout_2.addWidget(self.addBoxROIBtn)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.anlgeROILbl = QtGui.QLabel(self.groupBox)
        self.anlgeROILbl.setObjectName(_fromUtf8("anlgeROILbl"))
        self.horizontalLayout_2.addWidget(self.anlgeROILbl)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.screenAngleROICheckBox = QtGui.QCheckBox(self.groupBox)
        self.screenAngleROICheckBox.setEnabled(False)
        self.screenAngleROICheckBox.setObjectName(_fromUtf8("screenAngleROICheckBox"))
        self.verticalLayout.addWidget(self.screenAngleROICheckBox)
        self.resetROIBtn = QtGui.QPushButton(self.groupBox)
        self.resetROIBtn.setEnabled(False)
        self.resetROIBtn.setObjectName(_fromUtf8("resetROIBtn"))
        self.verticalLayout.addWidget(self.resetROIBtn)
        self.removeROIBtn = QtGui.QPushButton(self.groupBox)
        self.removeROIBtn.setEnabled(False)
        self.removeROIBtn.setObjectName(_fromUtf8("removeROIBtn"))
        self.verticalLayout.addWidget(self.removeROIBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)

        self.retranslateUi(Tools_ROIWidget)
        QtCore.QMetaObject.connectSlotsByName(Tools_ROIWidget)

    def retranslateUi(self, Tools_ROIWidget):
        Tools_ROIWidget.setWindowTitle(_translate("Tools_ROIWidget", "Form", None))
        self.groupBox.setTitle(_translate("Tools_ROIWidget", "Region of interest", None))
        self.label.setText(_translate("Tools_ROIWidget", "Add:", None))
        self.horAddILROIBtn.setText(_translate("Tools_ROIWidget", "Hor line", None))
        self.verAddILROIBtn.setText(_translate("Tools_ROIWidget", "Ver line", None))
        self.addBoxROIBtn.setText(_translate("Tools_ROIWidget", "Box", None))
        self.label_2.setText(_translate("Tools_ROIWidget", "Selected:", None))
        self.label_3.setText(_translate("Tools_ROIWidget", "Angle:", None))
        self.anlgeROILbl.setText(_translate("Tools_ROIWidget", "0", None))
        self.label_4.setText(_translate("Tools_ROIWidget", "°", None))
        self.screenAngleROICheckBox.setText(_translate("Tools_ROIWidget", "Detector angles", None))
        self.resetROIBtn.setText(_translate("Tools_ROIWidget", "Reset", None))
        self.removeROIBtn.setText(_translate("Tools_ROIWidget", "Remove", None))

