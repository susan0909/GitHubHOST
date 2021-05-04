#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from PyQt5 import QtGui
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QDialog, QStyle

import dialog_advance
from config import configurations


class AdvanceDialog(QDialog):
    def __init__(self, parent=None):
        super(AdvanceDialog, self).__init__(parent)
        self.ui = dialog_advance.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btnCancel.clicked.connect(self.close)
        self.ui.btnSave.clicked.connect(self.handleClickedButtonSave)

        self.customInitDialog()

    def customInitDialog(self):

        self.ui.btnSave.setIcon(self.style().standardIcon(QStyle.SP_DialogApplyButton))
        self.ui.btnCancel.setIcon(self.style().standardIcon(QStyle.SP_DialogCancelButton))

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        domains = []
        setting = QSettings()
        # MacOS: ~/Library/Preferences/QCoreApplication.organizationDomain().QCoreApplication.applicationName().plist
        # Linux: ~/.config/QCoreApplication.organizationName()/QCoreApplication.applicationName().conf
        # print(f"Setting storage: {setting.fileName()}")
        if "domains" in setting.childGroups():
            setting.beginGroup("domains")
            domains = setting.childKeys()
            setting.endGroup()
        if not domains:
            domains = configurations.get("domains")
        self.ui.textEdit.setPlainText(f"{os.linesep}".join(list(domains)))

    def handleClickedButtonSave(self):
        setting = QSettings()
        setting.clear()
        text = self.ui.textEdit.toPlainText()
        lines = text.split()
        setting.beginGroup("domains")
        for line in lines:
            line = line.strip()
            line = line.replace('http://', '').replace('https://', '')
            line = (line.split('/'))[0]
            if line:
                setting.setValue(line, "")
        setting.endGroup()
        setting.sync()
        self.close()
