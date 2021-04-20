# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowApp(object):
    def setupUi(self, WindowApp):
        WindowApp.setObjectName("WindowApp")
        WindowApp.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WindowApp.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(WindowApp)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelPath = QtWidgets.QLabel(self.centralwidget)
        self.labelPath.setObjectName("labelPath")
        self.horizontalLayout.addWidget(self.labelPath)
        self.hostPath = QtWidgets.QLineEdit(self.centralwidget)
        self.hostPath.setStyleSheet("*{border:none;background-color:transparent;}")
        self.hostPath.setReadOnly(True)
        self.hostPath.setObjectName("hostPath")
        self.horizontalLayout.addWidget(self.hostPath)
        self.btnOpen = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout.addWidget(self.btnOpen)
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setObjectName("btnUpdate")
        self.horizontalLayout.addWidget(self.btnUpdate)
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnDonate = QtWidgets.QPushButton(self.centralwidget)
        self.btnDonate.setObjectName("btnDonate")
        self.horizontalLayout.addWidget(self.btnDonate)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.labelPreview = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelPreview.setFont(font)
        self.labelPreview.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPreview.setObjectName("labelPreview")
        self.horizontalLayout_2.addWidget(self.labelPreview)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textHost = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textHost.setObjectName("textHost")
        self.verticalLayout.addWidget(self.textHost)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.setStretch(1, 1)
        WindowApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        WindowApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowApp)
        self.statusbar.setObjectName("statusbar")
        WindowApp.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(WindowApp)
        self.actionExit.setShortcut("Ctrl+X")
        self.actionExit.setObjectName("actionExit")
        self.actionOnlineManual = QtWidgets.QAction(WindowApp)
        self.actionOnlineManual.setShortcut("Ctrl+M")
        self.actionOnlineManual.setObjectName("actionOnlineManual")
        self.actionReportIssue = QtWidgets.QAction(WindowApp)
        self.actionReportIssue.setShortcut("Ctrl+B")
        self.actionReportIssue.setObjectName("actionReportIssue")
        self.actionAbout = QtWidgets.QAction(WindowApp)
        self.actionAbout.setShortcut("Ctrl+I")
        self.actionAbout.setObjectName("actionAbout")
        self.actionDonate = QtWidgets.QAction(WindowApp)
        self.actionDonate.setShortcut("Ctrl+D")
        self.actionDonate.setObjectName("actionDonate")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionOnlineManual)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDonate)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionReportIssue)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(WindowApp)
        QtCore.QMetaObject.connectSlotsByName(WindowApp)

    def retranslateUi(self, WindowApp):
        _translate = QtCore.QCoreApplication.translate
        WindowApp.setWindowTitle(_translate("WindowApp", "GitHub HOST"))
        self.labelPath.setText(_translate("WindowApp", "HOST Path"))
        self.btnOpen.setText(_translate("WindowApp", "Local HOST"))
        self.btnUpdate.setText(_translate("WindowApp", "Update"))
        self.btnSave.setText(_translate("WindowApp", "Save"))
        self.btnDonate.setText(_translate("WindowApp", "Donate"))
        self.labelPreview.setText(_translate("WindowApp", "Preview"))
        self.menuFile.setTitle(_translate("WindowApp", "File(&F)"))
        self.menuHelp.setTitle(_translate("WindowApp", "Help(&H)"))
        self.actionExit.setText(_translate("WindowApp", "Quit(&X)"))
        self.actionExit.setToolTip(_translate("WindowApp", "Quit Application"))
        self.actionOnlineManual.setText(_translate("WindowApp", "Manual(&?)"))
        self.actionOnlineManual.setToolTip(_translate("WindowApp", "Online manual(?)"))
        self.actionReportIssue.setText(_translate("WindowApp", "Issues(&B)"))
        self.actionReportIssue.setToolTip(_translate("WindowApp", "Report issue(B)"))
        self.actionAbout.setText(_translate("WindowApp", "About(&I)"))
        self.actionAbout.setToolTip(_translate("WindowApp", "About(I)"))
        self.actionDonate.setText(_translate("WindowApp", "Donate(&D)"))
        self.actionDonate.setToolTip(_translate("WindowApp", "Buy Me a Beer(D)"))
import res_rc
