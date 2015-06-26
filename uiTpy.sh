#!/bin/sh
python /usr/bin/pyside-uic view/mainView.ui > view/mainView.py
python /usr/bin/pyside-uic view/bandView.ui > view/bandView.py
python /usr/bin/pyside-uic view/fermiView.ui > view/fermiView.py
python /usr/bin/pyside-uic view/buildView.ui > view/buildView.py