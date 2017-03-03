# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/ui/Tools_ImageWidget.ui'
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

class Ui_Tools_ImageWidget(object):
    def setupUi(self, Tools_ImageWidget):
        Tools_ImageWidget.setObjectName(_fromUtf8("Tools_ImageWidget"))
        Tools_ImageWidget.resize(211, 87)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Tools_ImageWidget.sizePolicy().hasHeightForWidth())
        Tools_ImageWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Tools_ImageWidget)
        self.verticalLayout_3.setContentsMargins(-1, 6, -1, 6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(Tools_ImageWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(-1, 6, -1, 6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.imageRotationSlider = QtGui.QSlider(self.groupBox)
        self.imageRotationSlider.setMinimum(-1800)
        self.imageRotationSlider.setMaximum(1800)
        self.imageRotationSlider.setProperty("value", 0)
        self.imageRotationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.imageRotationSlider.setObjectName(_fromUtf8("imageRotationSlider"))
        self.horizontalLayout.addWidget(self.imageRotationSlider)
        self.imageRotationSB = QtGui.QDoubleSpinBox(self.groupBox)
        self.imageRotationSB.setDecimals(1)
        self.imageRotationSB.setMinimum(-180.0)
        self.imageRotationSB.setMaximum(180.0)
        self.imageRotationSB.setSingleStep(0.1)
        self.imageRotationSB.setObjectName(_fromUtf8("imageRotationSB"))
        self.horizontalLayout.addWidget(self.imageRotationSB)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)

        self.retranslateUi(Tools_ImageWidget)
        QtCore.QMetaObject.connectSlotsByName(Tools_ImageWidget)

    def retranslateUi(self, Tools_ImageWidget):
        Tools_ImageWidget.setWindowTitle(_translate("Tools_ImageWidget", "Form", None))
        self.groupBox.setTitle(_translate("Tools_ImageWidget", "Image tools", None))
        self.label.setText(_translate("Tools_ImageWidget", "Rotation: ", None))

