# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainViewCageTree.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_Cages_Tree_View_Main(object):
    def setupUi(self, Cages_Tree_View_Main):
        if not Cages_Tree_View_Main.objectName():
            Cages_Tree_View_Main.setObjectName(u"Cages_Tree_View_Main")
        Cages_Tree_View_Main.resize(1031, 867)
        Cages_Tree_View_Main.setMinimumSize(QSize(1031, 867))
        Cages_Tree_View_Main.setMaximumSize(QSize(1031, 867))
        Cages_Tree_View_Main.setStyleSheet(u"")
        self.Background = QFrame(Cages_Tree_View_Main)
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
        self.Exit_Cages_Tree_View = QPushButton(self.Background)
        self.Exit_Cages_Tree_View.setObjectName(u"Exit_Cages_Tree_View")
        self.Exit_Cages_Tree_View.setEnabled(True)
        self.Exit_Cages_Tree_View.setGeometry(QRect(970, 30, 33, 33))
        self.Exit_Cages_Tree_View.setMinimumSize(QSize(33, 33))
        self.Exit_Cages_Tree_View.setMaximumSize(QSize(33, 33))
        font = QFont()
        font.setFamilies([u"Orbitron"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.Exit_Cages_Tree_View.setFont(font)
        self.Exit_Cages_Tree_View.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Exit_Cages_Tree_View.setStyleSheet(u"QPushButton {\n"
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
        self.Exit_Cages_Tree_View.setIconSize(QSize(20, 20))
        self.Exit_Cages_Tree_View.setCheckable(False)
        self.Exit_Cages_Tree_View.setAutoRepeat(False)
        self.Exit_Cages_Tree_View.setAutoExclusive(False)
        self.Exit_Cages_Tree_View.setAutoRepeatDelay(50)
        self.Exit_Cages_Tree_View.setAutoRepeatInterval(10)
        self.TreeFrame = QFrame(self.Background)
        self.TreeFrame.setObjectName(u"TreeFrame")
        self.TreeFrame.setGeometry(QRect(0, 80, 1031, 787))
        self.TreeFrame.setMinimumSize(QSize(1031, 787))
        self.TreeFrame.setMaximumSize(QSize(1031, 787))
        self.TreeFrame.setStyleSheet(u"")
        self.TreeFrame.setFrameShape(QFrame.StyledPanel)
        self.TreeFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.TreeFrame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 991, 741))
        self.TreeVerticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.TreeVerticalLayout.setObjectName(u"TreeVerticalLayout")
        self.TreeVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ScreenShot_Button = QPushButton(self.Background)
        self.ScreenShot_Button.setObjectName(u"ScreenShot_Button")
        self.ScreenShot_Button.setEnabled(True)
        self.ScreenShot_Button.setGeometry(QRect(40, 30, 33, 33))
        self.ScreenShot_Button.setMinimumSize(QSize(33, 33))
        self.ScreenShot_Button.setMaximumSize(QSize(33, 33))
        self.ScreenShot_Button.setFont(font)
        self.ScreenShot_Button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ScreenShot_Button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Screenshot_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Screenshot_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Screenshot_Green.png);\n"
"}")
        self.ScreenShot_Button.setIconSize(QSize(20, 20))
        self.ScreenShot_Button.setCheckable(False)
        self.ScreenShot_Button.setAutoRepeat(False)
        self.ScreenShot_Button.setAutoExclusive(False)
        self.ScreenShot_Button.setAutoRepeatDelay(50)
        self.ScreenShot_Button.setAutoRepeatInterval(10)

        self.retranslateUi(Cages_Tree_View_Main)
        self.Exit_Cages_Tree_View.clicked.connect(Cages_Tree_View_Main.close)

        QMetaObject.connectSlotsByName(Cages_Tree_View_Main)
    # setupUi

    def retranslateUi(self, Cages_Tree_View_Main):
        Cages_Tree_View_Main.setWindowTitle(QCoreApplication.translate("Cages_Tree_View_Main", u"Dialog", None))
        self.Title.setText(QCoreApplication.translate("Cages_Tree_View_Main", u"Cages Tree Viewer Window", None))
        self.Exit_Cages_Tree_View.setText("")
#if QT_CONFIG(shortcut)
        self.Exit_Cages_Tree_View.setShortcut(QCoreApplication.translate("Cages_Tree_View_Main", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.ScreenShot_Button.setText("")
#if QT_CONFIG(shortcut)
        self.ScreenShot_Button.setShortcut(QCoreApplication.translate("Cages_Tree_View_Main", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

