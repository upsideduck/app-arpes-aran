from PyQt4 import QtGui
from view.Tools_ARPESWidget import Ui_Tools_ARPESWidget
from view.Tools_ROIWidget import Ui_Tools_ROIWidget
from view.Tools_ViewsWidget import Ui_Tools_ViewsWidget
from view.Tools_ARPESWidget import Ui_Tools_ARPESWidget
from view.Tools_ImageWidget import Ui_Tools_ImageWidget

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
		self.ui.verAddILROIBtn.clicked.connect(parent.on_btnAddVerIlRoi)
		self.ui.addBoxROIBtn.clicked.connect(parent.on_btnAddBoxRoi)
		self.ui.removeROIBtn.clicked.connect(parent.on_btnRemRoi)
		self.ui.resetROIBtn.clicked.connect(parent.on_btnResetRoi)
		self.ui.screenAngleROICheckBox.stateChanged[int].connect(parent.on_screenAngleROICheckBox)

class Tools_ImageWidget(QtGui.QWidget):
	def __init__(self, parent):
		super(Tools_ImageWidget, self).__init__()
		self.ui = Ui_Tools_ImageWidget()
		self.ui.setupUi(self)
		self.ui.imageRotationSlider.valueChanged[int].connect(parent.on_imageRotationSliderMoved)
		self.ui.imageRotationSB.valueChanged[float].connect(parent.on_imageRotationSBChanged)
		self.ui.imageRotationSlider.sliderReleased.connect(parent.on_imageRotationSliderReleased)



class Tools_ViewsWidget(QtGui.QWidget):
	def __init__(self, parent):
		super(Tools_ViewsWidget, self).__init__()
		self.ui = Ui_Tools_ViewsWidget()
		self.ui.setupUi(self)
		self.ui.volumeViewBtn.clicked.connect(parent.on_openVolumeView)
		self.ui.slicesViewBtn.clicked.connect(parent.on_openSlicesView)


		