#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dialog_donate

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QStyle
from config import ResourcePath


class DialogDonate(QDialog):

    def __init__(self, parent=None):
        super(DialogDonate, self).__init__(parent)

        self.ui = dialog_donate.Ui_DialogDonate()
        self.ui.setupUi(self)

        self.customDialog()

    def customDialog(self):
        """Custom donate dialog"""

        size = QSize(256, 256)

        self.ui.labelWechat.setFixedWidth(size.width())
        self.ui.labelAlipay.setFixedWidth(size.width())

        # self.ui.btnIconWechat.setStyleSheet('QPushButton:focus {border: none;outline: none;}')
        # self.ui.btnIconAlipay.setStyleSheet('QPushButton:focus {border: none;outline: none;}')

        iconWx = QIcon()
        iconWx.addFile(ResourcePath("assets/images/susan-wechat-256.jpg"))
        self.ui.btnIconWechat.setIcon(iconWx)
        self.ui.btnIconWechat.setIconSize(size)
        self.ui.btnIconWechat.setFixedSize(size)

        iconAli = QIcon()
        iconAli.addFile(ResourcePath("assets/images/susan-alipay-256.jpg"))
        self.ui.btnIconAlipay.setIcon(iconAli)
        self.ui.btnIconAlipay.setIconSize(size)
        self.ui.btnIconAlipay.setFixedSize(size)

        self.ui.btnClose.setIcon(self.style().standardIcon(QStyle.SP_DialogApplyButton))

    def display(self):
        """Show dialog"""

        self.exec()
