# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_donate.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogDonate(object):
    def setupUi(self, DialogDonate):
        DialogDonate.setObjectName("DialogDonate")
        DialogDonate.resize(600, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.label.setPixmap(QtGui.QPixmap(":/icon/donate.png"))
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
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelWechat = QtWidgets.QLabel(DialogDonate)
        self.labelWechat.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWechat.setObjectName("labelWechat")
        self.verticalLayout_6.addWidget(self.labelWechat)
        self.btnIconWechat = QtWidgets.QPushButton(DialogDonate)
        self.btnIconWechat.setText("")
        self.btnIconWechat.setAutoDefault(False)
        self.btnIconWechat.setFlat(True)
        self.btnIconWechat.setObjectName("btnIconWechat")
        self.verticalLayout_6.addWidget(self.btnIconWechat)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelAlipay = QtWidgets.QLabel(DialogDonate)
        self.labelAlipay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAlipay.setObjectName("labelAlipay")
        self.verticalLayout_7.addWidget(self.labelAlipay)
        self.btnIconAlipay = QtWidgets.QPushButton(DialogDonate)
        self.btnIconAlipay.setText("")
        self.btnIconAlipay.setAutoDefault(False)
        self.btnIconAlipay.setFlat(True)
        self.btnIconAlipay.setObjectName("btnIconAlipay")
        self.verticalLayout_7.addWidget(self.btnIconAlipay)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.labelInfo = QtWidgets.QLabel(DialogDonate)
        self.labelInfo.setMinimumSize(QtCore.QSize(40, 40))
        self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfo.setObjectName("labelInfo")
        self.horizontalLayout_4.addWidget(self.labelInfo)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
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
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.btnClose = QtWidgets.QPushButton(DialogDonate)
        self.btnClose.setStyleSheet("* { border: none; background-color: transparent; }")
        self.btnClose.setText("OK")
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_2.addWidget(self.btnClose)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.retranslateUi(DialogDonate)
        self.btnClose.clicked.connect(DialogDonate.close)
        QtCore.QMetaObject.connectSlotsByName(DialogDonate)

    def retranslateUi(self, DialogDonate):
        _translate = QtCore.QCoreApplication.translate
        DialogDonate.setWindowTitle(_translate("DialogDonate", "GitHub HOST - Donate"))
        self.labelDonate.setText(_translate("DialogDonate", "Buy me a beer"))
        self.labelWechat.setText(_translate("DialogDonate", "WeChat"))
        self.labelAlipay.setText(_translate("DialogDonate", "AliPay"))
        self.labelInfo.setText(_translate("DialogDonate", "Buy me a beer if it is helpful to you!"))
import res_rc
