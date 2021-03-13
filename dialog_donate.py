# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_donate.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogDonate(object):
    def setupUi(self, DialogDonate):
        DialogDonate.setObjectName("DialogDonate")
        DialogDonate.resize(600, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogDonate.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DialogDonate)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(DialogDonate)
        self.label.setMaximumSize(QtCore.QSize(32, 32))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Resources/icons/donate.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.labelDonate = QtWidgets.QLabel(DialogDonate)
        self.labelDonate.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelDonate.setFont(font)
        self.labelDonate.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDonate.setObjectName("labelDonate")
        self.horizontalLayout_3.addWidget(self.labelDonate)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelWechat = QtWidgets.QLabel(DialogDonate)
        self.labelWechat.setMinimumSize(QtCore.QSize(100, 100))
        self.labelWechat.setText("")
        self.labelWechat.setPixmap(QtGui.QPixmap("Resources/logo256.png"))
        self.labelWechat.setScaledContents(True)
        self.labelWechat.setObjectName("labelWechat")
        self.horizontalLayout.addWidget(self.labelWechat)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnWechat = QtWidgets.QPushButton(DialogDonate)
        self.btnWechat.setStyleSheet("* { border: none; background-color: transparent; }")
        self.btnWechat.setObjectName("btnWechat")
        self.verticalLayout.addWidget(self.btnWechat)
        self.btnAlipay = QtWidgets.QPushButton(DialogDonate)
        self.btnAlipay.setStyleSheet("* { border: none; background-color: transparent; }")
        self.btnAlipay.setObjectName("btnAlipay")
        self.verticalLayout.addWidget(self.btnAlipay)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.labelAlipay = QtWidgets.QLabel(DialogDonate)
        self.labelAlipay.setMinimumSize(QtCore.QSize(100, 100))
        self.labelAlipay.setText("")
        self.labelAlipay.setPixmap(QtGui.QPixmap("Resources/logo256.png"))
        self.labelAlipay.setScaledContents(True)
        self.labelAlipay.setObjectName("labelAlipay")
        self.horizontalLayout.addWidget(self.labelAlipay)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.labelInfo = QtWidgets.QLabel(DialogDonate)
        self.labelInfo.setMinimumSize(QtCore.QSize(40, 40))
        self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfo.setObjectName("labelInfo")
        self.verticalLayout_2.addWidget(self.labelInfo)
        self.line = QtWidgets.QFrame(DialogDonate)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btnClose = QtWidgets.QPushButton(DialogDonate)
        self.btnClose.setStyleSheet("* { border: none; background-color: transparent; }")
        self.btnClose.setText("OK")
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_2.addWidget(self.btnClose)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(DialogDonate)
        self.btnClose.clicked.connect(DialogDonate.close)
        QtCore.QMetaObject.connectSlotsByName(DialogDonate)

    def retranslateUi(self, DialogDonate):
        _translate = QtCore.QCoreApplication.translate
        DialogDonate.setWindowTitle(_translate("DialogDonate", "GitHub HOST - Donate"))
        self.labelDonate.setText(_translate("DialogDonate", "请我喝一杯"))
        self.btnWechat.setText(_translate("DialogDonate", "微信"))
        self.btnAlipay.setText(_translate("DialogDonate", "支付宝"))
        self.labelInfo.setText(_translate("DialogDonate", "如果此开源软件对您有帮助, 欢迎打赏支持我!"))
