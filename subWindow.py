# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'subWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        font = QFont()
        font.setFamily(u"Adobe Heiti Std")
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Adobe Heiti Std")
        font1.setPointSize(12)
        self.label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(238, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.plusButton = QPushButton(self.centralwidget)
        self.plusButton.setObjectName(u"plusButton")
        self.plusButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.plusButton)

        self.minusButton = QPushButton(self.centralwidget)
        self.minusButton.setObjectName(u"minusButton")
        self.minusButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.minusButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.EMGLayout = QHBoxLayout()
        self.EMGLayout.setObjectName(u"EMGLayout")

        self.verticalLayout.addLayout(self.EMGLayout)

        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"EMG", None))
        self.plusButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.minusButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
    # retranslateUi

