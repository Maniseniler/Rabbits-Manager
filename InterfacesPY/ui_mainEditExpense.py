# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainEditExpense.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDialog, QDoubleSpinBox,
    QFrame, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_EditExpense_Main(object):
    def setupUi(self, EditExpense_Main):
        if not EditExpense_Main.objectName():
            EditExpense_Main.setObjectName(u"EditExpense_Main")
        EditExpense_Main.resize(431, 410)
        EditExpense_Main.setMinimumSize(QSize(431, 410))
        EditExpense_Main.setMaximumSize(QSize(431, 410))
        EditExpense_Main.setStyleSheet(u"")
        self.Background = QFrame(EditExpense_Main)
        self.Background.setObjectName(u"Background")
        self.Background.setGeometry(QRect(0, 0, 431, 410))
        self.Background.setMinimumSize(QSize(431, 410))
        self.Background.setMaximumSize(QSize(431, 410))
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
        self.Infos_Frame.setGeometry(QRect(25, 25, 381, 361))
        self.Infos_Frame.setMinimumSize(QSize(381, 361))
        self.Infos_Frame.setMaximumSize(QSize(381, 361))
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
        self.Bought_Frame = QFrame(self.Infos_Frame)
        self.Bought_Frame.setObjectName(u"Bought_Frame")
        self.Bought_Frame.setGeometry(QRect(10, 132, 341, 68))
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
        self.Expense_Expense_Label = QLabel(self.Bought_Frame)
        self.Expense_Expense_Label.setObjectName(u"Expense_Expense_Label")
        self.Expense_Expense_Label.setGeometry(QRect(50, 11, 80, 21))
        self.Expense_Expense_Label.setMinimumSize(QSize(80, 21))
        self.Expense_Expense_Label.setMaximumSize(QSize(80, 21))
        self.Expense_Expense_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Expense_Input = QDoubleSpinBox(self.Bought_Frame)
        self.Expense_Input.setObjectName(u"Expense_Input")
        self.Expense_Input.setGeometry(QRect(110, 11, 191, 21))
        self.Expense_Input.setMinimumSize(QSize(191, 21))
        self.Expense_Input.setMaximumSize(QSize(191, 21))
        self.Expense_Input.setStyleSheet(u"QDoubleSpinBox {\n"
"	background-color:rgb(167, 164, 147);\n"
"	padding-left: 5px;\n"
"	border: 2px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 15pt \"Acme\";\n"
"}")
        self.Expense_Input.setWrapping(False)
        self.Expense_Input.setAlignment(Qt.AlignCenter)
        self.Expense_Input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Expense_Input.setAccelerated(True)
        self.Expense_Input.setDecimals(3)
        self.Expense_Input.setMaximum(9999.989999999999782)
        self.Expense_Input.setSingleStep(0.500000000000000)
        self.Expense_Expense_Icon = QLabel(self.Bought_Frame)
        self.Expense_Expense_Icon.setObjectName(u"Expense_Expense_Icon")
        self.Expense_Expense_Icon.setGeometry(QRect(20, 11, 21, 21))
        self.Expense_Expense_Icon.setMinimumSize(QSize(21, 21))
        self.Expense_Expense_Icon.setMaximumSize(QSize(21, 21))
        self.Expense_Expense_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Expense_Expense_Icon.setPixmap(QPixmap(u":/Icons/TND_White.png"))
        self.Expense_Expense_Icon.setScaledContents(True)
        self.Expense_Expense_Icon.setAlignment(Qt.AlignCenter)
        self.Expense_Infos = QLabel(self.Bought_Frame)
        self.Expense_Infos.setObjectName(u"Expense_Infos")
        self.Expense_Infos.setGeometry(QRect(20, 37, 301, 21))
        self.Expense_Infos.setMinimumSize(QSize(301, 21))
        self.Expense_Infos.setMaximumSize(QSize(301, 21))
        self.Expense_Infos.setStyleSheet(u"QLabel {border: none;\n"
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
        self.Edit_Expense_Button = QPushButton(self.Infos_Frame)
        self.Edit_Expense_Button.setObjectName(u"Edit_Expense_Button")
        self.Edit_Expense_Button.setEnabled(True)
        self.Edit_Expense_Button.setGeometry(QRect(260, 9, 43, 33))
        self.Edit_Expense_Button.setMinimumSize(QSize(43, 33))
        self.Edit_Expense_Button.setMaximumSize(QSize(43, 33))
        font = QFont()
        font.setFamilies([u"Acme"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.Edit_Expense_Button.setFont(font)
        self.Edit_Expense_Button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Edit_Expense_Button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Edit_Expenses_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image:url(:/Icons/Edit_Expenses_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Edit_Expenses_Green.png);\n"
"}")
        self.Edit_Expense_Button.setIconSize(QSize(20, 20))
        self.Edit_Expense_Button.setCheckable(False)
        self.Edit_Expense_Button.setAutoRepeat(False)
        self.Edit_Expense_Button.setAutoExclusive(False)
        self.Edit_Expense_Button.setAutoRepeatDelay(50)
        self.Edit_Expense_Button.setAutoRepeatInterval(10)
        self.Exit_Expense_Button = QPushButton(self.Infos_Frame)
        self.Exit_Expense_Button.setObjectName(u"Exit_Expense_Button")
        self.Exit_Expense_Button.setEnabled(True)
        self.Exit_Expense_Button.setGeometry(QRect(310, 10, 43, 33))
        self.Exit_Expense_Button.setMinimumSize(QSize(43, 33))
        self.Exit_Expense_Button.setMaximumSize(QSize(43, 33))
        self.Exit_Expense_Button.setFont(font)
        self.Exit_Expense_Button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Exit_Expense_Button.setStyleSheet(u"QPushButton {\n"
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
        self.Exit_Expense_Button.setIconSize(QSize(20, 20))
        self.Exit_Expense_Button.setCheckable(False)
        self.Exit_Expense_Button.setAutoRepeat(False)
        self.Exit_Expense_Button.setAutoExclusive(False)
        self.Exit_Expense_Button.setAutoRepeatDelay(50)
        self.Exit_Expense_Button.setAutoRepeatInterval(10)
        self.Name_Frame = QFrame(self.Infos_Frame)
        self.Name_Frame.setObjectName(u"Name_Frame")
        self.Name_Frame.setGeometry(QRect(10, 54, 341, 68))
        self.Name_Frame.setMinimumSize(QSize(341, 68))
        self.Name_Frame.setMaximumSize(QSize(341, 68))
        self.Name_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Name_Frame.setFrameShape(QFrame.StyledPanel)
        self.Name_Frame.setFrameShadow(QFrame.Raised)
        self.Expense_Name_Icon = QLabel(self.Name_Frame)
        self.Expense_Name_Icon.setObjectName(u"Expense_Name_Icon")
        self.Expense_Name_Icon.setGeometry(QRect(20, 11, 21, 21))
        self.Expense_Name_Icon.setMinimumSize(QSize(21, 21))
        self.Expense_Name_Icon.setMaximumSize(QSize(21, 21))
        self.Expense_Name_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Expense_Name_Icon.setPixmap(QPixmap(u":/Icons/Customer_Whitre.png"))
        self.Expense_Name_Icon.setScaledContents(True)
        self.Expense_Name_Icon.setAlignment(Qt.AlignCenter)
        self.Expense_Name_Icon.setWordWrap(False)
        self.Name_Input = QLineEdit(self.Name_Frame)
        self.Name_Input.setObjectName(u"Name_Input")
        self.Name_Input.setGeometry(QRect(110, 11, 191, 21))
        self.Name_Input.setMinimumSize(QSize(191, 21))
        self.Name_Input.setMaximumSize(QSize(191, 21))
        self.Name_Input.setStyleSheet(u"QLineEdit {\n"
"	background-color:rgb(167, 164, 147);\n"
"	padding-left: 5px;\n"
"	border: 2px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 15pt \"Acme\";\n"
"}")
        self.Expense_Name_Label = QLabel(self.Name_Frame)
        self.Expense_Name_Label.setObjectName(u"Expense_Name_Label")
        self.Expense_Name_Label.setGeometry(QRect(50, 11, 51, 21))
        self.Expense_Name_Label.setMinimumSize(QSize(51, 21))
        self.Expense_Name_Label.setMaximumSize(QSize(51, 21))
        self.Expense_Name_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Name_Infos = QLabel(self.Name_Frame)
        self.Name_Infos.setObjectName(u"Name_Infos")
        self.Name_Infos.setGeometry(QRect(20, 37, 301, 21))
        self.Name_Infos.setMinimumSize(QSize(301, 21))
        self.Name_Infos.setMaximumSize(QSize(301, 21))
        self.Name_Infos.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 13pt \"Acme\";\n"
"}")
        self.Expense_Title = QLabel(self.Background)
        self.Expense_Title.setObjectName(u"Expense_Title")
        self.Expense_Title.setGeometry(QRect(50, 2, 331, 21))
        self.Expense_Title.setMinimumSize(QSize(331, 21))
        self.Expense_Title.setMaximumSize(QSize(331, 21))
        self.Expense_Title.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";")
        self.Expense_Title.setAlignment(Qt.AlignCenter)
        QWidget.setTabOrder(self.Notes_Input, self.Edit_Expense_Button)
        QWidget.setTabOrder(self.Edit_Expense_Button, self.Exit_Expense_Button)

        self.retranslateUi(EditExpense_Main)
        self.Exit_Expense_Button.clicked.connect(EditExpense_Main.close)

        QMetaObject.connectSlotsByName(EditExpense_Main)
    # setupUi

    def retranslateUi(self, EditExpense_Main):
        EditExpense_Main.setWindowTitle(QCoreApplication.translate("EditExpense_Main", u"Dialog", None))
        self.ID_Label.setText(QCoreApplication.translate("EditExpense_Main", u"ID : ", None))
        self.Expense_Expense_Label.setText(QCoreApplication.translate("EditExpense_Main", u"Expense", None))
        self.Expense_Input.setPrefix("")
        self.Expense_Input.setSuffix(QCoreApplication.translate("EditExpense_Main", u"  TND", None))
        self.Expense_Expense_Icon.setText("")
        self.Expense_Infos.setText(QCoreApplication.translate("EditExpense_Main", u"How Much You Expense.", None))
        self.Notes_Text_Label.setText(QCoreApplication.translate("EditExpense_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">N</span></p></body></html>", None))
        self.Notes_Text_Label_2.setText(QCoreApplication.translate("EditExpense_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">O</span></p></body></html>", None))
        self.Notes_Text_Label_3.setText(QCoreApplication.translate("EditExpense_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">T</span></p></body></html>", None))
        self.Notes_Text_Label_4.setText(QCoreApplication.translate("EditExpense_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">E</span></p></body></html>", None))
        self.Notes_Text_Label_5.setText(QCoreApplication.translate("EditExpense_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">S</span></p></body></html>", None))
        self.Notes_Input.setDocumentTitle("")
        self.Notes_Input.setPlaceholderText(QCoreApplication.translate("EditExpense_Main", u"Write Here...", None))
        self.Edit_Expense_Button.setText("")
#if QT_CONFIG(shortcut)
        self.Edit_Expense_Button.setShortcut(QCoreApplication.translate("EditExpense_Main", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.Exit_Expense_Button.setText("")
#if QT_CONFIG(shortcut)
        self.Exit_Expense_Button.setShortcut(QCoreApplication.translate("EditExpense_Main", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.Expense_Name_Icon.setText("")
        self.Name_Input.setPlaceholderText(QCoreApplication.translate("EditExpense_Main", u"Write Here...", None))
        self.Expense_Name_Label.setText(QCoreApplication.translate("EditExpense_Main", u"Name ", None))
        self.Name_Infos.setText(QCoreApplication.translate("EditExpense_Main", u"The Name Of The Expense.", None))
        self.Expense_Title.setText(QCoreApplication.translate("EditExpense_Main", u"Edit A Expense", None))
    # retranslateUi

