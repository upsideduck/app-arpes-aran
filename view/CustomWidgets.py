from PySide import QtGui
from view.Tools_ARPESWidget import Ui_Tools_ARPESWidget
from view.Tools_ROIWidget import Ui_Tools_ROIWidget

class Tools_ARPESWidget(QtGui.QWidget):
	def __init__(self, parent=None):
		super(Tools_ARPESWidget, self).__init__(parent)
		self.ui = Ui_Tools_ARPESWidget()
		self.ui.setupUi(self)

class Tools_ROIWidget(QtGui.QWidget):
	def __init__(self, parent):
		super(Tools_ROIWidget, self).__init__()
		self.ui = Ui_Tools_ROIWidget()
		self.ui.setupUi(self)
		self.ui.horAddILROIBtn.clicked.connect(parent.on_btnAddHorIlRoi)
		self.ui.horRemILROIBtn.clicked.connect(parent.on_btnRemHorIlRoi)
		self.ui.verAddILROIBtn.clicked.connect(parent.on_btnAddVerIlRoi)
		self.ui.verRemILROIBtn.clicked.connect(parent.on_btnRemVerIlRoi)
		self.ui.addBoxROIBtn.clicked.connect(parent.on_btnAddBoxRoi)
		self.ui.remBoxROIBtn.clicked.connect(parent.on_btnRemBoxRoi)

		