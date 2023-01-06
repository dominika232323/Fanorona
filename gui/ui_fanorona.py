# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fanorona.ui'
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
        MainWindow.resize(1100, 868)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stack = QStackedWidget(self.centralwidget)
        self.stack.setObjectName(u"stack")
        self.stack.setGeometry(QRect(0, 0, 561, 451))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stack.sizePolicy().hasHeightForWidth())
        self.stack.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelWidth = QLabel(self.page)
        self.labelWidth.setObjectName(u"labelWidth")
        font = QFont()
        font.setPointSize(11)
        self.labelWidth.setFont(font)
        self.labelWidth.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelWidth)

        self.boardWidth = QSpinBox(self.page)
        self.boardWidth.setObjectName(u"boardWidth")
        self.boardWidth.setMinimum(3)
        self.boardWidth.setMaximum(15)
        self.boardWidth.setSingleStep(2)

        self.verticalLayout_2.addWidget(self.boardWidth)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 8, 0, 1, 2)

        self.labelFirstColor = QLabel(self.page)
        self.labelFirstColor.setObjectName(u"labelFirstColor")
        self.labelFirstColor.setFont(font)
        self.labelFirstColor.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelFirstColor, 5, 0, 1, 2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelOpponent = QLabel(self.page)
        self.labelOpponent.setObjectName(u"labelOpponent")
        self.labelOpponent.setFont(font)
        self.labelOpponent.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.labelOpponent)

        self.labelOppontnPlayer = QLabel(self.page)
        self.labelOppontnPlayer.setObjectName(u"labelOppontnPlayer")
        self.labelOppontnPlayer.setFont(font)
        self.labelOppontnPlayer.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.labelOppontnPlayer)

        self.labelOppontnComputerRandom = QLabel(self.page)
        self.labelOppontnComputerRandom.setObjectName(u"labelOppontnComputerRandom")
        self.labelOppontnComputerRandom.setFont(font)
        self.labelOppontnComputerRandom.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.labelOppontnComputerRandom)

        self.labelOppontnComputerBest = QLabel(self.page)
        self.labelOppontnComputerBest.setObjectName(u"labelOppontnComputerBest")
        self.labelOppontnComputerBest.setFont(font)
        self.labelOppontnComputerBest.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.labelOppontnComputerBest)

        self.ChooseOpponent = QSpinBox(self.page)
        self.ChooseOpponent.setObjectName(u"ChooseOpponent")
        self.ChooseOpponent.setMinimum(1)
        self.ChooseOpponent.setMaximum(3)

        self.verticalLayout_3.addWidget(self.ChooseOpponent)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 2)

        self.labelChooseColor = QLabel(self.page)
        self.labelChooseColor.setObjectName(u"labelChooseColor")
        self.labelChooseColor.setFont(font)
        self.labelChooseColor.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelChooseColor, 4, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelLength = QLabel(self.page)
        self.labelLength.setObjectName(u"labelLength")
        self.labelLength.setFont(font)
        self.labelLength.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelLength)

        self.boardLength = QSpinBox(self.page)
        self.boardLength.setObjectName(u"boardLength")
        self.boardLength.setInputMethodHints(Qt.ImhDigitsOnly)
        self.boardLength.setKeyboardTracking(True)
        self.boardLength.setMinimum(3)
        self.boardLength.setMaximum(15)
        self.boardLength.setSingleStep(2)

        self.verticalLayout.addWidget(self.boardLength)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.playButton = QPushButton(self.page)
        self.playButton.setObjectName(u"playButton")
        font1 = QFont()
        font1.setPointSize(12)
        self.playButton.setFont(font1)

        self.gridLayout.addWidget(self.playButton, 9, 0, 1, 2)

        self.spinBoxChooseColor = QSpinBox(self.page)
        self.spinBoxChooseColor.setObjectName(u"spinBoxChooseColor")
        self.spinBoxChooseColor.setMinimum(1)
        self.spinBoxChooseColor.setMaximum(2)

        self.gridLayout.addWidget(self.spinBoxChooseColor, 7, 0, 1, 2)

        self.labelSecondColor = QLabel(self.page)
        self.labelSecondColor.setObjectName(u"labelSecondColor")
        self.labelSecondColor.setFont(font)
        self.labelSecondColor.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelSecondColor, 6, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 0, 1, 2)

        self.stack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stack.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1100, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fanorona", None))
        self.labelWidth.setText(QCoreApplication.translate("MainWindow", u"Chose number of rows", None))
        self.labelFirstColor.setText(QCoreApplication.translate("MainWindow", u"1 - Pawns with the first move color", None))
        self.labelOpponent.setText(QCoreApplication.translate("MainWindow", u"Choose your opponent", None))
        self.labelOppontnPlayer.setText(QCoreApplication.translate("MainWindow", u"1 - Play against another player", None))
        self.labelOppontnComputerRandom.setText(QCoreApplication.translate("MainWindow", u"2 - Play against computer with random choice", None))
        self.labelOppontnComputerBest.setText(QCoreApplication.translate("MainWindow", u"3 - Play against computer with the best choice", None))
        self.labelChooseColor.setText(QCoreApplication.translate("MainWindow", u"Choose the color of your pawns", None))
        self.labelLength.setText(QCoreApplication.translate("MainWindow", u"Chose number of columns", None))
        self.boardLength.setSpecialValueText("")
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.labelSecondColor.setText(QCoreApplication.translate("MainWindow", u"2 - Pawns with the second move color", None))
    # retranslateUi

