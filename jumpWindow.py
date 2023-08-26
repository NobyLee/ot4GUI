# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jumpWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(758, 602)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.EMGlabel = QLabel(Dialog)
        self.EMGlabel.setObjectName(u"EMGlabel")
        font = QFont()
        font.setFamily(u"Adobe Heiti Std")
        font.setPointSize(12)
        self.EMGlabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.EMGlabel)

        self.horizontalSpacer = QSpacerItem(238, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.plusButton = QPushButton(Dialog)
        self.plusButton.setObjectName(u"plusButton")
        self.plusButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.plusButton)

        self.minusButton = QPushButton(Dialog)
        self.minusButton.setObjectName(u"minusButton")
        self.minusButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.minusButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.EMGLayout = QHBoxLayout()
        self.EMGLayout.setObjectName(u"EMGLayout")

        self.verticalLayout.addLayout(self.EMGLayout)

        self.verticalLayout.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.AUXlabel = QLabel(Dialog)
        self.AUXlabel.setObjectName(u"AUXlabel")
        self.AUXlabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.AUXlabel)

        self.horizontalSpacer_2 = QSpacerItem(238, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.plusAUXButton = QPushButton(Dialog)
        self.plusAUXButton.setObjectName(u"plusAUXButton")
        self.plusAUXButton.setFont(font)

        self.horizontalLayout_3.addWidget(self.plusAUXButton)

        self.minusAUXButton = QPushButton(Dialog)
        self.minusAUXButton.setObjectName(u"minusAUXButton")
        self.minusAUXButton.setFont(font)

        self.horizontalLayout_3.addWidget(self.minusAUXButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.AUXLayout = QHBoxLayout()
        self.AUXLayout.setObjectName(u"AUXLayout")

        self.verticalLayout_2.addLayout(self.AUXLayout)

        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3.setStretch(0, 64)
        self.verticalLayout_3.setStretch(1, 10)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.EMGlabel.setText(QCoreApplication.translate("Dialog", u"EMG module Signal", None))
        self.plusButton.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.minusButton.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.AUXlabel.setText(QCoreApplication.translate("Dialog", u"AUX Signal", None))
        self.plusAUXButton.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.minusAUXButton.setText(QCoreApplication.translate("Dialog", u"-", None))
    # retranslateUi

