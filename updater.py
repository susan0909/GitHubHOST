#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import dialog_updater

import qtawesome as qta

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtWidgets import QDialog

from config import configurations
from worker import WorkerThread, CleanerThread


class DialogUpdater(QDialog):

    def __init__(self, parent=None):
        super(DialogUpdater, self).__init__(parent)
        # super(DialogUpdater, self).__init__(parent, Qt.CustomizeWindowHint | Qt.WindowTitleHint)

        self.ui = dialog_updater.Ui_DialogUpdater()
        self.ui.setupUi(self)

        self.ui.listWidget.setStyleSheet("QListWidget { outline:0; background-color: transparent; }"
                                         "QListWidget::item {border-bottom: 1px solid #999;}"
                                         "QListWidget::item::selected { color: #fff; }")

        # self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)

        self.worker = None
        self.cleaner = None

        self.setting = QSettings()
        self.updating = False
        self.domains = []
        if "domains" in self.setting.childGroups():
            self.setting.beginGroup("domains")
            self.domains = self.setting.childKeys()
            self.setting.endGroup()
        if not self.domains:
            self.domains = configurations.get("domains")

    def process(self, data):
        # print(data)
        action, host, ip, secs, last = data
        if "end" == action and ip and host and secs and secs < 10000:
            if hasattr(self.parent(), "addParsedDomain"):
                self.parent().addParsedDomain(host, ip)

        if self.ui.listWidget.count() > 0:
            for index in range(self.ui.listWidget.count()):
                item = self.ui.listWidget.item(index)
                data = item.data(QtWidgets.QListWidgetItem.UserType)
                if data and data == host:
                    # oldWidget = self.ui.listWidget.itemWidget(item)
                    widget = self.makeDomainItemWidget(index, host, action, ip, secs)
                    self.ui.listWidget.removeItemWidget(item)
                    self.ui.listWidget.setItemWidget(item, widget)
                    self.ui.listWidget.scrollToItem(item)
                    # self.ui.listWidget.setCurrentItem(item)
                    # itemIndex = self.ui.listWidget.indexFromItem(item)
                    # self.ui.listWidget.update(itemIndex)

        if last:
            self.updating = False
            self.cleaner = CleanerThread()
            self.cleaner.signal.connect(self.close)
            self.cleaner.start()

    def makeDomainItemWidget(self, idx, domain, status=None, ip=None, ms=None):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        no = QtWidgets.QLabel()
        # no.setStyleSheet('background-color:blue')
        no.setText(f"#{idx+1}")
        no.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(no)
        layout.setStretch(0, 1)

        name = QtWidgets.QLabel()
        name.setText(domain)
        # name.setStyleSheet('background-color:gray')
        layout.addWidget(name)
        layout.setStretch(1, 3)

        flag = QtWidgets.QPushButton()
        flag.setStyleSheet('background-color: transparent')
        flag.setFlat(True)
        if "end" == status:
            flag.setText('')
            if ip and ms:
                flag.setIcon(qta.icon('fa5.check-circle', color='green'))
                ms = "{:.3f}s".format(ms/1000)
            else:
                flag.setIcon(qta.icon('fa5.times-circle', color='red'))
                ms = ""
        elif "begin" == status:
            flag.setText('')
            flag.setIcon(qta.icon('fa5s.sync', color='gray', animation=qta.Spin(self)))
            ip = ""
            ms = ""
        else:
            flag.setText('')
            ip = ""
            ms = ""
        layout.addWidget(flag)
        layout.setStretch(2, 1)

        ipLabel = QtWidgets.QLabel()
        # ipLabel.setStyleSheet('background-color:green')
        ipLabel.setText(ip)
        layout.addWidget(ipLabel)
        layout.setStretch(3, 2)

        timer = QtWidgets.QLabel()
        # timer.setStyleSheet('background-color:blue')
        timer.setText(ms)
        layout.addWidget(timer)
        layout.setStretch(4, 1)

        widget.setLayout(layout)
        return widget

    def showEvent(self, event: QtGui.QShowEvent) -> None:

        if not self.updating and self.domains:
            self.updating = True

            self.ui.listWidget.clear()
            if hasattr(self.parent(), "resetParsedDomains"):
                self.parent().resetParsedDomains()
            itemSize = QtCore.QSize(self.ui.listWidget.width() - self.ui.listWidget.autoScrollMargin() * 2, 50)
            no = 0
            for domain in self.domains:
                item = QtWidgets.QListWidgetItem()
                item.setSizeHint(itemSize)
                item.setData(QtWidgets.QListWidgetItem.UserType, domain)
                widget = self.makeDomainItemWidget(no, domain)
                self.ui.listWidget.addItem(item)
                self.ui.listWidget.setItemWidget(item, widget)
                no += 1

            self.worker = WorkerThread(self.domains)
            self.worker.signal.connect(self.process)
            self.worker.start()
