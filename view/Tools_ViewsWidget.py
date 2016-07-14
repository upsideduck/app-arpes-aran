# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/ui/Tools_ViewsWidget.ui'
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

class Ui_Tools_ViewsWidget(object):
    def setupUi(self, Tools_ViewsWidget):
        Tools_ViewsWidget.setObjectName(_fromUtf8("Tools_ViewsWidget"))
        Tools_ViewsWidget.resize(128, 162)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Tools_ViewsWidget.sizePolicy().hasHeightForWidth())
        Tools_ViewsWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Tools_ViewsWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Tools_ViewsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.volumeViewBtn = QtGui.QPushButton(self.groupBox)
        self.volumeViewBtn.setObjectName(_fromUtf8("volumeViewBtn"))
        self.verticalLayout_2.addWidget(self.volumeViewBtn)
        self.slicesViewBtn = QtGui.QPushButton(self.groupBox)
        self.slicesViewBtn.setObjectName(_fromUtf8("slicesViewBtn"))
        self.verticalLayout_2.addWidget(self.slicesViewBtn)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Tools_ViewsWidget)
        QtCore.QMetaObject.connectSlotsByName(Tools_ViewsWidget)

    def retranslateUi(self, Tools_ViewsWidget):
        Tools_ViewsWidget.setWindowTitle(_translate("Tools_ViewsWidget", "Form", None))
        self.groupBox.setTitle(_translate("Tools_ViewsWidget", "Views", None))
        self.volumeViewBtn.setText(_translate("Tools_ViewsWidget", "Volume", None))
        self.slicesViewBtn.setText(_translate("Tools_ViewsWidget", "Slices", None))

