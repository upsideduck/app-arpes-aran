# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/ui/ImageSlicesView.ui'
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

class Ui_ImageSlicesViewer(object):
    def setupUi(self, ImageSlicesViewer):
        ImageSlicesViewer.setObjectName(_fromUtf8("ImageSlicesViewer"))
        ImageSlicesViewer.resize(681, 727)
        self.horizontalLayout = QtGui.QHBoxLayout(ImageSlicesViewer)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.plotLayout = QtGui.QVBoxLayout()
        self.plotLayout.setObjectName(_fromUtf8("plotLayout"))
        self.horizontalLayout.addLayout(self.plotLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(ImageSlicesViewer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.testBtn = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testBtn.sizePolicy().hasHeightForWidth())
        self.testBtn.setSizePolicy(sizePolicy)
        self.testBtn.setObjectName(_fromUtf8("testBtn"))
        self.verticalLayout_2.addWidget(self.testBtn)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(ImageSlicesViewer)
        QtCore.QMetaObject.connectSlotsByName(ImageSlicesViewer)

    def retranslateUi(self, ImageSlicesViewer):
        ImageSlicesViewer.setWindowTitle(_translate("ImageSlicesViewer", "Image slices view", None))
        self.groupBox.setTitle(_translate("ImageSlicesViewer", "Tools", None))
        self.testBtn.setText(_translate("ImageSlicesViewer", "Test", None))

