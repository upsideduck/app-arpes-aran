#!/bin/sh
python /usr/local/bin/pyside-uic view/mainView.ui > view/mainView.py
python /usr/local/bin/pyside-uic view/Generic2dimView.ui > view/Generic2dimView.py
python /usr/local/bin/pyside-uic view/Generic3dimView.ui > view/Generic3dimView.py
python /usr/local/bin/pyside-uic view/ArpesBuildView.ui > view/ArpesBuildView.py
python /usr/local/bin/pyside-uic view/Tools_ARPESWidget.ui > view/Tools_ARPESWidget.py
python /usr/local/bin/pyside-uic view/Tools_ROIWidget.ui > view/Tools_ROIWidget.py
python /usr/local/bin/pyside-uic view/GenericPQGView.ui > view/GenericPQGView.py