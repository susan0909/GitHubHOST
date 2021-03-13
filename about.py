#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import dialog_about

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QStyle


class DialogAbout(QDialog):

    def __init__(self, app, parent=None):
        super(DialogAbout, self).__init__(parent)
        self.ui = dialog_about.Ui_DialogAbout()
        self.ui.setupUi(self)
        from app import AppWindow
        if isinstance(app, AppWindow):
            self.app = app
            self.customDialog()

    def customDialog(self):
        """Custom about dialog"""

        _translate = QtCore.QCoreApplication.translate
        name = "{}: {}".format(_translate("WindowApp", self.app.config.get("name")), self.app.config.get("version", "1.0"))
        self.ui.labelVersion.setText(name)

        email = self.app.config.get("email")
        self.ui.labelMailAddress.setText(f' <a href="mailto:{email}">{email}</a>')

        url = self.app.config.get("website")
        self.ui.labelHomeUrl.setText(f' <a href="{url}">{url}</a>')

        url = self.app.config.get("issue")
        self.ui.labelIssueUrl.setText(f' <a href="{url}">{url}</a>')

        self.ui.btnClose.setIcon(self.style().standardIcon(QStyle.SP_DialogApplyButton))

    def display(self):
        """Show dialog"""

        self.exec()
