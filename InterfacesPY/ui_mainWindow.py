# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1272, 867)
        MainWindow.setMinimumSize(QSize(1272, 867))
        MainWindow.setMaximumSize(QSize(1272, 867))
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.Window = QWidget(MainWindow)
        self.Window.setObjectName(u"Window")
        self.Window.setMinimumSize(QSize(1272, 867))
        self.Window.setMaximumSize(QSize(1272, 867))
        self.MenuFrame = QFrame(self.Window)
        self.MenuFrame.setObjectName(u"MenuFrame")
        self.MenuFrame.setEnabled(True)
        self.MenuFrame.setGeometry(QRect(0, 0, 300, 867))
        self.MenuFrame.setMinimumSize(QSize(300, 867))
        self.MenuFrame.setMaximumSize(QSize(300, 867))
        self.MenuFrame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 50px;\n"
"}")
        self.MenuFrame.setFrameShape(QFrame.StyledPanel)
        self.MenuFrame.setFrameShadow(QFrame.Raised)
        self.Farm_Logo = QLabel(self.MenuFrame)
        self.Farm_Logo.setObjectName(u"Farm_Logo")
        self.Farm_Logo.setGeometry(QRect(17, 13, 68, 68))
        self.Farm_Logo.setMinimumSize(QSize(68, 68))
        self.Farm_Logo.setMaximumSize(QSize(68, 68))
        self.Farm_Logo.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.Farm_Logo.setPixmap(QPixmap(u":/Icons/Logo.png"))
        self.Farm_Logo.setScaledContents(True)
        self.Farm_Logo.setAlignment(Qt.AlignCenter)
        self.Project_Name = QLabel(self.MenuFrame)
        self.Project_Name.setObjectName(u"Project_Name")
        self.Project_Name.setGeometry(QRect(85, 36, 156, 22))
        self.Project_Name.setMinimumSize(QSize(156, 22))
        self.Project_Name.setMaximumSize(QSize(156, 22))
        font = QFont()
        font.setFamilies([u"Acme"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.Project_Name.setFont(font)
        self.Project_Name.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Acme\";")
        self.Project_Name.setAlignment(Qt.AlignCenter)
        self.Dashboard_Button = QPushButton(self.MenuFrame)
        self.Dashboard_Button.setObjectName(u"Dashboard_Button")
        self.Dashboard_Button.setGeometry(QRect(6, 121, 227, 65))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dashboard_Button.sizePolicy().hasHeightForWidth())
        self.Dashboard_Button.setSizePolicy(sizePolicy)
        self.Dashboard_Button.setMinimumSize(QSize(227, 65))
        self.Dashboard_Button.setMaximumSize(QSize(227, 65))
        font1 = QFont()
        font1.setFamilies([u"Acme"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.Dashboard_Button.setFont(font1)
        self.Dashboard_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 16px;\n"
"	font: 75 20pt \"Acme\";\n"
"}\n"
"QPushButton:checked:hover {\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(98, 114, 90);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(27, 27, 27);\n"
"	color: rgb(98, 114, 90);\n"
"	border-style: outset;\n"
"    	border-radius: 10px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/Dashboard_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/Icons/Dashboard_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Dashboard_Button.setIcon(icon)
        self.Dashboard_Button.setIconSize(QSize(32, 32))
        self.Dashboard_Button.setCheckable(True)
        self.Dashboard_Button.setChecked(False)
        self.Dashboard_Button.setFlat(False)
        self.Customers_Button = QPushButton(self.MenuFrame)
        self.Customers_Button.setObjectName(u"Customers_Button")
        self.Customers_Button.setGeometry(QRect(6, 216, 227, 65))
        sizePolicy.setHeightForWidth(self.Customers_Button.sizePolicy().hasHeightForWidth())
        self.Customers_Button.setSizePolicy(sizePolicy)
        self.Customers_Button.setMinimumSize(QSize(227, 65))
        self.Customers_Button.setMaximumSize(QSize(227, 65))
        self.Customers_Button.setFont(font1)
        self.Customers_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 16px;\n"
"	font: 75 20pt \"Acme\";\n"
"}\n"
"QPushButton:checked:hover {\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(98, 114, 90);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(27, 27, 27);\n"
"	color: rgb(98, 114, 90);\n"
"	border-style: outset;\n"
"    	border-radius: 10px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Customer_Whitre.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/Icons/Customer_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Customers_Button.setIcon(icon1)
        self.Customers_Button.setIconSize(QSize(32, 32))
        self.Customers_Button.setCheckable(True)
        self.Customers_Button.setChecked(False)
        self.Customers_Button.setFlat(False)
        self.Rabbits_Button = QPushButton(self.MenuFrame)
        self.Rabbits_Button.setObjectName(u"Rabbits_Button")
        self.Rabbits_Button.setGeometry(QRect(6, 311, 227, 65))
        sizePolicy.setHeightForWidth(self.Rabbits_Button.sizePolicy().hasHeightForWidth())
        self.Rabbits_Button.setSizePolicy(sizePolicy)
        self.Rabbits_Button.setMinimumSize(QSize(227, 65))
        self.Rabbits_Button.setMaximumSize(QSize(227, 65))
        self.Rabbits_Button.setFont(font1)
        self.Rabbits_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 16px;\n"
"	font: 75 20pt \"Acme\";\n"
"}\n"
"QPushButton:checked:hover {\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(98, 114, 90);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(27, 27, 27);\n"
"	color: rgb(98, 114, 90);\n"
"	border-style: outset;\n"
"    	border-radius: 10px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Rabbits_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/Icons/Rabbits_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Rabbits_Button.setIcon(icon2)
        self.Rabbits_Button.setIconSize(QSize(32, 32))
        self.Rabbits_Button.setCheckable(True)
        self.Rabbits_Button.setChecked(False)
        self.Rabbits_Button.setFlat(False)
        self.Cages_Button = QPushButton(self.MenuFrame)
        self.Cages_Button.setObjectName(u"Cages_Button")
        self.Cages_Button.setGeometry(QRect(6, 406, 227, 65))
        sizePolicy.setHeightForWidth(self.Cages_Button.sizePolicy().hasHeightForWidth())
        self.Cages_Button.setSizePolicy(sizePolicy)
        self.Cages_Button.setMinimumSize(QSize(227, 65))
        self.Cages_Button.setMaximumSize(QSize(227, 65))
        self.Cages_Button.setFont(font1)
        self.Cages_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 16px;\n"
"	font: 75 20pt \"Acme\";\n"
"}\n"
"QPushButton:checked:hover {\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(98, 114, 90);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(27, 27, 27);\n"
"	color: rgb(98, 114, 90);\n"
"	border-style: outset;\n"
"    	border-radius: 10px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Cages_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Icons/Cages_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Cages_Button.setIcon(icon3)
        self.Cages_Button.setIconSize(QSize(32, 32))
        self.Cages_Button.setCheckable(True)
        self.Cages_Button.setChecked(False)
        self.Cages_Button.setFlat(False)
        self.Factures_Button = QPushButton(self.MenuFrame)
        self.Factures_Button.setObjectName(u"Factures_Button")
        self.Factures_Button.setGeometry(QRect(6, 501, 227, 65))
        sizePolicy.setHeightForWidth(self.Factures_Button.sizePolicy().hasHeightForWidth())
        self.Factures_Button.setSizePolicy(sizePolicy)
        self.Factures_Button.setMinimumSize(QSize(227, 65))
        self.Factures_Button.setMaximumSize(QSize(227, 65))
        self.Factures_Button.setFont(font1)
        self.Factures_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 16px;\n"
"	font: 75 20pt \"Acme\";\n"
"}\n"
"QPushButton:checked:hover {\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(98, 114, 90);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(27, 27, 27);\n"
"	color: rgb(98, 114, 90);\n"
"	border-style: outset;\n"
"    	border-radius: 10px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Facture_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/Icons/Facture_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Factures_Button.setIcon(icon4)
        self.Factures_Button.setIconSize(QSize(32, 32))
        self.Factures_Button.setCheckable(True)
        self.Factures_Button.setChecked(False)
        self.Factures_Button.setFlat(False)
        self.Expenses_Button = QPushButton(self.MenuFrame)
        self.Expenses_Button.setObjectName(u"Expenses_Button")
        self.Expenses_Button.setGeometry(QRect(6, 596, 227, 65))
        sizePolicy.setHeightForWidth(self.Expenses_Button.sizePolicy().hasHeightForWidth())
        self.Expenses_Button.setSizePolicy(sizePolicy)
        self.Expenses_Button.setMinimumSize(QSize(227, 65))
        self.Expenses_Button.setMaximumSize(QSize(227, 65))
        self.Expenses_Button.setFont(font1)
        self.Expenses_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 16px;\n"
"	font: 75 20pt \"Acme\";\n"
"}\n"
"QPushButton:checked:hover {\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(98, 114, 90);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(27, 27, 27);\n"
"	color: rgb(98, 114, 90);\n"
"	border-style: outset;\n"
"    	border-radius: 10px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Expenses_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/Icons/Expenses_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Expenses_Button.setIcon(icon5)
        self.Expenses_Button.setIconSize(QSize(32, 32))
        self.Expenses_Button.setCheckable(True)
        self.Expenses_Button.setChecked(False)
        self.Expenses_Button.setFlat(False)
        self.Account_Logo = QLabel(self.MenuFrame)
        self.Account_Logo.setObjectName(u"Account_Logo")
        self.Account_Logo.setGeometry(QRect(17, 720, 68, 68))
        self.Account_Logo.setMinimumSize(QSize(68, 68))
        self.Account_Logo.setMaximumSize(QSize(68, 68))
        self.Account_Logo.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.Account_Logo.setPixmap(QPixmap(u":/Icons/Profile.png"))
        self.Account_Logo.setScaledContents(True)
        self.Account_Logo.setAlignment(Qt.AlignCenter)
        self.Account_Name = QLabel(self.MenuFrame)
        self.Account_Name.setObjectName(u"Account_Name")
        self.Account_Name.setGeometry(QRect(85, 730, 156, 50))
        self.Account_Name.setMinimumSize(QSize(156, 50))
        self.Account_Name.setMaximumSize(QSize(156, 50))
        font2 = QFont()
        font2.setFamilies([u"Acme"])
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        self.Account_Name.setFont(font2)
        self.Account_Name.setFocusPolicy(Qt.NoFocus)
        self.Account_Name.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Acme\";")
        self.Account_Name.setTextFormat(Qt.RichText)
        self.Account_Name.setScaledContents(True)
        self.Account_Name.setAlignment(Qt.AlignCenter)
        self.Account_Name.setWordWrap(True)
        self.Settings_Button = QPushButton(self.MenuFrame)
        self.Settings_Button.setObjectName(u"Settings_Button")
        self.Settings_Button.setGeometry(QRect(69, 799, 44, 44))
        sizePolicy.setHeightForWidth(self.Settings_Button.sizePolicy().hasHeightForWidth())
        self.Settings_Button.setSizePolicy(sizePolicy)
        self.Settings_Button.setMinimumSize(QSize(44, 44))
        self.Settings_Button.setMaximumSize(QSize(44, 44))
        self.Settings_Button.setFont(font1)
        self.Settings_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 10px;\n"
"	font: 75 20pt \"Acme\";\n"
"}\n"
"QPushButton:checked:hover {\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(88, 89, 114);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(27, 27, 27);\n"
"	color: rgb(98, 114, 90);\n"
"	border-style: outset;\n"
"    	border-radius: 10px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Settings_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/Icons/Settings_Blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Settings_Button.setIcon(icon6)
        self.Settings_Button.setIconSize(QSize(32, 32))
        self.Settings_Button.setCheckable(True)
        self.Settings_Button.setChecked(False)
        self.Settings_Button.setFlat(False)
        self.Logout_Button = QPushButton(self.MenuFrame)
        self.Logout_Button.setObjectName(u"Logout_Button")
        self.Logout_Button.setGeometry(QRect(129, 799, 44, 44))
        sizePolicy.setHeightForWidth(self.Logout_Button.sizePolicy().hasHeightForWidth())
        self.Logout_Button.setSizePolicy(sizePolicy)
        self.Logout_Button.setMinimumSize(QSize(44, 44))
        self.Logout_Button.setMaximumSize(QSize(44, 44))
        self.Logout_Button.setFont(font1)
        self.Logout_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 10px;\n"
"	font: 75 20pt \"Acme\";\n"
"}\n"
"QPushButton:checked:hover {\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	border-right: 3px solid rgb(114, 87, 88);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(27, 27, 27);\n"
"	color: rgb(98, 114, 90);\n"
"	border-style: outset;\n"
"    	border-radius: 10px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/Logout_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/Icons/Logout_Red.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Logout_Button.setIcon(icon7)
        self.Logout_Button.setIconSize(QSize(32, 32))
        self.Logout_Button.setCheckable(True)
        self.Logout_Button.setChecked(False)
        self.Logout_Button.setFlat(False)
        self.BackgroundFrame = QFrame(self.Window)
        self.BackgroundFrame.setObjectName(u"BackgroundFrame")
        self.BackgroundFrame.setGeometry(QRect(241, 0, 1031, 867))
        self.BackgroundFrame.setMinimumSize(QSize(1031, 867))
        self.BackgroundFrame.setMaximumSize(QSize(1031, 867))
        self.BackgroundFrame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"Orbitron\";\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.BackgroundFrame.setFrameShape(QFrame.StyledPanel)
        self.BackgroundFrame.setFrameShadow(QFrame.Raised)
        self.Menu_Pages = QStackedWidget(self.BackgroundFrame)
        self.Menu_Pages.setObjectName(u"Menu_Pages")
        self.Menu_Pages.setGeometry(QRect(0, 20, 1031, 825))
        self.Menu_Pages.setMinimumSize(QSize(1031, 825))
        self.Menu_Pages.setMaximumSize(QSize(1031, 825))
        self.Menu_Pages.setStyleSheet(u"border-style: outset;\n"
"border-radius: 20px;")
        self.Dashboard = QWidget()
        self.Dashboard.setObjectName(u"Dashboard")
        self.Dashboard_Logo = QLabel(self.Dashboard)
        self.Dashboard_Logo.setObjectName(u"Dashboard_Logo")
        self.Dashboard_Logo.setGeometry(QRect(23, 33, 32, 32))
        self.Dashboard_Logo.setMinimumSize(QSize(32, 32))
        self.Dashboard_Logo.setMaximumSize(QSize(32, 32))
        self.Dashboard_Logo.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.Dashboard_Logo.setPixmap(QPixmap(u":/Icons/Dashboard_White.png"))
        self.Dashboard_Logo.setScaledContents(True)
        self.Dashboard_Logo.setAlignment(Qt.AlignCenter)
        self.Dashboard_Message = QLabel(self.Dashboard)
        self.Dashboard_Message.setObjectName(u"Dashboard_Message")
        self.Dashboard_Message.setGeometry(QRect(65, 33, 760, 37))
        self.Dashboard_Message.setMinimumSize(QSize(760, 37))
        self.Dashboard_Message.setMaximumSize(QSize(760, 37))
        self.Dashboard_Message.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Dashboard_Message.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.AllFrame = QFrame(self.Dashboard)
        self.AllFrame.setObjectName(u"AllFrame")
        self.AllFrame.setGeometry(QRect(10, 101, 1001, 65))
        self.AllFrame.setMinimumSize(QSize(0, 65))
        self.AllFrame.setMaximumSize(QSize(16777215, 65))
        self.AllFrame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"	border: 2px solid #ffffff;\n"
"}")
        self.AllFrame.setFrameShape(QFrame.StyledPanel)
        self.AllFrame.setFrameShadow(QFrame.Raised)
        self.TND_Logo_2 = QLabel(self.AllFrame)
        self.TND_Logo_2.setObjectName(u"TND_Logo_2")
        self.TND_Logo_2.setGeometry(QRect(40, 10, 45, 45))
        self.TND_Logo_2.setMinimumSize(QSize(45, 45))
        self.TND_Logo_2.setMaximumSize(QSize(45, 45))
        self.TND_Logo_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.TND_Logo_2.setPixmap(QPixmap(u":/Icons/TND_White.png"))
        self.TND_Logo_2.setScaledContents(True)
        self.TND_Logo_2.setAlignment(Qt.AlignCenter)
        self.Earning_Text = QLabel(self.AllFrame)
        self.Earning_Text.setObjectName(u"Earning_Text")
        self.Earning_Text.setGeometry(QRect(95, 2, 163, 37))
        self.Earning_Text.setMinimumSize(QSize(163, 37))
        self.Earning_Text.setMaximumSize(QSize(163, 37))
        self.Earning_Text.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(251, 255, 146);\n"
"font: 75 25pt \"Acme\";\n"
"border:none;")
        self.Earning_Text.setAlignment(Qt.AlignCenter)
        self.Earning_Inter = QLabel(self.AllFrame)
        self.Earning_Inter.setObjectName(u"Earning_Inter")
        self.Earning_Inter.setGeometry(QRect(95, 30, 163, 37))
        self.Earning_Inter.setMinimumSize(QSize(163, 37))
        self.Earning_Inter.setMaximumSize(QSize(163, 37))
        self.Earning_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(251, 255, 146);font: 75 15pt 'Acme';")
        self.Earning_Inter.setAlignment(Qt.AlignCenter)
        self.Rabbits_Logo_2 = QLabel(self.AllFrame)
        self.Rabbits_Logo_2.setObjectName(u"Rabbits_Logo_2")
        self.Rabbits_Logo_2.setGeometry(QRect(268, 10, 45, 45))
        self.Rabbits_Logo_2.setMinimumSize(QSize(45, 45))
        self.Rabbits_Logo_2.setMaximumSize(QSize(45, 45))
        self.Rabbits_Logo_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.Rabbits_Logo_2.setPixmap(QPixmap(u":/Icons/Rabbit_White.png"))
        self.Rabbits_Logo_2.setScaledContents(True)
        self.Rabbits_Logo_2.setAlignment(Qt.AlignCenter)
        self.Rabbits_Text = QLabel(self.AllFrame)
        self.Rabbits_Text.setObjectName(u"Rabbits_Text")
        self.Rabbits_Text.setGeometry(QRect(323, 2, 163, 37))
        self.Rabbits_Text.setMinimumSize(QSize(163, 37))
        self.Rabbits_Text.setMaximumSize(QSize(163, 37))
        self.Rabbits_Text.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(137, 255, 141);\n"
"font: 75 25pt \"Acme\";")
        self.Rabbits_Text.setAlignment(Qt.AlignCenter)
        self.Rabbits_Inter = QLabel(self.AllFrame)
        self.Rabbits_Inter.setObjectName(u"Rabbits_Inter")
        self.Rabbits_Inter.setGeometry(QRect(323, 30, 163, 37))
        self.Rabbits_Inter.setMinimumSize(QSize(163, 37))
        self.Rabbits_Inter.setMaximumSize(QSize(163, 37))
        self.Rabbits_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(137, 255, 141);font: 75 15pt 'Acme';")
        self.Rabbits_Inter.setAlignment(Qt.AlignCenter)
        self.Customers_Logo_2 = QLabel(self.AllFrame)
        self.Customers_Logo_2.setObjectName(u"Customers_Logo_2")
        self.Customers_Logo_2.setGeometry(QRect(496, 10, 45, 45))
        self.Customers_Logo_2.setMinimumSize(QSize(45, 45))
        self.Customers_Logo_2.setMaximumSize(QSize(45, 45))
        self.Customers_Logo_2.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Customers_Logo_2.setPixmap(QPixmap(u":/Icons/Customer_Whitre.png"))
        self.Customers_Logo_2.setScaledContents(True)
        self.Customers_Logo_2.setAlignment(Qt.AlignCenter)
        self.Customers_Text = QLabel(self.AllFrame)
        self.Customers_Text.setObjectName(u"Customers_Text")
        self.Customers_Text.setGeometry(QRect(551, 2, 163, 37))
        self.Customers_Text.setMinimumSize(QSize(163, 37))
        self.Customers_Text.setMaximumSize(QSize(163, 37))
        self.Customers_Text.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(137, 255, 141);\n"
"font: 75 25pt \"Acme\";")
        self.Customers_Text.setAlignment(Qt.AlignCenter)
        self.Customers_Inter = QLabel(self.AllFrame)
        self.Customers_Inter.setObjectName(u"Customers_Inter")
        self.Customers_Inter.setGeometry(QRect(551, 30, 163, 37))
        self.Customers_Inter.setMinimumSize(QSize(163, 37))
        self.Customers_Inter.setMaximumSize(QSize(163, 37))
        self.Customers_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(137, 255, 141);font: 75 15pt 'Acme';")
        self.Customers_Inter.setAlignment(Qt.AlignCenter)
        self.Cages_Logo_2 = QLabel(self.AllFrame)
        self.Cages_Logo_2.setObjectName(u"Cages_Logo_2")
        self.Cages_Logo_2.setGeometry(QRect(724, 10, 45, 45))
        self.Cages_Logo_2.setMinimumSize(QSize(45, 45))
        self.Cages_Logo_2.setMaximumSize(QSize(45, 45))
        self.Cages_Logo_2.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Cages_Logo_2.setPixmap(QPixmap(u":/Icons/Cages_White.png"))
        self.Cages_Logo_2.setScaledContents(True)
        self.Cages_Logo_2.setAlignment(Qt.AlignCenter)
        self.Cages_Text = QLabel(self.AllFrame)
        self.Cages_Text.setObjectName(u"Cages_Text")
        self.Cages_Text.setGeometry(QRect(779, 2, 163, 37))
        self.Cages_Text.setMinimumSize(QSize(163, 37))
        self.Cages_Text.setMaximumSize(QSize(163, 37))
        self.Cages_Text.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(137, 255, 141);\n"
"font: 75 25pt \"Acme\";")
        self.Cages_Text.setAlignment(Qt.AlignCenter)
        self.Cages_Inter = QLabel(self.AllFrame)
        self.Cages_Inter.setObjectName(u"Cages_Inter")
        self.Cages_Inter.setGeometry(QRect(779, 30, 163, 37))
        self.Cages_Inter.setMinimumSize(QSize(163, 37))
        self.Cages_Inter.setMaximumSize(QSize(163, 37))
        self.Cages_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(137, 255, 141);font: 75 15pt 'Acme';")
        self.Cages_Inter.setAlignment(Qt.AlignCenter)
        self.Earning = QFrame(self.Dashboard)
        self.Earning.setObjectName(u"Earning")
        self.Earning.setGeometry(QRect(10, 179, 1001, 65))
        self.Earning.setMinimumSize(QSize(0, 65))
        self.Earning.setMaximumSize(QSize(16777215, 65))
        self.Earning.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"	border: 2px solid #ffffff;\n"
"}")
        self.Earning.setFrameShape(QFrame.StyledPanel)
        self.Earning.setFrameShadow(QFrame.Raised)
        self.TND_Logo_3 = QLabel(self.Earning)
        self.TND_Logo_3.setObjectName(u"TND_Logo_3")
        self.TND_Logo_3.setGeometry(QRect(40, 10, 45, 45))
        self.TND_Logo_3.setMinimumSize(QSize(45, 45))
        self.TND_Logo_3.setMaximumSize(QSize(45, 45))
        self.TND_Logo_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.TND_Logo_3.setPixmap(QPixmap(u":/Icons/TND_White.png"))
        self.TND_Logo_3.setScaledContents(True)
        self.TND_Logo_3.setAlignment(Qt.AlignCenter)
        self.Income_Text = QLabel(self.Earning)
        self.Income_Text.setObjectName(u"Income_Text")
        self.Income_Text.setGeometry(QRect(95, 2, 163, 37))
        self.Income_Text.setMinimumSize(QSize(163, 37))
        self.Income_Text.setMaximumSize(QSize(163, 37))
        self.Income_Text.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(251, 255, 146);\n"
"font: 75 25pt \"Acme\";\n"
"border:none;")
        self.Income_Text.setAlignment(Qt.AlignCenter)
        self.Income_Inter = QLabel(self.Earning)
        self.Income_Inter.setObjectName(u"Income_Inter")
        self.Income_Inter.setGeometry(QRect(95, 30, 163, 37))
        self.Income_Inter.setMinimumSize(QSize(163, 37))
        self.Income_Inter.setMaximumSize(QSize(163, 37))
        self.Income_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(251, 255, 146);font: 75 15pt 'Acme';")
        self.Income_Inter.setAlignment(Qt.AlignCenter)
        self.TND_Logo_4 = QLabel(self.Earning)
        self.TND_Logo_4.setObjectName(u"TND_Logo_4")
        self.TND_Logo_4.setGeometry(QRect(268, 10, 45, 45))
        self.TND_Logo_4.setMinimumSize(QSize(45, 45))
        self.TND_Logo_4.setMaximumSize(QSize(45, 45))
        self.TND_Logo_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.TND_Logo_4.setPixmap(QPixmap(u":/Icons/TND_White.png"))
        self.TND_Logo_4.setScaledContents(True)
        self.TND_Logo_4.setAlignment(Qt.AlignCenter)
        self.Expenses_Text = QLabel(self.Earning)
        self.Expenses_Text.setObjectName(u"Expenses_Text")
        self.Expenses_Text.setGeometry(QRect(323, 2, 163, 37))
        self.Expenses_Text.setMinimumSize(QSize(163, 37))
        self.Expenses_Text.setMaximumSize(QSize(163, 37))
        self.Expenses_Text.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(251, 255, 146);\n"
"font: 75 25pt \"Acme\";\n"
"border:none;")
        self.Expenses_Text.setAlignment(Qt.AlignCenter)
        self.Expenses_Inter = QLabel(self.Earning)
        self.Expenses_Inter.setObjectName(u"Expenses_Inter")
        self.Expenses_Inter.setGeometry(QRect(323, 30, 163, 37))
        self.Expenses_Inter.setMinimumSize(QSize(163, 37))
        self.Expenses_Inter.setMaximumSize(QSize(163, 37))
        self.Expenses_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(251, 255, 146);font: 75 15pt 'Acme';")
        self.Expenses_Inter.setAlignment(Qt.AlignCenter)
        self.Date_Logo = QLabel(self.Earning)
        self.Date_Logo.setObjectName(u"Date_Logo")
        self.Date_Logo.setGeometry(QRect(496, 10, 45, 45))
        self.Date_Logo.setMinimumSize(QSize(45, 45))
        self.Date_Logo.setMaximumSize(QSize(45, 45))
        self.Date_Logo.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Date_Logo.setPixmap(QPixmap(u":/Icons/Calendar_White.png"))
        self.Date_Logo.setScaledContents(True)
        self.Date_Logo.setAlignment(Qt.AlignCenter)
        self.LastIncome_Text = QLabel(self.Earning)
        self.LastIncome_Text.setObjectName(u"LastIncome_Text")
        self.LastIncome_Text.setGeometry(QRect(551, 2, 163, 37))
        self.LastIncome_Text.setMinimumSize(QSize(163, 37))
        self.LastIncome_Text.setMaximumSize(QSize(163, 37))
        self.LastIncome_Text.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(0, 170, 196);\n"
"font: 75 25pt \"Acme\";")
        self.LastIncome_Text.setAlignment(Qt.AlignCenter)
        self.LastIncome_Inter = QLabel(self.Earning)
        self.LastIncome_Inter.setObjectName(u"LastIncome_Inter")
        self.LastIncome_Inter.setGeometry(QRect(551, 30, 163, 37))
        self.LastIncome_Inter.setMinimumSize(QSize(163, 37))
        self.LastIncome_Inter.setMaximumSize(QSize(163, 37))
        self.LastIncome_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(0, 170, 196);font: 75 15pt 'Acme';")
        self.LastIncome_Inter.setAlignment(Qt.AlignCenter)
        self.Date_Logo_2 = QLabel(self.Earning)
        self.Date_Logo_2.setObjectName(u"Date_Logo_2")
        self.Date_Logo_2.setGeometry(QRect(724, 10, 45, 45))
        self.Date_Logo_2.setMinimumSize(QSize(45, 45))
        self.Date_Logo_2.setMaximumSize(QSize(45, 45))
        self.Date_Logo_2.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Date_Logo_2.setPixmap(QPixmap(u":/Icons/Expenses_White.png"))
        self.Date_Logo_2.setScaledContents(True)
        self.Date_Logo_2.setAlignment(Qt.AlignCenter)
        self.TopBuyer_Text = QLabel(self.Earning)
        self.TopBuyer_Text.setObjectName(u"TopBuyer_Text")
        self.TopBuyer_Text.setGeometry(QRect(779, 2, 211, 37))
        self.TopBuyer_Text.setMinimumSize(QSize(211, 37))
        self.TopBuyer_Text.setMaximumSize(QSize(211, 37))
        self.TopBuyer_Text.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(0, 170, 196);;\n"
"font: 75 25pt \"Acme\";")
        self.TopBuyer_Text.setAlignment(Qt.AlignCenter)
        self.TopBuyer_Inter = QLabel(self.Earning)
        self.TopBuyer_Inter.setObjectName(u"TopBuyer_Inter")
        self.TopBuyer_Inter.setGeometry(QRect(779, 30, 211, 37))
        self.TopBuyer_Inter.setMinimumSize(QSize(211, 37))
        self.TopBuyer_Inter.setMaximumSize(QSize(211, 37))
        self.TopBuyer_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(0, 170, 196);font: 75 15pt 'Acme';")
        self.TopBuyer_Inter.setAlignment(Qt.AlignCenter)
        self.Rabbit = QFrame(self.Dashboard)
        self.Rabbit.setObjectName(u"Rabbit")
        self.Rabbit.setGeometry(QRect(10, 266, 1001, 65))
        self.Rabbit.setMinimumSize(QSize(0, 65))
        self.Rabbit.setMaximumSize(QSize(16777215, 65))
        self.Rabbit.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"	border: 2px solid #ffffff;\n"
"}")
        self.Rabbit.setFrameShape(QFrame.StyledPanel)
        self.Rabbit.setFrameShadow(QFrame.Raised)
        self.Rabbits_Logo_3 = QLabel(self.Rabbit)
        self.Rabbits_Logo_3.setObjectName(u"Rabbits_Logo_3")
        self.Rabbits_Logo_3.setGeometry(QRect(40, 10, 45, 45))
        self.Rabbits_Logo_3.setMinimumSize(QSize(45, 45))
        self.Rabbits_Logo_3.setMaximumSize(QSize(45, 45))
        self.Rabbits_Logo_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.Rabbits_Logo_3.setPixmap(QPixmap(u":/Icons/Rabbit_White.png"))
        self.Rabbits_Logo_3.setScaledContents(True)
        self.Rabbits_Logo_3.setAlignment(Qt.AlignCenter)
        self.Males_Text = QLabel(self.Rabbit)
        self.Males_Text.setObjectName(u"Males_Text")
        self.Males_Text.setGeometry(QRect(95, 2, 163, 37))
        self.Males_Text.setMinimumSize(QSize(163, 37))
        self.Males_Text.setMaximumSize(QSize(163, 37))
        self.Males_Text.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(0, 140, 179);\n"
"font: 75 25pt \"Acme\";\n"
"border:none;")
        self.Males_Text.setAlignment(Qt.AlignCenter)
        self.Rabbits_Males_Inter = QLabel(self.Rabbit)
        self.Rabbits_Males_Inter.setObjectName(u"Rabbits_Males_Inter")
        self.Rabbits_Males_Inter.setGeometry(QRect(95, 30, 163, 37))
        self.Rabbits_Males_Inter.setMinimumSize(QSize(163, 37))
        self.Rabbits_Males_Inter.setMaximumSize(QSize(163, 37))
        self.Rabbits_Males_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color: rgb(0, 140, 179);;font: 75 15pt 'Acme';")
        self.Rabbits_Males_Inter.setAlignment(Qt.AlignCenter)
        self.Rabbits_Logo_4 = QLabel(self.Rabbit)
        self.Rabbits_Logo_4.setObjectName(u"Rabbits_Logo_4")
        self.Rabbits_Logo_4.setGeometry(QRect(268, 10, 45, 45))
        self.Rabbits_Logo_4.setMinimumSize(QSize(45, 45))
        self.Rabbits_Logo_4.setMaximumSize(QSize(45, 45))
        self.Rabbits_Logo_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.Rabbits_Logo_4.setPixmap(QPixmap(u":/Icons/Rabbit_White.png"))
        self.Rabbits_Logo_4.setScaledContents(True)
        self.Rabbits_Logo_4.setAlignment(Qt.AlignCenter)
        self.Females_Text = QLabel(self.Rabbit)
        self.Females_Text.setObjectName(u"Females_Text")
        self.Females_Text.setGeometry(QRect(323, 2, 163, 37))
        self.Females_Text.setMinimumSize(QSize(163, 37))
        self.Females_Text.setMaximumSize(QSize(163, 37))
        self.Females_Text.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(199, 0, 217);\n"
"font: 75 25pt \"Acme\";\n"
"border:none;")
        self.Females_Text.setAlignment(Qt.AlignCenter)
        self.Rabbits_Females_Inter = QLabel(self.Rabbit)
        self.Rabbits_Females_Inter.setObjectName(u"Rabbits_Females_Inter")
        self.Rabbits_Females_Inter.setGeometry(QRect(323, 30, 163, 37))
        self.Rabbits_Females_Inter.setMinimumSize(QSize(163, 37))
        self.Rabbits_Females_Inter.setMaximumSize(QSize(163, 37))
        self.Rabbits_Females_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(199, 0, 217);font: 75 15pt 'Acme';")
        self.Rabbits_Females_Inter.setAlignment(Qt.AlignCenter)
        self.Rabbits_Logo_5 = QLabel(self.Rabbit)
        self.Rabbits_Logo_5.setObjectName(u"Rabbits_Logo_5")
        self.Rabbits_Logo_5.setGeometry(QRect(496, 10, 45, 45))
        self.Rabbits_Logo_5.setMinimumSize(QSize(45, 45))
        self.Rabbits_Logo_5.setMaximumSize(QSize(45, 45))
        self.Rabbits_Logo_5.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Rabbits_Logo_5.setPixmap(QPixmap(u":/Icons/Rabbit_White.png"))
        self.Rabbits_Logo_5.setScaledContents(True)
        self.Rabbits_Logo_5.setAlignment(Qt.AlignCenter)
        self.Nulls_Text = QLabel(self.Rabbit)
        self.Nulls_Text.setObjectName(u"Nulls_Text")
        self.Nulls_Text.setGeometry(QRect(551, 2, 163, 37))
        self.Nulls_Text.setMinimumSize(QSize(163, 37))
        self.Nulls_Text.setMaximumSize(QSize(163, 37))
        self.Nulls_Text.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(182, 155, 0);\n"
"font: 75 25pt \"Acme\";")
        self.Nulls_Text.setAlignment(Qt.AlignCenter)
        self.Rabbits_Nulls_Inter = QLabel(self.Rabbit)
        self.Rabbits_Nulls_Inter.setObjectName(u"Rabbits_Nulls_Inter")
        self.Rabbits_Nulls_Inter.setGeometry(QRect(551, 30, 163, 37))
        self.Rabbits_Nulls_Inter.setMinimumSize(QSize(163, 37))
        self.Rabbits_Nulls_Inter.setMaximumSize(QSize(163, 37))
        self.Rabbits_Nulls_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(182, 155, 0);font: 75 15pt 'Acme';")
        self.Rabbits_Nulls_Inter.setAlignment(Qt.AlignCenter)
        self.Rabbits_Logo_6 = QLabel(self.Rabbit)
        self.Rabbits_Logo_6.setObjectName(u"Rabbits_Logo_6")
        self.Rabbits_Logo_6.setGeometry(QRect(724, 10, 45, 45))
        self.Rabbits_Logo_6.setMinimumSize(QSize(45, 45))
        self.Rabbits_Logo_6.setMaximumSize(QSize(45, 45))
        self.Rabbits_Logo_6.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Rabbits_Logo_6.setPixmap(QPixmap(u":/Icons/Rabbits_White.png"))
        self.Rabbits_Logo_6.setScaledContents(True)
        self.Rabbits_Logo_6.setAlignment(Qt.AlignCenter)
        self.All_Text_2 = QLabel(self.Rabbit)
        self.All_Text_2.setObjectName(u"All_Text_2")
        self.All_Text_2.setGeometry(QRect(779, 2, 163, 37))
        self.All_Text_2.setMinimumSize(QSize(163, 37))
        self.All_Text_2.setMaximumSize(QSize(163, 37))
        self.All_Text_2.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(137, 255, 141);\n"
"font: 75 25pt \"Acme\";")
        self.All_Text_2.setAlignment(Qt.AlignCenter)
        self.Rabbits_All_Inter = QLabel(self.Rabbit)
        self.Rabbits_All_Inter.setObjectName(u"Rabbits_All_Inter")
        self.Rabbits_All_Inter.setGeometry(QRect(779, 30, 163, 37))
        self.Rabbits_All_Inter.setMinimumSize(QSize(163, 37))
        self.Rabbits_All_Inter.setMaximumSize(QSize(163, 37))
        self.Rabbits_All_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(137, 255, 141);font: 75 15pt 'Acme';")
        self.Rabbits_All_Inter.setAlignment(Qt.AlignCenter)
        self.Rabbit_2 = QFrame(self.Dashboard)
        self.Rabbit_2.setObjectName(u"Rabbit_2")
        self.Rabbit_2.setGeometry(QRect(10, 331, 1001, 65))
        self.Rabbit_2.setMinimumSize(QSize(0, 65))
        self.Rabbit_2.setMaximumSize(QSize(16777215, 65))
        self.Rabbit_2.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"	border: 2px solid #ffffff;\n"
"}")
        self.Rabbit_2.setFrameShape(QFrame.StyledPanel)
        self.Rabbit_2.setFrameShadow(QFrame.Raised)
        self.Rabbits_Logo_7 = QLabel(self.Rabbit_2)
        self.Rabbits_Logo_7.setObjectName(u"Rabbits_Logo_7")
        self.Rabbits_Logo_7.setGeometry(QRect(40, 10, 45, 45))
        self.Rabbits_Logo_7.setMinimumSize(QSize(45, 45))
        self.Rabbits_Logo_7.setMaximumSize(QSize(45, 45))
        self.Rabbits_Logo_7.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.Rabbits_Logo_7.setPixmap(QPixmap(u":/Icons/Rabbit_White.png"))
        self.Rabbits_Logo_7.setScaledContents(True)
        self.Rabbits_Logo_7.setAlignment(Qt.AlignCenter)
        self.Disponible_Text = QLabel(self.Rabbit_2)
        self.Disponible_Text.setObjectName(u"Disponible_Text")
        self.Disponible_Text.setGeometry(QRect(95, 2, 163, 37))
        self.Disponible_Text.setMinimumSize(QSize(163, 37))
        self.Disponible_Text.setMaximumSize(QSize(163, 37))
        self.Disponible_Text.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(85, 255, 127);\n"
"font: 75 25pt \"Acme\";\n"
"border:none;")
        self.Disponible_Text.setAlignment(Qt.AlignCenter)
        self.Rabbits_Disponible_Inter = QLabel(self.Rabbit_2)
        self.Rabbits_Disponible_Inter.setObjectName(u"Rabbits_Disponible_Inter")
        self.Rabbits_Disponible_Inter.setGeometry(QRect(95, 30, 163, 37))
        self.Rabbits_Disponible_Inter.setMinimumSize(QSize(163, 37))
        self.Rabbits_Disponible_Inter.setMaximumSize(QSize(163, 37))
        self.Rabbits_Disponible_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(137, 255, 141);font: 75 15pt 'Acme';")
        self.Rabbits_Disponible_Inter.setAlignment(Qt.AlignCenter)
        self.Rabbits_Logo_8 = QLabel(self.Rabbit_2)
        self.Rabbits_Logo_8.setObjectName(u"Rabbits_Logo_8")
        self.Rabbits_Logo_8.setGeometry(QRect(268, 10, 45, 45))
        self.Rabbits_Logo_8.setMinimumSize(QSize(45, 45))
        self.Rabbits_Logo_8.setMaximumSize(QSize(45, 45))
        self.Rabbits_Logo_8.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.Rabbits_Logo_8.setPixmap(QPixmap(u":/Icons/Rabbit_White.png"))
        self.Rabbits_Logo_8.setScaledContents(True)
        self.Rabbits_Logo_8.setAlignment(Qt.AlignCenter)
        self.SoldOut_Text = QLabel(self.Rabbit_2)
        self.SoldOut_Text.setObjectName(u"SoldOut_Text")
        self.SoldOut_Text.setGeometry(QRect(323, 2, 163, 37))
        self.SoldOut_Text.setMinimumSize(QSize(163, 37))
        self.SoldOut_Text.setMaximumSize(QSize(163, 37))
        self.SoldOut_Text.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(170, 0, 0);\n"
"font: 75 25pt \"Acme\";\n"
"border:none;")
        self.SoldOut_Text.setAlignment(Qt.AlignCenter)
        self.Rabbits_SoldOut_Inter = QLabel(self.Rabbit_2)
        self.Rabbits_SoldOut_Inter.setObjectName(u"Rabbits_SoldOut_Inter")
        self.Rabbits_SoldOut_Inter.setGeometry(QRect(323, 30, 163, 37))
        self.Rabbits_SoldOut_Inter.setMinimumSize(QSize(163, 37))
        self.Rabbits_SoldOut_Inter.setMaximumSize(QSize(163, 37))
        self.Rabbits_SoldOut_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(170, 0, 0);font: 75 15pt 'Acme';")
        self.Rabbits_SoldOut_Inter.setAlignment(Qt.AlignCenter)
        self.Rabbits_Logo_9 = QLabel(self.Rabbit_2)
        self.Rabbits_Logo_9.setObjectName(u"Rabbits_Logo_9")
        self.Rabbits_Logo_9.setGeometry(QRect(496, 10, 45, 45))
        self.Rabbits_Logo_9.setMinimumSize(QSize(45, 45))
        self.Rabbits_Logo_9.setMaximumSize(QSize(45, 45))
        self.Rabbits_Logo_9.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Rabbits_Logo_9.setPixmap(QPixmap(u":/Icons/Rabbit_White.png"))
        self.Rabbits_Logo_9.setScaledContents(True)
        self.Rabbits_Logo_9.setAlignment(Qt.AlignCenter)
        self.Owned_Text = QLabel(self.Rabbit_2)
        self.Owned_Text.setObjectName(u"Owned_Text")
        self.Owned_Text.setGeometry(QRect(551, 2, 163, 37))
        self.Owned_Text.setMinimumSize(QSize(163, 37))
        self.Owned_Text.setMaximumSize(QSize(163, 37))
        self.Owned_Text.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(0, 170, 255);\n"
"font: 75 25pt \"Acme\";")
        self.Owned_Text.setAlignment(Qt.AlignCenter)
        self.Rabbits_Owned_Inter = QLabel(self.Rabbit_2)
        self.Rabbits_Owned_Inter.setObjectName(u"Rabbits_Owned_Inter")
        self.Rabbits_Owned_Inter.setGeometry(QRect(551, 30, 163, 37))
        self.Rabbits_Owned_Inter.setMinimumSize(QSize(163, 37))
        self.Rabbits_Owned_Inter.setMaximumSize(QSize(163, 37))
        self.Rabbits_Owned_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(0, 170, 255);font: 75 15pt 'Acme';")
        self.Rabbits_Owned_Inter.setAlignment(Qt.AlignCenter)
        self.Rabbits_Logo_10 = QLabel(self.Rabbit_2)
        self.Rabbits_Logo_10.setObjectName(u"Rabbits_Logo_10")
        self.Rabbits_Logo_10.setGeometry(QRect(724, 10, 45, 45))
        self.Rabbits_Logo_10.setMinimumSize(QSize(45, 45))
        self.Rabbits_Logo_10.setMaximumSize(QSize(45, 45))
        self.Rabbits_Logo_10.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Rabbits_Logo_10.setPixmap(QPixmap(u":/Icons/Rabbit_White.png"))
        self.Rabbits_Logo_10.setScaledContents(True)
        self.Rabbits_Logo_10.setAlignment(Qt.AlignCenter)
        self.Dead_Text = QLabel(self.Rabbit_2)
        self.Dead_Text.setObjectName(u"Dead_Text")
        self.Dead_Text.setGeometry(QRect(779, 2, 163, 37))
        self.Dead_Text.setMinimumSize(QSize(163, 37))
        self.Dead_Text.setMaximumSize(QSize(163, 37))
        self.Dead_Text.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(234, 66, 0);\n"
"font: 75 25pt \"Acme\";")
        self.Dead_Text.setAlignment(Qt.AlignCenter)
        self.Rabbits_Dead_Inter = QLabel(self.Rabbit_2)
        self.Rabbits_Dead_Inter.setObjectName(u"Rabbits_Dead_Inter")
        self.Rabbits_Dead_Inter.setGeometry(QRect(779, 30, 163, 37))
        self.Rabbits_Dead_Inter.setMinimumSize(QSize(163, 37))
        self.Rabbits_Dead_Inter.setMaximumSize(QSize(163, 37))
        self.Rabbits_Dead_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(234, 66, 0);font: 75 15pt 'Acme';")
        self.Rabbits_Dead_Inter.setAlignment(Qt.AlignCenter)
        self.Cage = QFrame(self.Dashboard)
        self.Cage.setObjectName(u"Cage")
        self.Cage.setGeometry(QRect(10, 421, 1001, 65))
        self.Cage.setMinimumSize(QSize(0, 65))
        self.Cage.setMaximumSize(QSize(16777215, 65))
        self.Cage.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"	border: 2px solid #ffffff;\n"
"}")
        self.Cage.setFrameShape(QFrame.StyledPanel)
        self.Cage.setFrameShadow(QFrame.Raised)
        self.Cages_Logo_3 = QLabel(self.Cage)
        self.Cages_Logo_3.setObjectName(u"Cages_Logo_3")
        self.Cages_Logo_3.setGeometry(QRect(40, 10, 45, 45))
        self.Cages_Logo_3.setMinimumSize(QSize(45, 45))
        self.Cages_Logo_3.setMaximumSize(QSize(45, 45))
        self.Cages_Logo_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.Cages_Logo_3.setPixmap(QPixmap(u":/Icons/Cages_White.png"))
        self.Cages_Logo_3.setScaledContents(True)
        self.Cages_Logo_3.setAlignment(Qt.AlignCenter)
        self.Males_Text_2 = QLabel(self.Cage)
        self.Males_Text_2.setObjectName(u"Males_Text_2")
        self.Males_Text_2.setGeometry(QRect(95, 2, 163, 37))
        self.Males_Text_2.setMinimumSize(QSize(163, 37))
        self.Males_Text_2.setMaximumSize(QSize(163, 37))
        self.Males_Text_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(0, 140, 179);\n"
"font: 75 25pt \"Acme\";\n"
"border:none;")
        self.Males_Text_2.setAlignment(Qt.AlignCenter)
        self.Cages_Males_Inter = QLabel(self.Cage)
        self.Cages_Males_Inter.setObjectName(u"Cages_Males_Inter")
        self.Cages_Males_Inter.setGeometry(QRect(95, 30, 163, 37))
        self.Cages_Males_Inter.setMinimumSize(QSize(163, 37))
        self.Cages_Males_Inter.setMaximumSize(QSize(163, 37))
        self.Cages_Males_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color: rgb(0, 140, 179);;font: 75 15pt 'Acme';")
        self.Cages_Males_Inter.setAlignment(Qt.AlignCenter)
        self.Cages_Logo_4 = QLabel(self.Cage)
        self.Cages_Logo_4.setObjectName(u"Cages_Logo_4")
        self.Cages_Logo_4.setGeometry(QRect(268, 10, 45, 45))
        self.Cages_Logo_4.setMinimumSize(QSize(45, 45))
        self.Cages_Logo_4.setMaximumSize(QSize(45, 45))
        self.Cages_Logo_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.Cages_Logo_4.setPixmap(QPixmap(u":/Icons/Cages_White.png"))
        self.Cages_Logo_4.setScaledContents(True)
        self.Cages_Logo_4.setAlignment(Qt.AlignCenter)
        self.Females_Text_2 = QLabel(self.Cage)
        self.Females_Text_2.setObjectName(u"Females_Text_2")
        self.Females_Text_2.setGeometry(QRect(323, 2, 163, 37))
        self.Females_Text_2.setMinimumSize(QSize(163, 37))
        self.Females_Text_2.setMaximumSize(QSize(163, 37))
        self.Females_Text_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(199, 0, 217);\n"
"font: 75 25pt \"Acme\";\n"
"border:none;")
        self.Females_Text_2.setAlignment(Qt.AlignCenter)
        self.Cages_Females_Inter = QLabel(self.Cage)
        self.Cages_Females_Inter.setObjectName(u"Cages_Females_Inter")
        self.Cages_Females_Inter.setGeometry(QRect(323, 30, 163, 37))
        self.Cages_Females_Inter.setMinimumSize(QSize(163, 37))
        self.Cages_Females_Inter.setMaximumSize(QSize(163, 37))
        self.Cages_Females_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(199, 0, 217);font: 75 15pt 'Acme';")
        self.Cages_Females_Inter.setAlignment(Qt.AlignCenter)
        self.Cages_Logo_5 = QLabel(self.Cage)
        self.Cages_Logo_5.setObjectName(u"Cages_Logo_5")
        self.Cages_Logo_5.setGeometry(QRect(496, 10, 45, 45))
        self.Cages_Logo_5.setMinimumSize(QSize(45, 45))
        self.Cages_Logo_5.setMaximumSize(QSize(45, 45))
        self.Cages_Logo_5.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Cages_Logo_5.setPixmap(QPixmap(u":/Icons/Cages_White.png"))
        self.Cages_Logo_5.setScaledContents(True)
        self.Cages_Logo_5.setAlignment(Qt.AlignCenter)
        self.Kids_Text = QLabel(self.Cage)
        self.Kids_Text.setObjectName(u"Kids_Text")
        self.Kids_Text.setGeometry(QRect(551, 2, 163, 37))
        self.Kids_Text.setMinimumSize(QSize(163, 37))
        self.Kids_Text.setMaximumSize(QSize(163, 37))
        self.Kids_Text.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(182, 155, 0);\n"
"font: 75 25pt \"Acme\";")
        self.Kids_Text.setAlignment(Qt.AlignCenter)
        self.Cages_Kids_Inter = QLabel(self.Cage)
        self.Cages_Kids_Inter.setObjectName(u"Cages_Kids_Inter")
        self.Cages_Kids_Inter.setGeometry(QRect(551, 30, 163, 37))
        self.Cages_Kids_Inter.setMinimumSize(QSize(163, 37))
        self.Cages_Kids_Inter.setMaximumSize(QSize(163, 37))
        self.Cages_Kids_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(182, 155, 0);font: 75 15pt 'Acme';")
        self.Cages_Kids_Inter.setAlignment(Qt.AlignCenter)
        self.Cages_Logo_6 = QLabel(self.Cage)
        self.Cages_Logo_6.setObjectName(u"Cages_Logo_6")
        self.Cages_Logo_6.setGeometry(QRect(724, 10, 45, 45))
        self.Cages_Logo_6.setMinimumSize(QSize(45, 45))
        self.Cages_Logo_6.setMaximumSize(QSize(45, 45))
        self.Cages_Logo_6.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Cages_Logo_6.setPixmap(QPixmap(u":/Icons/Cages_White.png"))
        self.Cages_Logo_6.setScaledContents(True)
        self.Cages_Logo_6.setAlignment(Qt.AlignCenter)
        self.All_Text = QLabel(self.Cage)
        self.All_Text.setObjectName(u"All_Text")
        self.All_Text.setGeometry(QRect(779, 2, 163, 37))
        self.All_Text.setMinimumSize(QSize(163, 37))
        self.All_Text.setMaximumSize(QSize(163, 37))
        self.All_Text.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(137, 255, 141);\n"
"font: 75 25pt \"Acme\";")
        self.All_Text.setAlignment(Qt.AlignCenter)
        self.Cages_All_Inter = QLabel(self.Cage)
        self.Cages_All_Inter.setObjectName(u"Cages_All_Inter")
        self.Cages_All_Inter.setGeometry(QRect(779, 30, 163, 37))
        self.Cages_All_Inter.setMinimumSize(QSize(163, 37))
        self.Cages_All_Inter.setMaximumSize(QSize(163, 37))
        self.Cages_All_Inter.setStyleSheet(u"border:none;background-color: rgba(0, 0, 0, 0);color:rgb(137, 255, 141);font: 75 15pt 'Acme';")
        self.Cages_All_Inter.setAlignment(Qt.AlignCenter)
        self.Dashboard_QText = QTextEdit(self.Dashboard)
        self.Dashboard_QText.setObjectName(u"Dashboard_QText")
        self.Dashboard_QText.setGeometry(QRect(10, 510, 1001, 291))
        self.Dashboard_QText.setStyleSheet(u"QTextEdit{\n"
"	background-color:rgb(25, 25, 25);\n"
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
        self.Dashboard_QText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Dashboard_QText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Dashboard_QText.setReadOnly(True)
        self.Menu_Pages.addWidget(self.Dashboard)
        self.Customers = QWidget()
        self.Customers.setObjectName(u"Customers")
        self.Customer_Windows = QTabWidget(self.Customers)
        self.Customer_Windows.setObjectName(u"Customer_Windows")
        self.Customer_Windows.setGeometry(QRect(25, 90, 981, 722))
        self.Customer_Windows.setMinimumSize(QSize(981, 722))
        self.Customer_Windows.setMaximumSize(QSize(981, 722))
        self.Customer_Windows.setStyleSheet(u"QTabWidget::pane {\n"
"    	border: 1px solid #C2C7CB;\n"
"	position: absolute;\n"
"    	top: -0.5em;\n"
"\n"
"}\n"
"QTabWidget::tab-bar {\n"
"	alignment: center;\n"
"}\n"
"QTabBar::tab {\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"   	border: 2px solid #ffffff;\n"
"	border-radius:50px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	padding: 7px;\n"
"	font: 75 13pt \"Acme\";\n"
"}\n"
"QTabBar::tab:selected {\n"
"	background-color: rgb(27, 27, 27);\n"
"	color: rgb(98, 114, 90);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-radius:50px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	padding: 7px;\n"
"}\n"
"QTabWidget::tab{\n"
"	background-color: rgb(255, 255, 0);\n"
"}")
        self.Customer_View = QWidget()
        self.Customer_View.setObjectName(u"Customer_View")
        self.View_Customers_Frame = QFrame(self.Customer_View)
        self.View_Customers_Frame.setObjectName(u"View_Customers_Frame")
        self.View_Customers_Frame.setEnabled(True)
        self.View_Customers_Frame.setGeometry(QRect(40, 40, 913, 580))
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
        self.ToolsFrame_View = QFrame(self.Customer_View)
        self.ToolsFrame_View.setObjectName(u"ToolsFrame_View")
        self.ToolsFrame_View.setGeometry(QRect(40, 630, 913, 47))
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
        self.Customer_Windows.addTab(self.Customer_View, "")
        self.Customer_Advanced = QWidget()
        self.Customer_Advanced.setObjectName(u"Customer_Advanced")
        self.CustomersTable_Advanced = QTableWidget(self.Customer_Advanced)
        if (self.CustomersTable_Advanced.columnCount() < 5):
            self.CustomersTable_Advanced.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setIcon(icon1);
        self.CustomersTable_Advanced.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setIcon(icon1);
        self.CustomersTable_Advanced.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon8 = QIcon()
        icon8.addFile(u":/Icons/Phone_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/Icons/Phone_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setIcon(icon8);
        self.CustomersTable_Advanced.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        icon9 = QIcon()
        icon9.addFile(u":/Icons/Address_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/Icons/Address_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setIcon(icon9);
        self.CustomersTable_Advanced.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        icon10 = QIcon()
        icon10.addFile(u":/Icons/Actions_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/Icons/Actions_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setIcon(icon10);
        self.CustomersTable_Advanced.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.CustomersTable_Advanced.setObjectName(u"CustomersTable_Advanced")
        self.CustomersTable_Advanced.setGeometry(QRect(40, 40, 913, 580))
        self.CustomersTable_Advanced.setMinimumSize(QSize(913, 580))
        self.CustomersTable_Advanced.setMaximumSize(QSize(913, 580))
        self.CustomersTable_Advanced.setStyleSheet(u"QHeaderView::section{\n"
"	font: 75 13pt \"Acme\";\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid #6c6c6c;\n"
"	border-top-right-radius: 6px;\n"
"	border-bottom-right-radius: 6px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	font: 75 13pt \"Acme\";\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.CustomersTable_Advanced.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.CustomersTable_Advanced.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.CustomersTable_Advanced.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.CustomersTable_Advanced.setTabKeyNavigation(True)
        self.CustomersTable_Advanced.setSortingEnabled(False)
        self.CustomersTable_Advanced.horizontalHeader().setCascadingSectionResizes(False)
        self.CustomersTable_Advanced.horizontalHeader().setDefaultSectionSize(180)
        self.CustomersTable_Advanced.horizontalHeader().setHighlightSections(True)
        self.CustomersTable_Advanced.horizontalHeader().setStretchLastSection(True)
        self.CustomersTable_Advanced.verticalHeader().setVisible(False)
        self.CustomersTable_Advanced.verticalHeader().setHighlightSections(False)
        self.ToolsFrame_Advanced = QFrame(self.Customer_Advanced)
        self.ToolsFrame_Advanced.setObjectName(u"ToolsFrame_Advanced")
        self.ToolsFrame_Advanced.setGeometry(QRect(40, 630, 913, 47))
        self.ToolsFrame_Advanced.setMinimumSize(QSize(913, 47))
        self.ToolsFrame_Advanced.setMaximumSize(QSize(913, 47))
        self.ToolsFrame_Advanced.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.ToolsFrame_Advanced.setFrameShape(QFrame.StyledPanel)
        self.ToolsFrame_Advanced.setFrameShadow(QFrame.Raised)
        self.Exporting_Frame = QFrame(self.ToolsFrame_Advanced)
        self.Exporting_Frame.setObjectName(u"Exporting_Frame")
        self.Exporting_Frame.setGeometry(QRect(781, 0, 132, 47))
        self.Exporting_Frame.setMinimumSize(QSize(0, 47))
        self.Exporting_Frame.setMaximumSize(QSize(16777215, 47))
        self.Exporting_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 73, 73);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Exporting_Frame.setFrameShape(QFrame.StyledPanel)
        self.Exporting_Frame.setFrameShadow(QFrame.Raised)
        self.Export_PDF_Customers = QPushButton(self.Exporting_Frame)
        self.Export_PDF_Customers.setObjectName(u"Export_PDF_Customers")
        self.Export_PDF_Customers.setGeometry(QRect(71, 7, 43, 33))
        self.Export_PDF_Customers.setMinimumSize(QSize(43, 33))
        self.Export_PDF_Customers.setMaximumSize(QSize(43, 33))
        font3 = QFont()
        font3.setFamilies([u"Orbitron"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        self.Export_PDF_Customers.setFont(font3)
        self.Export_PDF_Customers.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Export_PDF_Customers.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/PDF_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/PDF_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/PDF_Green.png);\n"
"}")
        self.Export_PDF_Customers.setIconSize(QSize(20, 20))
        self.Export_PDF_Customers.setCheckable(False)
        self.Export_PDF_Customers.setAutoRepeat(False)
        self.Export_PDF_Customers.setAutoExclusive(False)
        self.Export_PDF_Customers.setAutoRepeatDelay(50)
        self.Export_PDF_Customers.setAutoRepeatInterval(10)
        self.Export_Exel_Customers = QPushButton(self.Exporting_Frame)
        self.Export_Exel_Customers.setObjectName(u"Export_Exel_Customers")
        self.Export_Exel_Customers.setGeometry(QRect(18, 7, 43, 33))
        self.Export_Exel_Customers.setMinimumSize(QSize(43, 33))
        self.Export_Exel_Customers.setMaximumSize(QSize(43, 33))
        self.Export_Exel_Customers.setFont(font3)
        self.Export_Exel_Customers.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Export_Exel_Customers.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Exel_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Exel_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/Exel_Green.png);\n"
"}")
        self.Export_Exel_Customers.setIconSize(QSize(20, 20))
        self.Export_Exel_Customers.setCheckable(False)
        self.Export_Exel_Customers.setAutoRepeat(False)
        self.Export_Exel_Customers.setAutoExclusive(False)
        self.Export_Exel_Customers.setAutoRepeatDelay(50)
        self.Export_Exel_Customers.setAutoRepeatInterval(10)
        self.Exportation_CustomerAdvanced_Info = QLabel(self.ToolsFrame_Advanced)
        self.Exportation_CustomerAdvanced_Info.setObjectName(u"Exportation_CustomerAdvanced_Info")
        self.Exportation_CustomerAdvanced_Info.setGeometry(QRect(20, 3, 750, 41))
        self.Exportation_CustomerAdvanced_Info.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 12pt \"Acme\";\n"
"}")
        self.Exportation_CustomerAdvanced_Info.setAlignment(Qt.AlignCenter)
        self.Exportation_CustomerAdvanced_Info.setWordWrap(True)
        self.Customer_Windows.addTab(self.Customer_Advanced, "")
        self.Add_Customer_View = QPushButton(self.Customers)
        self.Add_Customer_View.setObjectName(u"Add_Customer_View")
        self.Add_Customer_View.setEnabled(True)
        self.Add_Customer_View.setGeometry(QRect(67, 28, 43, 33))
        self.Add_Customer_View.setMinimumSize(QSize(43, 33))
        self.Add_Customer_View.setMaximumSize(QSize(43, 33))
        self.Add_Customer_View.setFont(font3)
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
        self.Filter_Frame_View = QFrame(self.Customers)
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
        icon11 = QIcon()
        icon11.addFile(u":/Icons/Search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.FilterBy_Customer.addItem(icon11, "")
        self.FilterBy_Customer.addItem(icon1, "")
        self.FilterBy_Customer.addItem(icon1, "")
        self.FilterBy_Customer.addItem(icon8, "")
        self.FilterBy_Customer.addItem(icon9, "")
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
        icon12 = QIcon()
        icon12.addFile(u":/Icons/Gender_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon12.addFile(u":/Icons/Gender_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterGender_Customer.addItem(icon12, "")
        icon13 = QIcon()
        icon13.addFile(u":/Icons/Gender_Null_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/Icons/Gender_Null_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterGender_Customer.addItem(icon13, "")
        icon14 = QIcon()
        icon14.addFile(u":/Icons/Gender_Male_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon14.addFile(u":/Icons/Gender_Male_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterGender_Customer.addItem(icon14, "")
        icon15 = QIcon()
        icon15.addFile(u":/Icons/Gender_Female_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon15.addFile(u":/Icons/Gender_Female_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterGender_Customer.addItem(icon15, "")
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
        self.Ordre_Customer.setFont(font3)
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
        self.Menu_Pages.addWidget(self.Customers)
        self.Rabbits = QWidget()
        self.Rabbits.setObjectName(u"Rabbits")
        self.Filter_Rabbits_Frame_View = QFrame(self.Rabbits)
        self.Filter_Rabbits_Frame_View.setObjectName(u"Filter_Rabbits_Frame_View")
        self.Filter_Rabbits_Frame_View.setGeometry(QRect(360, 20, 620, 47))
        self.Filter_Rabbits_Frame_View.setMinimumSize(QSize(620, 47))
        self.Filter_Rabbits_Frame_View.setMaximumSize(QSize(620, 47))
        self.Filter_Rabbits_Frame_View.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 73, 73);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Filter_Rabbits_Frame_View.setFrameShape(QFrame.StyledPanel)
        self.Filter_Rabbits_Frame_View.setFrameShadow(QFrame.Raised)
        self.FilterBy_Rabbits = QComboBox(self.Filter_Rabbits_Frame_View)
        self.FilterBy_Rabbits.addItem(icon11, "")
        icon16 = QIcon()
        icon16.addFile(u":/Icons/Rabbit_Tag.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon16.addFile(u":/Icons/Rabbit_Tag.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon16, "")
        self.FilterBy_Rabbits.addItem(icon16, "")
        icon17 = QIcon()
        icon17.addFile(u":/Icons/Calendar_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon17.addFile(u":/Icons/Calendar_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon17, "")
        icon18 = QIcon()
        icon18.addFile(u":/Icons/Rabbit_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon18.addFile(u":/Icons/Rabbit_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon18, "")
        icon19 = QIcon()
        icon19.addFile(u":/Icons/Rabbit_Tree_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon19.addFile(u":/Icons/Rabbit_Tree_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon19, "")
        self.FilterBy_Rabbits.addItem(icon19, "")
        self.FilterBy_Rabbits.addItem(icon19, "")
        icon20 = QIcon()
        icon20.addFile(u":/Icons/Settings_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon20.addFile(u":/Icons/Settings_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon20, "")
        self.FilterBy_Rabbits.addItem(icon3, "")
        self.FilterBy_Rabbits.addItem(icon4, "")
        self.FilterBy_Rabbits.addItem(icon1, "")
        icon21 = QIcon()
        icon21.addFile(u":/Icons/TND_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon21.addFile(u":/Icons/TND_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon21, "")
        self.FilterBy_Rabbits.addItem(icon21, "")
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
        self.FilterGender_Rabbits = QComboBox(self.Filter_Rabbits_Frame_View)
        self.FilterGender_Rabbits.addItem(icon12, "")
        self.FilterGender_Rabbits.addItem(icon13, "")
        self.FilterGender_Rabbits.addItem(icon14, "")
        self.FilterGender_Rabbits.addItem(icon15, "")
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
        self.Ordre_Rabbits = QPushButton(self.Filter_Rabbits_Frame_View)
        self.Ordre_Rabbits.setObjectName(u"Ordre_Rabbits")
        self.Ordre_Rabbits.setGeometry(QRect(18, 7, 43, 33))
        self.Ordre_Rabbits.setMinimumSize(QSize(43, 33))
        self.Ordre_Rabbits.setMaximumSize(QSize(43, 33))
        self.Ordre_Rabbits.setFont(font3)
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
        self.Rabbit_Windows = QTabWidget(self.Rabbits)
        self.Rabbit_Windows.setObjectName(u"Rabbit_Windows")
        self.Rabbit_Windows.setGeometry(QRect(25, 90, 981, 722))
        self.Rabbit_Windows.setMinimumSize(QSize(981, 722))
        self.Rabbit_Windows.setMaximumSize(QSize(981, 722))
        self.Rabbit_Windows.setStyleSheet(u"QTabWidget::pane {\n"
"    	border: 1px solid #C2C7CB;\n"
"	position: absolute;\n"
"    	top: -0.5em;\n"
"\n"
"}\n"
"QTabWidget::tab-bar {\n"
"	alignment: center;\n"
"}\n"
"QTabBar::tab {\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"   	border: 2px solid #ffffff;\n"
"	border-radius:50px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	padding: 7px;\n"
"	font: 75 13pt \"Acme\";\n"
"}\n"
"QTabBar::tab:selected {\n"
"	background-color: rgb(27, 27, 27);\n"
"	color: rgb(98, 114, 90);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-radius:50px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	padding: 7px;\n"
"}\n"
"QTabWidget::tab{\n"
"	background-color: rgb(255, 255, 0);\n"
"}")
        self.Rabbit_View = QWidget()
        self.Rabbit_View.setObjectName(u"Rabbit_View")
        self.View_Rabbits_Frame = QFrame(self.Rabbit_View)
        self.View_Rabbits_Frame.setObjectName(u"View_Rabbits_Frame")
        self.View_Rabbits_Frame.setEnabled(True)
        self.View_Rabbits_Frame.setGeometry(QRect(40, 40, 913, 580))
        self.View_Rabbits_Frame.setMinimumSize(QSize(913, 580))
        self.View_Rabbits_Frame.setMaximumSize(QSize(913, 580))
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
        self.Scroll_Rabbits_Area_View.setGeometry(QRect(0, 20, 913, 540))
        self.Scroll_Rabbits_Area_View.setMinimumSize(QSize(913, 0))
        self.Scroll_Rabbits_Area_View.setMaximumSize(QSize(913, 16777215))
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
        self.gridLayoutWidget_2.setGeometry(QRect(1, 0, 911, 541))
        self.GridLayout_Rabbits_View = QGridLayout(self.gridLayoutWidget_2)
        self.GridLayout_Rabbits_View.setObjectName(u"GridLayout_Rabbits_View")
        self.GridLayout_Rabbits_View.setContentsMargins(0, 0, 0, 0)
        self.Scroll_Rabbits_Area_View.setWidget(self.SrollWidget_Rabbits_View)
        self.ToolsFrame_Rabbits_View = QFrame(self.Rabbit_View)
        self.ToolsFrame_Rabbits_View.setObjectName(u"ToolsFrame_Rabbits_View")
        self.ToolsFrame_Rabbits_View.setGeometry(QRect(40, 630, 913, 47))
        self.ToolsFrame_Rabbits_View.setMinimumSize(QSize(913, 47))
        self.ToolsFrame_Rabbits_View.setMaximumSize(QSize(913, 47))
        self.ToolsFrame_Rabbits_View.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.ToolsFrame_Rabbits_View.setFrameShape(QFrame.StyledPanel)
        self.ToolsFrame_Rabbits_View.setFrameShadow(QFrame.Raised)
        self.Exportation_RabbitsView_Info = QLabel(self.ToolsFrame_Rabbits_View)
        self.Exportation_RabbitsView_Info.setObjectName(u"Exportation_RabbitsView_Info")
        self.Exportation_RabbitsView_Info.setGeometry(QRect(20, 3, 871, 41))
        self.Exportation_RabbitsView_Info.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 12pt \"Acme\";\n"
"}")
        self.Exportation_RabbitsView_Info.setAlignment(Qt.AlignCenter)
        self.Exportation_RabbitsView_Info.setWordWrap(True)
        self.Rabbit_Windows.addTab(self.Rabbit_View, "")
        self.Rabbits_Advanced = QWidget()
        self.Rabbits_Advanced.setObjectName(u"Rabbits_Advanced")
        self.RabbitsTable_Advanced = QTableWidget(self.Rabbits_Advanced)
        if (self.RabbitsTable_Advanced.columnCount() < 7):
            self.RabbitsTable_Advanced.setColumnCount(7)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setIcon(icon18);
        self.RabbitsTable_Advanced.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setIcon(icon18);
        self.RabbitsTable_Advanced.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setIcon(icon18);
        self.RabbitsTable_Advanced.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setIcon(icon2);
        self.RabbitsTable_Advanced.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setIcon(icon3);
        self.RabbitsTable_Advanced.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        icon22 = QIcon()
        icon22.addFile(u":/Icons/Settings_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon22.addFile(u":/Icons/Settings_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setIcon(icon22);
        self.RabbitsTable_Advanced.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setIcon(icon10);
        self.RabbitsTable_Advanced.setHorizontalHeaderItem(6, __qtablewidgetitem11)
        self.RabbitsTable_Advanced.setObjectName(u"RabbitsTable_Advanced")
        self.RabbitsTable_Advanced.setGeometry(QRect(40, 40, 913, 580))
        self.RabbitsTable_Advanced.setMinimumSize(QSize(913, 580))
        self.RabbitsTable_Advanced.setMaximumSize(QSize(913, 580))
        self.RabbitsTable_Advanced.setStyleSheet(u"QHeaderView::section{\n"
"	font: 75 13pt \"Acme\";\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid #6c6c6c;\n"
"	border-top-right-radius: 6px;\n"
"	border-bottom-right-radius: 6px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	font: 75 13pt \"Acme\";\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.RabbitsTable_Advanced.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.RabbitsTable_Advanced.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.RabbitsTable_Advanced.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.RabbitsTable_Advanced.setTabKeyNavigation(True)
        self.RabbitsTable_Advanced.setSortingEnabled(False)
        self.RabbitsTable_Advanced.horizontalHeader().setCascadingSectionResizes(False)
        self.RabbitsTable_Advanced.horizontalHeader().setDefaultSectionSize(127)
        self.RabbitsTable_Advanced.horizontalHeader().setHighlightSections(False)
        self.RabbitsTable_Advanced.horizontalHeader().setStretchLastSection(True)
        self.RabbitsTable_Advanced.verticalHeader().setVisible(False)
        self.RabbitsTable_Advanced.verticalHeader().setHighlightSections(False)
        self.ToolsFrame_Rabbits_Advanced = QFrame(self.Rabbits_Advanced)
        self.ToolsFrame_Rabbits_Advanced.setObjectName(u"ToolsFrame_Rabbits_Advanced")
        self.ToolsFrame_Rabbits_Advanced.setGeometry(QRect(40, 630, 913, 47))
        self.ToolsFrame_Rabbits_Advanced.setMinimumSize(QSize(913, 47))
        self.ToolsFrame_Rabbits_Advanced.setMaximumSize(QSize(913, 47))
        self.ToolsFrame_Rabbits_Advanced.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.ToolsFrame_Rabbits_Advanced.setFrameShape(QFrame.StyledPanel)
        self.ToolsFrame_Rabbits_Advanced.setFrameShadow(QFrame.Raised)
        self.Exporting_Rabbits_Frame = QFrame(self.ToolsFrame_Rabbits_Advanced)
        self.Exporting_Rabbits_Frame.setObjectName(u"Exporting_Rabbits_Frame")
        self.Exporting_Rabbits_Frame.setGeometry(QRect(781, 0, 132, 47))
        self.Exporting_Rabbits_Frame.setMinimumSize(QSize(0, 47))
        self.Exporting_Rabbits_Frame.setMaximumSize(QSize(16777215, 47))
        self.Exporting_Rabbits_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 73, 73);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Exporting_Rabbits_Frame.setFrameShape(QFrame.StyledPanel)
        self.Exporting_Rabbits_Frame.setFrameShadow(QFrame.Raised)
        self.Export_PDF_Rabbits = QPushButton(self.Exporting_Rabbits_Frame)
        self.Export_PDF_Rabbits.setObjectName(u"Export_PDF_Rabbits")
        self.Export_PDF_Rabbits.setGeometry(QRect(71, 7, 43, 33))
        self.Export_PDF_Rabbits.setMinimumSize(QSize(43, 33))
        self.Export_PDF_Rabbits.setMaximumSize(QSize(43, 33))
        self.Export_PDF_Rabbits.setFont(font3)
        self.Export_PDF_Rabbits.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Export_PDF_Rabbits.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/PDF_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/PDF_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/PDF_Green.png);\n"
"}")
        self.Export_PDF_Rabbits.setIconSize(QSize(20, 20))
        self.Export_PDF_Rabbits.setCheckable(False)
        self.Export_PDF_Rabbits.setAutoRepeat(False)
        self.Export_PDF_Rabbits.setAutoExclusive(False)
        self.Export_PDF_Rabbits.setAutoRepeatDelay(50)
        self.Export_PDF_Rabbits.setAutoRepeatInterval(10)
        self.Export_Exel_Rabbits = QPushButton(self.Exporting_Rabbits_Frame)
        self.Export_Exel_Rabbits.setObjectName(u"Export_Exel_Rabbits")
        self.Export_Exel_Rabbits.setGeometry(QRect(18, 7, 43, 33))
        self.Export_Exel_Rabbits.setMinimumSize(QSize(43, 33))
        self.Export_Exel_Rabbits.setMaximumSize(QSize(43, 33))
        self.Export_Exel_Rabbits.setFont(font3)
        self.Export_Exel_Rabbits.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Export_Exel_Rabbits.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Exel_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Exel_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/Exel_Green.png);\n"
"}")
        self.Export_Exel_Rabbits.setIconSize(QSize(20, 20))
        self.Export_Exel_Rabbits.setCheckable(False)
        self.Export_Exel_Rabbits.setAutoRepeat(False)
        self.Export_Exel_Rabbits.setAutoExclusive(False)
        self.Export_Exel_Rabbits.setAutoRepeatDelay(50)
        self.Export_Exel_Rabbits.setAutoRepeatInterval(10)
        self.Exportation_RabbitsAdvanced_Info = QLabel(self.ToolsFrame_Rabbits_Advanced)
        self.Exportation_RabbitsAdvanced_Info.setObjectName(u"Exportation_RabbitsAdvanced_Info")
        self.Exportation_RabbitsAdvanced_Info.setGeometry(QRect(20, 3, 750, 41))
        self.Exportation_RabbitsAdvanced_Info.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 12pt \"Acme\";\n"
"}")
        self.Exportation_RabbitsAdvanced_Info.setAlignment(Qt.AlignCenter)
        self.Exportation_RabbitsAdvanced_Info.setWordWrap(True)
        self.Rabbit_Windows.addTab(self.Rabbits_Advanced, "")
        self.Add_Rabbit_View = QPushButton(self.Rabbits)
        self.Add_Rabbit_View.setObjectName(u"Add_Rabbit_View")
        self.Add_Rabbit_View.setEnabled(True)
        self.Add_Rabbit_View.setGeometry(QRect(67, 28, 43, 33))
        self.Add_Rabbit_View.setMinimumSize(QSize(43, 33))
        self.Add_Rabbit_View.setMaximumSize(QSize(43, 33))
        self.Add_Rabbit_View.setFont(font3)
        self.Add_Rabbit_View.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Add_Rabbit_View.setStyleSheet(u"QPushButton {\n"
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
        self.Add_Rabbit_View.setIconSize(QSize(20, 20))
        self.Add_Rabbit_View.setCheckable(False)
        self.Add_Rabbit_View.setAutoRepeat(False)
        self.Add_Rabbit_View.setAutoExclusive(False)
        self.Add_Rabbit_View.setAutoRepeatDelay(50)
        self.Add_Rabbit_View.setAutoRepeatInterval(10)
        self.Rabbit_Tree = QPushButton(self.Rabbits)
        self.Rabbit_Tree.setObjectName(u"Rabbit_Tree")
        self.Rabbit_Tree.setEnabled(True)
        self.Rabbit_Tree.setGeometry(QRect(125, 28, 43, 33))
        self.Rabbit_Tree.setMinimumSize(QSize(43, 33))
        self.Rabbit_Tree.setMaximumSize(QSize(43, 33))
        self.Rabbit_Tree.setFont(font3)
        self.Rabbit_Tree.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Rabbit_Tree.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Rabbit_Tree_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Rabbit_Tree_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Rabbit_Tree_Green.png);\n"
"}")
        self.Rabbit_Tree.setIconSize(QSize(20, 20))
        self.Rabbit_Tree.setCheckable(False)
        self.Rabbit_Tree.setAutoRepeat(False)
        self.Rabbit_Tree.setAutoExclusive(False)
        self.Rabbit_Tree.setAutoRepeatDelay(50)
        self.Rabbit_Tree.setAutoRepeatInterval(10)
        self.Menu_Pages.addWidget(self.Rabbits)
        self.Cages = QWidget()
        self.Cages.setObjectName(u"Cages")
        self.Cages_Tree = QPushButton(self.Cages)
        self.Cages_Tree.setObjectName(u"Cages_Tree")
        self.Cages_Tree.setEnabled(True)
        self.Cages_Tree.setGeometry(QRect(125, 28, 43, 33))
        self.Cages_Tree.setMinimumSize(QSize(43, 33))
        self.Cages_Tree.setMaximumSize(QSize(43, 33))
        self.Cages_Tree.setFont(font3)
        self.Cages_Tree.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Cages_Tree.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Cage_Tree_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Cage_Tree_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Cage_Tree_Green.png);\n"
"}")
        self.Cages_Tree.setIconSize(QSize(20, 20))
        self.Cages_Tree.setCheckable(False)
        self.Cages_Tree.setAutoRepeat(False)
        self.Cages_Tree.setAutoExclusive(False)
        self.Cages_Tree.setAutoRepeatDelay(50)
        self.Cages_Tree.setAutoRepeatInterval(10)
        self.Cages_Windows = QTabWidget(self.Cages)
        self.Cages_Windows.setObjectName(u"Cages_Windows")
        self.Cages_Windows.setGeometry(QRect(25, 90, 981, 722))
        self.Cages_Windows.setMinimumSize(QSize(981, 722))
        self.Cages_Windows.setMaximumSize(QSize(981, 722))
        self.Cages_Windows.setStyleSheet(u"QTabWidget::pane {\n"
"    	border: 1px solid #C2C7CB;\n"
"	position: absolute;\n"
"    	top: -0.5em;\n"
"\n"
"}\n"
"QTabWidget::tab-bar {\n"
"	alignment: center;\n"
"}\n"
"QTabBar::tab {\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"   	border: 2px solid #ffffff;\n"
"	border-radius:50px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	padding: 7px;\n"
"	font: 75 13pt \"Acme\";\n"
"}\n"
"QTabBar::tab:selected {\n"
"	background-color: rgb(27, 27, 27);\n"
"	color: rgb(98, 114, 90);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-radius:50px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	padding: 7px;\n"
"}\n"
"QTabWidget::tab{\n"
"	background-color: rgb(255, 255, 0);\n"
"}")
        self.Cage_View = QWidget()
        self.Cage_View.setObjectName(u"Cage_View")
        self.View_Cages_Frame = QFrame(self.Cage_View)
        self.View_Cages_Frame.setObjectName(u"View_Cages_Frame")
        self.View_Cages_Frame.setEnabled(True)
        self.View_Cages_Frame.setGeometry(QRect(40, 40, 913, 580))
        self.View_Cages_Frame.setMinimumSize(QSize(913, 580))
        self.View_Cages_Frame.setMaximumSize(QSize(913, 580))
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
        self.Scroll_Cages_Area_View.setGeometry(QRect(0, 20, 913, 540))
        self.Scroll_Cages_Area_View.setMinimumSize(QSize(913, 0))
        self.Scroll_Cages_Area_View.setMaximumSize(QSize(913, 16777215))
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
        self.gridLayoutWidget_3.setGeometry(QRect(1, 0, 911, 541))
        self.GridLayout_Cages_View = QGridLayout(self.gridLayoutWidget_3)
        self.GridLayout_Cages_View.setObjectName(u"GridLayout_Cages_View")
        self.GridLayout_Cages_View.setContentsMargins(0, 0, 0, 0)
        self.Scroll_Cages_Area_View.setWidget(self.SrollWidget_Cages_View)
        self.ToolsFrame_Cages_View = QFrame(self.Cage_View)
        self.ToolsFrame_Cages_View.setObjectName(u"ToolsFrame_Cages_View")
        self.ToolsFrame_Cages_View.setGeometry(QRect(40, 630, 913, 47))
        self.ToolsFrame_Cages_View.setMinimumSize(QSize(913, 47))
        self.ToolsFrame_Cages_View.setMaximumSize(QSize(913, 47))
        self.ToolsFrame_Cages_View.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.ToolsFrame_Cages_View.setFrameShape(QFrame.StyledPanel)
        self.ToolsFrame_Cages_View.setFrameShadow(QFrame.Raised)
        self.Exportation_CagesView_Info = QLabel(self.ToolsFrame_Cages_View)
        self.Exportation_CagesView_Info.setObjectName(u"Exportation_CagesView_Info")
        self.Exportation_CagesView_Info.setGeometry(QRect(20, 3, 871, 41))
        self.Exportation_CagesView_Info.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 12pt \"Acme\";\n"
"}")
        self.Exportation_CagesView_Info.setAlignment(Qt.AlignCenter)
        self.Exportation_CagesView_Info.setWordWrap(True)
        self.Cages_Windows.addTab(self.Cage_View, "")
        self.Cages_Advanced = QWidget()
        self.Cages_Advanced.setObjectName(u"Cages_Advanced")
        self.CagesTable_Advanced = QTableWidget(self.Cages_Advanced)
        if (self.CagesTable_Advanced.columnCount() < 4):
            self.CagesTable_Advanced.setColumnCount(4)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setIcon(icon3);
        self.CagesTable_Advanced.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setIcon(icon21);
        self.CagesTable_Advanced.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        icon23 = QIcon()
        icon23.addFile(u":/Icons/Edit_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon23.addFile(u":/Icons/Edit_Blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setIcon(icon23);
        self.CagesTable_Advanced.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setIcon(icon10);
        self.CagesTable_Advanced.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        self.CagesTable_Advanced.setObjectName(u"CagesTable_Advanced")
        self.CagesTable_Advanced.setGeometry(QRect(40, 40, 913, 580))
        self.CagesTable_Advanced.setMinimumSize(QSize(913, 580))
        self.CagesTable_Advanced.setMaximumSize(QSize(913, 580))
        self.CagesTable_Advanced.setStyleSheet(u"QHeaderView::section{\n"
"	font: 75 13pt \"Acme\";\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid #6c6c6c;\n"
"	border-top-right-radius: 6px;\n"
"	border-bottom-right-radius: 6px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	font: 75 13pt \"Acme\";\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.CagesTable_Advanced.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.CagesTable_Advanced.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.CagesTable_Advanced.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.CagesTable_Advanced.setTabKeyNavigation(True)
        self.CagesTable_Advanced.setSortingEnabled(False)
        self.CagesTable_Advanced.horizontalHeader().setCascadingSectionResizes(False)
        self.CagesTable_Advanced.horizontalHeader().setDefaultSectionSize(150)
        self.CagesTable_Advanced.horizontalHeader().setHighlightSections(False)
        self.CagesTable_Advanced.horizontalHeader().setStretchLastSection(True)
        self.CagesTable_Advanced.verticalHeader().setVisible(False)
        self.CagesTable_Advanced.verticalHeader().setHighlightSections(False)
        self.ToolsFrame_Cages_Advanced = QFrame(self.Cages_Advanced)
        self.ToolsFrame_Cages_Advanced.setObjectName(u"ToolsFrame_Cages_Advanced")
        self.ToolsFrame_Cages_Advanced.setGeometry(QRect(40, 630, 913, 47))
        self.ToolsFrame_Cages_Advanced.setMinimumSize(QSize(913, 47))
        self.ToolsFrame_Cages_Advanced.setMaximumSize(QSize(913, 47))
        self.ToolsFrame_Cages_Advanced.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.ToolsFrame_Cages_Advanced.setFrameShape(QFrame.StyledPanel)
        self.ToolsFrame_Cages_Advanced.setFrameShadow(QFrame.Raised)
        self.Exporting_Cages_Frame = QFrame(self.ToolsFrame_Cages_Advanced)
        self.Exporting_Cages_Frame.setObjectName(u"Exporting_Cages_Frame")
        self.Exporting_Cages_Frame.setGeometry(QRect(781, 0, 132, 47))
        self.Exporting_Cages_Frame.setMinimumSize(QSize(0, 47))
        self.Exporting_Cages_Frame.setMaximumSize(QSize(16777215, 47))
        self.Exporting_Cages_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 73, 73);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Exporting_Cages_Frame.setFrameShape(QFrame.StyledPanel)
        self.Exporting_Cages_Frame.setFrameShadow(QFrame.Raised)
        self.Export_PDF_Cages = QPushButton(self.Exporting_Cages_Frame)
        self.Export_PDF_Cages.setObjectName(u"Export_PDF_Cages")
        self.Export_PDF_Cages.setGeometry(QRect(71, 7, 43, 33))
        self.Export_PDF_Cages.setMinimumSize(QSize(43, 33))
        self.Export_PDF_Cages.setMaximumSize(QSize(43, 33))
        self.Export_PDF_Cages.setFont(font3)
        self.Export_PDF_Cages.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Export_PDF_Cages.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/PDF_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/PDF_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/PDF_Green.png);\n"
"}")
        self.Export_PDF_Cages.setIconSize(QSize(20, 20))
        self.Export_PDF_Cages.setCheckable(False)
        self.Export_PDF_Cages.setAutoRepeat(False)
        self.Export_PDF_Cages.setAutoExclusive(False)
        self.Export_PDF_Cages.setAutoRepeatDelay(50)
        self.Export_PDF_Cages.setAutoRepeatInterval(10)
        self.Export_Exel_Cages = QPushButton(self.Exporting_Cages_Frame)
        self.Export_Exel_Cages.setObjectName(u"Export_Exel_Cages")
        self.Export_Exel_Cages.setGeometry(QRect(18, 7, 43, 33))
        self.Export_Exel_Cages.setMinimumSize(QSize(43, 33))
        self.Export_Exel_Cages.setMaximumSize(QSize(43, 33))
        self.Export_Exel_Cages.setFont(font3)
        self.Export_Exel_Cages.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Export_Exel_Cages.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Exel_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Exel_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/Exel_Green.png);\n"
"}")
        self.Export_Exel_Cages.setIconSize(QSize(20, 20))
        self.Export_Exel_Cages.setCheckable(False)
        self.Export_Exel_Cages.setAutoRepeat(False)
        self.Export_Exel_Cages.setAutoExclusive(False)
        self.Export_Exel_Cages.setAutoRepeatDelay(50)
        self.Export_Exel_Cages.setAutoRepeatInterval(10)
        self.Exportation_CagesAdvanced_Info = QLabel(self.ToolsFrame_Cages_Advanced)
        self.Exportation_CagesAdvanced_Info.setObjectName(u"Exportation_CagesAdvanced_Info")
        self.Exportation_CagesAdvanced_Info.setGeometry(QRect(20, 3, 750, 41))
        self.Exportation_CagesAdvanced_Info.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 12pt \"Acme\";\n"
"}")
        self.Exportation_CagesAdvanced_Info.setAlignment(Qt.AlignCenter)
        self.Exportation_CagesAdvanced_Info.setWordWrap(True)
        self.Cages_Windows.addTab(self.Cages_Advanced, "")
        self.Add_Cage_View = QPushButton(self.Cages)
        self.Add_Cage_View.setObjectName(u"Add_Cage_View")
        self.Add_Cage_View.setEnabled(True)
        self.Add_Cage_View.setGeometry(QRect(67, 28, 43, 33))
        self.Add_Cage_View.setMinimumSize(QSize(43, 33))
        self.Add_Cage_View.setMaximumSize(QSize(43, 33))
        self.Add_Cage_View.setFont(font3)
        self.Add_Cage_View.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Add_Cage_View.setStyleSheet(u"QPushButton {\n"
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
        self.Add_Cage_View.setIconSize(QSize(20, 20))
        self.Add_Cage_View.setCheckable(False)
        self.Add_Cage_View.setAutoRepeat(False)
        self.Add_Cage_View.setAutoExclusive(False)
        self.Add_Cage_View.setAutoRepeatDelay(50)
        self.Add_Cage_View.setAutoRepeatInterval(10)
        self.Filter_Cages_Frame_View = QFrame(self.Cages)
        self.Filter_Cages_Frame_View.setObjectName(u"Filter_Cages_Frame_View")
        self.Filter_Cages_Frame_View.setGeometry(QRect(360, 20, 620, 47))
        self.Filter_Cages_Frame_View.setMinimumSize(QSize(620, 47))
        self.Filter_Cages_Frame_View.setMaximumSize(QSize(620, 47))
        self.Filter_Cages_Frame_View.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 73, 73);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Filter_Cages_Frame_View.setFrameShape(QFrame.StyledPanel)
        self.Filter_Cages_Frame_View.setFrameShadow(QFrame.Raised)
        self.FilterBy_Cages = QComboBox(self.Filter_Cages_Frame_View)
        self.FilterBy_Cages.addItem(icon11, "")
        self.FilterBy_Cages.addItem(icon3, "")
        self.FilterBy_Cages.addItem(icon4, "")
        self.FilterBy_Cages.addItem(icon1, "")
        self.FilterBy_Cages.addItem(icon21, "")
        self.FilterBy_Cages.addItem(icon21, "")
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
        self.FilterGender_Cages.addItem(icon12, "")
        self.FilterGender_Cages.addItem(icon14, "")
        self.FilterGender_Cages.addItem(icon15, "")
        self.FilterGender_Cages.addItem(icon13, "")
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
        self.Ordre_Cages.setFont(font3)
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
        self.Search_Cages.setGeometry(QRect(331, 7, 275, 33))
        self.Search_Cages.setMinimumSize(QSize(275, 33))
        self.Search_Cages.setMaximumSize(QSize(275, 31))
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
        self.Menu_Pages.addWidget(self.Cages)
        self.Factures = QWidget()
        self.Factures.setObjectName(u"Factures")
        self.Add_Facture_View = QPushButton(self.Factures)
        self.Add_Facture_View.setObjectName(u"Add_Facture_View")
        self.Add_Facture_View.setEnabled(True)
        self.Add_Facture_View.setGeometry(QRect(67, 28, 43, 33))
        self.Add_Facture_View.setMinimumSize(QSize(43, 33))
        self.Add_Facture_View.setMaximumSize(QSize(43, 33))
        self.Add_Facture_View.setFont(font3)
        self.Add_Facture_View.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Add_Facture_View.setStyleSheet(u"QPushButton {\n"
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
"	image: url(:/Icons/Add_Facture_Green.png);\n"
"}")
        self.Add_Facture_View.setIconSize(QSize(20, 20))
        self.Add_Facture_View.setCheckable(False)
        self.Add_Facture_View.setAutoRepeat(False)
        self.Add_Facture_View.setAutoExclusive(False)
        self.Add_Facture_View.setAutoRepeatDelay(50)
        self.Add_Facture_View.setAutoRepeatInterval(10)
        self.Filter_Facture_Frame_View = QFrame(self.Factures)
        self.Filter_Facture_Frame_View.setObjectName(u"Filter_Facture_Frame_View")
        self.Filter_Facture_Frame_View.setGeometry(QRect(486, 20, 494, 47))
        self.Filter_Facture_Frame_View.setMinimumSize(QSize(494, 47))
        self.Filter_Facture_Frame_View.setMaximumSize(QSize(494, 47))
        self.Filter_Facture_Frame_View.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 73, 73);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Filter_Facture_Frame_View.setFrameShape(QFrame.StyledPanel)
        self.Filter_Facture_Frame_View.setFrameShadow(QFrame.Raised)
        self.FilterBy_Facture = QComboBox(self.Filter_Facture_Frame_View)
        self.FilterBy_Facture.addItem(icon11, "")
        self.FilterBy_Facture.addItem(icon4, "")
        self.FilterBy_Facture.addItem(icon17, "")
        self.FilterBy_Facture.addItem(icon1, "")
        self.FilterBy_Facture.addItem(icon21, "")
        self.FilterBy_Facture.setObjectName(u"FilterBy_Facture")
        self.FilterBy_Facture.setGeometry(QRect(71, 7, 120, 33))
        self.FilterBy_Facture.setMinimumSize(QSize(120, 33))
        self.FilterBy_Facture.setMaximumSize(QSize(120, 33))
        self.FilterBy_Facture.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid white;\n"
"	border-radius:6px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 12pt \"Acme\";\n"
"	padding-left: 15px;\n"
"	selection-background-color: #2980B9;\n"
"}")
        self.Ordre_Facture = QPushButton(self.Filter_Facture_Frame_View)
        self.Ordre_Facture.setObjectName(u"Ordre_Facture")
        self.Ordre_Facture.setGeometry(QRect(18, 7, 43, 33))
        self.Ordre_Facture.setMinimumSize(QSize(43, 33))
        self.Ordre_Facture.setMaximumSize(QSize(43, 33))
        self.Ordre_Facture.setFont(font3)
        self.Ordre_Facture.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Ordre_Facture.setStyleSheet(u"QPushButton {\n"
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
        self.Ordre_Facture.setIconSize(QSize(20, 20))
        self.Ordre_Facture.setCheckable(True)
        self.Ordre_Facture.setChecked(False)
        self.Ordre_Facture.setAutoRepeat(False)
        self.Ordre_Facture.setAutoExclusive(False)
        self.Ordre_Facture.setAutoRepeatDelay(50)
        self.Ordre_Facture.setAutoRepeatInterval(10)
        self.Search_Facture = QLineEdit(self.Filter_Facture_Frame_View)
        self.Search_Facture.setObjectName(u"Search_Facture")
        self.Search_Facture.setGeometry(QRect(201, 7, 275, 33))
        self.Search_Facture.setMinimumSize(QSize(275, 33))
        self.Search_Facture.setMaximumSize(QSize(275, 31))
        self.Search_Facture.setStyleSheet(u"QLineEdit {\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	padding-left: 30px;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-image: url(:/Icons/Search.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 10pt \"Acme\";\n"
"}")
        self.Facture_Windows = QTabWidget(self.Factures)
        self.Facture_Windows.setObjectName(u"Facture_Windows")
        self.Facture_Windows.setGeometry(QRect(25, 90, 981, 722))
        self.Facture_Windows.setMinimumSize(QSize(981, 722))
        self.Facture_Windows.setMaximumSize(QSize(981, 722))
        self.Facture_Windows.setStyleSheet(u"QTabWidget::pane {\n"
"    	border: 1px solid #C2C7CB;\n"
"	position: absolute;\n"
"    	top: -0.5em;\n"
"\n"
"}\n"
"QTabWidget::tab-bar {\n"
"	alignment: center;\n"
"}\n"
"QTabBar::tab {\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"   	border: 2px solid #ffffff;\n"
"	border-radius:50px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	padding: 7px;\n"
"	font: 75 13pt \"Acme\";\n"
"}\n"
"QTabBar::tab:selected {\n"
"	background-color: rgb(27, 27, 27);\n"
"	color: rgb(98, 114, 90);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-radius:50px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	padding: 7px;\n"
"}\n"
"QTabWidget::tab{\n"
"	background-color: rgb(255, 255, 0);\n"
"}")
        self.Facture_View = QWidget()
        self.Facture_View.setObjectName(u"Facture_View")
        self.View_Facture_Frame = QFrame(self.Facture_View)
        self.View_Facture_Frame.setObjectName(u"View_Facture_Frame")
        self.View_Facture_Frame.setEnabled(True)
        self.View_Facture_Frame.setGeometry(QRect(40, 40, 913, 580))
        self.View_Facture_Frame.setMinimumSize(QSize(913, 580))
        self.View_Facture_Frame.setMaximumSize(QSize(913, 580))
        self.View_Facture_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.View_Facture_Frame.setFrameShape(QFrame.Box)
        self.View_Facture_Frame.setFrameShadow(QFrame.Plain)
        self.Scroll_Facture_Area_View = QScrollArea(self.View_Facture_Frame)
        self.Scroll_Facture_Area_View.setObjectName(u"Scroll_Facture_Area_View")
        self.Scroll_Facture_Area_View.setGeometry(QRect(0, 20, 913, 540))
        self.Scroll_Facture_Area_View.setMinimumSize(QSize(913, 0))
        self.Scroll_Facture_Area_View.setMaximumSize(QSize(913, 16777215))
        self.Scroll_Facture_Area_View.setAutoFillBackground(False)
        self.Scroll_Facture_Area_View.setStyleSheet(u"")
        self.Scroll_Facture_Area_View.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Scroll_Facture_Area_View.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Scroll_Facture_Area_View.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.SrollWidget_Facture_View = QWidget()
        self.SrollWidget_Facture_View.setObjectName(u"SrollWidget_Facture_View")
        self.SrollWidget_Facture_View.setGeometry(QRect(0, 0, 913, 540))
        self.SrollWidget_Facture_View.setMinimumSize(QSize(913, 0))
        self.SrollWidget_Facture_View.setMaximumSize(QSize(913, 16777215))
        self.gridLayoutWidget_4 = QWidget(self.SrollWidget_Facture_View)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(1, 0, 911, 541))
        self.GridLayout_Facture_View = QGridLayout(self.gridLayoutWidget_4)
        self.GridLayout_Facture_View.setObjectName(u"GridLayout_Facture_View")
        self.GridLayout_Facture_View.setContentsMargins(0, 0, 0, 0)
        self.Scroll_Facture_Area_View.setWidget(self.SrollWidget_Facture_View)
        self.ToolsFrame_Facture_View = QFrame(self.Facture_View)
        self.ToolsFrame_Facture_View.setObjectName(u"ToolsFrame_Facture_View")
        self.ToolsFrame_Facture_View.setGeometry(QRect(40, 630, 913, 47))
        self.ToolsFrame_Facture_View.setMinimumSize(QSize(913, 47))
        self.ToolsFrame_Facture_View.setMaximumSize(QSize(913, 47))
        self.ToolsFrame_Facture_View.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.ToolsFrame_Facture_View.setFrameShape(QFrame.StyledPanel)
        self.ToolsFrame_Facture_View.setFrameShadow(QFrame.Raised)
        self.Exportation_FactureView_Info = QLabel(self.ToolsFrame_Facture_View)
        self.Exportation_FactureView_Info.setObjectName(u"Exportation_FactureView_Info")
        self.Exportation_FactureView_Info.setGeometry(QRect(20, 3, 871, 41))
        self.Exportation_FactureView_Info.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 12pt \"Acme\";\n"
"}")
        self.Exportation_FactureView_Info.setAlignment(Qt.AlignCenter)
        self.Exportation_FactureView_Info.setWordWrap(True)
        self.Facture_Windows.addTab(self.Facture_View, "")
        self.Facture_Advanced = QWidget()
        self.Facture_Advanced.setObjectName(u"Facture_Advanced")
        self.FactureTable_Advanced = QTableWidget(self.Facture_Advanced)
        if (self.FactureTable_Advanced.columnCount() < 5):
            self.FactureTable_Advanced.setColumnCount(5)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setIcon(icon4);
        self.FactureTable_Advanced.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setIcon(icon17);
        self.FactureTable_Advanced.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setIcon(icon1);
        self.FactureTable_Advanced.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setIcon(icon21);
        self.FactureTable_Advanced.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setIcon(icon10);
        self.FactureTable_Advanced.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        self.FactureTable_Advanced.setObjectName(u"FactureTable_Advanced")
        self.FactureTable_Advanced.setGeometry(QRect(40, 40, 913, 580))
        self.FactureTable_Advanced.setMinimumSize(QSize(913, 580))
        self.FactureTable_Advanced.setMaximumSize(QSize(913, 580))
        self.FactureTable_Advanced.setStyleSheet(u"QHeaderView::section{\n"
"	font: 75 13pt \"Acme\";\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid #6c6c6c;\n"
"	border-top-right-radius: 6px;\n"
"	border-bottom-right-radius: 6px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	font: 75 13pt \"Acme\";\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.FactureTable_Advanced.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.FactureTable_Advanced.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.FactureTable_Advanced.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.FactureTable_Advanced.setTabKeyNavigation(True)
        self.FactureTable_Advanced.setSortingEnabled(False)
        self.FactureTable_Advanced.horizontalHeader().setCascadingSectionResizes(False)
        self.FactureTable_Advanced.horizontalHeader().setDefaultSectionSize(180)
        self.FactureTable_Advanced.horizontalHeader().setHighlightSections(False)
        self.FactureTable_Advanced.horizontalHeader().setStretchLastSection(True)
        self.FactureTable_Advanced.verticalHeader().setVisible(False)
        self.FactureTable_Advanced.verticalHeader().setHighlightSections(False)
        self.ToolsFrame_Facture_Advanced = QFrame(self.Facture_Advanced)
        self.ToolsFrame_Facture_Advanced.setObjectName(u"ToolsFrame_Facture_Advanced")
        self.ToolsFrame_Facture_Advanced.setGeometry(QRect(40, 630, 913, 47))
        self.ToolsFrame_Facture_Advanced.setMinimumSize(QSize(913, 47))
        self.ToolsFrame_Facture_Advanced.setMaximumSize(QSize(913, 47))
        self.ToolsFrame_Facture_Advanced.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.ToolsFrame_Facture_Advanced.setFrameShape(QFrame.StyledPanel)
        self.ToolsFrame_Facture_Advanced.setFrameShadow(QFrame.Raised)
        self.Exporting_Factures_Frame = QFrame(self.ToolsFrame_Facture_Advanced)
        self.Exporting_Factures_Frame.setObjectName(u"Exporting_Factures_Frame")
        self.Exporting_Factures_Frame.setGeometry(QRect(781, 0, 132, 47))
        self.Exporting_Factures_Frame.setMinimumSize(QSize(0, 47))
        self.Exporting_Factures_Frame.setMaximumSize(QSize(16777215, 47))
        self.Exporting_Factures_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 73, 73);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Exporting_Factures_Frame.setFrameShape(QFrame.StyledPanel)
        self.Exporting_Factures_Frame.setFrameShadow(QFrame.Raised)
        self.Export_PDF_Facture = QPushButton(self.Exporting_Factures_Frame)
        self.Export_PDF_Facture.setObjectName(u"Export_PDF_Facture")
        self.Export_PDF_Facture.setGeometry(QRect(71, 7, 43, 33))
        self.Export_PDF_Facture.setMinimumSize(QSize(43, 33))
        self.Export_PDF_Facture.setMaximumSize(QSize(43, 33))
        self.Export_PDF_Facture.setFont(font3)
        self.Export_PDF_Facture.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Export_PDF_Facture.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/PDF_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/PDF_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/PDF_Green.png);\n"
"}")
        self.Export_PDF_Facture.setIconSize(QSize(20, 20))
        self.Export_PDF_Facture.setCheckable(False)
        self.Export_PDF_Facture.setAutoRepeat(False)
        self.Export_PDF_Facture.setAutoExclusive(False)
        self.Export_PDF_Facture.setAutoRepeatDelay(50)
        self.Export_PDF_Facture.setAutoRepeatInterval(10)
        self.Export_Exel_Facture = QPushButton(self.Exporting_Factures_Frame)
        self.Export_Exel_Facture.setObjectName(u"Export_Exel_Facture")
        self.Export_Exel_Facture.setGeometry(QRect(18, 7, 43, 33))
        self.Export_Exel_Facture.setMinimumSize(QSize(43, 33))
        self.Export_Exel_Facture.setMaximumSize(QSize(43, 33))
        self.Export_Exel_Facture.setFont(font3)
        self.Export_Exel_Facture.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Export_Exel_Facture.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Exel_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Exel_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/Exel_Green.png);\n"
"}")
        self.Export_Exel_Facture.setIconSize(QSize(20, 20))
        self.Export_Exel_Facture.setCheckable(False)
        self.Export_Exel_Facture.setAutoRepeat(False)
        self.Export_Exel_Facture.setAutoExclusive(False)
        self.Export_Exel_Facture.setAutoRepeatDelay(50)
        self.Export_Exel_Facture.setAutoRepeatInterval(10)
        self.Exportation_FactureAdvanced_Info = QLabel(self.ToolsFrame_Facture_Advanced)
        self.Exportation_FactureAdvanced_Info.setObjectName(u"Exportation_FactureAdvanced_Info")
        self.Exportation_FactureAdvanced_Info.setGeometry(QRect(20, 3, 750, 41))
        self.Exportation_FactureAdvanced_Info.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 12pt \"Acme\";\n"
"}")
        self.Exportation_FactureAdvanced_Info.setAlignment(Qt.AlignCenter)
        self.Exportation_FactureAdvanced_Info.setWordWrap(True)
        self.Facture_Windows.addTab(self.Facture_Advanced, "")
        self.Menu_Pages.addWidget(self.Factures)
        self.Expenses = QWidget()
        self.Expenses.setObjectName(u"Expenses")
        self.ExpensesTable_Advanced = QTableWidget(self.Expenses)
        if (self.ExpensesTable_Advanced.columnCount() < 5):
            self.ExpensesTable_Advanced.setColumnCount(5)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setIcon(icon5);
        self.ExpensesTable_Advanced.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setIcon(icon5);
        self.ExpensesTable_Advanced.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setIcon(icon21);
        self.ExpensesTable_Advanced.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        icon24 = QIcon()
        icon24.addFile(u":/Icons/Edit_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon24.addFile(u":/Icons/Edit_Mix.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem24.setIcon(icon24);
        self.ExpensesTable_Advanced.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem25.setIcon(icon10);
        self.ExpensesTable_Advanced.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        self.ExpensesTable_Advanced.setObjectName(u"ExpensesTable_Advanced")
        self.ExpensesTable_Advanced.setGeometry(QRect(67, 90, 913, 671))
        self.ExpensesTable_Advanced.setMinimumSize(QSize(913, 671))
        self.ExpensesTable_Advanced.setMaximumSize(QSize(913, 671))
        self.ExpensesTable_Advanced.setStyleSheet(u"QHeaderView::section{\n"
"	font: 75 13pt \"Acme\";\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid #6c6c6c;\n"
"	border-top-right-radius: 6px;\n"
"	border-bottom-right-radius: 6px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	font: 75 16pt \"Acme\";\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.ExpensesTable_Advanced.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ExpensesTable_Advanced.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ExpensesTable_Advanced.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ExpensesTable_Advanced.setTabKeyNavigation(True)
        self.ExpensesTable_Advanced.setSortingEnabled(False)
        self.ExpensesTable_Advanced.horizontalHeader().setCascadingSectionResizes(False)
        self.ExpensesTable_Advanced.horizontalHeader().setDefaultSectionSize(180)
        self.ExpensesTable_Advanced.horizontalHeader().setHighlightSections(True)
        self.ExpensesTable_Advanced.horizontalHeader().setStretchLastSection(True)
        self.ExpensesTable_Advanced.verticalHeader().setVisible(False)
        self.ExpensesTable_Advanced.verticalHeader().setHighlightSections(False)
        self.Add_Expenses_View = QPushButton(self.Expenses)
        self.Add_Expenses_View.setObjectName(u"Add_Expenses_View")
        self.Add_Expenses_View.setEnabled(True)
        self.Add_Expenses_View.setGeometry(QRect(67, 28, 43, 33))
        self.Add_Expenses_View.setMinimumSize(QSize(43, 33))
        self.Add_Expenses_View.setMaximumSize(QSize(43, 33))
        self.Add_Expenses_View.setFont(font3)
        self.Add_Expenses_View.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Add_Expenses_View.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Add_Expenses_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/Add_Expenses_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Add_Expenses_Green.png);\n"
"}")
        self.Add_Expenses_View.setIconSize(QSize(20, 20))
        self.Add_Expenses_View.setCheckable(False)
        self.Add_Expenses_View.setAutoRepeat(False)
        self.Add_Expenses_View.setAutoExclusive(False)
        self.Add_Expenses_View.setAutoRepeatDelay(50)
        self.Add_Expenses_View.setAutoRepeatInterval(10)
        self.ToolsFrame_Advanced_Expenses = QFrame(self.Expenses)
        self.ToolsFrame_Advanced_Expenses.setObjectName(u"ToolsFrame_Advanced_Expenses")
        self.ToolsFrame_Advanced_Expenses.setGeometry(QRect(67, 770, 913, 47))
        self.ToolsFrame_Advanced_Expenses.setMinimumSize(QSize(913, 47))
        self.ToolsFrame_Advanced_Expenses.setMaximumSize(QSize(913, 47))
        self.ToolsFrame_Advanced_Expenses.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.ToolsFrame_Advanced_Expenses.setFrameShape(QFrame.StyledPanel)
        self.ToolsFrame_Advanced_Expenses.setFrameShadow(QFrame.Raised)
        self.Exporting_Frame_Expenses = QFrame(self.ToolsFrame_Advanced_Expenses)
        self.Exporting_Frame_Expenses.setObjectName(u"Exporting_Frame_Expenses")
        self.Exporting_Frame_Expenses.setGeometry(QRect(781, 0, 132, 47))
        self.Exporting_Frame_Expenses.setMinimumSize(QSize(0, 47))
        self.Exporting_Frame_Expenses.setMaximumSize(QSize(16777215, 47))
        self.Exporting_Frame_Expenses.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 73, 73);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Exporting_Frame_Expenses.setFrameShape(QFrame.StyledPanel)
        self.Exporting_Frame_Expenses.setFrameShadow(QFrame.Raised)
        self.Export_PDF_Expenses = QPushButton(self.Exporting_Frame_Expenses)
        self.Export_PDF_Expenses.setObjectName(u"Export_PDF_Expenses")
        self.Export_PDF_Expenses.setGeometry(QRect(71, 7, 43, 33))
        self.Export_PDF_Expenses.setMinimumSize(QSize(43, 33))
        self.Export_PDF_Expenses.setMaximumSize(QSize(43, 33))
        self.Export_PDF_Expenses.setFont(font3)
        self.Export_PDF_Expenses.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Export_PDF_Expenses.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/PDF_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/PDF_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/PDF_Green.png);\n"
"}")
        self.Export_PDF_Expenses.setIconSize(QSize(20, 20))
        self.Export_PDF_Expenses.setCheckable(False)
        self.Export_PDF_Expenses.setAutoRepeat(False)
        self.Export_PDF_Expenses.setAutoExclusive(False)
        self.Export_PDF_Expenses.setAutoRepeatDelay(50)
        self.Export_PDF_Expenses.setAutoRepeatInterval(10)
        self.Export_Exel_Expenses = QPushButton(self.Exporting_Frame_Expenses)
        self.Export_Exel_Expenses.setObjectName(u"Export_Exel_Expenses")
        self.Export_Exel_Expenses.setGeometry(QRect(18, 7, 43, 33))
        self.Export_Exel_Expenses.setMinimumSize(QSize(43, 33))
        self.Export_Exel_Expenses.setMaximumSize(QSize(43, 33))
        self.Export_Exel_Expenses.setFont(font3)
        self.Export_Exel_Expenses.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Export_Exel_Expenses.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Exel_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Exel_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/Exel_Green.png);\n"
"}")
        self.Export_Exel_Expenses.setIconSize(QSize(20, 20))
        self.Export_Exel_Expenses.setCheckable(False)
        self.Export_Exel_Expenses.setAutoRepeat(False)
        self.Export_Exel_Expenses.setAutoExclusive(False)
        self.Export_Exel_Expenses.setAutoRepeatDelay(50)
        self.Export_Exel_Expenses.setAutoRepeatInterval(10)
        self.Exportation_ExpensesAdvanced_Info = QLabel(self.ToolsFrame_Advanced_Expenses)
        self.Exportation_ExpensesAdvanced_Info.setObjectName(u"Exportation_ExpensesAdvanced_Info")
        self.Exportation_ExpensesAdvanced_Info.setGeometry(QRect(20, 3, 750, 41))
        self.Exportation_ExpensesAdvanced_Info.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 12pt \"Acme\";\n"
"}")
        self.Exportation_ExpensesAdvanced_Info.setAlignment(Qt.AlignCenter)
        self.Exportation_ExpensesAdvanced_Info.setWordWrap(True)
        self.Filter_Expenses_Frame_View = QFrame(self.Expenses)
        self.Filter_Expenses_Frame_View.setObjectName(u"Filter_Expenses_Frame_View")
        self.Filter_Expenses_Frame_View.setGeometry(QRect(486, 20, 494, 47))
        self.Filter_Expenses_Frame_View.setMinimumSize(QSize(494, 47))
        self.Filter_Expenses_Frame_View.setMaximumSize(QSize(494, 47))
        self.Filter_Expenses_Frame_View.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 73, 73);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Filter_Expenses_Frame_View.setFrameShape(QFrame.StyledPanel)
        self.Filter_Expenses_Frame_View.setFrameShadow(QFrame.Raised)
        self.FilterBy_Expenses = QComboBox(self.Filter_Expenses_Frame_View)
        self.FilterBy_Expenses.addItem(icon11, "")
        self.FilterBy_Expenses.addItem(icon5, "")
        self.FilterBy_Expenses.addItem(icon5, "")
        self.FilterBy_Expenses.addItem(icon21, "")
        self.FilterBy_Expenses.setObjectName(u"FilterBy_Expenses")
        self.FilterBy_Expenses.setGeometry(QRect(71, 7, 120, 33))
        self.FilterBy_Expenses.setMinimumSize(QSize(120, 33))
        self.FilterBy_Expenses.setMaximumSize(QSize(120, 33))
        self.FilterBy_Expenses.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid white;\n"
"	border-radius:6px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 12pt \"Acme\";\n"
"	padding-left: 15px;\n"
"	selection-background-color: #2980B9;\n"
"}")
        self.Ordre_Expenses = QPushButton(self.Filter_Expenses_Frame_View)
        self.Ordre_Expenses.setObjectName(u"Ordre_Expenses")
        self.Ordre_Expenses.setGeometry(QRect(18, 7, 43, 33))
        self.Ordre_Expenses.setMinimumSize(QSize(43, 33))
        self.Ordre_Expenses.setMaximumSize(QSize(43, 33))
        self.Ordre_Expenses.setFont(font3)
        self.Ordre_Expenses.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Ordre_Expenses.setStyleSheet(u"QPushButton {\n"
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
        self.Ordre_Expenses.setIconSize(QSize(20, 20))
        self.Ordre_Expenses.setCheckable(True)
        self.Ordre_Expenses.setChecked(False)
        self.Ordre_Expenses.setAutoRepeat(False)
        self.Ordre_Expenses.setAutoExclusive(False)
        self.Ordre_Expenses.setAutoRepeatDelay(50)
        self.Ordre_Expenses.setAutoRepeatInterval(10)
        self.Search_Expenses = QLineEdit(self.Filter_Expenses_Frame_View)
        self.Search_Expenses.setObjectName(u"Search_Expenses")
        self.Search_Expenses.setGeometry(QRect(201, 7, 275, 33))
        self.Search_Expenses.setMinimumSize(QSize(275, 33))
        self.Search_Expenses.setMaximumSize(QSize(275, 31))
        self.Search_Expenses.setStyleSheet(u"QLineEdit {\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	padding-left: 30px;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-image: url(:/Icons/Search.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 10pt \"Acme\";\n"
"}")
        self.Menu_Pages.addWidget(self.Expenses)
        MainWindow.setCentralWidget(self.Window)

        self.retranslateUi(MainWindow)

        self.Menu_Pages.setCurrentIndex(0)
        self.Customer_Windows.setCurrentIndex(1)
        self.Rabbit_Windows.setCurrentIndex(0)
        self.Cages_Windows.setCurrentIndex(0)
        self.Facture_Windows.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Farm_Logo.setText("")
        self.Project_Name.setText(QCoreApplication.translate("MainWindow", u"ELEVAGE BOUCHA", None))
        self.Dashboard_Button.setText(QCoreApplication.translate("MainWindow", u"  Dashboard", None))
        self.Customers_Button.setText(QCoreApplication.translate("MainWindow", u"  Customers", None))
        self.Rabbits_Button.setText(QCoreApplication.translate("MainWindow", u"  Rabbits", None))
        self.Cages_Button.setText(QCoreApplication.translate("MainWindow", u"  Cages", None))
        self.Factures_Button.setText(QCoreApplication.translate("MainWindow", u"  Factures", None))
        self.Expenses_Button.setText(QCoreApplication.translate("MainWindow", u"  Expenses", None))
        self.Account_Logo.setText("")
        self.Account_Name.setText(QCoreApplication.translate("MainWindow", u"Mohamed Amine Bouchaala", None))
        self.Settings_Button.setText("")
        self.Logout_Button.setText("")
        self.Dashboard_Logo.setText("")
        self.Dashboard_Message.setText(QCoreApplication.translate("MainWindow", u"Welcome To The Dashboard! Here, You Can See An Overview Of The Farm.", None))
        self.TND_Logo_2.setText("")
        self.Earning_Text.setText(QCoreApplication.translate("MainWindow", u"Earning", None))
        self.Earning_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000,000", None))
        self.Rabbits_Logo_2.setText("")
        self.Rabbits_Text.setText(QCoreApplication.translate("MainWindow", u"Rabbits", None))
        self.Rabbits_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000 000", None))
        self.Customers_Logo_2.setText("")
        self.Customers_Text.setText(QCoreApplication.translate("MainWindow", u"Customers", None))
        self.Customers_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000 000", None))
        self.Cages_Logo_2.setText("")
        self.Cages_Text.setText(QCoreApplication.translate("MainWindow", u"Cages", None))
        self.Cages_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000 000", None))
        self.TND_Logo_3.setText("")
        self.Income_Text.setText(QCoreApplication.translate("MainWindow", u"Incomes", None))
        self.Income_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000,000", None))
        self.TND_Logo_4.setText("")
        self.Expenses_Text.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.Expenses_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000,000", None))
        self.Date_Logo.setText("")
        self.LastIncome_Text.setText(QCoreApplication.translate("MainWindow", u"Last Income", None))
        self.LastIncome_Inter.setText(QCoreApplication.translate("MainWindow", u"2/22/2025", None))
        self.Date_Logo_2.setText("")
        self.TopBuyer_Text.setText(QCoreApplication.translate("MainWindow", u"Top Buyer", None))
        self.TopBuyer_Inter.setText(QCoreApplication.translate("MainWindow", u"Name _ ID", None))
        self.Rabbits_Logo_3.setText("")
        self.Males_Text.setText(QCoreApplication.translate("MainWindow", u"Males", None))
        self.Rabbits_Males_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000 000", None))
        self.Rabbits_Logo_4.setText("")
        self.Females_Text.setText(QCoreApplication.translate("MainWindow", u"Females", None))
        self.Rabbits_Females_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000 000", None))
        self.Rabbits_Logo_5.setText("")
        self.Nulls_Text.setText(QCoreApplication.translate("MainWindow", u"Nulls", None))
        self.Rabbits_Nulls_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000 000", None))
        self.Rabbits_Logo_6.setText("")
        self.All_Text_2.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.Rabbits_All_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000 000", None))
        self.Rabbits_Logo_7.setText("")
        self.Disponible_Text.setText(QCoreApplication.translate("MainWindow", u"Disponible", None))
        self.Rabbits_Disponible_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000 000", None))
        self.Rabbits_Logo_8.setText("")
        self.SoldOut_Text.setText(QCoreApplication.translate("MainWindow", u"Sold Out", None))
        self.Rabbits_SoldOut_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000 000", None))
        self.Rabbits_Logo_9.setText("")
        self.Owned_Text.setText(QCoreApplication.translate("MainWindow", u"Owned", None))
        self.Rabbits_Owned_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000 000", None))
        self.Rabbits_Logo_10.setText("")
        self.Dead_Text.setText(QCoreApplication.translate("MainWindow", u"Dead", None))
        self.Rabbits_Dead_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000 000", None))
        self.Cages_Logo_3.setText("")
        self.Males_Text_2.setText(QCoreApplication.translate("MainWindow", u"Males", None))
        self.Cages_Males_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000 000", None))
        self.Cages_Logo_4.setText("")
        self.Females_Text_2.setText(QCoreApplication.translate("MainWindow", u"Females", None))
        self.Cages_Females_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000 000", None))
        self.Cages_Logo_5.setText("")
        self.Kids_Text.setText(QCoreApplication.translate("MainWindow", u"Kids", None))
        self.Cages_Kids_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000 000", None))
        self.Cages_Logo_6.setText("")
        self.All_Text.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.Cages_All_Inter.setText(QCoreApplication.translate("MainWindow", u"100 000 000", None))
        self.Exportation_CustomerView_Info.setText("")
        self.Customer_Windows.setTabText(self.Customer_Windows.indexOf(self.Customer_View), QCoreApplication.translate("MainWindow", u"View", None))
        ___qtablewidgetitem = self.CustomersTable_Advanced.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.CustomersTable_Advanced.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.CustomersTable_Advanced.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem3 = self.CustomersTable_Advanced.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem4 = self.CustomersTable_Advanced.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.Export_PDF_Customers.setText("")
        self.Export_Exel_Customers.setText("")
        self.Exportation_CustomerAdvanced_Info.setText("")
        self.Customer_Windows.setTabText(self.Customer_Windows.indexOf(self.Customer_Advanced), QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.Add_Customer_View.setText("")
        self.FilterBy_Customer.setItemText(0, QCoreApplication.translate("MainWindow", u"By", None))
        self.FilterBy_Customer.setItemText(1, QCoreApplication.translate("MainWindow", u"ID", None))
        self.FilterBy_Customer.setItemText(2, QCoreApplication.translate("MainWindow", u"Name", None))
        self.FilterBy_Customer.setItemText(3, QCoreApplication.translate("MainWindow", u"Phone", None))
        self.FilterBy_Customer.setItemText(4, QCoreApplication.translate("MainWindow", u"Address", None))

        self.FilterGender_Customer.setItemText(0, QCoreApplication.translate("MainWindow", u"Gender", None))
        self.FilterGender_Customer.setItemText(1, QCoreApplication.translate("MainWindow", u"Null", None))
        self.FilterGender_Customer.setItemText(2, QCoreApplication.translate("MainWindow", u"Male", None))
        self.FilterGender_Customer.setItemText(3, QCoreApplication.translate("MainWindow", u"Female", None))

        self.Ordre_Customer.setText("")
        self.Search_Customer.setInputMask("")
        self.Search_Customer.setText("")
        self.Search_Customer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Customer...", None))
        self.FilterBy_Rabbits.setItemText(0, QCoreApplication.translate("MainWindow", u"By", None))
        self.FilterBy_Rabbits.setItemText(1, QCoreApplication.translate("MainWindow", u"ID", None))
        self.FilterBy_Rabbits.setItemText(2, QCoreApplication.translate("MainWindow", u"Breed", None))
        self.FilterBy_Rabbits.setItemText(3, QCoreApplication.translate("MainWindow", u"Born", None))
        self.FilterBy_Rabbits.setItemText(4, QCoreApplication.translate("MainWindow", u"Color", None))
        self.FilterBy_Rabbits.setItemText(5, QCoreApplication.translate("MainWindow", u"Mother", None))
        self.FilterBy_Rabbits.setItemText(6, QCoreApplication.translate("MainWindow", u"Father", None))
        self.FilterBy_Rabbits.setItemText(7, QCoreApplication.translate("MainWindow", u"Generation", None))
        self.FilterBy_Rabbits.setItemText(8, QCoreApplication.translate("MainWindow", u"Type", None))
        self.FilterBy_Rabbits.setItemText(9, QCoreApplication.translate("MainWindow", u"CageID", None))
        self.FilterBy_Rabbits.setItemText(10, QCoreApplication.translate("MainWindow", u"FactureID", None))
        self.FilterBy_Rabbits.setItemText(11, QCoreApplication.translate("MainWindow", u"CustomerID", None))
        self.FilterBy_Rabbits.setItemText(12, QCoreApplication.translate("MainWindow", u"Bought", None))
        self.FilterBy_Rabbits.setItemText(13, QCoreApplication.translate("MainWindow", u"Sold", None))

        self.FilterGender_Rabbits.setItemText(0, QCoreApplication.translate("MainWindow", u"Gender", None))
        self.FilterGender_Rabbits.setItemText(1, QCoreApplication.translate("MainWindow", u"Null", None))
        self.FilterGender_Rabbits.setItemText(2, QCoreApplication.translate("MainWindow", u"Male", None))
        self.FilterGender_Rabbits.setItemText(3, QCoreApplication.translate("MainWindow", u"Female", None))

        self.Ordre_Rabbits.setText("")
        self.Search_Rabbits.setInputMask("")
        self.Search_Rabbits.setText("")
        self.Search_Rabbits.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Rabbit...", None))
        self.Exportation_RabbitsView_Info.setText("")
        self.Rabbit_Windows.setTabText(self.Rabbit_Windows.indexOf(self.Rabbit_View), QCoreApplication.translate("MainWindow", u"View", None))
        ___qtablewidgetitem5 = self.RabbitsTable_Advanced.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem6 = self.RabbitsTable_Advanced.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Breed", None));
        ___qtablewidgetitem7 = self.RabbitsTable_Advanced.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Born", None));
        ___qtablewidgetitem8 = self.RabbitsTable_Advanced.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Generation", None));
        ___qtablewidgetitem9 = self.RabbitsTable_Advanced.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Cage", None));
        ___qtablewidgetitem10 = self.RabbitsTable_Advanced.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Color", None));
        ___qtablewidgetitem11 = self.RabbitsTable_Advanced.horizontalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.Export_PDF_Rabbits.setText("")
        self.Export_Exel_Rabbits.setText("")
        self.Exportation_RabbitsAdvanced_Info.setText("")
        self.Rabbit_Windows.setTabText(self.Rabbit_Windows.indexOf(self.Rabbits_Advanced), QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.Add_Rabbit_View.setText("")
        self.Rabbit_Tree.setText("")
        self.Cages_Tree.setText("")
        self.Exportation_CagesView_Info.setText("")
        self.Cages_Windows.setTabText(self.Cages_Windows.indexOf(self.Cage_View), QCoreApplication.translate("MainWindow", u"View", None))
        ___qtablewidgetitem12 = self.CagesTable_Advanced.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem13 = self.CagesTable_Advanced.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Bought", None));
        ___qtablewidgetitem14 = self.CagesTable_Advanced.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Notes", None));
        ___qtablewidgetitem15 = self.CagesTable_Advanced.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.Export_PDF_Cages.setText("")
        self.Export_Exel_Cages.setText("")
        self.Exportation_CagesAdvanced_Info.setText("")
        self.Cages_Windows.setTabText(self.Cages_Windows.indexOf(self.Cages_Advanced), QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.Add_Cage_View.setText("")
        self.FilterBy_Cages.setItemText(0, QCoreApplication.translate("MainWindow", u"By", None))
        self.FilterBy_Cages.setItemText(1, QCoreApplication.translate("MainWindow", u"ID", None))
        self.FilterBy_Cages.setItemText(2, QCoreApplication.translate("MainWindow", u"FactureID", None))
        self.FilterBy_Cages.setItemText(3, QCoreApplication.translate("MainWindow", u"CustomerID", None))
        self.FilterBy_Cages.setItemText(4, QCoreApplication.translate("MainWindow", u"Sold", None))
        self.FilterBy_Cages.setItemText(5, QCoreApplication.translate("MainWindow", u"Bought", None))

        self.FilterGender_Cages.setItemText(0, QCoreApplication.translate("MainWindow", u"Gender", None))
        self.FilterGender_Cages.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.FilterGender_Cages.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))
        self.FilterGender_Cages.setItemText(3, QCoreApplication.translate("MainWindow", u"Kids", None))

        self.Ordre_Cages.setText("")
        self.Search_Cages.setInputMask("")
        self.Search_Cages.setText("")
        self.Search_Cages.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Cage...", None))
        self.Add_Facture_View.setText("")
        self.FilterBy_Facture.setItemText(0, QCoreApplication.translate("MainWindow", u"By", None))
        self.FilterBy_Facture.setItemText(1, QCoreApplication.translate("MainWindow", u"ID", None))
        self.FilterBy_Facture.setItemText(2, QCoreApplication.translate("MainWindow", u"Date", None))
        self.FilterBy_Facture.setItemText(3, QCoreApplication.translate("MainWindow", u"CustomerID", None))
        self.FilterBy_Facture.setItemText(4, QCoreApplication.translate("MainWindow", u"Total", None))

        self.Ordre_Facture.setText("")
        self.Search_Facture.setInputMask("")
        self.Search_Facture.setText("")
        self.Search_Facture.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Facture...", None))
        self.Exportation_FactureView_Info.setText("")
        self.Facture_Windows.setTabText(self.Facture_Windows.indexOf(self.Facture_View), QCoreApplication.translate("MainWindow", u"View", None))
        ___qtablewidgetitem16 = self.FactureTable_Advanced.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem17 = self.FactureTable_Advanced.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem18 = self.FactureTable_Advanced.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Customer", None));
        ___qtablewidgetitem19 = self.FactureTable_Advanced.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem20 = self.FactureTable_Advanced.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.Export_PDF_Facture.setText("")
        self.Export_Exel_Facture.setText("")
        self.Exportation_FactureAdvanced_Info.setText("")
        self.Facture_Windows.setTabText(self.Facture_Windows.indexOf(self.Facture_Advanced), QCoreApplication.translate("MainWindow", u"Advanced", None))
        ___qtablewidgetitem21 = self.ExpensesTable_Advanced.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem22 = self.ExpensesTable_Advanced.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem23 = self.ExpensesTable_Advanced.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem24 = self.ExpensesTable_Advanced.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Notes", None));
        ___qtablewidgetitem25 = self.ExpensesTable_Advanced.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.Add_Expenses_View.setText("")
        self.Export_PDF_Expenses.setText("")
        self.Export_Exel_Expenses.setText("")
        self.Exportation_ExpensesAdvanced_Info.setText("")
        self.FilterBy_Expenses.setItemText(0, QCoreApplication.translate("MainWindow", u"By", None))
        self.FilterBy_Expenses.setItemText(1, QCoreApplication.translate("MainWindow", u"ID", None))
        self.FilterBy_Expenses.setItemText(2, QCoreApplication.translate("MainWindow", u"Name", None))
        self.FilterBy_Expenses.setItemText(3, QCoreApplication.translate("MainWindow", u"Total", None))

        self.Ordre_Expenses.setText("")
        self.Search_Expenses.setInputMask("")
        self.Search_Expenses.setText("")
        self.Search_Expenses.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Expense...", None))
    # retranslateUi

