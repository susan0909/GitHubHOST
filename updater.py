#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dialog_updater

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtWidgets import QDialog

from config import configurations
from worker import WorkerThread


class DialogUpdater(QDialog):

    def __init__(self, parent=None):
        super(DialogUpdater, self).__init__(parent)
        # super(DialogUpdater, self).__init__(parent, Qt.CustomizeWindowHint | Qt.WindowTitleHint)

        self.ui = dialog_updater.Ui_DialogUpdater()
        self.ui.setupUi(self)

        # self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)

        self.setting = QSettings()
        self.worker = None
        self.updating = False
        self.domains = []
        if "domains" in self.setting.childGroups():
            self.setting.beginGroup("domains")
            self.domains = self.setting.childKeys()
            self.setting.endGroup()
        if not self.domains:
            self.domains = configurations.get("domains")

    def process(self, data):
        print(data)
        action, host, ip, secs, last = data
        if last:
            self.updating = False
            print("Finished!")

    def showEvent(self, event: QtGui.QShowEvent) -> None:

        if not self.updating:
            self.updating = True
            self.worker = WorkerThread(self.domains)
            self.worker.signal.connect(self.process)
            self.worker.start()
