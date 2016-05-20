# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/ui/ImageSlicesView.ui'
#
# Created: Wed May 18 16:16:09 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ImageSlicesViewer(object):
    def setupUi(self, ImageSlicesViewer):
        ImageSlicesViewer.setObjectName("ImageSlicesViewer")
        ImageSlicesViewer.resize(681, 727)
        self.horizontalLayout = QtGui.QHBoxLayout(ImageSlicesViewer)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plotLayout = QtGui.QVBoxLayout()
        self.plotLayout.setObjectName("plotLayout")
        self.horizontalLayout.addLayout(self.plotLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(ImageSlicesViewer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.testBtn = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testBtn.sizePolicy().hasHeightForWidth())
        self.testBtn.setSizePolicy(sizePolicy)
        self.testBtn.setObjectName("testBtn")
        self.verticalLayout_2.addWidget(self.testBtn)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(ImageSlicesViewer)
        QtCore.QMetaObject.connectSlotsByName(ImageSlicesViewer)

    def retranslateUi(self, ImageSlicesViewer):
        ImageSlicesViewer.setWindowTitle(QtGui.QApplication.translate("ImageSlicesViewer", "Image slices view", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ImageSlicesViewer", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.testBtn.setText(QtGui.QApplication.translate("ImageSlicesViewer", "Test", None, QtGui.QApplication.UnicodeUTF8))

