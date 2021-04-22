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

        # MacOS: ~/Library/Preferences/QCoreApplication.organizationDomain().QCoreApplication.applicationName().plist
        self.settings = QSettings()
        # print(self.settings.fileName())

        self.ui.btnCancel.clicked.connect(self.close)
        self.ui.btnSave.clicked.connect(self.handleClickedButtonSave)

        self.customInitDialog()

    def customInitDialog(self):

        self.ui.btnSave.setIcon(self.style().standardIcon(QStyle.SP_DialogApplyButton))
        self.ui.btnCancel.setIcon(self.style().standardIcon(QStyle.SP_DialogCancelButton))

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        domains = []
        if "domains" in self.settings.childGroups():
            self.settings.beginGroup("domains")
            domains = self.settings.childKeys()
            self.settings.endGroup()
        if not domains:
            domains = configurations.get("domains")
        self.ui.textEdit.setPlainText(f"{os.linesep}".join(list(domains)))

    def handleClickedButtonSave(self):
        text = self.ui.textEdit.toPlainText()
        lines = text.split()
        self.settings.beginGroup("domains")
        for line in lines:
            line = line.strip()
            line = line.replace('http://', '').replace('https://', '')
            line = (line.split('/'))[0]
            if line:
                self.settings.setValue(line, "")
        self.settings.endGroup()
        self.settings.sync()
        self.close()
