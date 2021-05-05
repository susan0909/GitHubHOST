#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import webbrowser
import qtawesome as qta
from datetime import datetime

import window_app

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QMainWindow, QStyle, QFileDialog, QMessageBox

from config import Config
from advance import AdvanceDialog
from about import DialogAbout
from donate import DialogDonate
from updater import DialogUpdater


class AppWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)

        self.ui = window_app.Ui_WindowApp()
        self.ui.setupUi(self)

        self.host = []
        self.hostPath = None
        self.hostWritable = False
        self.domains = {}
        self.config = Config()
        self.initStatusBar()
        self.bindMenuActions()
        self.bindTools()
        self.initWindow()

    def resetParsedDomains(self):
        self.domains = {}

    def addParsedDomain(self, domain, ip):
        self.domains[domain] = ip

    def initStatusBar(self):
        """Init window status bar"""

        lang = QtCore.QLocale().system().uiLanguages()
        if len(lang):
            labelLang = QtWidgets.QLabel()
            labelLang.setText(lang[0])
            self.ui.statusbar.addPermanentWidget(labelLang)

        statusVersion = QtWidgets.QLabel()
        _translate = QtCore.QCoreApplication.translate

        version = "{}: {}".format(_translate("WindowApp", "Version"), self.config.get("version", "0.0"))
        statusVersion.setText(version)
        self.ui.statusbar.addPermanentWidget(statusVersion)

    def bindTools(self):
        """Bind tools button"""

        self.ui.btnOpen.setIcon(self.style().standardIcon(QStyle.SP_DialogOpenButton))
        self.ui.btnOpen.clicked.connect(self.clickHostOpen)

        self.ui.btnUpdate.clicked.connect(self.clickHostUpdate)
        self.ui.btnUpdate.setIcon(self.style().standardIcon(QStyle.SP_BrowserReload))

        self.ui.btnSave.clicked.connect(self.clickHostSave)
        self.ui.btnSave.setIcon(self.style().standardIcon(QStyle.SP_DialogSaveButton))
        self.ui.btnSave.setEnabled(False)

        self.ui.btnAdvance.setIcon(qta.icon('fa5s.cog'))
        self.ui.btnAdvance.clicked.connect(self.openAdvanceDialog)

        self.ui.btnDonate.clicked.connect(self.menuActionDonate)
        # self.ui.btnDonate.setIcon(self.style().standardIcon(QStyle.SP_DialogHelpButton))
        self.ui.btnDonate.setIcon(qta.icon('fa5s.donate'))

    def initWindow(self):
        """Init the window"""

        self.previewHostContent(os.path.join(self.config.hostDirectory(), 'hosts'))

    def bindMenuActions(self):
        """Menu click actions register"""

        self.ui.actionExit.setIcon(self.style().standardIcon(QStyle.SP_MessageBoxCritical))
        self.ui.actionExit.triggered.connect(self.menuActionExit)

        self.ui.actionAbout.setIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        self.ui.actionAbout.triggered.connect(self.menuActionAbout)

        self.ui.actionOnlineManual.setIcon(self.style().standardIcon(QStyle.SP_TitleBarContextHelpButton))
        self.ui.actionOnlineManual.triggered.connect(self.menuActionManual)

        self.ui.actionDonate.setIcon(qta.icon('fa5s.donate'))
        self.ui.actionDonate.triggered.connect(self.menuActionDonate)

        self.ui.actionReportIssue.setIcon(self.style().standardIcon(QStyle.SP_MessageBoxWarning))
        self.ui.actionReportIssue.triggered.connect(self.menuActionIssue)

    def menuActionExit(self):
        """Exit application"""

        self.close()

    def menuActionAbout(self):
        """Click menu about"""

        dialog = DialogAbout(self)
        dialog.display()

    def menuActionManual(self):
        """Click menu manual"""

        url = self.config.get("manual")
        webbrowser.open(url)

    def menuActionDonate(self):
        """Donate me"""

        dialog = DialogDonate(self)
        dialog.display()

    def menuActionIssue(self):
        """Click menu issue"""

        url = self.config.get("issue")
        webbrowser.open(url)

    def openAdvanceDialog(self):
        dialog = AdvanceDialog(self)
        dialog.exec()

    def previewHostContent(self, host):
        """Get the host content"""

        if host and os.path.exists(host):
            self.hostPath = host
            self.ui.hostPath.setText(host)
            palette = self.ui.hostPath.palette()
            if os.access(host, os.W_OK):
                self.hostWritable = True
                palette.setColor(QPalette.Text, QtCore.Qt.darkGreen)
            else:
                self.hostWritable = False
                palette.setColor(QPalette.Text, QtCore.Qt.red)
            self.ui.hostPath.setPalette(palette)

            try:
                self.host = []
                with open(host, mode="r", encoding="utf-8") as f:
                    for line in f.readlines():
                        self.host.append(line.strip())
                    f.close()

                self.ui.textHost.setPlainText(f"{os.linesep}".join(self.host))
                return True
            except Exception as e:
                print(f"Read host error:{e}")
                return False
        else:
            return False

    def clickHostOpen(self):
        """Select host file dialog"""

        _translate = QtCore.QCoreApplication.translate
        host, _ = QFileDialog.getOpenFileName(
            self,
            _translate("WindowApp", "Select the HOST"),
            self.config.hostDirectory(),
            ""
        )
        if host and not self.previewHostContent(host):

            QMessageBox.critical(
                self,
                _translate("WindowApp", "Host read error"),
                _translate("WindowApp", "Read host content failed!"),
                QMessageBox.Ok)

    def clickHostUpdate(self):
        """Start update host dns"""

        dialog = DialogUpdater(self)
        # dialog.setWindowFlag(QtCore.Qt.CustomizeWindowHint)
        # dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint)
        # dialog.setWindowFlags(QtCore.Qt.WindowTitleHint)
        dialog.exec()

        self.rebuildHostData()

    def clickHostSave(self):
        """Save the updated host"""

        if not self.hostPath:
            return

        # os.access 不能正确检测 HOST 文件的可写性
        # print(f"Host:{self.hostPath} permission:{os.access(self.hostPath, os.W_OK)}")
        _translate = QtCore.QCoreApplication.translate
        content = self.ui.textHost.toPlainText()
        try:
            with open(self.hostPath, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            print(f"Update host error:{e}")
            QMessageBox.warning(
                self,
                _translate("WindowApp", "Warning"),
                _translate("WindowApp",
                           "Can not rewrite the host content,\nPlease copy the content replace the host file manually."),
                QMessageBox.Ok)
            return

        QMessageBox.information(
            self,
            _translate("WindowApp", "Success"),
            _translate("WindowApp",
                       "Congratulations!\nThe latest GitHub HOST information was updated in your host."),
            QMessageBox.Ok)

    def rebuildHostData(self):
        """Rebuild host content"""

        rows = []
        spaces = []
        for line in self.host:
            if not line:
                spaces.append(line)
                if len(spaces) < 2:
                    rows.append(line)
                continue
            else:
                spaces = []

            if line.startswith("#"):
                if not line.strip().startswith("# Github host"):
                    rows.append(line)
                continue

            words = set(re.split(r"\s+", line))
            for key in self.domains.keys():
                if key in words:
                    words.remove(key)

            list_words = list(words)
            if len(list_words) > 1:
                new_words = []
                for word in list_words:
                    if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", word):
                        new_words.append(word)
                        list_words.remove(word)
                        break
                new_words.extend(list_words)
                rows.append(" ".join(new_words))
            elif len(list_words) == 1:
                if not re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", list_words[0]):
                    rows.append(list_words[0])

        rows.append("")
        start = "# Github host dns updated at: {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        rows.append(start)

        for domain in self.domains.keys():
            if self.domains[domain]:
                rows.append("{} {}".format(self.domains[domain], domain))

        rows.append("")
        self.ui.textHost.setPlainText(f"{os.linesep}".join(rows))
        self.ui.btnSave.setEnabled(True)
