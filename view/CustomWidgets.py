from PySide import QtGui
from view.Tools_ARPESWidget import Ui_Tools_ARPESWidget
from view.Tools_ROIWidget import Ui_Tools_ROIWidget
from view.Tools_ViewsWidget import Ui_Tools_ViewsWidget
from view.Tools_ARPESWidget import Ui_Tools_ARPESWidget

class Tools_ARPESWidget(QtGui.QWidget):
	def __init__(self, parent=None):
		super(Tools_ARPESWidget, self).__init__(parent)
		self.ui = Ui_Tools_ARPESWidget()
		self.ui.setupUi(self)
		self.kSpaceCheckBox = self.ui.kSpaceCheckBox		
		self.ui.kSpaceCheckBox.stateChanged[int].connect(parent.on_cboxKSpaceChanged)

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


class Tools_ViewsWidget(QtGui.QWidget):
	def __init__(self, parent):
		super(Tools_ViewsWidget, self).__init__()
		self.ui = Ui_Tools_ViewsWidget()
		self.ui.setupUi(self)
		self.ui.volumeViewBtn.clicked.connect(parent.on_openVolumeView)
		self.ui.slicesViewBtn.clicked.connect(parent.on_openSlicesView)


		