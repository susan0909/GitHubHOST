#!/usr/bin/env python3
# encoding: utf-8

import time
import dialog_update

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog


class DialogUpdate(QDialog):

    def __init__(self, app, parent=None):
        super(DialogUpdate, self).__init__(parent)
        self.ui = dialog_update.Ui_DialogUpdate()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.fetched = []
        from app import AppWindow
        if isinstance(app, AppWindow):
            self.app = app

    def updateProgress(self, item):
        """Update Progress bar"""

        host, ip = item
        self.fetched.append(host)
        self.app.domains[host] = ip
        total = len(self.app.domains)
        current = len(self.fetched)
        self.ui.labelItem .setText(host)
        progress = 100 * (current / total)
        self.ui.progressBar.setValue(progress)

        if total == current:
            time.sleep(1)
            self.close()
