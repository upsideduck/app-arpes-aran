# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/ui/VolumeView.ui'
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

class Ui_VolumeViewer(object):
    def setupUi(self, VolumeViewer):
        VolumeViewer.setObjectName(_fromUtf8("VolumeViewer"))
        VolumeViewer.resize(681, 727)
        self.horizontalLayout = QtGui.QHBoxLayout(VolumeViewer)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.plotLayout = QtGui.QVBoxLayout()
        self.plotLayout.setObjectName(_fromUtf8("plotLayout"))
        self.horizontalLayout.addLayout(self.plotLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(VolumeViewer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.thresholdLineEdit = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thresholdLineEdit.sizePolicy().hasHeightForWidth())
        self.thresholdLineEdit.setSizePolicy(sizePolicy)
        self.thresholdLineEdit.setObjectName(_fromUtf8("thresholdLineEdit"))
        self.verticalLayout_2.addWidget(self.thresholdLineEdit)
        self.thresholdBtn = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thresholdBtn.sizePolicy().hasHeightForWidth())
        self.thresholdBtn.setSizePolicy(sizePolicy)
        self.thresholdBtn.setObjectName(_fromUtf8("thresholdBtn"))
        self.verticalLayout_2.addWidget(self.thresholdBtn)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(VolumeViewer)
        QtCore.QMetaObject.connectSlotsByName(VolumeViewer)

    def retranslateUi(self, VolumeViewer):
        VolumeViewer.setWindowTitle(_translate("VolumeViewer", "Volume view", None))
        self.groupBox.setTitle(_translate("VolumeViewer", "Tools", None))
        self.thresholdBtn.setText(_translate("VolumeViewer", "Threshold", None))

