# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainAddRabbit.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QDoubleSpinBox, QFrame, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)
import resources_rc

class Ui_AddRabbitr_Main(object):
    def setupUi(self, AddRabbitr_Main):
        if not AddRabbitr_Main.objectName():
            AddRabbitr_Main.setObjectName(u"AddRabbitr_Main")
        AddRabbitr_Main.resize(550, 867)
        AddRabbitr_Main.setMinimumSize(QSize(550, 867))
        AddRabbitr_Main.setMaximumSize(QSize(550, 867))
        AddRabbitr_Main.setStyleSheet(u"")
        self.Background = QFrame(AddRabbitr_Main)
        self.Background.setObjectName(u"Background")
        self.Background.setGeometry(QRect(0, 0, 550, 867))
        self.Background.setMinimumSize(QSize(550, 867))
        self.Background.setMaximumSize(QSize(550, 867))
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
        self.Infos_Frame.setGeometry(QRect(25, 25, 500, 825))
        self.Infos_Frame.setMinimumSize(QSize(500, 825))
        self.Infos_Frame.setMaximumSize(QSize(500, 825))
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
        self.ID_Label.setGeometry(QRect(37, 6, 121, 31))
        self.ID_Label.setMinimumSize(QSize(121, 31))
        self.ID_Label.setMaximumSize(QSize(121, 31))
        self.ID_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";\n"
"}")
        self.ID_Icon = QLabel(self.ID_Frame)
        self.ID_Icon.setObjectName(u"ID_Icon")
        self.ID_Icon.setGeometry(QRect(11, 11, 21, 21))
        self.ID_Icon.setMinimumSize(QSize(21, 21))
        self.ID_Icon.setMaximumSize(QSize(21, 21))
        self.ID_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.ID_Icon.setPixmap(QPixmap(u":/Icons/Rabbit_Tag.png"))
        self.ID_Icon.setScaledContents(True)
        self.ID_Icon.setAlignment(Qt.AlignCenter)
        self.ID_Icon.setWordWrap(False)
        self.Rabbit_Avatar_Frame = QFrame(self.Infos_Frame)
        self.Rabbit_Avatar_Frame.setObjectName(u"Rabbit_Avatar_Frame")
        self.Rabbit_Avatar_Frame.setGeometry(QRect(371, 10, 119, 161))
        self.Rabbit_Avatar_Frame.setMinimumSize(QSize(119, 161))
        self.Rabbit_Avatar_Frame.setMaximumSize(QSize(119, 161))
        self.Rabbit_Avatar_Frame.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(167, 164, 147);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Rabbit_Avatar_Frame.setFrameShape(QFrame.StyledPanel)
        self.Rabbit_Avatar_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Avatar_Button = QPushButton(self.Rabbit_Avatar_Frame)
        self.Rabbit_Avatar_Button.setObjectName(u"Rabbit_Avatar_Button")
        self.Rabbit_Avatar_Button.setGeometry(QRect(4, 6, 111, 151))
        self.Rabbit_Avatar_Button.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u":/Icons/Rabbit_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Rabbit_Avatar_Button.setIcon(icon)
        self.Rabbit_Avatar_Button.setCheckable(False)
        self.Rabbit_Avatar_Button.setFlat(False)
        self.Mother_Frame = QFrame(self.Infos_Frame)
        self.Mother_Frame.setObjectName(u"Mother_Frame")
        self.Mother_Frame.setGeometry(QRect(10, 132, 341, 68))
        self.Mother_Frame.setMinimumSize(QSize(341, 68))
        self.Mother_Frame.setMaximumSize(QSize(341, 68))
        self.Mother_Frame.setFrameShape(QFrame.StyledPanel)
        self.Mother_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Mother_Icon = QLabel(self.Mother_Frame)
        self.Rabbit_Mother_Icon.setObjectName(u"Rabbit_Mother_Icon")
        self.Rabbit_Mother_Icon.setGeometry(QRect(20, 11, 21, 21))
        self.Rabbit_Mother_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Mother_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Mother_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Mother_Icon.setPixmap(QPixmap(u":/Icons/Rabbit_Tree_White.png"))
        self.Rabbit_Mother_Icon.setScaledContents(True)
        self.Rabbit_Mother_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Mother_Label = QLabel(self.Mother_Frame)
        self.Rabbit_Mother_Label.setObjectName(u"Rabbit_Mother_Label")
        self.Rabbit_Mother_Label.setGeometry(QRect(50, 11, 51, 21))
        self.Rabbit_Mother_Label.setMinimumSize(QSize(51, 21))
        self.Rabbit_Mother_Label.setMaximumSize(QSize(51, 21))
        self.Rabbit_Mother_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Mother_Infos = QLabel(self.Mother_Frame)
        self.Mother_Infos.setObjectName(u"Mother_Infos")
        self.Mother_Infos.setGeometry(QRect(20, 37, 301, 21))
        self.Mother_Infos.setMinimumSize(QSize(301, 21))
        self.Mother_Infos.setMaximumSize(QSize(301, 21))
        self.Mother_Infos.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Mother_Input = QSpinBox(self.Mother_Frame)
        self.Mother_Input.setObjectName(u"Mother_Input")
        self.Mother_Input.setGeometry(QRect(110, 11, 191, 21))
        self.Mother_Input.setStyleSheet(u"QSpinBox {\n"
"	background-color:rgb(167, 164, 147);\n"
"	padding-left: 5px;\n"
"	border: 2px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 15pt \"Acme\";\n"
"}")
        self.Mother_Input.setAlignment(Qt.AlignCenter)
        self.Mother_Input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Breed_Frame = QFrame(self.Infos_Frame)
        self.Breed_Frame.setObjectName(u"Breed_Frame")
        self.Breed_Frame.setGeometry(QRect(10, 54, 341, 68))
        self.Breed_Frame.setMinimumSize(QSize(341, 68))
        self.Breed_Frame.setMaximumSize(QSize(341, 68))
        self.Breed_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Breed_Frame.setFrameShape(QFrame.StyledPanel)
        self.Breed_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Breed_Icon = QLabel(self.Breed_Frame)
        self.Rabbit_Breed_Icon.setObjectName(u"Rabbit_Breed_Icon")
        self.Rabbit_Breed_Icon.setGeometry(QRect(20, 11, 21, 21))
        self.Rabbit_Breed_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Breed_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Breed_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Breed_Icon.setPixmap(QPixmap(u":/Icons/Rabbit_White.png"))
        self.Rabbit_Breed_Icon.setScaledContents(True)
        self.Rabbit_Breed_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Breed_Icon.setWordWrap(False)
        self.Breed_Input = QLineEdit(self.Breed_Frame)
        self.Breed_Input.setObjectName(u"Breed_Input")
        self.Breed_Input.setGeometry(QRect(110, 11, 191, 21))
        self.Breed_Input.setMinimumSize(QSize(191, 21))
        self.Breed_Input.setMaximumSize(QSize(191, 21))
        self.Breed_Input.setStyleSheet(u"QLineEdit {\n"
"	background-color:rgb(167, 164, 147);\n"
"	padding-left: 5px;\n"
"	border: 2px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 15pt \"Acme\";\n"
"}")
        self.Rabbit_Breed_Label = QLabel(self.Breed_Frame)
        self.Rabbit_Breed_Label.setObjectName(u"Rabbit_Breed_Label")
        self.Rabbit_Breed_Label.setGeometry(QRect(50, 11, 51, 21))
        self.Rabbit_Breed_Label.setMinimumSize(QSize(51, 21))
        self.Rabbit_Breed_Label.setMaximumSize(QSize(51, 21))
        self.Rabbit_Breed_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Breed_Infos = QLabel(self.Breed_Frame)
        self.Breed_Infos.setObjectName(u"Breed_Infos")
        self.Breed_Infos.setGeometry(QRect(20, 37, 301, 21))
        self.Breed_Infos.setMinimumSize(QSize(301, 21))
        self.Breed_Infos.setMaximumSize(QSize(301, 21))
        self.Breed_Infos.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Gender_Frame = QFrame(self.Infos_Frame)
        self.Gender_Frame.setObjectName(u"Gender_Frame")
        self.Gender_Frame.setGeometry(QRect(10, 444, 341, 68))
        self.Gender_Frame.setMinimumSize(QSize(341, 68))
        self.Gender_Frame.setMaximumSize(QSize(341, 68))
        self.Gender_Frame.setFrameShape(QFrame.StyledPanel)
        self.Gender_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Gender_Icon = QLabel(self.Gender_Frame)
        self.Rabbit_Gender_Icon.setObjectName(u"Rabbit_Gender_Icon")
        self.Rabbit_Gender_Icon.setGeometry(QRect(20, 11, 21, 21))
        self.Rabbit_Gender_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Gender_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Gender_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Gender_Icon.setPixmap(QPixmap(u":/Icons/Gender_White.png"))
        self.Rabbit_Gender_Icon.setScaledContents(True)
        self.Rabbit_Gender_Icon.setAlignment(Qt.AlignCenter)
        self.Gender_Input = QComboBox(self.Gender_Frame)
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Gender_Null_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/Icons/Gender_Null_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Gender_Input.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Gender_Male_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/Icons/Gender_Male_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Gender_Input.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Gender_Female_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Icons/Gender_Female_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
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
        self.Rabbit_Gender_Label = QLabel(self.Gender_Frame)
        self.Rabbit_Gender_Label.setObjectName(u"Rabbit_Gender_Label")
        self.Rabbit_Gender_Label.setGeometry(QRect(50, 11, 61, 21))
        self.Rabbit_Gender_Label.setMinimumSize(QSize(61, 21))
        self.Rabbit_Gender_Label.setMaximumSize(QSize(61, 21))
        self.Rabbit_Gender_Label.setStyleSheet(u"QLabel {\n"
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
        self.Notes_Label_Frame.setGeometry(QRect(10, 678, 41, 131))
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
        self.Notes_Input.setGeometry(QRect(49, 678, 300, 131))
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
        self.Add_Rabbit_Button = QPushButton(self.Infos_Frame)
        self.Add_Rabbit_Button.setObjectName(u"Add_Rabbit_Button")
        self.Add_Rabbit_Button.setEnabled(True)
        self.Add_Rabbit_Button.setGeometry(QRect(408, 702, 43, 33))
        self.Add_Rabbit_Button.setMinimumSize(QSize(43, 33))
        self.Add_Rabbit_Button.setMaximumSize(QSize(43, 33))
        font = QFont()
        font.setFamilies([u"Acme"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.Add_Rabbit_Button.setFont(font)
        self.Add_Rabbit_Button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Add_Rabbit_Button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Add_Rabbit_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Add_Rabbit_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Add_Rabbit_Green.png);\n"
"}")
        self.Add_Rabbit_Button.setIconSize(QSize(20, 20))
        self.Add_Rabbit_Button.setCheckable(False)
        self.Add_Rabbit_Button.setAutoRepeat(False)
        self.Add_Rabbit_Button.setAutoExclusive(False)
        self.Add_Rabbit_Button.setAutoRepeatDelay(50)
        self.Add_Rabbit_Button.setAutoRepeatInterval(10)
        self.Exit_Rabbit_Button = QPushButton(self.Infos_Frame)
        self.Exit_Rabbit_Button.setObjectName(u"Exit_Rabbit_Button")
        self.Exit_Rabbit_Button.setEnabled(True)
        self.Exit_Rabbit_Button.setGeometry(QRect(408, 753, 43, 33))
        self.Exit_Rabbit_Button.setMinimumSize(QSize(43, 33))
        self.Exit_Rabbit_Button.setMaximumSize(QSize(43, 33))
        self.Exit_Rabbit_Button.setFont(font)
        self.Exit_Rabbit_Button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Exit_Rabbit_Button.setStyleSheet(u"QPushButton {\n"
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
        self.Exit_Rabbit_Button.setIconSize(QSize(20, 20))
        self.Exit_Rabbit_Button.setCheckable(False)
        self.Exit_Rabbit_Button.setAutoRepeat(False)
        self.Exit_Rabbit_Button.setAutoExclusive(False)
        self.Exit_Rabbit_Button.setAutoRepeatDelay(50)
        self.Exit_Rabbit_Button.setAutoRepeatInterval(10)
        self.Father_Frame = QFrame(self.Infos_Frame)
        self.Father_Frame.setObjectName(u"Father_Frame")
        self.Father_Frame.setGeometry(QRect(10, 210, 341, 68))
        self.Father_Frame.setMinimumSize(QSize(341, 68))
        self.Father_Frame.setMaximumSize(QSize(341, 68))
        self.Father_Frame.setFrameShape(QFrame.StyledPanel)
        self.Father_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Father_Icon = QLabel(self.Father_Frame)
        self.Rabbit_Father_Icon.setObjectName(u"Rabbit_Father_Icon")
        self.Rabbit_Father_Icon.setGeometry(QRect(20, 11, 21, 21))
        self.Rabbit_Father_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Father_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Father_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Father_Icon.setPixmap(QPixmap(u":/Icons/Rabbit_Tree_White.png"))
        self.Rabbit_Father_Icon.setScaledContents(True)
        self.Rabbit_Father_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Father_Label = QLabel(self.Father_Frame)
        self.Rabbit_Father_Label.setObjectName(u"Rabbit_Father_Label")
        self.Rabbit_Father_Label.setGeometry(QRect(50, 11, 51, 21))
        self.Rabbit_Father_Label.setMinimumSize(QSize(51, 21))
        self.Rabbit_Father_Label.setMaximumSize(QSize(51, 21))
        self.Rabbit_Father_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Father_Infos = QLabel(self.Father_Frame)
        self.Father_Infos.setObjectName(u"Father_Infos")
        self.Father_Infos.setGeometry(QRect(20, 37, 301, 21))
        self.Father_Infos.setMinimumSize(QSize(301, 21))
        self.Father_Infos.setMaximumSize(QSize(301, 21))
        self.Father_Infos.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Father_Input = QSpinBox(self.Father_Frame)
        self.Father_Input.setObjectName(u"Father_Input")
        self.Father_Input.setGeometry(QRect(110, 11, 191, 21))
        self.Father_Input.setStyleSheet(u"QSpinBox {\n"
"	background-color:rgb(167, 164, 147);\n"
"	padding-left: 5px;\n"
"	border: 2px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 15pt \"Acme\";\n"
"}")
        self.Father_Input.setAlignment(Qt.AlignCenter)
        self.Father_Input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Color_Frame = QFrame(self.Infos_Frame)
        self.Color_Frame.setObjectName(u"Color_Frame")
        self.Color_Frame.setGeometry(QRect(10, 288, 341, 68))
        self.Color_Frame.setMinimumSize(QSize(341, 68))
        self.Color_Frame.setMaximumSize(QSize(341, 68))
        self.Color_Frame.setFrameShape(QFrame.StyledPanel)
        self.Color_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Color_Icon = QLabel(self.Color_Frame)
        self.Rabbit_Color_Icon.setObjectName(u"Rabbit_Color_Icon")
        self.Rabbit_Color_Icon.setGeometry(QRect(20, 11, 21, 21))
        self.Rabbit_Color_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Color_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Color_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Color_Icon.setPixmap(QPixmap(u":/Icons/Rabbit_White.png"))
        self.Rabbit_Color_Icon.setScaledContents(True)
        self.Rabbit_Color_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Color_Label = QLabel(self.Color_Frame)
        self.Rabbit_Color_Label.setObjectName(u"Rabbit_Color_Label")
        self.Rabbit_Color_Label.setGeometry(QRect(50, 11, 51, 21))
        self.Rabbit_Color_Label.setMinimumSize(QSize(51, 21))
        self.Rabbit_Color_Label.setMaximumSize(QSize(51, 21))
        self.Rabbit_Color_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Color_Input = QLineEdit(self.Color_Frame)
        self.Color_Input.setObjectName(u"Color_Input")
        self.Color_Input.setGeometry(QRect(110, 11, 191, 21))
        self.Color_Input.setMinimumSize(QSize(191, 21))
        self.Color_Input.setMaximumSize(QSize(191, 21))
        self.Color_Input.setStyleSheet(u"QLineEdit {\n"
"	background-color:rgb(167, 164, 147);\n"
"	padding-left: 5px;\n"
"	border: 2px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 15pt \"Acme\";\n"
"}")
        self.Color_Input.setMaxLength(8)
        self.Color_Infos = QLabel(self.Color_Frame)
        self.Color_Infos.setObjectName(u"Color_Infos")
        self.Color_Infos.setGeometry(QRect(20, 37, 301, 21))
        self.Color_Infos.setMinimumSize(QSize(301, 21))
        self.Color_Infos.setMaximumSize(QSize(301, 21))
        self.Color_Infos.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Born_Frame = QFrame(self.Infos_Frame)
        self.Born_Frame.setObjectName(u"Born_Frame")
        self.Born_Frame.setGeometry(QRect(10, 366, 341, 68))
        self.Born_Frame.setMinimumSize(QSize(341, 68))
        self.Born_Frame.setMaximumSize(QSize(341, 68))
        self.Born_Frame.setFrameShape(QFrame.StyledPanel)
        self.Born_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Born_Icon = QLabel(self.Born_Frame)
        self.Rabbit_Born_Icon.setObjectName(u"Rabbit_Born_Icon")
        self.Rabbit_Born_Icon.setGeometry(QRect(20, 11, 21, 21))
        self.Rabbit_Born_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Born_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Born_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Born_Icon.setPixmap(QPixmap(u":/Icons/Calendar_White.png"))
        self.Rabbit_Born_Icon.setScaledContents(True)
        self.Rabbit_Born_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Born_Label = QLabel(self.Born_Frame)
        self.Rabbit_Born_Label.setObjectName(u"Rabbit_Born_Label")
        self.Rabbit_Born_Label.setGeometry(QRect(50, 11, 61, 21))
        self.Rabbit_Born_Label.setMinimumSize(QSize(61, 21))
        self.Rabbit_Born_Label.setMaximumSize(QSize(61, 21))
        self.Rabbit_Born_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Born_Infos = QLabel(self.Born_Frame)
        self.Born_Infos.setObjectName(u"Born_Infos")
        self.Born_Infos.setGeometry(QRect(20, 37, 301, 21))
        self.Born_Infos.setMinimumSize(QSize(301, 21))
        self.Born_Infos.setMaximumSize(QSize(301, 21))
        self.Born_Infos.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Born_Input = QDateEdit(self.Born_Frame)
        self.Born_Input.setObjectName(u"Born_Input")
        self.Born_Input.setGeometry(QRect(110, 11, 191, 21))
        self.Born_Input.setMinimumSize(QSize(191, 21))
        self.Born_Input.setMaximumSize(QSize(191, 21))
        self.Born_Input.setStyleSheet(u"QDateEdit {\n"
"	background-color:rgb(167, 164, 147);\n"
"	padding:1px 18px 1px 3px;\n"
"	padding-left: 15px;\n"
"	border: 2px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 15pt \"Acme\";\n"
"}")
        self.Born_Input.setDateTime(QDateTime(QDate(2024, 8, 15), QTime(0, 0, 0)))
        self.Born_Input.setMinimumDate(QDate(2023, 9, 14))
        self.Born_Input.setCalendarPopup(True)
        self.Bought = QFrame(self.Infos_Frame)
        self.Bought.setObjectName(u"Bought")
        self.Bought.setGeometry(QRect(355, 188, 140, 481))
        self.Bought.setMinimumSize(QSize(140, 481))
        self.Bought.setMaximumSize(QSize(140, 481))
        self.Bought.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: none;\n"
"	border-style: outset;\n"
"}")
        self.Bought.setFrameShape(QFrame.StyledPanel)
        self.Bought.setFrameShadow(QFrame.Raised)
        self.Rabbit_Bought_Label = QLabel(self.Bought)
        self.Rabbit_Bought_Label.setObjectName(u"Rabbit_Bought_Label")
        self.Rabbit_Bought_Label.setGeometry(QRect(50, 10, 80, 21))
        self.Rabbit_Bought_Label.setMinimumSize(QSize(80, 21))
        self.Rabbit_Bought_Label.setMaximumSize(QSize(80, 21))
        self.Rabbit_Bought_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Rabbit_Bought_Icon = QLabel(self.Bought)
        self.Rabbit_Bought_Icon.setObjectName(u"Rabbit_Bought_Icon")
        self.Rabbit_Bought_Icon.setGeometry(QRect(24, 10, 21, 21))
        self.Rabbit_Bought_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Bought_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Bought_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Bought_Icon.setPixmap(QPixmap(u":/Icons/TND_White.png"))
        self.Rabbit_Bought_Icon.setScaledContents(True)
        self.Rabbit_Bought_Icon.setAlignment(Qt.AlignCenter)
        self.Bought_Infos = QLabel(self.Bought)
        self.Bought_Infos.setObjectName(u"Bought_Infos")
        self.Bought_Infos.setGeometry(QRect(10, 80, 120, 361))
        self.Bought_Infos.setMinimumSize(QSize(120, 361))
        self.Bought_Infos.setMaximumSize(QSize(120, 361))
        self.Bought_Infos.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Bought_Infos.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.Bought_Infos.setWordWrap(True)
        self.Bought_Input = QDoubleSpinBox(self.Bought)
        self.Bought_Input.setObjectName(u"Bought_Input")
        self.Bought_Input.setGeometry(QRect(11, 47, 120, 21))
        self.Bought_Input.setMinimumSize(QSize(120, 21))
        self.Bought_Input.setMaximumSize(QSize(120, 21))
        self.Bought_Input.setStyleSheet(u"QDoubleSpinBox {\n"
"	background-color:rgb(167, 164, 147);\n"
"	padding-left: 5px;\n"
"	border: 2px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 13pt \"Acme\";\n"
"}")
        self.Bought_Input.setWrapping(False)
        self.Bought_Input.setAlignment(Qt.AlignCenter)
        self.Bought_Input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Bought_Input.setAccelerated(True)
        self.Bought_Input.setDecimals(3)
        self.Bought_Input.setMaximum(9999.989999999999782)
        self.Bought_Input.setSingleStep(0.500000000000000)
        self.Type_Frame = QFrame(self.Infos_Frame)
        self.Type_Frame.setObjectName(u"Type_Frame")
        self.Type_Frame.setGeometry(QRect(10, 522, 341, 68))
        self.Type_Frame.setMinimumSize(QSize(341, 68))
        self.Type_Frame.setMaximumSize(QSize(341, 68))
        self.Type_Frame.setFrameShape(QFrame.StyledPanel)
        self.Type_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Type_Icon = QLabel(self.Type_Frame)
        self.Rabbit_Type_Icon.setObjectName(u"Rabbit_Type_Icon")
        self.Rabbit_Type_Icon.setGeometry(QRect(20, 11, 21, 21))
        self.Rabbit_Type_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Type_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Type_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Type_Icon.setPixmap(QPixmap(u":/Icons/Rabbits_White.png"))
        self.Rabbit_Type_Icon.setScaledContents(True)
        self.Rabbit_Type_Icon.setAlignment(Qt.AlignCenter)
        self.Type_Input = QComboBox(self.Type_Frame)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Rabbits_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/Icons/Rabbits_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Type_Input.addItem(icon4, "")
        self.Type_Input.addItem(icon4, "")
        self.Type_Input.setObjectName(u"Type_Input")
        self.Type_Input.setGeometry(QRect(110, 11, 191, 21))
        self.Type_Input.setMinimumSize(QSize(191, 21))
        self.Type_Input.setMaximumSize(QSize(191, 21))
        self.Type_Input.setStyleSheet(u"QComboBox {\n"
"	background-color:rgb(167, 164, 147);\n"
"	padding:1px 18px 1px 3px;\n"
"	padding-left: 15px;\n"
"	border: 2px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 15pt \"Acme\";\n"
"}")
        self.Rabbit_Type_Label = QLabel(self.Type_Frame)
        self.Rabbit_Type_Label.setObjectName(u"Rabbit_Type_Label")
        self.Rabbit_Type_Label.setGeometry(QRect(50, 11, 61, 21))
        self.Rabbit_Type_Label.setMinimumSize(QSize(61, 21))
        self.Rabbit_Type_Label.setMaximumSize(QSize(61, 21))
        self.Rabbit_Type_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Type_Infos = QLabel(self.Type_Frame)
        self.Type_Infos.setObjectName(u"Type_Infos")
        self.Type_Infos.setGeometry(QRect(20, 37, 301, 21))
        self.Type_Infos.setMinimumSize(QSize(301, 21))
        self.Type_Infos.setMaximumSize(QSize(301, 21))
        self.Type_Infos.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Cage_Frame = QFrame(self.Infos_Frame)
        self.Cage_Frame.setObjectName(u"Cage_Frame")
        self.Cage_Frame.setGeometry(QRect(10, 600, 341, 68))
        self.Cage_Frame.setMinimumSize(QSize(341, 68))
        self.Cage_Frame.setMaximumSize(QSize(341, 68))
        self.Cage_Frame.setFrameShape(QFrame.StyledPanel)
        self.Cage_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Cage_Icon = QLabel(self.Cage_Frame)
        self.Rabbit_Cage_Icon.setObjectName(u"Rabbit_Cage_Icon")
        self.Rabbit_Cage_Icon.setGeometry(QRect(20, 11, 21, 21))
        self.Rabbit_Cage_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Cage_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Cage_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Cage_Icon.setPixmap(QPixmap(u":/Icons/Cages_White.png"))
        self.Rabbit_Cage_Icon.setScaledContents(True)
        self.Rabbit_Cage_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Cage_Label = QLabel(self.Cage_Frame)
        self.Rabbit_Cage_Label.setObjectName(u"Rabbit_Cage_Label")
        self.Rabbit_Cage_Label.setGeometry(QRect(50, 11, 51, 21))
        self.Rabbit_Cage_Label.setMinimumSize(QSize(51, 21))
        self.Rabbit_Cage_Label.setMaximumSize(QSize(51, 21))
        self.Rabbit_Cage_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Cage_Infos = QLabel(self.Cage_Frame)
        self.Cage_Infos.setObjectName(u"Cage_Infos")
        self.Cage_Infos.setGeometry(QRect(20, 37, 301, 21))
        self.Cage_Infos.setMinimumSize(QSize(301, 21))
        self.Cage_Infos.setMaximumSize(QSize(301, 21))
        self.Cage_Infos.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Cage_Input = QSpinBox(self.Cage_Frame)
        self.Cage_Input.setObjectName(u"Cage_Input")
        self.Cage_Input.setGeometry(QRect(110, 11, 191, 21))
        self.Cage_Input.setStyleSheet(u"QSpinBox {\n"
"	background-color:rgb(167, 164, 147);\n"
"	padding-left: 5px;\n"
"	border: 2px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 15pt \"Acme\";\n"
"}")
        self.Cage_Input.setAlignment(Qt.AlignCenter)
        self.Cage_Input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Rabbit_Title = QLabel(self.Background)
        self.Rabbit_Title.setObjectName(u"Rabbit_Title")
        self.Rabbit_Title.setGeometry(QRect(50, 2, 450, 21))
        self.Rabbit_Title.setMinimumSize(QSize(450, 21))
        self.Rabbit_Title.setMaximumSize(QSize(450, 21))
        self.Rabbit_Title.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";")
        self.Rabbit_Title.setAlignment(Qt.AlignCenter)
        QWidget.setTabOrder(self.Breed_Input, self.Gender_Input)
        QWidget.setTabOrder(self.Gender_Input, self.Notes_Input)
        QWidget.setTabOrder(self.Notes_Input, self.Rabbit_Avatar_Button)
        QWidget.setTabOrder(self.Rabbit_Avatar_Button, self.Add_Rabbit_Button)
        QWidget.setTabOrder(self.Add_Rabbit_Button, self.Exit_Rabbit_Button)

        self.retranslateUi(AddRabbitr_Main)
        self.Exit_Rabbit_Button.clicked.connect(AddRabbitr_Main.close)

        QMetaObject.connectSlotsByName(AddRabbitr_Main)
    # setupUi

    def retranslateUi(self, AddRabbitr_Main):
        AddRabbitr_Main.setWindowTitle(QCoreApplication.translate("AddRabbitr_Main", u"Dialog", None))
        self.ID_Label.setText(QCoreApplication.translate("AddRabbitr_Main", u"ID : ", None))
        self.ID_Icon.setText("")
        self.Rabbit_Avatar_Button.setText(QCoreApplication.translate("AddRabbitr_Main", u"Click Here", None))
        self.Rabbit_Mother_Icon.setText("")
        self.Rabbit_Mother_Label.setText(QCoreApplication.translate("AddRabbitr_Main", u"Mother", None))
        self.Mother_Infos.setText(QCoreApplication.translate("AddRabbitr_Main", u"The Mother Of The Rabbit. *", None))
        self.Rabbit_Breed_Icon.setText("")
        self.Breed_Input.setPlaceholderText(QCoreApplication.translate("AddRabbitr_Main", u"Write Here...", None))
        self.Rabbit_Breed_Label.setText(QCoreApplication.translate("AddRabbitr_Main", u"Breed", None))
        self.Breed_Infos.setText(QCoreApplication.translate("AddRabbitr_Main", u"The Breed Of The Rabbit.", None))
        self.Rabbit_Gender_Icon.setText("")
        self.Gender_Input.setItemText(0, QCoreApplication.translate("AddRabbitr_Main", u"Null", None))
        self.Gender_Input.setItemText(1, QCoreApplication.translate("AddRabbitr_Main", u"Male", None))
        self.Gender_Input.setItemText(2, QCoreApplication.translate("AddRabbitr_Main", u"Female", None))

        self.Rabbit_Gender_Label.setText(QCoreApplication.translate("AddRabbitr_Main", u"Gender", None))
        self.Gender_Infos.setText(QCoreApplication.translate("AddRabbitr_Main", u"The Rabbit's Gender.", None))
        self.Notes_Text_Label.setText(QCoreApplication.translate("AddRabbitr_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">N</span></p></body></html>", None))
        self.Notes_Text_Label_2.setText(QCoreApplication.translate("AddRabbitr_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">O</span></p></body></html>", None))
        self.Notes_Text_Label_3.setText(QCoreApplication.translate("AddRabbitr_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">T</span></p></body></html>", None))
        self.Notes_Text_Label_4.setText(QCoreApplication.translate("AddRabbitr_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">E</span></p></body></html>", None))
        self.Notes_Text_Label_5.setText(QCoreApplication.translate("AddRabbitr_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">S</span></p></body></html>", None))
        self.Notes_Input.setDocumentTitle("")
        self.Notes_Input.setPlaceholderText(QCoreApplication.translate("AddRabbitr_Main", u"Write Here...", None))
        self.Add_Rabbit_Button.setText("")
#if QT_CONFIG(shortcut)
        self.Add_Rabbit_Button.setShortcut(QCoreApplication.translate("AddRabbitr_Main", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.Exit_Rabbit_Button.setText("")
#if QT_CONFIG(shortcut)
        self.Exit_Rabbit_Button.setShortcut(QCoreApplication.translate("AddRabbitr_Main", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.Rabbit_Father_Icon.setText("")
        self.Rabbit_Father_Label.setText(QCoreApplication.translate("AddRabbitr_Main", u"Father", None))
        self.Father_Infos.setText(QCoreApplication.translate("AddRabbitr_Main", u"The Father Of The Rabbit. *", None))
        self.Rabbit_Color_Icon.setText("")
        self.Rabbit_Color_Label.setText(QCoreApplication.translate("AddRabbitr_Main", u"Color", None))
        self.Color_Input.setPlaceholderText(QCoreApplication.translate("AddRabbitr_Main", u"Write Here...", None))
        self.Color_Infos.setText(QCoreApplication.translate("AddRabbitr_Main", u"The Rabbit's Color.", None))
        self.Rabbit_Born_Icon.setText("")
        self.Rabbit_Born_Label.setText(QCoreApplication.translate("AddRabbitr_Main", u"Born", None))
        self.Born_Infos.setText(QCoreApplication.translate("AddRabbitr_Main", u"The Birthday Of The Rabbit.", None))
        self.Rabbit_Bought_Label.setText(QCoreApplication.translate("AddRabbitr_Main", u"Bought", None))
        self.Rabbit_Bought_Icon.setText("")
        self.Bought_Infos.setText(QCoreApplication.translate("AddRabbitr_Main", u"How Much You Buy This Rabbit", None))
        self.Bought_Input.setPrefix("")
        self.Bought_Input.setSuffix(QCoreApplication.translate("AddRabbitr_Main", u"  TND", None))
        self.Rabbit_Type_Icon.setText("")
        self.Type_Input.setItemText(0, QCoreApplication.translate("AddRabbitr_Main", u"Meat", None))
        self.Type_Input.setItemText(1, QCoreApplication.translate("AddRabbitr_Main", u"Breeding", None))

        self.Rabbit_Type_Label.setText(QCoreApplication.translate("AddRabbitr_Main", u"Type", None))
        self.Type_Infos.setText(QCoreApplication.translate("AddRabbitr_Main", u"The Type Of The Rabbit.", None))
        self.Rabbit_Cage_Icon.setText("")
        self.Rabbit_Cage_Label.setText(QCoreApplication.translate("AddRabbitr_Main", u"Cage", None))
        self.Cage_Infos.setText(QCoreApplication.translate("AddRabbitr_Main", u"The Cage ID Where The Rabbit.", None))
        self.Rabbit_Title.setText(QCoreApplication.translate("AddRabbitr_Main", u"Add A New Rabbit", None))
    # retranslateUi

