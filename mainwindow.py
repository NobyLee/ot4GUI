# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
        MainWindow.resize(880, 455)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 11, 851, 321))
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.lcdNumber = QLCDNumber(self.widget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMinimumSize(QSize(494, 50))
        self.lcdNumber.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_5.addWidget(self.lcdNumber)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(6777197, 16777215))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(12, 12))
        self.label_4.setStyleSheet(u"background-color: red;")

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(12, 12))
        self.label_6.setStyleSheet(u"background-color: red;\n"
"")

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(12, 12))
        self.label_8.setStyleSheet(u"background-color: red;")

        self.verticalLayout_5.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(12, 12))
        self.label_10.setStyleSheet(u"background-color: red;")

        self.verticalLayout_6.addWidget(self.label_10)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_6.addWidget(self.label_11)


        self.horizontalLayout.addLayout(self.verticalLayout_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.label)

        self.filenameEdit = QLineEdit(self.widget)
        self.filenameEdit.setObjectName(u"filenameEdit")

        self.verticalLayout.addWidget(self.filenameEdit)

        self.applyButton = QPushButton(self.widget)
        self.applyButton.setObjectName(u"applyButton")

        self.verticalLayout.addWidget(self.applyButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_9.addWidget(self.label_13)

        self.displayModuleEdit = QLineEdit(self.widget)
        self.displayModuleEdit.setObjectName(u"displayModuleEdit")

        self.verticalLayout_9.addWidget(self.displayModuleEdit)

        self.displayButton = QPushButton(self.widget)
        self.displayButton.setObjectName(u"displayButton")

        self.verticalLayout_9.addWidget(self.displayButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_2.addWidget(self.label_12)

        self.portEdit = QLineEdit(self.widget)
        self.portEdit.setObjectName(u"portEdit")

        self.verticalLayout_2.addWidget(self.portEdit)

        self.setButton = QPushButton(self.widget)
        self.setButton.setObjectName(u"setButton")

        self.verticalLayout_2.addWidget(self.setButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.startButton = QPushButton(self.widget)
        self.startButton.setObjectName(u"startButton")

        self.verticalLayout_7.addWidget(self.startButton)

        self.endButton = QPushButton(self.widget)
        self.endButton.setObjectName(u"endButton")

        self.verticalLayout_7.addWidget(self.endButton)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 880, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Seconds", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Module Connection", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"M1", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"M2", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"M3", None))
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"M4", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"File Name", None))
        self.applyButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"EMG Module", None))
        self.displayButton.setText(QCoreApplication.translate("MainWindow", u"Display", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"IMU Port", None))
        self.setButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.endButton.setText(QCoreApplication.translate("MainWindow", u"End", None))
    # retranslateUi

