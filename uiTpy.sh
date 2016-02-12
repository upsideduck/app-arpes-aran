#!/bin/sh
python /usr/local/bin/pyside-uic view/ui/mainView.ui > view/mainView.py
python /usr/local/bin/pyside-uic view/ui/ArpesBuildView.ui > view/ArpesBuildView.py
python /usr/local/bin/pyside-uic view/ui/Tools_ARPESWidget.ui > view/Tools_ARPESWidget.py
python /usr/local/bin/pyside-uic view/ui/Tools_ViewsWidget.ui > view/Tools_ViewsWidget.py
python /usr/local/bin/pyside-uic view/ui/Tools_ROIWidget.ui > view/Tools_ROIWidget.py
python /usr/local/bin/pyside-uic view/ui/Tools_RotationWidget.ui > view/Tools_RotationWidget.py
python /usr/local/bin/pyside-uic view/ui/GenericPQGView.ui > view/GenericPQGView.py
python /usr/local/bin/pyside-uic view/ui/VolumeView.ui > view/VolumeView.py
python /usr/local/bin/pyside-uic view/ui/ImageSlicesView.ui > view/ImageSlicesView.py