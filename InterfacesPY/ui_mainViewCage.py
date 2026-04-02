# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainViewCage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QWidget)
import resources_rc

class Ui_Cage_View_Main(object):
    def setupUi(self, Cage_View_Main):
        if not Cage_View_Main.objectName():
            Cage_View_Main.setObjectName(u"Cage_View_Main")
        Cage_View_Main.resize(1031, 867)
        Cage_View_Main.setMinimumSize(QSize(1031, 867))
        Cage_View_Main.setMaximumSize(QSize(1031, 867))
        Cage_View_Main.setStyleSheet(u"")
        self.Background = QFrame(Cage_View_Main)
        self.Background.setObjectName(u"Background")
        self.Background.setGeometry(QRect(0, 0, 1031, 867))
        self.Background.setMinimumSize(QSize(1031, 867))
        self.Background.setMaximumSize(QSize(1031, 867))
        self.Background.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"Orbitron\";\n"
"	border-style: outset;\n"
"    	border-radius: 50px;\n"
"}")
        self.Background.setFrameShape(QFrame.StyledPanel)
        self.Background.setFrameShadow(QFrame.Raised)
        self.Cage_Rabbits_Frame = QFrame(self.Background)
        self.Cage_Rabbits_Frame.setObjectName(u"Cage_Rabbits_Frame")
        self.Cage_Rabbits_Frame.setGeometry(QRect(30, 264, 971, 565))
        self.Cage_Rabbits_Frame.setMinimumSize(QSize(971, 565))
        self.Cage_Rabbits_Frame.setMaximumSize(QSize(971, 565))
        self.Cage_Rabbits_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Cage_Rabbits_Frame.setFrameShape(QFrame.StyledPanel)
        self.Cage_Rabbits_Frame.setFrameShadow(QFrame.Raised)
        self.RabbitsLabel_Frame = QFrame(self.Cage_Rabbits_Frame)
        self.RabbitsLabel_Frame.setObjectName(u"RabbitsLabel_Frame")
        self.RabbitsLabel_Frame.setEnabled(True)
        self.RabbitsLabel_Frame.setGeometry(QRect(0, 0, 120, 44))
        self.RabbitsLabel_Frame.setMinimumSize(QSize(120, 44))
        self.RabbitsLabel_Frame.setMaximumSize(QSize(120, 44))
        self.RabbitsLabel_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #2F2F2F;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.RabbitsLabel_Frame.setFrameShape(QFrame.StyledPanel)
        self.RabbitsLabel_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Label = QLabel(self.RabbitsLabel_Frame)
        self.Rabbit_Label.setObjectName(u"Rabbit_Label")
        self.Rabbit_Label.setGeometry(QRect(10, 6, 100, 31))
        self.Rabbit_Label.setMinimumSize(QSize(100, 31))
        self.Rabbit_Label.setMaximumSize(QSize(100, 31))
        self.Rabbit_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";\n"
"}")
        self.Rabbit_Label.setAlignment(Qt.AlignCenter)
        self.Cage_Rabbits_ScrollArea = QScrollArea(self.Cage_Rabbits_Frame)
        self.Cage_Rabbits_ScrollArea.setObjectName(u"Cage_Rabbits_ScrollArea")
        self.Cage_Rabbits_ScrollArea.setGeometry(QRect(11, 62, 950, 481))
        self.Cage_Rabbits_ScrollArea.setMinimumSize(QSize(950, 481))
        self.Cage_Rabbits_ScrollArea.setMaximumSize(QSize(950, 481))
        self.Cage_Rabbits_ScrollArea.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: none;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Cage_Rabbits_ScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Cage_Rabbits_ScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Cage_Rabbits_ScrollArea.setWidgetResizable(True)
        self.Cage_Rabbits_ScrollArea_Widget = QWidget()
        self.Cage_Rabbits_ScrollArea_Widget.setObjectName(u"Cage_Rabbits_ScrollArea_Widget")
        self.Cage_Rabbits_ScrollArea_Widget.setGeometry(QRect(0, 0, 950, 481))
        self.gridLayoutWidget = QWidget(self.Cage_Rabbits_ScrollArea_Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(5, 0, 931, 481))
        self.GridRabbits_ScrollArea = QGridLayout(self.gridLayoutWidget)
        self.GridRabbits_ScrollArea.setObjectName(u"GridRabbits_ScrollArea")
        self.GridRabbits_ScrollArea.setContentsMargins(0, 0, 0, 0)
        self.Cage_Rabbits_ScrollArea.setWidget(self.Cage_Rabbits_ScrollArea_Widget)
        self.Filter_Frame_View = QFrame(self.Cage_Rabbits_Frame)
        self.Filter_Frame_View.setObjectName(u"Filter_Frame_View")
        self.Filter_Frame_View.setGeometry(QRect(200, 0, 620, 47))
        self.Filter_Frame_View.setMinimumSize(QSize(620, 47))
        self.Filter_Frame_View.setMaximumSize(QSize(620, 47))
        self.Filter_Frame_View.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 73, 73);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Filter_Frame_View.setFrameShape(QFrame.StyledPanel)
        self.Filter_Frame_View.setFrameShadow(QFrame.Raised)
        self.FilterGender_Rabbits = QComboBox(self.Filter_Frame_View)
        icon = QIcon()
        icon.addFile(u":/Icons/Gender_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/Icons/Gender_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterGender_Rabbits.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Gender_Null_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/Icons/Gender_Null_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterGender_Rabbits.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Gender_Male_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/Icons/Gender_Male_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterGender_Rabbits.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Gender_Female_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Icons/Gender_Female_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterGender_Rabbits.addItem(icon3, "")
        self.FilterGender_Rabbits.setObjectName(u"FilterGender_Rabbits")
        self.FilterGender_Rabbits.setGeometry(QRect(71, 7, 123, 33))
        self.FilterGender_Rabbits.setMinimumSize(QSize(123, 33))
        self.FilterGender_Rabbits.setMaximumSize(QSize(123, 33))
        self.FilterGender_Rabbits.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid white;\n"
"	border-radius:6px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 12pt \"Acme\";\n"
"	padding-left: 15px;\n"
"	selection-background-color: #2980B9;\n"
"}")
        self.Ordre_Rabbits = QPushButton(self.Filter_Frame_View)
        self.Ordre_Rabbits.setObjectName(u"Ordre_Rabbits")
        self.Ordre_Rabbits.setGeometry(QRect(18, 7, 43, 33))
        self.Ordre_Rabbits.setMinimumSize(QSize(43, 33))
        self.Ordre_Rabbits.setMaximumSize(QSize(43, 33))
        font = QFont()
        font.setFamilies([u"Acme"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.Ordre_Rabbits.setFont(font)
        self.Ordre_Rabbits.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Ordre_Rabbits.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Order_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Order_Mix.png);\n"
"}\n"
"QPushButton:checked:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Order_Mix.png);\n"
"}\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Order_Green.png);\n"
"}\n"
"QPushButton:checked{\n"
"	border-style: outset;\n"
"    	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Order_Green.png);\n"
"}")
        self.Ordre_Rabbits.setIconSize(QSize(20, 20))
        self.Ordre_Rabbits.setCheckable(True)
        self.Ordre_Rabbits.setChecked(True)
        self.Ordre_Rabbits.setAutoRepeat(False)
        self.Ordre_Rabbits.setAutoExclusive(False)
        self.Ordre_Rabbits.setAutoRepeatDelay(50)
        self.Ordre_Rabbits.setAutoRepeatInterval(10)
        self.Search_Rabbits = QLineEdit(self.Filter_Frame_View)
        self.Search_Rabbits.setObjectName(u"Search_Rabbits")
        self.Search_Rabbits.setGeometry(QRect(331, 7, 275, 33))
        self.Search_Rabbits.setMinimumSize(QSize(275, 33))
        self.Search_Rabbits.setMaximumSize(QSize(275, 31))
        self.Search_Rabbits.setStyleSheet(u"QLineEdit {\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	padding-left: 30px;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-image: url(:/Icons/Search.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 10pt \"Acme\";\n"
"}")
        self.FilterBy_Rabbits = QComboBox(self.Filter_Frame_View)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.FilterBy_Rabbits.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Rabbit_Tag.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/Icons/Rabbit_Tag.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon5, "")
        self.FilterBy_Rabbits.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Calendar_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/Icons/Calendar_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/Rabbit_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/Icons/Rabbit_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon7, "")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/Rabbit_Tree_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/Icons/Rabbit_Tree_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon8, "")
        self.FilterBy_Rabbits.addItem(icon8, "")
        self.FilterBy_Rabbits.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/Settings_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/Icons/Settings_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon9, "")
        self.FilterBy_Rabbits.setObjectName(u"FilterBy_Rabbits")
        self.FilterBy_Rabbits.setGeometry(QRect(201, 7, 120, 33))
        self.FilterBy_Rabbits.setMinimumSize(QSize(120, 33))
        self.FilterBy_Rabbits.setMaximumSize(QSize(120, 33))
        self.FilterBy_Rabbits.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid white;\n"
"	border-radius:6px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 12pt \"Acme\";\n"
"	padding-left: 15px;\n"
"	selection-background-color: #2980B9;\n"
"}")
        self.Title = QLabel(self.Background)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(40, 10, 961, 21))
        self.Title.setMinimumSize(QSize(301, 21))
        self.Title.setMaximumSize(QSize(1000, 21))
        self.Title.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";")
        self.Title.setAlignment(Qt.AlignCenter)
        self.Infos_Frame = QFrame(self.Background)
        self.Infos_Frame.setObjectName(u"Infos_Frame")
        self.Infos_Frame.setEnabled(True)
        self.Infos_Frame.setGeometry(QRect(72, 42, 831, 207))
        self.Infos_Frame.setMinimumSize(QSize(831, 207))
        self.Infos_Frame.setMaximumSize(QSize(831, 207))
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
        self.Cage_Gender_Label = QLabel(self.Infos_Frame)
        self.Cage_Gender_Label.setObjectName(u"Cage_Gender_Label")
        self.Cage_Gender_Label.setGeometry(QRect(50, 51, 311, 21))
        self.Cage_Gender_Label.setMinimumSize(QSize(311, 21))
        self.Cage_Gender_Label.setMaximumSize(QSize(311, 21))
        self.Cage_Gender_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";")
        self.Cage_Bought_Label = QLabel(self.Infos_Frame)
        self.Cage_Bought_Label.setObjectName(u"Cage_Bought_Label")
        self.Cage_Bought_Label.setGeometry(QRect(50, 86, 311, 21))
        self.Cage_Bought_Label.setMinimumSize(QSize(311, 21))
        self.Cage_Bought_Label.setMaximumSize(QSize(311, 21))
        self.Cage_Bought_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";\n"
"}")
        self.Cage_Avatar_Frame = QFrame(self.Infos_Frame)
        self.Cage_Avatar_Frame.setObjectName(u"Cage_Avatar_Frame")
        self.Cage_Avatar_Frame.setGeometry(QRect(703, 10, 119, 161))
        self.Cage_Avatar_Frame.setMinimumSize(QSize(119, 161))
        self.Cage_Avatar_Frame.setMaximumSize(QSize(119, 161))
        self.Cage_Avatar_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #D9D9D9;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Cage_Avatar_Frame.setFrameShape(QFrame.StyledPanel)
        self.Cage_Avatar_Frame.setFrameShadow(QFrame.Raised)
        self.Cage_Avatar_Label = QLabel(self.Cage_Avatar_Frame)
        self.Cage_Avatar_Label.setObjectName(u"Cage_Avatar_Label")
        self.Cage_Avatar_Label.setGeometry(QRect(9, 10, 101, 141))
        self.Cage_Avatar_Label.setStyleSheet(u"border:none;")
        self.Cage_Avatar_Label.setPixmap(QPixmap(u":/Icons/Cages_Green.png"))
        self.Cage_Avatar_Label.setScaledContents(False)
        self.Cage_Avatar_Label.setAlignment(Qt.AlignCenter)
        self.Cage_Gender_Icon = QLabel(self.Infos_Frame)
        self.Cage_Gender_Icon.setObjectName(u"Cage_Gender_Icon")
        self.Cage_Gender_Icon.setGeometry(QRect(20, 51, 21, 21))
        self.Cage_Gender_Icon.setMinimumSize(QSize(21, 21))
        self.Cage_Gender_Icon.setMaximumSize(QSize(21, 21))
        self.Cage_Gender_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Cage_Gender_Icon.setPixmap(QPixmap(u":/Icons/Gender_White.png"))
        self.Cage_Gender_Icon.setScaledContents(True)
        self.Cage_Gender_Icon.setAlignment(Qt.AlignCenter)
        self.Cage_Gender_Icon.setWordWrap(False)
        self.Cage_Brought_Icon = QLabel(self.Infos_Frame)
        self.Cage_Brought_Icon.setObjectName(u"Cage_Brought_Icon")
        self.Cage_Brought_Icon.setGeometry(QRect(20, 86, 21, 21))
        self.Cage_Brought_Icon.setMinimumSize(QSize(21, 21))
        self.Cage_Brought_Icon.setMaximumSize(QSize(21, 21))
        self.Cage_Brought_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Cage_Brought_Icon.setPixmap(QPixmap(u":/Icons/TND_White.png"))
        self.Cage_Brought_Icon.setScaledContents(True)
        self.Cage_Brought_Icon.setAlignment(Qt.AlignCenter)
        self.Cage_Notes_PleinText = QPlainTextEdit(self.Infos_Frame)
        self.Cage_Notes_PleinText.setObjectName(u"Cage_Notes_PleinText")
        self.Cage_Notes_PleinText.setGeometry(QRect(445, 10, 251, 187))
        self.Cage_Notes_PleinText.setMinimumSize(QSize(251, 187))
        self.Cage_Notes_PleinText.setMaximumSize(QSize(251, 187))
        self.Cage_Notes_PleinText.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.UpArrowCursor))
        self.Cage_Notes_PleinText.setStyleSheet(u"QPlainTextEdit{\n"
"	background-color: rgb(69, 69, 69);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Cage_Notes_PleinText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Cage_Notes_PleinText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Cage_Notes_PleinText.setReadOnly(True)
        self.Notes_Label_Frame = QFrame(self.Infos_Frame)
        self.Notes_Label_Frame.setObjectName(u"Notes_Label_Frame")
        self.Notes_Label_Frame.setGeometry(QRect(400, 38, 41, 131))
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
        self.Selled_Frame = QFrame(self.Infos_Frame)
        self.Selled_Frame.setObjectName(u"Selled_Frame")
        self.Selled_Frame.setEnabled(True)
        self.Selled_Frame.setGeometry(QRect(5, 110, 391, 91))
        self.Selled_Frame.setMinimumSize(QSize(158, 44))
        self.Selled_Frame.setMaximumSize(QSize(5454645, 654664))
        self.Selled_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #2F2F2F;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Selled_Frame.setFrameShape(QFrame.StyledPanel)
        self.Selled_Frame.setFrameShadow(QFrame.Raised)
        self.Cage_Facture_Label = QLabel(self.Selled_Frame)
        self.Cage_Facture_Label.setObjectName(u"Cage_Facture_Label")
        self.Cage_Facture_Label.setGeometry(QRect(50, 20, 190, 21))
        self.Cage_Facture_Label.setMinimumSize(QSize(190, 21))
        self.Cage_Facture_Label.setMaximumSize(QSize(190, 21))
        self.Cage_Facture_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";\n"
"}")
        self.Cage_Facture_Icon = QLabel(self.Selled_Frame)
        self.Cage_Facture_Icon.setObjectName(u"Cage_Facture_Icon")
        self.Cage_Facture_Icon.setGeometry(QRect(20, 20, 21, 21))
        self.Cage_Facture_Icon.setMinimumSize(QSize(21, 21))
        self.Cage_Facture_Icon.setMaximumSize(QSize(21, 21))
        self.Cage_Facture_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Cage_Facture_Icon.setPixmap(QPixmap(u":/Icons/Facture_White.png"))
        self.Cage_Facture_Icon.setScaledContents(True)
        self.Cage_Facture_Icon.setAlignment(Qt.AlignCenter)
        self.Cage_Customer_Label = QLabel(self.Selled_Frame)
        self.Cage_Customer_Label.setObjectName(u"Cage_Customer_Label")
        self.Cage_Customer_Label.setGeometry(QRect(50, 50, 190, 21))
        self.Cage_Customer_Label.setMinimumSize(QSize(190, 21))
        self.Cage_Customer_Label.setMaximumSize(QSize(190, 21))
        self.Cage_Customer_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";\n"
"}")
        self.Cage_Customer_Label.setScaledContents(True)
        self.Cage_Customer_Label.setWordWrap(False)
        self.Cage_Customer_Icon = QLabel(self.Selled_Frame)
        self.Cage_Customer_Icon.setObjectName(u"Cage_Customer_Icon")
        self.Cage_Customer_Icon.setGeometry(QRect(20, 50, 21, 21))
        self.Cage_Customer_Icon.setMinimumSize(QSize(21, 21))
        self.Cage_Customer_Icon.setMaximumSize(QSize(21, 21))
        self.Cage_Customer_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Cage_Customer_Icon.setPixmap(QPixmap(u":/Icons/Customer_Whitre.png"))
        self.Cage_Customer_Icon.setScaledContents(True)
        self.Cage_Customer_Icon.setAlignment(Qt.AlignCenter)
        self.Cage_Sold_Icon = QLabel(self.Selled_Frame)
        self.Cage_Sold_Icon.setObjectName(u"Cage_Sold_Icon")
        self.Cage_Sold_Icon.setGeometry(QRect(260, 20, 21, 21))
        self.Cage_Sold_Icon.setMinimumSize(QSize(21, 21))
        self.Cage_Sold_Icon.setMaximumSize(QSize(21, 21))
        self.Cage_Sold_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Cage_Sold_Icon.setPixmap(QPixmap(u":/Icons/TND_White.png"))
        self.Cage_Sold_Icon.setScaledContents(True)
        self.Cage_Sold_Icon.setAlignment(Qt.AlignCenter)
        self.Cage_Sold_Text = QLabel(self.Selled_Frame)
        self.Cage_Sold_Text.setObjectName(u"Cage_Sold_Text")
        self.Cage_Sold_Text.setGeometry(QRect(290, 20, 50, 21))
        self.Cage_Sold_Text.setMinimumSize(QSize(50, 21))
        self.Cage_Sold_Text.setMaximumSize(QSize(50, 21))
        self.Cage_Sold_Text.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";\n"
"}")
        self.Cage_Sold_Label = QLabel(self.Selled_Frame)
        self.Cage_Sold_Label.setObjectName(u"Cage_Sold_Label")
        self.Cage_Sold_Label.setGeometry(QRect(260, 50, 111, 31))
        self.Cage_Sold_Label.setMinimumSize(QSize(50, 21))
        self.Cage_Sold_Label.setMaximumSize(QSize(565, 645645))
        self.Cage_Sold_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";\n"
"}")
        self.Cage_Sold_Label.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.Selled_Frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(245, 0, 2, 91))
        self.line.setMinimumSize(QSize(2, 91))
        self.line.setMaximumSize(QSize(2, 91))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.Activity_Frame = QFrame(self.Background)
        self.Activity_Frame.setObjectName(u"Activity_Frame")
        self.Activity_Frame.setGeometry(QRect(913, 42, 46, 207))
        self.Activity_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(48, 48, 48);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Activity_Frame.setFrameShape(QFrame.StyledPanel)
        self.Activity_Frame.setFrameShadow(QFrame.Raised)
        self.Exit_Cage_View = QPushButton(self.Activity_Frame)
        self.Exit_Cage_View.setObjectName(u"Exit_Cage_View")
        self.Exit_Cage_View.setEnabled(True)
        self.Exit_Cage_View.setGeometry(QRect(7, 20, 33, 33))
        self.Exit_Cage_View.setMinimumSize(QSize(33, 33))
        self.Exit_Cage_View.setMaximumSize(QSize(33, 33))
        font1 = QFont()
        font1.setFamilies([u"Orbitron"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.Exit_Cage_View.setFont(font1)
        self.Exit_Cage_View.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Exit_Cage_View.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Exit_Red.png);\n"
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
"	image: url(:/Icons/Exit_White.png);\n"
"}")
        self.Exit_Cage_View.setIconSize(QSize(20, 20))
        self.Exit_Cage_View.setCheckable(False)
        self.Exit_Cage_View.setAutoRepeat(False)
        self.Exit_Cage_View.setAutoExclusive(False)
        self.Exit_Cage_View.setAutoRepeatDelay(50)
        self.Exit_Cage_View.setAutoRepeatInterval(10)
        self.Edit_Cage = QPushButton(self.Activity_Frame)
        self.Edit_Cage.setObjectName(u"Edit_Cage")
        self.Edit_Cage.setEnabled(True)
        self.Edit_Cage.setGeometry(QRect(7, 83, 33, 33))
        self.Edit_Cage.setMinimumSize(QSize(33, 33))
        self.Edit_Cage.setMaximumSize(QSize(33, 33))
        self.Edit_Cage.setFont(font1)
        self.Edit_Cage.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Edit_Cage.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Edit_Blue.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Edit_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Edit_White.png);\n"
"}")
        self.Edit_Cage.setIconSize(QSize(20, 20))
        self.Edit_Cage.setCheckable(False)
        self.Edit_Cage.setAutoRepeat(False)
        self.Edit_Cage.setAutoExclusive(False)
        self.Edit_Cage.setAutoRepeatDelay(50)
        self.Edit_Cage.setAutoRepeatInterval(10)
        self.Delete_Cage = QPushButton(self.Activity_Frame)
        self.Delete_Cage.setObjectName(u"Delete_Cage")
        self.Delete_Cage.setEnabled(True)
        self.Delete_Cage.setGeometry(QRect(7, 146, 33, 33))
        self.Delete_Cage.setMinimumSize(QSize(33, 33))
        self.Delete_Cage.setMaximumSize(QSize(33, 33))
        self.Delete_Cage.setFont(font1)
        self.Delete_Cage.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Delete_Cage.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Delete_Pink.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Delete_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Delete_White.png);\n"
"}")
        self.Delete_Cage.setIconSize(QSize(20, 20))
        self.Delete_Cage.setCheckable(False)
        self.Delete_Cage.setAutoRepeat(False)
        self.Delete_Cage.setAutoExclusive(False)
        self.Delete_Cage.setAutoRepeatDelay(50)
        self.Delete_Cage.setAutoRepeatInterval(10)

        self.retranslateUi(Cage_View_Main)
        self.Exit_Cage_View.clicked.connect(Cage_View_Main.close)

        QMetaObject.connectSlotsByName(Cage_View_Main)
    # setupUi

    def retranslateUi(self, Cage_View_Main):
        Cage_View_Main.setWindowTitle(QCoreApplication.translate("Cage_View_Main", u"Dialog", None))
        self.Rabbit_Label.setText(QCoreApplication.translate("Cage_View_Main", u"Rabbits", None))
        self.FilterGender_Rabbits.setItemText(0, QCoreApplication.translate("Cage_View_Main", u"Gender", None))
        self.FilterGender_Rabbits.setItemText(1, QCoreApplication.translate("Cage_View_Main", u"Null", None))
        self.FilterGender_Rabbits.setItemText(2, QCoreApplication.translate("Cage_View_Main", u"Male", None))
        self.FilterGender_Rabbits.setItemText(3, QCoreApplication.translate("Cage_View_Main", u"Female", None))

        self.Ordre_Rabbits.setText("")
        self.Search_Rabbits.setInputMask("")
        self.Search_Rabbits.setText("")
        self.Search_Rabbits.setPlaceholderText(QCoreApplication.translate("Cage_View_Main", u"Search Rabbit...", None))
        self.FilterBy_Rabbits.setItemText(0, QCoreApplication.translate("Cage_View_Main", u"By", None))
        self.FilterBy_Rabbits.setItemText(1, QCoreApplication.translate("Cage_View_Main", u"ID", None))
        self.FilterBy_Rabbits.setItemText(2, QCoreApplication.translate("Cage_View_Main", u"Breed", None))
        self.FilterBy_Rabbits.setItemText(3, QCoreApplication.translate("Cage_View_Main", u"Born", None))
        self.FilterBy_Rabbits.setItemText(4, QCoreApplication.translate("Cage_View_Main", u"Color", None))
        self.FilterBy_Rabbits.setItemText(5, QCoreApplication.translate("Cage_View_Main", u"Mother", None))
        self.FilterBy_Rabbits.setItemText(6, QCoreApplication.translate("Cage_View_Main", u"Father", None))
        self.FilterBy_Rabbits.setItemText(7, QCoreApplication.translate("Cage_View_Main", u"Generation", None))
        self.FilterBy_Rabbits.setItemText(8, QCoreApplication.translate("Cage_View_Main", u"Type", None))

        self.Title.setText(QCoreApplication.translate("Cage_View_Main", u"Cage Viewer Window", None))
        self.ID_Label.setText(QCoreApplication.translate("Cage_View_Main", u"ID : ", None))
        self.Cage_Gender_Label.setText(QCoreApplication.translate("Cage_View_Main", u"Gender", None))
        self.Cage_Bought_Label.setText(QCoreApplication.translate("Cage_View_Main", u"Bought", None))
        self.Cage_Avatar_Label.setText("")
        self.Cage_Gender_Icon.setText("")
        self.Cage_Brought_Icon.setText("")
        self.Notes_Text_Label.setText(QCoreApplication.translate("Cage_View_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">N</span></p></body></html>", None))
        self.Notes_Text_Label_2.setText(QCoreApplication.translate("Cage_View_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">O</span></p></body></html>", None))
        self.Notes_Text_Label_3.setText(QCoreApplication.translate("Cage_View_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">T</span></p></body></html>", None))
        self.Notes_Text_Label_4.setText(QCoreApplication.translate("Cage_View_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">E</span></p></body></html>", None))
        self.Notes_Text_Label_5.setText(QCoreApplication.translate("Cage_View_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">S</span></p></body></html>", None))
        self.Cage_Facture_Label.setText(QCoreApplication.translate("Cage_View_Main", u"Facture", None))
        self.Cage_Facture_Icon.setText("")
        self.Cage_Customer_Label.setText(QCoreApplication.translate("Cage_View_Main", u"Customer", None))
        self.Cage_Customer_Icon.setText("")
        self.Cage_Sold_Icon.setText("")
        self.Cage_Sold_Text.setText(QCoreApplication.translate("Cage_View_Main", u"Sold", None))
        self.Cage_Sold_Label.setText("")
        self.Exit_Cage_View.setText("")
#if QT_CONFIG(shortcut)
        self.Exit_Cage_View.setShortcut(QCoreApplication.translate("Cage_View_Main", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.Edit_Cage.setText("")
        self.Delete_Cage.setText("")
#if QT_CONFIG(shortcut)
        self.Delete_Cage.setShortcut(QCoreApplication.translate("Cage_View_Main", u"Del", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

