# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainViewFacture.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QWidget)
import resources_rc

class Ui_Facture_View_Main(object):
    def setupUi(self, Facture_View_Main):
        if not Facture_View_Main.objectName():
            Facture_View_Main.setObjectName(u"Facture_View_Main")
        Facture_View_Main.resize(1031, 867)
        Facture_View_Main.setMinimumSize(QSize(1031, 867))
        Facture_View_Main.setMaximumSize(QSize(1031, 867))
        Facture_View_Main.setStyleSheet(u"")
        self.Infos_Frame = QFrame(Facture_View_Main)
        self.Infos_Frame.setObjectName(u"Infos_Frame")
        self.Infos_Frame.setEnabled(True)
        self.Infos_Frame.setGeometry(QRect(588, 42, 361, 207))
        self.Infos_Frame.setMinimumSize(QSize(361, 207))
        self.Infos_Frame.setMaximumSize(QSize(361, 207))
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
        self.Customer_Name_Label = QLabel(self.Infos_Frame)
        self.Customer_Name_Label.setObjectName(u"Customer_Name_Label")
        self.Customer_Name_Label.setGeometry(QRect(50, 51, 301, 21))
        self.Customer_Name_Label.setMinimumSize(QSize(301, 21))
        self.Customer_Name_Label.setMaximumSize(QSize(301, 21))
        self.Customer_Name_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";")
        self.Customer_Phone_Label = QLabel(self.Infos_Frame)
        self.Customer_Phone_Label.setObjectName(u"Customer_Phone_Label")
        self.Customer_Phone_Label.setGeometry(QRect(50, 86, 301, 21))
        self.Customer_Phone_Label.setMinimumSize(QSize(301, 21))
        self.Customer_Phone_Label.setMaximumSize(QSize(301, 21))
        self.Customer_Phone_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";\n"
"}")
        self.Customer_Gender_Label = QLabel(self.Infos_Frame)
        self.Customer_Gender_Label.setObjectName(u"Customer_Gender_Label")
        self.Customer_Gender_Label.setGeometry(QRect(50, 121, 301, 21))
        self.Customer_Gender_Label.setMinimumSize(QSize(301, 21))
        self.Customer_Gender_Label.setMaximumSize(QSize(301, 21))
        self.Customer_Gender_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";\n"
"}")
        self.Customer_Address_Label = QLabel(self.Infos_Frame)
        self.Customer_Address_Label.setObjectName(u"Customer_Address_Label")
        self.Customer_Address_Label.setGeometry(QRect(50, 159, 301, 21))
        self.Customer_Address_Label.setMinimumSize(QSize(301, 21))
        self.Customer_Address_Label.setMaximumSize(QSize(230, 21))
        self.Customer_Address_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";\n"
"}")
        self.Customer_Address_Label.setScaledContents(True)
        self.Customer_Address_Label.setWordWrap(False)
        self.Customer_Name_Icon = QLabel(self.Infos_Frame)
        self.Customer_Name_Icon.setObjectName(u"Customer_Name_Icon")
        self.Customer_Name_Icon.setGeometry(QRect(20, 51, 21, 21))
        self.Customer_Name_Icon.setMinimumSize(QSize(21, 21))
        self.Customer_Name_Icon.setMaximumSize(QSize(21, 21))
        self.Customer_Name_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Customer_Name_Icon.setPixmap(QPixmap(u":/Icons/Customer_Whitre.png"))
        self.Customer_Name_Icon.setScaledContents(True)
        self.Customer_Name_Icon.setAlignment(Qt.AlignCenter)
        self.Customer_Name_Icon.setWordWrap(False)
        self.Customer_Phone_Icon = QLabel(self.Infos_Frame)
        self.Customer_Phone_Icon.setObjectName(u"Customer_Phone_Icon")
        self.Customer_Phone_Icon.setGeometry(QRect(20, 86, 21, 21))
        self.Customer_Phone_Icon.setMinimumSize(QSize(21, 21))
        self.Customer_Phone_Icon.setMaximumSize(QSize(21, 21))
        self.Customer_Phone_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Customer_Phone_Icon.setPixmap(QPixmap(u":/Icons/Phone_White.png"))
        self.Customer_Phone_Icon.setScaledContents(True)
        self.Customer_Phone_Icon.setAlignment(Qt.AlignCenter)
        self.Customer_Gender_Icon = QLabel(self.Infos_Frame)
        self.Customer_Gender_Icon.setObjectName(u"Customer_Gender_Icon")
        self.Customer_Gender_Icon.setGeometry(QRect(20, 121, 21, 21))
        self.Customer_Gender_Icon.setMinimumSize(QSize(21, 21))
        self.Customer_Gender_Icon.setMaximumSize(QSize(21, 21))
        self.Customer_Gender_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Customer_Gender_Icon.setPixmap(QPixmap(u":/Icons/Gender_White.png"))
        self.Customer_Gender_Icon.setScaledContents(True)
        self.Customer_Gender_Icon.setAlignment(Qt.AlignCenter)
        self.Customer_Address_Icon = QLabel(self.Infos_Frame)
        self.Customer_Address_Icon.setObjectName(u"Customer_Address_Icon")
        self.Customer_Address_Icon.setGeometry(QRect(20, 159, 21, 21))
        self.Customer_Address_Icon.setMinimumSize(QSize(21, 21))
        self.Customer_Address_Icon.setMaximumSize(QSize(21, 21))
        self.Customer_Address_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Customer_Address_Icon.setPixmap(QPixmap(u":/Icons/Address_White.png"))
        self.Customer_Address_Icon.setScaledContents(True)
        self.Customer_Address_Icon.setAlignment(Qt.AlignCenter)
        self.Customer_ID_Frame = QFrame(self.Infos_Frame)
        self.Customer_ID_Frame.setObjectName(u"Customer_ID_Frame")
        self.Customer_ID_Frame.setEnabled(True)
        self.Customer_ID_Frame.setGeometry(QRect(0, 0, 120, 44))
        self.Customer_ID_Frame.setMinimumSize(QSize(120, 44))
        self.Customer_ID_Frame.setMaximumSize(QSize(120, 44))
        self.Customer_ID_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #2F2F2F;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Customer_ID_Frame.setFrameShape(QFrame.StyledPanel)
        self.Customer_ID_Frame.setFrameShadow(QFrame.Raised)
        self.Customer_ID_Label = QLabel(self.Customer_ID_Frame)
        self.Customer_ID_Label.setObjectName(u"Customer_ID_Label")
        self.Customer_ID_Label.setGeometry(QRect(10, 6, 100, 31))
        self.Customer_ID_Label.setMinimumSize(QSize(100, 31))
        self.Customer_ID_Label.setMaximumSize(QSize(100, 31))
        self.Customer_ID_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";\n"
"}")
        self.Activity_Frame = QFrame(Facture_View_Main)
        self.Activity_Frame.setObjectName(u"Activity_Frame")
        self.Activity_Frame.setGeometry(QRect(957, 40, 46, 207))
        self.Activity_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(48, 48, 48);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Activity_Frame.setFrameShape(QFrame.StyledPanel)
        self.Activity_Frame.setFrameShadow(QFrame.Raised)
        self.Exit_Customer_View = QPushButton(self.Activity_Frame)
        self.Exit_Customer_View.setObjectName(u"Exit_Customer_View")
        self.Exit_Customer_View.setEnabled(True)
        self.Exit_Customer_View.setGeometry(QRect(7, 35, 33, 33))
        self.Exit_Customer_View.setMinimumSize(QSize(33, 33))
        self.Exit_Customer_View.setMaximumSize(QSize(33, 33))
        font = QFont()
        font.setFamilies([u"Orbitron"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.Exit_Customer_View.setFont(font)
        self.Exit_Customer_View.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Exit_Customer_View.setStyleSheet(u"QPushButton {\n"
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
        self.Exit_Customer_View.setIconSize(QSize(20, 20))
        self.Exit_Customer_View.setCheckable(False)
        self.Exit_Customer_View.setAutoRepeat(False)
        self.Exit_Customer_View.setAutoExclusive(False)
        self.Exit_Customer_View.setAutoRepeatDelay(50)
        self.Exit_Customer_View.setAutoRepeatInterval(10)
        self.Delete_Facture = QPushButton(self.Activity_Frame)
        self.Delete_Facture.setObjectName(u"Delete_Facture")
        self.Delete_Facture.setEnabled(True)
        self.Delete_Facture.setGeometry(QRect(7, 139, 33, 33))
        self.Delete_Facture.setMinimumSize(QSize(33, 33))
        self.Delete_Facture.setMaximumSize(QSize(33, 33))
        self.Delete_Facture.setFont(font)
        self.Delete_Facture.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Delete_Facture.setStyleSheet(u"QPushButton {\n"
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
        self.Delete_Facture.setIconSize(QSize(20, 20))
        self.Delete_Facture.setCheckable(False)
        self.Delete_Facture.setAutoRepeat(False)
        self.Delete_Facture.setAutoExclusive(False)
        self.Delete_Facture.setAutoRepeatDelay(50)
        self.Delete_Facture.setAutoRepeatInterval(10)
        self.Background = QFrame(Facture_View_Main)
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
        self.Facture_A4_Frame = QFrame(self.Background)
        self.Facture_A4_Frame.setObjectName(u"Facture_A4_Frame")
        self.Facture_A4_Frame.setGeometry(QRect(20, 42, 556, 787))
        self.Facture_A4_Frame.setMinimumSize(QSize(556, 787))
        self.Facture_A4_Frame.setMaximumSize(QSize(556, 787))
        self.Facture_A4_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Facture_A4_Frame.setFrameShape(QFrame.StyledPanel)
        self.Facture_A4_Frame.setFrameShadow(QFrame.Raised)
        self.Facture_Label = QLabel(self.Facture_A4_Frame)
        self.Facture_Label.setObjectName(u"Facture_Label")
        self.Facture_Label.setGeometry(QRect(10, 10, 536, 767))
        self.Facture_Label.setMinimumSize(QSize(536, 767))
        self.Facture_Label.setMaximumSize(QSize(536, 767))
        self.Facture_Label.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: none;\n"
"}")
        self.Facture_Label.setAlignment(Qt.AlignCenter)
        self.ID_Frame = QFrame(self.Facture_A4_Frame)
        self.ID_Frame.setObjectName(u"ID_Frame")
        self.ID_Frame.setEnabled(True)
        self.ID_Frame.setGeometry(QRect(0, 0, 120, 44))
        self.ID_Frame.setMinimumSize(QSize(120, 44))
        self.ID_Frame.setMaximumSize(QSize(120, 44))
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
        self.ID_Label.setGeometry(QRect(15, 6, 100, 31))
        self.ID_Label.setMinimumSize(QSize(100, 31))
        self.ID_Label.setMaximumSize(QSize(100, 31))
        self.ID_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";\n"
"}")
        self.Facture_Rabbits_Frame = QFrame(self.Background)
        self.Facture_Rabbits_Frame.setObjectName(u"Facture_Rabbits_Frame")
        self.Facture_Rabbits_Frame.setGeometry(QRect(594, 264, 193, 565))
        self.Facture_Rabbits_Frame.setMinimumSize(QSize(193, 565))
        self.Facture_Rabbits_Frame.setMaximumSize(QSize(193, 565))
        self.Facture_Rabbits_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Facture_Rabbits_Frame.setFrameShape(QFrame.StyledPanel)
        self.Facture_Rabbits_Frame.setFrameShadow(QFrame.Raised)
        self.RabbitsLabel_Frame = QFrame(self.Facture_Rabbits_Frame)
        self.RabbitsLabel_Frame.setObjectName(u"RabbitsLabel_Frame")
        self.RabbitsLabel_Frame.setEnabled(True)
        self.RabbitsLabel_Frame.setGeometry(QRect(36, 0, 120, 44))
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
        self.Facture_Rabbits_ScrollArea = QScrollArea(self.Facture_Rabbits_Frame)
        self.Facture_Rabbits_ScrollArea.setObjectName(u"Facture_Rabbits_ScrollArea")
        self.Facture_Rabbits_ScrollArea.setGeometry(QRect(11, 62, 171, 481))
        self.Facture_Rabbits_ScrollArea.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: none;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Facture_Rabbits_ScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Facture_Rabbits_ScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Facture_Rabbits_ScrollArea.setWidgetResizable(True)
        self.Facture_Rabbits_ScrollArea_Widget = QWidget()
        self.Facture_Rabbits_ScrollArea_Widget.setObjectName(u"Facture_Rabbits_ScrollArea_Widget")
        self.Facture_Rabbits_ScrollArea_Widget.setGeometry(QRect(0, 0, 171, 481))
        self.gridLayoutWidget = QWidget(self.Facture_Rabbits_ScrollArea_Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(5, 0, 161, 481))
        self.GridRabbits_ScrollArea = QGridLayout(self.gridLayoutWidget)
        self.GridRabbits_ScrollArea.setObjectName(u"GridRabbits_ScrollArea")
        self.GridRabbits_ScrollArea.setContentsMargins(0, 0, 0, 0)
        self.Facture_Rabbits_ScrollArea.setWidget(self.Facture_Rabbits_ScrollArea_Widget)
        self.Facture_Cages_Frame = QFrame(self.Background)
        self.Facture_Cages_Frame.setObjectName(u"Facture_Cages_Frame")
        self.Facture_Cages_Frame.setGeometry(QRect(802, 264, 193, 565))
        self.Facture_Cages_Frame.setMinimumSize(QSize(193, 565))
        self.Facture_Cages_Frame.setMaximumSize(QSize(193, 565))
        self.Facture_Cages_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Facture_Cages_Frame.setFrameShape(QFrame.StyledPanel)
        self.Facture_Cages_Frame.setFrameShadow(QFrame.Raised)
        self.CagesLabel_Frame = QFrame(self.Facture_Cages_Frame)
        self.CagesLabel_Frame.setObjectName(u"CagesLabel_Frame")
        self.CagesLabel_Frame.setEnabled(True)
        self.CagesLabel_Frame.setGeometry(QRect(36, 0, 120, 44))
        self.CagesLabel_Frame.setMinimumSize(QSize(120, 44))
        self.CagesLabel_Frame.setMaximumSize(QSize(120, 44))
        self.CagesLabel_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #2F2F2F;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.CagesLabel_Frame.setFrameShape(QFrame.StyledPanel)
        self.CagesLabel_Frame.setFrameShadow(QFrame.Raised)
        self.CagesLabel = QLabel(self.CagesLabel_Frame)
        self.CagesLabel.setObjectName(u"CagesLabel")
        self.CagesLabel.setGeometry(QRect(10, 6, 100, 31))
        self.CagesLabel.setMinimumSize(QSize(100, 31))
        self.CagesLabel.setMaximumSize(QSize(100, 31))
        self.CagesLabel.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";\n"
"}")
        self.CagesLabel.setAlignment(Qt.AlignCenter)
        self.Facture_Cages_ScrollArea = QScrollArea(self.Facture_Cages_Frame)
        self.Facture_Cages_ScrollArea.setObjectName(u"Facture_Cages_ScrollArea")
        self.Facture_Cages_ScrollArea.setGeometry(QRect(11, 62, 171, 481))
        self.Facture_Cages_ScrollArea.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: none;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Facture_Cages_ScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Facture_Cages_ScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Facture_Cages_ScrollArea.setWidgetResizable(True)
        self.Facture_Cages_ScrollArea_Widget = QWidget()
        self.Facture_Cages_ScrollArea_Widget.setObjectName(u"Facture_Cages_ScrollArea_Widget")
        self.Facture_Cages_ScrollArea_Widget.setGeometry(QRect(0, 0, 171, 481))
        self.gridLayoutWidget_2 = QWidget(self.Facture_Cages_ScrollArea_Widget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(8, 0, 161, 481))
        self.GridCages_ScrollArea = QGridLayout(self.gridLayoutWidget_2)
        self.GridCages_ScrollArea.setObjectName(u"GridCages_ScrollArea")
        self.GridCages_ScrollArea.setContentsMargins(0, 0, 0, 0)
        self.Facture_Cages_ScrollArea.setWidget(self.Facture_Cages_ScrollArea_Widget)
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
        self.Background.raise_()
        self.Infos_Frame.raise_()
        self.Activity_Frame.raise_()

        self.retranslateUi(Facture_View_Main)
        self.Exit_Customer_View.clicked.connect(Facture_View_Main.close)

        QMetaObject.connectSlotsByName(Facture_View_Main)
    # setupUi

    def retranslateUi(self, Facture_View_Main):
        Facture_View_Main.setWindowTitle(QCoreApplication.translate("Facture_View_Main", u"Dialog", None))
        self.Customer_Name_Label.setText("")
        self.Customer_Phone_Label.setText("")
        self.Customer_Gender_Label.setText("")
        self.Customer_Address_Label.setText("")
        self.Customer_Name_Icon.setText("")
        self.Customer_Phone_Icon.setText("")
        self.Customer_Gender_Icon.setText("")
        self.Customer_Address_Icon.setText("")
        self.Customer_ID_Label.setText(QCoreApplication.translate("Facture_View_Main", u"ID :", None))
        self.Exit_Customer_View.setText("")
#if QT_CONFIG(shortcut)
        self.Exit_Customer_View.setShortcut(QCoreApplication.translate("Facture_View_Main", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.Delete_Facture.setText("")
#if QT_CONFIG(shortcut)
        self.Delete_Facture.setShortcut(QCoreApplication.translate("Facture_View_Main", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.Facture_Label.setText("")
        self.ID_Label.setText(QCoreApplication.translate("Facture_View_Main", u"ID : ", None))
        self.Rabbit_Label.setText(QCoreApplication.translate("Facture_View_Main", u"Rabbits", None))
        self.CagesLabel.setText(QCoreApplication.translate("Facture_View_Main", u"Cages", None))
        self.Title.setText(QCoreApplication.translate("Facture_View_Main", u"Facture Viewer Window", None))
    # retranslateUi

