#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import config

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from app import AppWindow


if __name__ == '__main__':

    # HiDPI Support
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)

    # Create application and initialize
    app = QApplication(sys.argv)
    # from PyQt5.QtGui import QFont
    # app.setFont(QFont("NSimSun", 9))
    config = config.Config()
    window = AppWindow(config)

    # Running
    window.show()
    sys.exit(app.exec_())
