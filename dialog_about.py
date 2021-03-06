# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_about.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogAbout(object):
    def setupUi(self, DialogAbout):
        DialogAbout.setObjectName("DialogAbout")
        DialogAbout.resize(424, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogAbout.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogAbout)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnLogo = QtWidgets.QPushButton(DialogAbout)
        self.btnLogo.setText("")
        self.btnLogo.setAutoDefault(False)
        self.btnLogo.setFlat(True)
        self.btnLogo.setObjectName("btnLogo")
        self.horizontalLayout.addWidget(self.btnLogo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.labelVersion = QtWidgets.QLabel(DialogAbout)
        self.labelVersion.setMinimumSize(QtCore.QSize(400, 40))
        self.labelVersion.setMaximumSize(QtCore.QSize(400, 40))
        self.labelVersion.setText("")
        self.labelVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVersion.setObjectName("labelVersion")
        self.verticalLayout.addWidget(self.labelVersion)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.labelMailIcon = QtWidgets.QLabel(DialogAbout)
        self.labelMailIcon.setMinimumSize(QtCore.QSize(20, 20))
        self.labelMailIcon.setMaximumSize(QtCore.QSize(20, 20))
        self.labelMailIcon.setText("")
        self.labelMailIcon.setPixmap(QtGui.QPixmap(":/icon/mail.png"))
        self.labelMailIcon.setScaledContents(True)
        self.labelMailIcon.setObjectName("labelMailIcon")
        self.horizontalLayout_2.addWidget(self.labelMailIcon)
        self.labelMailAddress = QtWidgets.QLabel(DialogAbout)
        self.labelMailAddress.setMaximumSize(QtCore.QSize(16777215, 24))
        self.labelMailAddress.setText("")
        self.labelMailAddress.setScaledContents(False)
        self.labelMailAddress.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMailAddress.setOpenExternalLinks(True)
        self.labelMailAddress.setObjectName("labelMailAddress")
        self.horizontalLayout_2.addWidget(self.labelMailAddress)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.labelHomeIcon = QtWidgets.QLabel(DialogAbout)
        self.labelHomeIcon.setMinimumSize(QtCore.QSize(20, 20))
        self.labelHomeIcon.setMaximumSize(QtCore.QSize(20, 20))
        self.labelHomeIcon.setText("")
        self.labelHomeIcon.setPixmap(QtGui.QPixmap(":/icon/www.png"))
        self.labelHomeIcon.setScaledContents(True)
        self.labelHomeIcon.setObjectName("labelHomeIcon")
        self.horizontalLayout_3.addWidget(self.labelHomeIcon)
        self.labelHomeUrl = QtWidgets.QLabel(DialogAbout)
        self.labelHomeUrl.setMaximumSize(QtCore.QSize(16777215, 32))
        self.labelHomeUrl.setText("")
        self.labelHomeUrl.setOpenExternalLinks(True)
        self.labelHomeUrl.setObjectName("labelHomeUrl")
        self.horizontalLayout_3.addWidget(self.labelHomeUrl)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.labelIssueIcon = QtWidgets.QLabel(DialogAbout)
        self.labelIssueIcon.setMinimumSize(QtCore.QSize(20, 20))
        self.labelIssueIcon.setMaximumSize(QtCore.QSize(20, 20))
        self.labelIssueIcon.setText("")
        self.labelIssueIcon.setPixmap(QtGui.QPixmap(":/icon/bug.png"))
        self.labelIssueIcon.setScaledContents(True)
        self.labelIssueIcon.setObjectName("labelIssueIcon")
        self.horizontalLayout_4.addWidget(self.labelIssueIcon)
        self.labelIssueUrl = QtWidgets.QLabel(DialogAbout)
        self.labelIssueUrl.setMaximumSize(QtCore.QSize(16777215, 32))
        self.labelIssueUrl.setText("")
        self.labelIssueUrl.setOpenExternalLinks(True)
        self.labelIssueUrl.setObjectName("labelIssueUrl")
        self.horizontalLayout_4.addWidget(self.labelIssueUrl)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(DialogAbout)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.btnClose = QtWidgets.QPushButton(DialogAbout)
        self.btnClose.setMaximumSize(QtCore.QSize(200, 30))
        self.btnClose.setStyleSheet("* {border: 0;}")
        self.btnClose.setText("  OK")
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_5.addWidget(self.btnClose)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(DialogAbout)
        self.btnClose.clicked.connect(DialogAbout.close)
        QtCore.QMetaObject.connectSlotsByName(DialogAbout)

    def retranslateUi(self, DialogAbout):
        _translate = QtCore.QCoreApplication.translate
        DialogAbout.setWindowTitle(_translate("DialogAbout", "GitHub HOST - About"))
import res_rc
