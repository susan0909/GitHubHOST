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
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(DialogDonate)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
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
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.labelWechat = QtWidgets.QLabel(DialogDonate)
        self.labelWechat.setMaximumSize(QtCore.QSize(220, 220))
        self.labelWechat.setText("")
        self.labelWechat.setPixmap(QtGui.QPixmap("Resources/susan-wechat.jpg"))
        self.labelWechat.setScaledContents(True)
        self.labelWechat.setObjectName("labelWechat")
        self.verticalLayout_3.addWidget(self.labelWechat)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.btnWechat = QtWidgets.QPushButton(DialogDonate)
        self.btnWechat.setMinimumSize(QtCore.QSize(0, 50))
        self.btnWechat.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btnWechat.setStyleSheet("* { border: none; background-color: transparent; }")
        self.btnWechat.setObjectName("btnWechat")
        self.verticalLayout.addWidget(self.btnWechat)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.btnAlipay = QtWidgets.QPushButton(DialogDonate)
        self.btnAlipay.setMinimumSize(QtCore.QSize(0, 50))
        self.btnAlipay.setMaximumSize(QtCore.QSize(16777215, 50))
        self.btnAlipay.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btnAlipay.setStyleSheet("* { border: none; background-color: transparent; }")
        self.btnAlipay.setObjectName("btnAlipay")
        self.verticalLayout.addWidget(self.btnAlipay)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.labelAlipay = QtWidgets.QLabel(DialogDonate)
        self.labelAlipay.setMaximumSize(QtCore.QSize(220, 220))
        self.labelAlipay.setText("")
        self.labelAlipay.setPixmap(QtGui.QPixmap("Resources/susan-alipay.jpg"))
        self.labelAlipay.setScaledContents(True)
        self.labelAlipay.setObjectName("labelAlipay")
        self.verticalLayout_4.addWidget(self.labelAlipay)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.labelInfo = QtWidgets.QLabel(DialogDonate)
        self.labelInfo.setMinimumSize(QtCore.QSize(40, 40))
        self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfo.setObjectName("labelInfo")
        self.horizontalLayout_4.addWidget(self.labelInfo)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line = QtWidgets.QFrame(DialogDonate)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        self.btnClose = QtWidgets.QPushButton(DialogDonate)
        self.btnClose.setStyleSheet("* { border: none; background-color: transparent; }")
        self.btnClose.setText("OK")
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_2.addWidget(self.btnClose)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem16)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)

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