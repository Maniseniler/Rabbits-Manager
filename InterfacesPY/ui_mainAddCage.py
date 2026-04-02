# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainAddCage.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDialog,
    QDoubleSpinBox, QFrame, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_AddCage_Main(object):
    def setupUi(self, AddCage_Main):
        if not AddCage_Main.objectName():
            AddCage_Main.setObjectName(u"AddCage_Main")
        AddCage_Main.resize(550, 410)
        AddCage_Main.setMinimumSize(QSize(550, 410))
        AddCage_Main.setMaximumSize(QSize(550, 410))
        AddCage_Main.setStyleSheet(u"")
        self.Background = QFrame(AddCage_Main)
        self.Background.setObjectName(u"Background")
        self.Background.setGeometry(QRect(0, 0, 550, 410))
        self.Background.setMinimumSize(QSize(550, 410))
        self.Background.setMaximumSize(QSize(550, 410))
        self.Background.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"Orbitron\";\n"
"	border-style: outset;\n"
"    	border-radius: 50px;\n"
"}")
        self.Background.setFrameShape(QFrame.StyledPanel)
        self.Background.setFrameShadow(QFrame.Raised)
        self.Infos_Frame = QFrame(self.Background)
        self.Infos_Frame.setObjectName(u"Infos_Frame")
        self.Infos_Frame.setEnabled(True)
        self.Infos_Frame.setGeometry(QRect(25, 25, 500, 361))
        self.Infos_Frame.setMinimumSize(QSize(500, 361))
        self.Infos_Frame.setMaximumSize(QSize(500, 361))
        self.Infos_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Infos_Frame.setFrameShape(QFrame.StyledPanel)
        self.Infos_Frame.setFrameShadow(QFrame.Raised)
        self.ID_Frame = QFrame(self.Infos_Frame)
        self.ID_Frame.setObjectName(u"ID_Frame")
        self.ID_Frame.setEnabled(True)
        self.ID_Frame.setGeometry(QRect(0, 0, 158, 44))
        self.ID_Frame.setMinimumSize(QSize(158, 44))
        self.ID_Frame.setMaximumSize(QSize(158, 44))
        self.ID_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #2F2F2F;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.ID_Frame.setFrameShape(QFrame.StyledPanel)
        self.ID_Frame.setFrameShadow(QFrame.Raised)
        self.ID_Label = QLabel(self.ID_Frame)
        self.ID_Label.setObjectName(u"ID_Label")
        self.ID_Label.setGeometry(QRect(20, 6, 121, 31))
        self.ID_Label.setMinimumSize(QSize(121, 31))
        self.ID_Label.setMaximumSize(QSize(121, 31))
        self.ID_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";\n"
"}")
        self.Cage_Avatar_Frame = QFrame(self.Infos_Frame)
        self.Cage_Avatar_Frame.setObjectName(u"Cage_Avatar_Frame")
        self.Cage_Avatar_Frame.setGeometry(QRect(371, 10, 119, 161))
        self.Cage_Avatar_Frame.setMinimumSize(QSize(119, 161))
        self.Cage_Avatar_Frame.setMaximumSize(QSize(119, 161))
        self.Cage_Avatar_Frame.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(167, 164, 147);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Cage_Avatar_Frame.setFrameShape(QFrame.StyledPanel)
        self.Cage_Avatar_Frame.setFrameShadow(QFrame.Raised)
        self.Cage_Avatar_Button = QPushButton(self.Cage_Avatar_Frame)
        self.Cage_Avatar_Button.setObjectName(u"Cage_Avatar_Button")
        self.Cage_Avatar_Button.setGeometry(QRect(4, 6, 111, 151))
        self.Cage_Avatar_Button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 15pt \"Acme\";\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(229, 255, 185);\n"
"	font: 75 15pt \"Acme\";\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(120, 133, 96);\n"
"	font: 75 15pt \"Acme\";\n"
"	border:none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/Cages_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Cage_Avatar_Button.setIcon(icon)
        self.Cage_Avatar_Button.setCheckable(False)
        self.Cage_Avatar_Button.setFlat(False)
        self.Bought_Frame = QFrame(self.Infos_Frame)
        self.Bought_Frame.setObjectName(u"Bought_Frame")
        self.Bought_Frame.setGeometry(QRect(10, 54, 341, 68))
        self.Bought_Frame.setMinimumSize(QSize(341, 68))
        self.Bought_Frame.setMaximumSize(QSize(341, 68))
        self.Bought_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Bought_Frame.setFrameShape(QFrame.StyledPanel)
        self.Bought_Frame.setFrameShadow(QFrame.Raised)
        self.Cage_Bought_Label = QLabel(self.Bought_Frame)
        self.Cage_Bought_Label.setObjectName(u"Cage_Bought_Label")
        self.Cage_Bought_Label.setGeometry(QRect(50, 11, 80, 21))
        self.Cage_Bought_Label.setMinimumSize(QSize(80, 21))
        self.Cage_Bought_Label.setMaximumSize(QSize(80, 21))
        self.Cage_Bought_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Bought_Input = QDoubleSpinBox(self.Bought_Frame)
        self.Bought_Input.setObjectName(u"Bought_Input")
        self.Bought_Input.setGeometry(QRect(110, 11, 191, 21))
        self.Bought_Input.setMinimumSize(QSize(191, 21))
        self.Bought_Input.setMaximumSize(QSize(191, 21))
        self.Bought_Input.setStyleSheet(u"QDoubleSpinBox {\n"
"	background-color:rgb(167, 164, 147);\n"
"	padding-left: 5px;\n"
"	border: 2px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 15pt \"Acme\";\n"
"}")
        self.Bought_Input.setWrapping(False)
        self.Bought_Input.setAlignment(Qt.AlignCenter)
        self.Bought_Input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Bought_Input.setAccelerated(True)
        self.Bought_Input.setDecimals(3)
        self.Bought_Input.setMaximum(9999.989999999999782)
        self.Bought_Input.setSingleStep(0.500000000000000)
        self.Cage_Bought_Icon = QLabel(self.Bought_Frame)
        self.Cage_Bought_Icon.setObjectName(u"Cage_Bought_Icon")
        self.Cage_Bought_Icon.setGeometry(QRect(20, 11, 21, 21))
        self.Cage_Bought_Icon.setMinimumSize(QSize(21, 21))
        self.Cage_Bought_Icon.setMaximumSize(QSize(21, 21))
        self.Cage_Bought_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Cage_Bought_Icon.setPixmap(QPixmap(u":/Icons/TND_White.png"))
        self.Cage_Bought_Icon.setScaledContents(True)
        self.Cage_Bought_Icon.setAlignment(Qt.AlignCenter)
        self.Bought_Infos = QLabel(self.Bought_Frame)
        self.Bought_Infos.setObjectName(u"Bought_Infos")
        self.Bought_Infos.setGeometry(QRect(20, 37, 301, 21))
        self.Bought_Infos.setMinimumSize(QSize(301, 21))
        self.Bought_Infos.setMaximumSize(QSize(301, 21))
        self.Bought_Infos.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Gender_Frame = QFrame(self.Infos_Frame)
        self.Gender_Frame.setObjectName(u"Gender_Frame")
        self.Gender_Frame.setGeometry(QRect(10, 132, 341, 68))
        self.Gender_Frame.setMinimumSize(QSize(341, 68))
        self.Gender_Frame.setMaximumSize(QSize(341, 68))
        self.Gender_Frame.setFrameShape(QFrame.StyledPanel)
        self.Gender_Frame.setFrameShadow(QFrame.Raised)
        self.Cage_Gender_Icon = QLabel(self.Gender_Frame)
        self.Cage_Gender_Icon.setObjectName(u"Cage_Gender_Icon")
        self.Cage_Gender_Icon.setGeometry(QRect(20, 11, 21, 21))
        self.Cage_Gender_Icon.setMinimumSize(QSize(21, 21))
        self.Cage_Gender_Icon.setMaximumSize(QSize(21, 21))
        self.Cage_Gender_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Cage_Gender_Icon.setPixmap(QPixmap(u":/Icons/Gender_White.png"))
        self.Cage_Gender_Icon.setScaledContents(True)
        self.Cage_Gender_Icon.setAlignment(Qt.AlignCenter)
        self.Gender_Input = QComboBox(self.Gender_Frame)
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Gender_Male_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/Icons/Gender_Male_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Gender_Input.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Gender_Female_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/Icons/Gender_Female_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Gender_Input.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Gender_Null_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Icons/Gender_Null_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Gender_Input.addItem(icon3, "")
        self.Gender_Input.setObjectName(u"Gender_Input")
        self.Gender_Input.setGeometry(QRect(110, 11, 191, 21))
        self.Gender_Input.setMinimumSize(QSize(191, 21))
        self.Gender_Input.setMaximumSize(QSize(191, 21))
        self.Gender_Input.setStyleSheet(u"QComboBox {\n"
"	background-color:rgb(167, 164, 147);\n"
"	padding:1px 18px 1px 3px;\n"
"	padding-left: 15px;\n"
"	border: 2px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 15pt \"Acme\";\n"
"}")
        self.Cage_Gender_Label = QLabel(self.Gender_Frame)
        self.Cage_Gender_Label.setObjectName(u"Cage_Gender_Label")
        self.Cage_Gender_Label.setGeometry(QRect(50, 11, 61, 21))
        self.Cage_Gender_Label.setMinimumSize(QSize(61, 21))
        self.Cage_Gender_Label.setMaximumSize(QSize(61, 21))
        self.Cage_Gender_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Gender_Infos = QLabel(self.Gender_Frame)
        self.Gender_Infos.setObjectName(u"Gender_Infos")
        self.Gender_Infos.setGeometry(QRect(20, 37, 301, 21))
        self.Gender_Infos.setMinimumSize(QSize(301, 21))
        self.Gender_Infos.setMaximumSize(QSize(301, 21))
        self.Gender_Infos.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Notes_Label_Frame = QFrame(self.Infos_Frame)
        self.Notes_Label_Frame.setObjectName(u"Notes_Label_Frame")
        self.Notes_Label_Frame.setGeometry(QRect(10, 212, 41, 131))
        self.Notes_Label_Frame.setMinimumSize(QSize(41, 131))
        self.Notes_Label_Frame.setMaximumSize(QSize(41, 131))
        self.Notes_Label_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #2F2F2F;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Notes_Label_Frame.setFrameShape(QFrame.StyledPanel)
        self.Notes_Label_Frame.setFrameShadow(QFrame.Raised)
        self.Notes_Text_Label = QLabel(self.Notes_Label_Frame)
        self.Notes_Text_Label.setObjectName(u"Notes_Text_Label")
        self.Notes_Text_Label.setGeometry(QRect(0, 2, 41, 41))
        self.Notes_Text_Label.setLayoutDirection(Qt.LeftToRight)
        self.Notes_Text_Label.setAutoFillBackground(False)
        self.Notes_Text_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";\n"
"}")
        self.Notes_Text_Label.setTextFormat(Qt.RichText)
        self.Notes_Text_Label.setScaledContents(False)
        self.Notes_Text_Label.setAlignment(Qt.AlignCenter)
        self.Notes_Text_Label.setWordWrap(False)
        self.Notes_Text_Label.setOpenExternalLinks(False)
        self.Notes_Text_Label_2 = QLabel(self.Notes_Label_Frame)
        self.Notes_Text_Label_2.setObjectName(u"Notes_Text_Label_2")
        self.Notes_Text_Label_2.setGeometry(QRect(0, 23, 41, 41))
        self.Notes_Text_Label_2.setLayoutDirection(Qt.LeftToRight)
        self.Notes_Text_Label_2.setAutoFillBackground(False)
        self.Notes_Text_Label_2.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";\n"
"}")
        self.Notes_Text_Label_2.setTextFormat(Qt.RichText)
        self.Notes_Text_Label_2.setScaledContents(False)
        self.Notes_Text_Label_2.setAlignment(Qt.AlignCenter)
        self.Notes_Text_Label_2.setWordWrap(False)
        self.Notes_Text_Label_2.setOpenExternalLinks(False)
        self.Notes_Text_Label_3 = QLabel(self.Notes_Label_Frame)
        self.Notes_Text_Label_3.setObjectName(u"Notes_Text_Label_3")
        self.Notes_Text_Label_3.setGeometry(QRect(0, 46, 41, 41))
        self.Notes_Text_Label_3.setLayoutDirection(Qt.LeftToRight)
        self.Notes_Text_Label_3.setAutoFillBackground(False)
        self.Notes_Text_Label_3.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";\n"
"}")
        self.Notes_Text_Label_3.setTextFormat(Qt.RichText)
        self.Notes_Text_Label_3.setScaledContents(False)
        self.Notes_Text_Label_3.setAlignment(Qt.AlignCenter)
        self.Notes_Text_Label_3.setWordWrap(False)
        self.Notes_Text_Label_3.setOpenExternalLinks(False)
        self.Notes_Text_Label_4 = QLabel(self.Notes_Label_Frame)
        self.Notes_Text_Label_4.setObjectName(u"Notes_Text_Label_4")
        self.Notes_Text_Label_4.setGeometry(QRect(0, 66, 41, 41))
        self.Notes_Text_Label_4.setLayoutDirection(Qt.LeftToRight)
        self.Notes_Text_Label_4.setAutoFillBackground(False)
        self.Notes_Text_Label_4.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";\n"
"}")
        self.Notes_Text_Label_4.setTextFormat(Qt.RichText)
        self.Notes_Text_Label_4.setScaledContents(False)
        self.Notes_Text_Label_4.setAlignment(Qt.AlignCenter)
        self.Notes_Text_Label_4.setWordWrap(False)
        self.Notes_Text_Label_4.setOpenExternalLinks(False)
        self.Notes_Text_Label_5 = QLabel(self.Notes_Label_Frame)
        self.Notes_Text_Label_5.setObjectName(u"Notes_Text_Label_5")
        self.Notes_Text_Label_5.setGeometry(QRect(0, 90, 41, 41))
        self.Notes_Text_Label_5.setLayoutDirection(Qt.LeftToRight)
        self.Notes_Text_Label_5.setAutoFillBackground(False)
        self.Notes_Text_Label_5.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";\n"
"}")
        self.Notes_Text_Label_5.setTextFormat(Qt.RichText)
        self.Notes_Text_Label_5.setScaledContents(False)
        self.Notes_Text_Label_5.setAlignment(Qt.AlignCenter)
        self.Notes_Text_Label_5.setWordWrap(False)
        self.Notes_Text_Label_5.setOpenExternalLinks(False)
        self.Notes_Input = QPlainTextEdit(self.Infos_Frame)
        self.Notes_Input.setObjectName(u"Notes_Input")
        self.Notes_Input.setGeometry(QRect(61, 212, 300, 131))
        self.Notes_Input.setMinimumSize(QSize(300, 131))
        self.Notes_Input.setMaximumSize(QSize(300, 131))
        self.Notes_Input.setStyleSheet(u"QPlainTextEdit{\n"
"	background-color:rgb(167, 164, 147);\n"
"	padding-left: 15px;\n"
"	padding-top: 15px;\n"
"	padding-right: 15px;\n"
"	border: 2px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 15pt \"Acme\";\n"
"    	border-radius: 20px;\n"
"}")
        self.Notes_Input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Notes_Input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Add_Cage_Button = QPushButton(self.Infos_Frame)
        self.Add_Cage_Button.setObjectName(u"Add_Cage_Button")
        self.Add_Cage_Button.setEnabled(True)
        self.Add_Cage_Button.setGeometry(QRect(408, 226, 43, 33))
        self.Add_Cage_Button.setMinimumSize(QSize(43, 33))
        self.Add_Cage_Button.setMaximumSize(QSize(43, 33))
        font = QFont()
        font.setFamilies([u"Acme"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.Add_Cage_Button.setFont(font)
        self.Add_Cage_Button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Add_Cage_Button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Add_Cages_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Add_Cages_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Add_Cages_Green.png);\n"
"}")
        self.Add_Cage_Button.setIconSize(QSize(20, 20))
        self.Add_Cage_Button.setCheckable(False)
        self.Add_Cage_Button.setAutoRepeat(False)
        self.Add_Cage_Button.setAutoExclusive(False)
        self.Add_Cage_Button.setAutoRepeatDelay(50)
        self.Add_Cage_Button.setAutoRepeatInterval(10)
        self.Exit_Cage_Button = QPushButton(self.Infos_Frame)
        self.Exit_Cage_Button.setObjectName(u"Exit_Cage_Button")
        self.Exit_Cage_Button.setEnabled(True)
        self.Exit_Cage_Button.setGeometry(QRect(408, 277, 43, 33))
        self.Exit_Cage_Button.setMinimumSize(QSize(43, 33))
        self.Exit_Cage_Button.setMaximumSize(QSize(43, 33))
        self.Exit_Cage_Button.setFont(font)
        self.Exit_Cage_Button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Exit_Cage_Button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Exit_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Exit_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Exit_Red.png);\n"
"}")
        self.Exit_Cage_Button.setIconSize(QSize(20, 20))
        self.Exit_Cage_Button.setCheckable(False)
        self.Exit_Cage_Button.setAutoRepeat(False)
        self.Exit_Cage_Button.setAutoExclusive(False)
        self.Exit_Cage_Button.setAutoRepeatDelay(50)
        self.Exit_Cage_Button.setAutoRepeatInterval(10)
        self.Cage_Title = QLabel(self.Background)
        self.Cage_Title.setObjectName(u"Cage_Title")
        self.Cage_Title.setGeometry(QRect(50, 2, 450, 21))
        self.Cage_Title.setMinimumSize(QSize(450, 21))
        self.Cage_Title.setMaximumSize(QSize(450, 21))
        self.Cage_Title.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";")
        self.Cage_Title.setAlignment(Qt.AlignCenter)
        QWidget.setTabOrder(self.Gender_Input, self.Notes_Input)
        QWidget.setTabOrder(self.Notes_Input, self.Cage_Avatar_Button)
        QWidget.setTabOrder(self.Cage_Avatar_Button, self.Add_Cage_Button)
        QWidget.setTabOrder(self.Add_Cage_Button, self.Exit_Cage_Button)

        self.retranslateUi(AddCage_Main)
        self.Exit_Cage_Button.clicked.connect(AddCage_Main.close)

        QMetaObject.connectSlotsByName(AddCage_Main)
    # setupUi

    def retranslateUi(self, AddCage_Main):
        AddCage_Main.setWindowTitle(QCoreApplication.translate("AddCage_Main", u"Dialog", None))
        self.ID_Label.setText(QCoreApplication.translate("AddCage_Main", u"ID : ", None))
        self.Cage_Avatar_Button.setText(QCoreApplication.translate("AddCage_Main", u"Click Here", None))
        self.Cage_Bought_Label.setText(QCoreApplication.translate("AddCage_Main", u"Bought", None))
        self.Bought_Input.setPrefix("")
        self.Bought_Input.setSuffix(QCoreApplication.translate("AddCage_Main", u"  TND", None))
        self.Cage_Bought_Icon.setText("")
        self.Bought_Infos.setText(QCoreApplication.translate("AddCage_Main", u"How Much You Bought This Cage", None))
        self.Cage_Gender_Icon.setText("")
        self.Gender_Input.setItemText(0, QCoreApplication.translate("AddCage_Main", u"Male", None))
        self.Gender_Input.setItemText(1, QCoreApplication.translate("AddCage_Main", u"Female", None))
        self.Gender_Input.setItemText(2, QCoreApplication.translate("AddCage_Main", u"Kids", None))

        self.Cage_Gender_Label.setText(QCoreApplication.translate("AddCage_Main", u"Gender", None))
        self.Gender_Infos.setText(QCoreApplication.translate("AddCage_Main", u"The Gender Of The Cage.", None))
        self.Notes_Text_Label.setText(QCoreApplication.translate("AddCage_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">N</span></p></body></html>", None))
        self.Notes_Text_Label_2.setText(QCoreApplication.translate("AddCage_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">O</span></p></body></html>", None))
        self.Notes_Text_Label_3.setText(QCoreApplication.translate("AddCage_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">T</span></p></body></html>", None))
        self.Notes_Text_Label_4.setText(QCoreApplication.translate("AddCage_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">E</span></p></body></html>", None))
        self.Notes_Text_Label_5.setText(QCoreApplication.translate("AddCage_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">S</span></p></body></html>", None))
        self.Notes_Input.setDocumentTitle("")
        self.Notes_Input.setPlaceholderText(QCoreApplication.translate("AddCage_Main", u"Write Here...", None))
        self.Add_Cage_Button.setText("")
#if QT_CONFIG(shortcut)
        self.Add_Cage_Button.setShortcut(QCoreApplication.translate("AddCage_Main", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.Exit_Cage_Button.setText("")
#if QT_CONFIG(shortcut)
        self.Exit_Cage_Button.setShortcut(QCoreApplication.translate("AddCage_Main", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.Cage_Title.setText(QCoreApplication.translate("AddCage_Main", u"Add A New Cage", None))
    # retranslateUi

