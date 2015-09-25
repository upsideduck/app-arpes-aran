from PySide import QtGui
from view.ArpesToolsView import Ui_ArpesToolsView

class ArpesToolsWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ArpesToolsWidget, self).__init__(parent)
        self.ui = Ui_ArpesToolsView()
        self.ui.setupUi(self)