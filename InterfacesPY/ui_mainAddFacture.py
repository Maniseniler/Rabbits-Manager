# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainAddFacture.ui'
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
    QDoubleSpinBox, QFrame, QGridLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QStackedWidget, QTextEdit, QWidget)
import resources_rc

class Ui_Facture_Add_Main(object):
    def setupUi(self, Facture_Add_Main):
        if not Facture_Add_Main.objectName():
            Facture_Add_Main.setObjectName(u"Facture_Add_Main")
        Facture_Add_Main.resize(1031, 867)
        Facture_Add_Main.setMinimumSize(QSize(1031, 867))
        Facture_Add_Main.setMaximumSize(QSize(1031, 867))
        Facture_Add_Main.setStyleSheet(u"")
        self.Background = QFrame(Facture_Add_Main)
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
        self.Sell_Windows = QStackedWidget(self.Background)
        self.Sell_Windows.setObjectName(u"Sell_Windows")
        self.Sell_Windows.setGeometry(QRect(10, 50, 1011, 771))
        self.Choose_Customer = QWidget()
        self.Choose_Customer.setObjectName(u"Choose_Customer")
        self.Add_Customer_View = QPushButton(self.Choose_Customer)
        self.Add_Customer_View.setObjectName(u"Add_Customer_View")
        self.Add_Customer_View.setEnabled(True)
        self.Add_Customer_View.setGeometry(QRect(67, 28, 43, 33))
        self.Add_Customer_View.setMinimumSize(QSize(43, 33))
        self.Add_Customer_View.setMaximumSize(QSize(43, 33))
        font = QFont()
        font.setFamilies([u"Orbitron"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.Add_Customer_View.setFont(font)
        self.Add_Customer_View.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Add_Customer_View.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Add_Customer_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Add_Customer_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Add_Customer_Green.png);\n"
"}")
        self.Add_Customer_View.setIconSize(QSize(20, 20))
        self.Add_Customer_View.setCheckable(False)
        self.Add_Customer_View.setAutoRepeat(False)
        self.Add_Customer_View.setAutoExclusive(False)
        self.Add_Customer_View.setAutoRepeatDelay(50)
        self.Add_Customer_View.setAutoRepeatInterval(10)
        self.Filter_Frame_View = QFrame(self.Choose_Customer)
        self.Filter_Frame_View.setObjectName(u"Filter_Frame_View")
        self.Filter_Frame_View.setGeometry(QRect(360, 20, 620, 47))
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
        self.FilterBy_Customer = QComboBox(self.Filter_Frame_View)
        icon = QIcon()
        icon.addFile(u":/Icons/Search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.FilterBy_Customer.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Customer_Whitre.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/Icons/Customer_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Customer.addItem(icon1, "")
        self.FilterBy_Customer.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Phone_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/Icons/Phone_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Customer.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Address_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Icons/Address_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Customer.addItem(icon3, "")
        self.FilterBy_Customer.setObjectName(u"FilterBy_Customer")
        self.FilterBy_Customer.setGeometry(QRect(201, 7, 120, 33))
        self.FilterBy_Customer.setMinimumSize(QSize(120, 33))
        self.FilterBy_Customer.setMaximumSize(QSize(120, 33))
        self.FilterBy_Customer.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid white;\n"
"	border-radius:6px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 12pt \"Acme\";\n"
"	padding-left: 15px;\n"
"	selection-background-color: #2980B9;\n"
"}")
        self.FilterGender_Customer = QComboBox(self.Filter_Frame_View)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Gender_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/Icons/Gender_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterGender_Customer.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Gender_Null_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/Icons/Gender_Null_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterGender_Customer.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Gender_Male_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/Icons/Gender_Male_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterGender_Customer.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/Gender_Female_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/Icons/Gender_Female_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterGender_Customer.addItem(icon7, "")
        self.FilterGender_Customer.setObjectName(u"FilterGender_Customer")
        self.FilterGender_Customer.setGeometry(QRect(71, 7, 123, 33))
        self.FilterGender_Customer.setMinimumSize(QSize(123, 33))
        self.FilterGender_Customer.setMaximumSize(QSize(123, 33))
        self.FilterGender_Customer.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid white;\n"
"	border-radius:6px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 12pt \"Acme\";\n"
"	padding-left: 15px;\n"
"	selection-background-color: #2980B9;\n"
"}")
        self.Ordre_Customer = QPushButton(self.Filter_Frame_View)
        self.Ordre_Customer.setObjectName(u"Ordre_Customer")
        self.Ordre_Customer.setGeometry(QRect(18, 7, 43, 33))
        self.Ordre_Customer.setMinimumSize(QSize(43, 33))
        self.Ordre_Customer.setMaximumSize(QSize(43, 33))
        self.Ordre_Customer.setFont(font)
        self.Ordre_Customer.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Ordre_Customer.setStyleSheet(u"QPushButton {\n"
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
        self.Ordre_Customer.setIconSize(QSize(20, 20))
        self.Ordre_Customer.setCheckable(True)
        self.Ordre_Customer.setChecked(False)
        self.Ordre_Customer.setAutoRepeat(False)
        self.Ordre_Customer.setAutoExclusive(False)
        self.Ordre_Customer.setAutoRepeatDelay(50)
        self.Ordre_Customer.setAutoRepeatInterval(10)
        self.Search_Customer = QLineEdit(self.Filter_Frame_View)
        self.Search_Customer.setObjectName(u"Search_Customer")
        self.Search_Customer.setGeometry(QRect(331, 7, 275, 33))
        self.Search_Customer.setMinimumSize(QSize(275, 33))
        self.Search_Customer.setMaximumSize(QSize(275, 31))
        self.Search_Customer.setStyleSheet(u"QLineEdit {\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	padding-left: 30px;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-image: url(:/Icons/Search.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 10pt \"Acme\";\n"
"}")
        self.View_Customers_Frame = QFrame(self.Choose_Customer)
        self.View_Customers_Frame.setObjectName(u"View_Customers_Frame")
        self.View_Customers_Frame.setEnabled(True)
        self.View_Customers_Frame.setGeometry(QRect(67, 90, 913, 580))
        self.View_Customers_Frame.setMinimumSize(QSize(913, 580))
        self.View_Customers_Frame.setMaximumSize(QSize(913, 580))
        self.View_Customers_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.View_Customers_Frame.setFrameShape(QFrame.Box)
        self.View_Customers_Frame.setFrameShadow(QFrame.Plain)
        self.Scroll_Customers_Area_View = QScrollArea(self.View_Customers_Frame)
        self.Scroll_Customers_Area_View.setObjectName(u"Scroll_Customers_Area_View")
        self.Scroll_Customers_Area_View.setGeometry(QRect(0, 20, 913, 540))
        self.Scroll_Customers_Area_View.setMinimumSize(QSize(913, 0))
        self.Scroll_Customers_Area_View.setMaximumSize(QSize(913, 16777215))
        self.Scroll_Customers_Area_View.setAutoFillBackground(False)
        self.Scroll_Customers_Area_View.setStyleSheet(u"")
        self.Scroll_Customers_Area_View.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Scroll_Customers_Area_View.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Scroll_Customers_Area_View.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.SrollWidget_Customers_View = QWidget()
        self.SrollWidget_Customers_View.setObjectName(u"SrollWidget_Customers_View")
        self.SrollWidget_Customers_View.setGeometry(QRect(0, 0, 913, 540))
        self.SrollWidget_Customers_View.setMinimumSize(QSize(913, 0))
        self.SrollWidget_Customers_View.setMaximumSize(QSize(913, 16777215))
        self.gridLayoutWidget = QWidget(self.SrollWidget_Customers_View)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(1, 0, 911, 541))
        self.GridLayout_Customers_View = QGridLayout(self.gridLayoutWidget)
        self.GridLayout_Customers_View.setObjectName(u"GridLayout_Customers_View")
        self.GridLayout_Customers_View.setContentsMargins(0, 0, 0, 0)
        self.Scroll_Customers_Area_View.setWidget(self.SrollWidget_Customers_View)
        self.ToolsFrame_View = QFrame(self.Choose_Customer)
        self.ToolsFrame_View.setObjectName(u"ToolsFrame_View")
        self.ToolsFrame_View.setGeometry(QRect(67, 679, 913, 47))
        self.ToolsFrame_View.setMinimumSize(QSize(913, 47))
        self.ToolsFrame_View.setMaximumSize(QSize(913, 47))
        self.ToolsFrame_View.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.ToolsFrame_View.setFrameShape(QFrame.StyledPanel)
        self.ToolsFrame_View.setFrameShadow(QFrame.Raised)
        self.Exportation_CustomerView_Info = QLabel(self.ToolsFrame_View)
        self.Exportation_CustomerView_Info.setObjectName(u"Exportation_CustomerView_Info")
        self.Exportation_CustomerView_Info.setGeometry(QRect(20, 3, 871, 41))
        self.Exportation_CustomerView_Info.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 12pt \"Acme\";\n"
"}")
        self.Exportation_CustomerView_Info.setAlignment(Qt.AlignCenter)
        self.Exportation_CustomerView_Info.setWordWrap(True)
        self.Exportation_CustomerAdvanced_Info = QLabel(self.Choose_Customer)
        self.Exportation_CustomerAdvanced_Info.setObjectName(u"Exportation_CustomerAdvanced_Info")
        self.Exportation_CustomerAdvanced_Info.setGeometry(QRect(80, 682, 871, 41))
        self.Exportation_CustomerAdvanced_Info.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 12pt \"Acme\";\n"
"}")
        self.Exportation_CustomerAdvanced_Info.setAlignment(Qt.AlignCenter)
        self.Exportation_CustomerAdvanced_Info.setWordWrap(True)
        self.Sell_Windows.addWidget(self.Choose_Customer)
        self.Exportation_CustomerAdvanced_Info.raise_()
        self.Add_Customer_View.raise_()
        self.Filter_Frame_View.raise_()
        self.View_Customers_Frame.raise_()
        self.ToolsFrame_View.raise_()
        self.Choose_Selled_Rabbits = QWidget()
        self.Choose_Selled_Rabbits.setObjectName(u"Choose_Selled_Rabbits")
        self.Filter_Rabbits_Frame_View = QFrame(self.Choose_Selled_Rabbits)
        self.Filter_Rabbits_Frame_View.setObjectName(u"Filter_Rabbits_Frame_View")
        self.Filter_Rabbits_Frame_View.setGeometry(QRect(10, 20, 591, 47))
        self.Filter_Rabbits_Frame_View.setMinimumSize(QSize(591, 47))
        self.Filter_Rabbits_Frame_View.setMaximumSize(QSize(591, 47))
        self.Filter_Rabbits_Frame_View.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 73, 73);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Filter_Rabbits_Frame_View.setFrameShape(QFrame.StyledPanel)
        self.Filter_Rabbits_Frame_View.setFrameShadow(QFrame.Raised)
        self.FilterBy_Rabbits = QComboBox(self.Filter_Rabbits_Frame_View)
        self.FilterBy_Rabbits.addItem(icon, "")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/Rabbit_Tag.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/Icons/Rabbit_Tag.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon8, "")
        self.FilterBy_Rabbits.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/Calendar_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/Icons/Calendar_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon9, "")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/Rabbit_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/Icons/Rabbit_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon10, "")
        icon11 = QIcon()
        icon11.addFile(u":/Icons/Rabbit_Tree_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/Icons/Rabbit_Tree_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon11, "")
        self.FilterBy_Rabbits.addItem(icon11, "")
        self.FilterBy_Rabbits.addItem(icon11, "")
        icon12 = QIcon()
        icon12.addFile(u":/Icons/Settings_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon12.addFile(u":/Icons/Settings_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon12, "")
        icon13 = QIcon()
        icon13.addFile(u":/Icons/Cages_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/Icons/Cages_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon13, "")
        icon14 = QIcon()
        icon14.addFile(u":/Icons/Facture_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon14.addFile(u":/Icons/Facture_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon14, "")
        self.FilterBy_Rabbits.addItem(icon1, "")
        icon15 = QIcon()
        icon15.addFile(u":/Icons/TND_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon15.addFile(u":/Icons/TND_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon15, "")
        self.FilterBy_Rabbits.addItem(icon15, "")
        self.FilterBy_Rabbits.setObjectName(u"FilterBy_Rabbits")
        self.FilterBy_Rabbits.setGeometry(QRect(248, 7, 120, 33))
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
        self.FilterGender_Rabbits = QComboBox(self.Filter_Rabbits_Frame_View)
        self.FilterGender_Rabbits.addItem(icon4, "")
        self.FilterGender_Rabbits.addItem(icon5, "")
        self.FilterGender_Rabbits.addItem(icon6, "")
        self.FilterGender_Rabbits.addItem(icon7, "")
        self.FilterGender_Rabbits.setObjectName(u"FilterGender_Rabbits")
        self.FilterGender_Rabbits.setGeometry(QRect(118, 7, 123, 33))
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
        self.Ordre_Rabbits = QPushButton(self.Filter_Rabbits_Frame_View)
        self.Ordre_Rabbits.setObjectName(u"Ordre_Rabbits")
        self.Ordre_Rabbits.setGeometry(QRect(18, 7, 43, 33))
        self.Ordre_Rabbits.setMinimumSize(QSize(43, 33))
        self.Ordre_Rabbits.setMaximumSize(QSize(43, 33))
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
        self.Ordre_Rabbits.setChecked(False)
        self.Ordre_Rabbits.setAutoRepeat(False)
        self.Ordre_Rabbits.setAutoExclusive(False)
        self.Ordre_Rabbits.setAutoRepeatDelay(50)
        self.Ordre_Rabbits.setAutoRepeatInterval(10)
        self.Search_Rabbits = QLineEdit(self.Filter_Rabbits_Frame_View)
        self.Search_Rabbits.setObjectName(u"Search_Rabbits")
        self.Search_Rabbits.setGeometry(QRect(378, 7, 200, 33))
        self.Search_Rabbits.setMinimumSize(QSize(200, 33))
        self.Search_Rabbits.setMaximumSize(QSize(200, 31))
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
        self.Verif_Rabbits = QPushButton(self.Filter_Rabbits_Frame_View)
        self.Verif_Rabbits.setObjectName(u"Verif_Rabbits")
        self.Verif_Rabbits.setGeometry(QRect(65, 7, 43, 33))
        self.Verif_Rabbits.setMinimumSize(QSize(43, 33))
        self.Verif_Rabbits.setMaximumSize(QSize(43, 33))
        self.Verif_Rabbits.setFont(font)
        self.Verif_Rabbits.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Verif_Rabbits.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Verified_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Verified_Mix.png);\n"
"}\n"
"QPushButton:checked:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/Verified_Green.png);\n"
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
        self.Verif_Rabbits.setIconSize(QSize(20, 20))
        self.Verif_Rabbits.setCheckable(True)
        self.Verif_Rabbits.setChecked(False)
        self.Verif_Rabbits.setAutoRepeat(False)
        self.Verif_Rabbits.setAutoExclusive(False)
        self.Verif_Rabbits.setAutoRepeatDelay(50)
        self.Verif_Rabbits.setAutoRepeatInterval(10)
        self.View_Rabbits_Frame = QFrame(self.Choose_Selled_Rabbits)
        self.View_Rabbits_Frame.setObjectName(u"View_Rabbits_Frame")
        self.View_Rabbits_Frame.setEnabled(True)
        self.View_Rabbits_Frame.setGeometry(QRect(10, 80, 545, 290))
        self.View_Rabbits_Frame.setMinimumSize(QSize(545, 290))
        self.View_Rabbits_Frame.setMaximumSize(QSize(545, 290))
        self.View_Rabbits_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.View_Rabbits_Frame.setFrameShape(QFrame.Box)
        self.View_Rabbits_Frame.setFrameShadow(QFrame.Plain)
        self.Scroll_Rabbits_Area_View = QScrollArea(self.View_Rabbits_Frame)
        self.Scroll_Rabbits_Area_View.setObjectName(u"Scroll_Rabbits_Area_View")
        self.Scroll_Rabbits_Area_View.setGeometry(QRect(0, 20, 545, 250))
        self.Scroll_Rabbits_Area_View.setMinimumSize(QSize(545, 250))
        self.Scroll_Rabbits_Area_View.setMaximumSize(QSize(545, 250))
        self.Scroll_Rabbits_Area_View.setAutoFillBackground(False)
        self.Scroll_Rabbits_Area_View.setStyleSheet(u"")
        self.Scroll_Rabbits_Area_View.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Scroll_Rabbits_Area_View.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Scroll_Rabbits_Area_View.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.SrollWidget_Rabbits_View = QWidget()
        self.SrollWidget_Rabbits_View.setObjectName(u"SrollWidget_Rabbits_View")
        self.SrollWidget_Rabbits_View.setGeometry(QRect(0, 0, 913, 540))
        self.SrollWidget_Rabbits_View.setMinimumSize(QSize(913, 0))
        self.SrollWidget_Rabbits_View.setMaximumSize(QSize(913, 16777215))
        self.gridLayoutWidget_2 = QWidget(self.SrollWidget_Rabbits_View)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 521, 231))
        self.GridLayout_Rabbits_View = QGridLayout(self.gridLayoutWidget_2)
        self.GridLayout_Rabbits_View.setObjectName(u"GridLayout_Rabbits_View")
        self.GridLayout_Rabbits_View.setSizeConstraint(QLayout.SetFixedSize)
        self.GridLayout_Rabbits_View.setContentsMargins(60, 0, 0, 0)
        self.Scroll_Rabbits_Area_View.setWidget(self.SrollWidget_Rabbits_View)
        self.View_Cages_Frame = QFrame(self.Choose_Selled_Rabbits)
        self.View_Cages_Frame.setObjectName(u"View_Cages_Frame")
        self.View_Cages_Frame.setEnabled(True)
        self.View_Cages_Frame.setGeometry(QRect(10, 460, 545, 290))
        self.View_Cages_Frame.setMinimumSize(QSize(545, 290))
        self.View_Cages_Frame.setMaximumSize(QSize(545, 290))
        self.View_Cages_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.View_Cages_Frame.setFrameShape(QFrame.Box)
        self.View_Cages_Frame.setFrameShadow(QFrame.Plain)
        self.Scroll_Cages_Area_View = QScrollArea(self.View_Cages_Frame)
        self.Scroll_Cages_Area_View.setObjectName(u"Scroll_Cages_Area_View")
        self.Scroll_Cages_Area_View.setGeometry(QRect(0, 20, 545, 250))
        self.Scroll_Cages_Area_View.setMinimumSize(QSize(545, 250))
        self.Scroll_Cages_Area_View.setMaximumSize(QSize(545, 250))
        self.Scroll_Cages_Area_View.setAutoFillBackground(False)
        self.Scroll_Cages_Area_View.setStyleSheet(u"")
        self.Scroll_Cages_Area_View.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Scroll_Cages_Area_View.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Scroll_Cages_Area_View.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.SrollWidget_Cages_View = QWidget()
        self.SrollWidget_Cages_View.setObjectName(u"SrollWidget_Cages_View")
        self.SrollWidget_Cages_View.setGeometry(QRect(0, 0, 913, 540))
        self.SrollWidget_Cages_View.setMinimumSize(QSize(913, 0))
        self.SrollWidget_Cages_View.setMaximumSize(QSize(913, 16777215))
        self.gridLayoutWidget_3 = QWidget(self.SrollWidget_Cages_View)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(20, 10, 501, 231))
        self.GridLayout_Cages_View = QGridLayout(self.gridLayoutWidget_3)
        self.GridLayout_Cages_View.setObjectName(u"GridLayout_Cages_View")
        self.GridLayout_Cages_View.setSizeConstraint(QLayout.SetFixedSize)
        self.GridLayout_Cages_View.setContentsMargins(60, 0, 0, 0)
        self.Scroll_Cages_Area_View.setWidget(self.SrollWidget_Cages_View)
        self.Filter_Cages_Frame_View = QFrame(self.Choose_Selled_Rabbits)
        self.Filter_Cages_Frame_View.setObjectName(u"Filter_Cages_Frame_View")
        self.Filter_Cages_Frame_View.setGeometry(QRect(10, 403, 545, 47))
        self.Filter_Cages_Frame_View.setMinimumSize(QSize(545, 47))
        self.Filter_Cages_Frame_View.setMaximumSize(QSize(545, 47))
        self.Filter_Cages_Frame_View.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 73, 73);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Filter_Cages_Frame_View.setFrameShape(QFrame.StyledPanel)
        self.Filter_Cages_Frame_View.setFrameShadow(QFrame.Raised)
        self.FilterBy_Cages = QComboBox(self.Filter_Cages_Frame_View)
        self.FilterBy_Cages.addItem(icon, "")
        self.FilterBy_Cages.addItem(icon13, "")
        self.FilterBy_Cages.addItem(icon14, "")
        self.FilterBy_Cages.addItem(icon1, "")
        self.FilterBy_Cages.addItem(icon15, "")
        self.FilterBy_Cages.addItem(icon15, "")
        self.FilterBy_Cages.setObjectName(u"FilterBy_Cages")
        self.FilterBy_Cages.setGeometry(QRect(201, 7, 120, 33))
        self.FilterBy_Cages.setMinimumSize(QSize(120, 33))
        self.FilterBy_Cages.setMaximumSize(QSize(120, 33))
        self.FilterBy_Cages.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid white;\n"
"	border-radius:6px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 12pt \"Acme\";\n"
"	padding-left: 15px;\n"
"	selection-background-color: #2980B9;\n"
"}")
        self.FilterGender_Cages = QComboBox(self.Filter_Cages_Frame_View)
        self.FilterGender_Cages.addItem(icon4, "")
        self.FilterGender_Cages.addItem(icon6, "")
        self.FilterGender_Cages.addItem(icon7, "")
        self.FilterGender_Cages.addItem(icon5, "")
        self.FilterGender_Cages.setObjectName(u"FilterGender_Cages")
        self.FilterGender_Cages.setGeometry(QRect(71, 7, 123, 33))
        self.FilterGender_Cages.setMinimumSize(QSize(123, 33))
        self.FilterGender_Cages.setMaximumSize(QSize(123, 33))
        self.FilterGender_Cages.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid white;\n"
"	border-radius:6px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 12pt \"Acme\";\n"
"	padding-left: 15px;\n"
"	selection-background-color: #2980B9;\n"
"}")
        self.Ordre_Cages = QPushButton(self.Filter_Cages_Frame_View)
        self.Ordre_Cages.setObjectName(u"Ordre_Cages")
        self.Ordre_Cages.setGeometry(QRect(18, 7, 43, 33))
        self.Ordre_Cages.setMinimumSize(QSize(43, 33))
        self.Ordre_Cages.setMaximumSize(QSize(43, 33))
        self.Ordre_Cages.setFont(font)
        self.Ordre_Cages.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Ordre_Cages.setStyleSheet(u"QPushButton {\n"
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
        self.Ordre_Cages.setIconSize(QSize(20, 20))
        self.Ordre_Cages.setCheckable(True)
        self.Ordre_Cages.setChecked(False)
        self.Ordre_Cages.setAutoRepeat(False)
        self.Ordre_Cages.setAutoExclusive(False)
        self.Ordre_Cages.setAutoRepeatDelay(50)
        self.Ordre_Cages.setAutoRepeatInterval(10)
        self.Search_Cages = QLineEdit(self.Filter_Cages_Frame_View)
        self.Search_Cages.setObjectName(u"Search_Cages")
        self.Search_Cages.setGeometry(QRect(331, 7, 200, 33))
        self.Search_Cages.setMinimumSize(QSize(200, 33))
        self.Search_Cages.setMaximumSize(QSize(200, 31))
        self.Search_Cages.setStyleSheet(u"QLineEdit {\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	padding-left: 30px;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-image: url(:/Icons/Search.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 10pt \"Acme\";\n"
"}")
        self.Infos_Frame = QFrame(self.Choose_Selled_Rabbits)
        self.Infos_Frame.setObjectName(u"Infos_Frame")
        self.Infos_Frame.setEnabled(True)
        self.Infos_Frame.setGeometry(QRect(610, 20, 361, 207))
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
        self.Sell_Item_Frame = QFrame(self.Choose_Selled_Rabbits)
        self.Sell_Item_Frame.setObjectName(u"Sell_Item_Frame")
        self.Sell_Item_Frame.setGeometry(QRect(20, 228, 401, 321))
        self.Sell_Item_Frame.setMinimumSize(QSize(401, 321))
        self.Sell_Item_Frame.setMaximumSize(QSize(401, 321))
        self.Sell_Item_Frame.setFrameShape(QFrame.StyledPanel)
        self.Sell_Item_Frame.setFrameShadow(QFrame.Raised)
        self.Item_Sold_Frame = QFrame(self.Sell_Item_Frame)
        self.Item_Sold_Frame.setObjectName(u"Item_Sold_Frame")
        self.Item_Sold_Frame.setGeometry(QRect(30, 220, 341, 68))
        self.Item_Sold_Frame.setMinimumSize(QSize(341, 68))
        self.Item_Sold_Frame.setMaximumSize(QSize(341, 68))
        self.Item_Sold_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Item_Sold_Frame.setFrameShape(QFrame.StyledPanel)
        self.Item_Sold_Frame.setFrameShadow(QFrame.Raised)
        self.Item_Sold_Label = QLabel(self.Item_Sold_Frame)
        self.Item_Sold_Label.setObjectName(u"Item_Sold_Label")
        self.Item_Sold_Label.setGeometry(QRect(50, 11, 80, 21))
        self.Item_Sold_Label.setMinimumSize(QSize(80, 21))
        self.Item_Sold_Label.setMaximumSize(QSize(80, 21))
        self.Item_Sold_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Item_Sold_Input = QDoubleSpinBox(self.Item_Sold_Frame)
        self.Item_Sold_Input.setObjectName(u"Item_Sold_Input")
        self.Item_Sold_Input.setGeometry(QRect(110, 11, 191, 21))
        self.Item_Sold_Input.setMinimumSize(QSize(191, 21))
        self.Item_Sold_Input.setMaximumSize(QSize(191, 21))
        self.Item_Sold_Input.setStyleSheet(u"QDoubleSpinBox {\n"
"	background-color:rgb(167, 164, 147);\n"
"	padding-left: 5px;\n"
"	border: 2px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 15pt \"Acme\";\n"
"}")
        self.Item_Sold_Input.setWrapping(False)
        self.Item_Sold_Input.setAlignment(Qt.AlignCenter)
        self.Item_Sold_Input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Item_Sold_Input.setAccelerated(True)
        self.Item_Sold_Input.setDecimals(3)
        self.Item_Sold_Input.setMaximum(9999.989999999999782)
        self.Item_Sold_Input.setSingleStep(0.500000000000000)
        self.Item_Sold_Icon = QLabel(self.Item_Sold_Frame)
        self.Item_Sold_Icon.setObjectName(u"Item_Sold_Icon")
        self.Item_Sold_Icon.setGeometry(QRect(20, 11, 21, 21))
        self.Item_Sold_Icon.setMinimumSize(QSize(21, 21))
        self.Item_Sold_Icon.setMaximumSize(QSize(21, 21))
        self.Item_Sold_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Item_Sold_Icon.setPixmap(QPixmap(u":/Icons/TND_White.png"))
        self.Item_Sold_Icon.setScaledContents(True)
        self.Item_Sold_Icon.setAlignment(Qt.AlignCenter)
        self.Item_Sold_Infos = QLabel(self.Item_Sold_Frame)
        self.Item_Sold_Infos.setObjectName(u"Item_Sold_Infos")
        self.Item_Sold_Infos.setGeometry(QRect(20, 37, 301, 21))
        self.Item_Sold_Infos.setMinimumSize(QSize(301, 21))
        self.Item_Sold_Infos.setMaximumSize(QSize(301, 21))
        self.Item_Sold_Infos.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Sell_Button = QPushButton(self.Sell_Item_Frame)
        self.Sell_Button.setObjectName(u"Sell_Button")
        self.Sell_Button.setEnabled(True)
        self.Sell_Button.setGeometry(QRect(290, 20, 43, 33))
        self.Sell_Button.setMinimumSize(QSize(43, 33))
        self.Sell_Button.setMaximumSize(QSize(43, 33))
        self.Sell_Button.setFont(font)
        self.Sell_Button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Sell_Button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Sell_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Sell_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Sell_Green.png);\n"
"}")
        self.Sell_Button.setIconSize(QSize(20, 20))
        self.Sell_Button.setCheckable(False)
        self.Sell_Button.setAutoRepeat(False)
        self.Sell_Button.setAutoExclusive(False)
        self.Sell_Button.setAutoRepeatDelay(50)
        self.Sell_Button.setAutoRepeatInterval(10)
        self.Exit_Sell_Button = QPushButton(self.Sell_Item_Frame)
        self.Exit_Sell_Button.setObjectName(u"Exit_Sell_Button")
        self.Exit_Sell_Button.setEnabled(True)
        self.Exit_Sell_Button.setGeometry(QRect(340, 20, 43, 33))
        self.Exit_Sell_Button.setMinimumSize(QSize(43, 33))
        self.Exit_Sell_Button.setMaximumSize(QSize(43, 33))
        self.Exit_Sell_Button.setFont(font)
        self.Exit_Sell_Button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Exit_Sell_Button.setStyleSheet(u"QPushButton {\n"
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
        self.Exit_Sell_Button.setIconSize(QSize(20, 20))
        self.Exit_Sell_Button.setCheckable(False)
        self.Exit_Sell_Button.setAutoRepeat(False)
        self.Exit_Sell_Button.setAutoExclusive(False)
        self.Exit_Sell_Button.setAutoRepeatDelay(50)
        self.Exit_Sell_Button.setAutoRepeatInterval(10)
        self.Item_Avatar_Frame = QFrame(self.Sell_Item_Frame)
        self.Item_Avatar_Frame.setObjectName(u"Item_Avatar_Frame")
        self.Item_Avatar_Frame.setGeometry(QRect(30, 40, 119, 161))
        self.Item_Avatar_Frame.setMinimumSize(QSize(119, 161))
        self.Item_Avatar_Frame.setMaximumSize(QSize(119, 161))
        self.Item_Avatar_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #D9D9D9;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Item_Avatar_Frame.setFrameShape(QFrame.StyledPanel)
        self.Item_Avatar_Frame.setFrameShadow(QFrame.Raised)
        self.Item_Avatar_Label = QLabel(self.Item_Avatar_Frame)
        self.Item_Avatar_Label.setObjectName(u"Item_Avatar_Label")
        self.Item_Avatar_Label.setGeometry(QRect(9, 10, 101, 141))
        self.Item_Avatar_Label.setStyleSheet(u"border:none;")
        self.Item_Avatar_Label.setPixmap(QPixmap(u":/Icons/Sell_Green.png"))
        self.Item_Avatar_Label.setScaledContents(False)
        self.Item_Avatar_Label.setAlignment(Qt.AlignCenter)
        self.Item_ID_Frame = QFrame(self.Sell_Item_Frame)
        self.Item_ID_Frame.setObjectName(u"Item_ID_Frame")
        self.Item_ID_Frame.setEnabled(True)
        self.Item_ID_Frame.setGeometry(QRect(190, 80, 158, 44))
        self.Item_ID_Frame.setMinimumSize(QSize(158, 44))
        self.Item_ID_Frame.setMaximumSize(QSize(158, 44))
        self.Item_ID_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #2F2F2F;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Item_ID_Frame.setFrameShape(QFrame.StyledPanel)
        self.Item_ID_Frame.setFrameShadow(QFrame.Raised)
        self.Item_ID_Label = QLabel(self.Item_ID_Frame)
        self.Item_ID_Label.setObjectName(u"Item_ID_Label")
        self.Item_ID_Label.setGeometry(QRect(20, 6, 121, 31))
        self.Item_ID_Label.setMinimumSize(QSize(121, 31))
        self.Item_ID_Label.setMaximumSize(QSize(121, 31))
        self.Item_ID_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";\n"
"}")
        self.Item_Type_Frame = QFrame(self.Sell_Item_Frame)
        self.Item_Type_Frame.setObjectName(u"Item_Type_Frame")
        self.Item_Type_Frame.setGeometry(QRect(170, 140, 200, 40))
        self.Item_Type_Frame.setMinimumSize(QSize(200, 40))
        self.Item_Type_Frame.setMaximumSize(QSize(200, 40))
        self.Item_Type_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Item_Type_Frame.setFrameShape(QFrame.StyledPanel)
        self.Item_Type_Frame.setFrameShadow(QFrame.Raised)
        self.Item_Type_Icon = QLabel(self.Item_Type_Frame)
        self.Item_Type_Icon.setObjectName(u"Item_Type_Icon")
        self.Item_Type_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Item_Type_Icon.setMinimumSize(QSize(21, 21))
        self.Item_Type_Icon.setMaximumSize(QSize(21, 21))
        self.Item_Type_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Item_Type_Icon.setPixmap(QPixmap(u":/Icons/Settings_White.png"))
        self.Item_Type_Icon.setScaledContents(True)
        self.Item_Type_Icon.setAlignment(Qt.AlignCenter)
        self.Item_Type_Icon.setWordWrap(False)
        self.Item_Type_Label = QLabel(self.Item_Type_Frame)
        self.Item_Type_Label.setObjectName(u"Item_Type_Label")
        self.Item_Type_Label.setGeometry(QRect(50, 9, 139, 21))
        self.Item_Type_Label.setMinimumSize(QSize(139, 21))
        self.Item_Type_Label.setMaximumSize(QSize(139, 21))
        self.Item_Type_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Selled_Items_Frame = QFrame(self.Choose_Selled_Rabbits)
        self.Selled_Items_Frame.setObjectName(u"Selled_Items_Frame")
        self.Selled_Items_Frame.setGeometry(QRect(610, 237, 361, 513))
        self.Selled_Items_Frame.setMinimumSize(QSize(361, 0))
        self.Selled_Items_Frame.setMaximumSize(QSize(361, 16777215))
        self.Selled_Items_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Selled_Items_Frame.setFrameShape(QFrame.StyledPanel)
        self.Selled_Items_Frame.setFrameShadow(QFrame.Raised)
        self.AllItems = QTextEdit(self.Selled_Items_Frame)
        self.AllItems.setObjectName(u"AllItems")
        self.AllItems.setGeometry(QRect(10, 10, 341, 491))
        self.AllItems.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(69, 69, 69);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 13pt \"Acme\";\n"
"	border: none;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.AllItems.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.AllItems.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.AllItems.setReadOnly(True)
        self.Block_Frame = QFrame(self.Choose_Selled_Rabbits)
        self.Block_Frame.setObjectName(u"Block_Frame")
        self.Block_Frame.setGeometry(QRect(0, 0, 1011, 761))
        self.Block_Frame.setMinimumSize(QSize(1011, 761))
        self.Block_Frame.setMaximumSize(QSize(1011, 761))
        self.Block_Frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.Block_Frame.setFrameShape(QFrame.StyledPanel)
        self.Block_Frame.setFrameShadow(QFrame.Raised)
        self.Sell_Windows.addWidget(self.Choose_Selled_Rabbits)
        self.Filter_Rabbits_Frame_View.raise_()
        self.View_Rabbits_Frame.raise_()
        self.View_Cages_Frame.raise_()
        self.Filter_Cages_Frame_View.raise_()
        self.Infos_Frame.raise_()
        self.Selled_Items_Frame.raise_()
        self.Block_Frame.raise_()
        self.Sell_Item_Frame.raise_()
        self.Exit_Facture_Button = QPushButton(self.Background)
        self.Exit_Facture_Button.setObjectName(u"Exit_Facture_Button")
        self.Exit_Facture_Button.setEnabled(True)
        self.Exit_Facture_Button.setGeometry(QRect(940, 10, 43, 33))
        self.Exit_Facture_Button.setMinimumSize(QSize(43, 33))
        self.Exit_Facture_Button.setMaximumSize(QSize(43, 33))
        self.Exit_Facture_Button.setFont(font)
        self.Exit_Facture_Button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Exit_Facture_Button.setStyleSheet(u"QPushButton {\n"
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
        self.Exit_Facture_Button.setIconSize(QSize(20, 20))
        self.Exit_Facture_Button.setCheckable(False)
        self.Exit_Facture_Button.setAutoRepeat(False)
        self.Exit_Facture_Button.setAutoExclusive(False)
        self.Exit_Facture_Button.setAutoRepeatDelay(50)
        self.Exit_Facture_Button.setAutoRepeatInterval(10)
        self.Add_Facture = QPushButton(self.Background)
        self.Add_Facture.setObjectName(u"Add_Facture")
        self.Add_Facture.setEnabled(True)
        self.Add_Facture.setGeometry(QRect(110, 10, 43, 33))
        self.Add_Facture.setMinimumSize(QSize(43, 33))
        self.Add_Facture.setMaximumSize(QSize(43, 33))
        self.Add_Facture.setFont(font)
        self.Add_Facture.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Add_Facture.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Add_Facture_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Add_Facture_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/Add_Facture_Green.png);\n"
"}")
        self.Add_Facture.setIconSize(QSize(20, 20))
        self.Add_Facture.setCheckable(False)
        self.Add_Facture.setAutoRepeat(False)
        self.Add_Facture.setAutoExclusive(False)
        self.Add_Facture.setAutoRepeatDelay(50)
        self.Add_Facture.setAutoRepeatInterval(10)
        self.Return_Page = QPushButton(self.Background)
        self.Return_Page.setObjectName(u"Return_Page")
        self.Return_Page.setEnabled(True)
        self.Return_Page.setGeometry(QRect(70, 13, 33, 33))
        self.Return_Page.setMinimumSize(QSize(33, 33))
        self.Return_Page.setMaximumSize(QSize(22, 22))
        self.Return_Page.setFont(font)
        self.Return_Page.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Return_Page.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Return_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Return_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Return_Red.png);\n"
"}")
        self.Return_Page.setIconSize(QSize(20, 20))
        self.Return_Page.setCheckable(False)
        self.Return_Page.setAutoRepeat(False)
        self.Return_Page.setAutoExclusive(False)
        self.Return_Page.setAutoRepeatDelay(50)
        self.Return_Page.setAutoRepeatInterval(10)

        self.retranslateUi(Facture_Add_Main)
        self.Exit_Facture_Button.clicked.connect(Facture_Add_Main.close)
        self.Exit_Sell_Button.clicked.connect(self.Sell_Item_Frame.hide)

        self.Sell_Windows.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Facture_Add_Main)
    # setupUi

    def retranslateUi(self, Facture_Add_Main):
        Facture_Add_Main.setWindowTitle(QCoreApplication.translate("Facture_Add_Main", u"Dialog", None))
        self.Title.setText(QCoreApplication.translate("Facture_Add_Main", u"Add New Facture", None))
        self.Add_Customer_View.setText("")
        self.FilterBy_Customer.setItemText(0, QCoreApplication.translate("Facture_Add_Main", u"By", None))
        self.FilterBy_Customer.setItemText(1, QCoreApplication.translate("Facture_Add_Main", u"ID", None))
        self.FilterBy_Customer.setItemText(2, QCoreApplication.translate("Facture_Add_Main", u"Name", None))
        self.FilterBy_Customer.setItemText(3, QCoreApplication.translate("Facture_Add_Main", u"Phone", None))
        self.FilterBy_Customer.setItemText(4, QCoreApplication.translate("Facture_Add_Main", u"Address", None))

        self.FilterGender_Customer.setItemText(0, QCoreApplication.translate("Facture_Add_Main", u"Gender", None))
        self.FilterGender_Customer.setItemText(1, QCoreApplication.translate("Facture_Add_Main", u"Null", None))
        self.FilterGender_Customer.setItemText(2, QCoreApplication.translate("Facture_Add_Main", u"Male", None))
        self.FilterGender_Customer.setItemText(3, QCoreApplication.translate("Facture_Add_Main", u"Female", None))

        self.Ordre_Customer.setText("")
        self.Search_Customer.setInputMask("")
        self.Search_Customer.setText("")
        self.Search_Customer.setPlaceholderText(QCoreApplication.translate("Facture_Add_Main", u"Search Customer...", None))
        self.Exportation_CustomerView_Info.setText("")
        self.Exportation_CustomerAdvanced_Info.setText("")
        self.FilterBy_Rabbits.setItemText(0, QCoreApplication.translate("Facture_Add_Main", u"By", None))
        self.FilterBy_Rabbits.setItemText(1, QCoreApplication.translate("Facture_Add_Main", u"ID", None))
        self.FilterBy_Rabbits.setItemText(2, QCoreApplication.translate("Facture_Add_Main", u"Breed", None))
        self.FilterBy_Rabbits.setItemText(3, QCoreApplication.translate("Facture_Add_Main", u"Born", None))
        self.FilterBy_Rabbits.setItemText(4, QCoreApplication.translate("Facture_Add_Main", u"Color", None))
        self.FilterBy_Rabbits.setItemText(5, QCoreApplication.translate("Facture_Add_Main", u"Mother", None))
        self.FilterBy_Rabbits.setItemText(6, QCoreApplication.translate("Facture_Add_Main", u"Father", None))
        self.FilterBy_Rabbits.setItemText(7, QCoreApplication.translate("Facture_Add_Main", u"Generation", None))
        self.FilterBy_Rabbits.setItemText(8, QCoreApplication.translate("Facture_Add_Main", u"Type", None))
        self.FilterBy_Rabbits.setItemText(9, QCoreApplication.translate("Facture_Add_Main", u"CageID", None))
        self.FilterBy_Rabbits.setItemText(10, QCoreApplication.translate("Facture_Add_Main", u"FactureID", None))
        self.FilterBy_Rabbits.setItemText(11, QCoreApplication.translate("Facture_Add_Main", u"CustomerID", None))
        self.FilterBy_Rabbits.setItemText(12, QCoreApplication.translate("Facture_Add_Main", u"Bought", None))
        self.FilterBy_Rabbits.setItemText(13, QCoreApplication.translate("Facture_Add_Main", u"Sold", None))

        self.FilterGender_Rabbits.setItemText(0, QCoreApplication.translate("Facture_Add_Main", u"Gender", None))
        self.FilterGender_Rabbits.setItemText(1, QCoreApplication.translate("Facture_Add_Main", u"Null", None))
        self.FilterGender_Rabbits.setItemText(2, QCoreApplication.translate("Facture_Add_Main", u"Male", None))
        self.FilterGender_Rabbits.setItemText(3, QCoreApplication.translate("Facture_Add_Main", u"Female", None))

        self.Ordre_Rabbits.setText("")
        self.Search_Rabbits.setInputMask("")
        self.Search_Rabbits.setText("")
        self.Search_Rabbits.setPlaceholderText(QCoreApplication.translate("Facture_Add_Main", u"Search Rabbit...", None))
        self.Verif_Rabbits.setText("")
        self.FilterBy_Cages.setItemText(0, QCoreApplication.translate("Facture_Add_Main", u"By", None))
        self.FilterBy_Cages.setItemText(1, QCoreApplication.translate("Facture_Add_Main", u"ID", None))
        self.FilterBy_Cages.setItemText(2, QCoreApplication.translate("Facture_Add_Main", u"FactureID", None))
        self.FilterBy_Cages.setItemText(3, QCoreApplication.translate("Facture_Add_Main", u"CustomerID", None))
        self.FilterBy_Cages.setItemText(4, QCoreApplication.translate("Facture_Add_Main", u"Sold", None))
        self.FilterBy_Cages.setItemText(5, QCoreApplication.translate("Facture_Add_Main", u"Bought", None))

        self.FilterGender_Cages.setItemText(0, QCoreApplication.translate("Facture_Add_Main", u"Gender", None))
        self.FilterGender_Cages.setItemText(1, QCoreApplication.translate("Facture_Add_Main", u"Male", None))
        self.FilterGender_Cages.setItemText(2, QCoreApplication.translate("Facture_Add_Main", u"Female", None))
        self.FilterGender_Cages.setItemText(3, QCoreApplication.translate("Facture_Add_Main", u"Kids", None))

        self.Ordre_Cages.setText("")
        self.Search_Cages.setInputMask("")
        self.Search_Cages.setText("")
        self.Search_Cages.setPlaceholderText(QCoreApplication.translate("Facture_Add_Main", u"Search Cage...", None))
        self.Customer_Name_Label.setText("")
        self.Customer_Phone_Label.setText("")
        self.Customer_Gender_Label.setText("")
        self.Customer_Address_Label.setText("")
        self.Customer_Name_Icon.setText("")
        self.Customer_Phone_Icon.setText("")
        self.Customer_Gender_Icon.setText("")
        self.Customer_Address_Icon.setText("")
        self.Customer_ID_Label.setText(QCoreApplication.translate("Facture_Add_Main", u"ID :", None))
        self.Item_Sold_Label.setText(QCoreApplication.translate("Facture_Add_Main", u"Sold", None))
        self.Item_Sold_Input.setPrefix("")
        self.Item_Sold_Input.setSuffix(QCoreApplication.translate("Facture_Add_Main", u"  TND", None))
        self.Item_Sold_Icon.setText("")
        self.Item_Sold_Infos.setText(QCoreApplication.translate("Facture_Add_Main", u"How Much You Want To Sell This", None))
        self.Sell_Button.setText("")
#if QT_CONFIG(shortcut)
        self.Sell_Button.setShortcut(QCoreApplication.translate("Facture_Add_Main", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.Exit_Sell_Button.setText("")
#if QT_CONFIG(shortcut)
        self.Exit_Sell_Button.setShortcut(QCoreApplication.translate("Facture_Add_Main", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.Item_Avatar_Label.setText("")
        self.Item_ID_Label.setText(QCoreApplication.translate("Facture_Add_Main", u"ID : ", None))
        self.Item_Type_Icon.setText("")
        self.Item_Type_Label.setText(QCoreApplication.translate("Facture_Add_Main", u"Type", None))
        self.AllItems.setDocumentTitle("")
        self.Exit_Facture_Button.setText("")
#if QT_CONFIG(shortcut)
        self.Exit_Facture_Button.setShortcut(QCoreApplication.translate("Facture_Add_Main", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.Add_Facture.setText("")
#if QT_CONFIG(shortcut)
        self.Add_Facture.setShortcut(QCoreApplication.translate("Facture_Add_Main", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.Return_Page.setText("")
#if QT_CONFIG(shortcut)
        self.Return_Page.setShortcut(QCoreApplication.translate("Facture_Add_Main", u"Esc", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

