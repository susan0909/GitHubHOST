#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dialog_donate

from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QApplication, QDialog, QStyle


class DialogDonate(QDialog):

    def __init__(self, app, parent=None):
        super(DialogDonate, self).__init__(parent)

        self.trans = QTranslator()
        self.trans.load(":/translations/dialog_donate")
        QApplication.instance().installTranslator(self.trans)

        self.ui = dialog_donate.Ui_DialogDonate()
        self.ui.setupUi(self)
        from app import AppWindow
        if isinstance(app, AppWindow):
            self.app = app
            self.customDialog()

    def customDialog(self):
        """Custom donate dialog"""

        self.ui.btnWechat.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
        self.ui.btnAlipay.setIcon(self.style().standardIcon(QStyle.SP_ArrowRight))
        self.ui.btnClose.setIcon(self.style().standardIcon(QStyle.SP_DialogApplyButton))

    def display(self):
        """Show dialog"""

        self.exec()
