# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/ui/VolumeView.ui'
#
# Created: Wed May 18 16:16:09 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_VolumeViewer(object):
    def setupUi(self, VolumeViewer):
        VolumeViewer.setObjectName("VolumeViewer")
        VolumeViewer.resize(681, 727)
        self.horizontalLayout = QtGui.QHBoxLayout(VolumeViewer)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plotLayout = QtGui.QVBoxLayout()
        self.plotLayout.setObjectName("plotLayout")
        self.horizontalLayout.addLayout(self.plotLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(VolumeViewer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.thresholdLineEdit = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thresholdLineEdit.sizePolicy().hasHeightForWidth())
        self.thresholdLineEdit.setSizePolicy(sizePolicy)
        self.thresholdLineEdit.setObjectName("thresholdLineEdit")
        self.verticalLayout_2.addWidget(self.thresholdLineEdit)
        self.thresholdBtn = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thresholdBtn.sizePolicy().hasHeightForWidth())
        self.thresholdBtn.setSizePolicy(sizePolicy)
        self.thresholdBtn.setObjectName("thresholdBtn")
        self.verticalLayout_2.addWidget(self.thresholdBtn)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(VolumeViewer)
        QtCore.QMetaObject.connectSlotsByName(VolumeViewer)

    def retranslateUi(self, VolumeViewer):
        VolumeViewer.setWindowTitle(QtGui.QApplication.translate("VolumeViewer", "Volume view", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("VolumeViewer", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.thresholdBtn.setText(QtGui.QApplication.translate("VolumeViewer", "Threshold", None, QtGui.QApplication.UnicodeUTF8))

