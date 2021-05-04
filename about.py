#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import dialog_about

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QStyle
from config import Config, ResourcePath


class DialogAbout(QDialog):

    def __init__(self, parent=None):
        super(DialogAbout, self).__init__(parent)
        self.ui = dialog_about.Ui_DialogAbout()
        self.ui.setupUi(self)

        self.config = Config()
        self.customDialog()

    def customDialog(self):
        """Custom about dialog"""

        size = QSize(128, 128)

        icon = QIcon()
        icon.addFile(ResourcePath("assets/images/logo128.png"))
        self.ui.btnLogo.setIcon(icon)
        self.ui.btnLogo.setIconSize(size)
        self.ui.btnLogo.setFixedSize(size)

        name = "{}: {}".format(self.config.get("name"), self.config.get("version", "1.0"))
        self.ui.labelVersion.setText(name)

        email = self.config.get("email")
        self.ui.labelMailAddress.setText(f' <a href="mailto:{email}">{email}</a>')

        url = self.config.get("website")
        self.ui.labelHomeUrl.setText(f' <a href="{url}">{url}</a>')

        url = self.config.get("issue")
        self.ui.labelIssueUrl.setText(f' <a href="{url}">{url}</a>')

        self.ui.btnClose.setIcon(self.style().standardIcon(QStyle.SP_DialogApplyButton))

    def display(self):
        """Show dialog"""

        self.exec()
