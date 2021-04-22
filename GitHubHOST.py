#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import config

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from app import AppWindow
from config import configurations


if __name__ == '__main__':

    # HiDPI Support
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)

    # Application register
    QtCore.QCoreApplication.setOrganizationName("Btz")
    QtCore.QCoreApplication.setOrganizationDomain("bentuzi.com")
    QtCore.QCoreApplication.setApplicationName(configurations.get("name"))
    QtCore.QCoreApplication.setApplicationVersion(configurations.get("version"))

    # Create application and initialize
    app = QApplication(sys.argv)
    config = config.Config()
    window = AppWindow(config)

    # Running
    window.show()
    sys.exit(app.exec_())
