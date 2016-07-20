#!/bin/sh
python ./pyuic.py src/view/ui/mainView.ui > src/view/mainView.py
python ./pyuic.py src/view/ui/ArpesBuildView.ui > src/view/ArpesBuildView.py
python ./pyuic.py src/view/ui/Tools_ARPESWidget.ui > src/view/Tools_ARPESWidget.py
python ./pyuic.py src/view/ui/Tools_ViewsWidget.ui > src/view/Tools_ViewsWidget.py
#python ./pyuic.py src/view/ui/Tools_ROIWidget.ui > src/view/Tools_ROIWidget.py
python ./pyuic.py src/view/ui/Tools_ROIWidget2.ui > src/view/Tools_ROIWidget.py
#python ./pyuic.py src/view/ui/Tools_RotationWidget.ui > src/view/Tools_RotationWidget.py
#python ./pyuic.py src/view/ui/GenericPQGView.ui > src/view/GenericPQGView.py
python ./pyuic.py src/view/ui/GenericPQGViewMW.ui > src/view/GenericPQGView.py
python ./pyuic.py src/view/ui/VolumeView.ui > src/view/VolumeView.py
python ./pyuic.py src/view/ui/ImageSlicesView.ui > src/view/ImageSlicesView.py
python ./pyuic.py src/view/ui/Tools_ImageWidget.ui > src/view/Tools_ImageWidget.py