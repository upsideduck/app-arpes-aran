# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/ui/Tools_ViewsWidget.ui'
#
# Created: Fri Dec  4 12:06:05 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Tools_ViewsWidget(object):
    def setupUi(self, Tools_ViewsWidget):
        Tools_ViewsWidget.setObjectName("Tools_ViewsWidget")
        Tools_ViewsWidget.resize(128, 78)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Tools_ViewsWidget.sizePolicy().hasHeightForWidth())
        Tools_ViewsWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Tools_ViewsWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(Tools_ViewsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.volumeViewBtn = QtGui.QPushButton(self.groupBox)
        self.volumeViewBtn.setObjectName("volumeViewBtn")
        self.verticalLayout_2.addWidget(self.volumeViewBtn)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Tools_ViewsWidget)
        QtCore.QMetaObject.connectSlotsByName(Tools_ViewsWidget)

    def retranslateUi(self, Tools_ViewsWidget):
        Tools_ViewsWidget.setWindowTitle(QtGui.QApplication.translate("Tools_ViewsWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Tools_ViewsWidget", "Views", None, QtGui.QApplication.UnicodeUTF8))
        self.volumeViewBtn.setText(QtGui.QApplication.translate("Tools_ViewsWidget", "Volume", None, QtGui.QApplication.UnicodeUTF8))
