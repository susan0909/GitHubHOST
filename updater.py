#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dialog_updater

import qtawesome as qta

from PyQt5 import QtGui, QtWidgets, QtCore
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

        self.ui.listWidget.setStyleSheet("QListWidget { outline:0; background-color: transparent; }"
                                         "QListWidget::item {border-bottom: 1px solid #999;}"
                                         "QListWidget::item::selected { color: #fff; }")

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

        self.spinBtn = QtWidgets.QPushButton()
        self.spinBtn.setFlat(True)
        self.spinBtn.setIcon(qta.icon('fa5s.spinner', color='red', animation=qta.Spin(self.spinBtn)))

    def process(self, data):
        print(data)
        action, host, ip, secs, last = data

        if self.ui.listWidget.count() > 0:
            for index in range(self.ui.listWidget.count()):
                item = self.ui.listWidget.item(index)
                data = item.data(QtWidgets.QListWidgetItem.UserType)
                if data and data == host:
                    widget = self.ui.listWidget.itemWidget(item)
                    statusWidget = widget.layout().itemAt(2)
                    if "begin" == action:
                        print(f'update begin {data}')
                        if isinstance(statusWidget, QtWidgets.QPushButton):
                            statusWidget.setText('...')
                    else:
                        print(f"update end {data}")
                        if isinstance(statusWidget, QtWidgets.QPushButton):
                            statusWidget.setText('')
                            if secs > 9999:
                                statusWidget.setIcon(qta.icon('fa5.times-circle', color='red'))
                            else:
                                statusWidget.setIcon(qta.icon('fa5.check-circle', color='green'))
                        ipWidget = widget.layout().itemAt(3)
                        if isinstance(ipWidget, QtWidgets.QLabel):
                            ipWidget.setText(ip)
                        timerWidget = widget.layout().itemAt(4)
                        if isinstance(timerWidget, QtWidgets.QLabel):
                            timerWidget.setText(str(secs))
                    print(f"Upload item {data}")
                self.ui.listWidget.repaint()

        if last:
            self.updating = False
            print("Finished!")

    def makeDomainItem(self, num, domain):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        no = QtWidgets.QLabel()
        # no.setStyleSheet('background-color:blue')
        no.setText(f"#{num}")
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
        flag.setText('')
        layout.addWidget(flag)
        # spin_widget = qta.IconWidget()
        # spin_icon = qta.icon('fa5s.spinner', color='red', animation=qta.Spin(spin_widget))
        # spin_widget.setIcon(spin_icon)
        # layout.addWidget(spin_widget)
        layout.setStretch(2, 1)

        ip = QtWidgets.QLabel()
        # ip.setStyleSheet('background-color:green')
        ip.setText('')
        layout.addWidget(ip)
        layout.setStretch(3, 2)

        timer = QtWidgets.QLabel()
        # timer.setStyleSheet('background-color:blue')
        timer.setText('')
        layout.addWidget(timer)
        layout.setStretch(4, 1)

        widget.setLayout(layout)
        return widget

    def showEvent(self, event: QtGui.QShowEvent) -> None:

        if not self.updating and self.domains:
            self.updating = True

            self.ui.listWidget.clear()
            itemSize = QtCore.QSize(self.ui.listWidget.width() - self.ui.listWidget.autoScrollMargin(), 50)
            no = 0
            for domain in self.domains:
                no += 1
                item = QtWidgets.QListWidgetItem()
                item.setSizeHint(itemSize)
                item.setData(QtWidgets.QListWidgetItem.UserType, domain)
                widget = self.makeDomainItem(no, domain)
                self.ui.listWidget.addItem(item)
                self.ui.listWidget.setItemWidget(item, widget)

            self.worker = WorkerThread(self.domains)
            self.worker.signal.connect(self.process)
            self.worker.start()
