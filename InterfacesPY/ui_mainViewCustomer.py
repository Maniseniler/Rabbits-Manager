# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainViewCustomer.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QFrame, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)
import resources_rc

class Ui_Customer_View_Main(object):
    def setupUi(self, Customer_View_Main):
        if not Customer_View_Main.objectName():
            Customer_View_Main.setObjectName(u"Customer_View_Main")
        Customer_View_Main.resize(1031, 867)
        Customer_View_Main.setMinimumSize(QSize(1031, 867))
        Customer_View_Main.setMaximumSize(QSize(1031, 867))
        Customer_View_Main.setStyleSheet(u"")
        self.Menu_Customer_View = QTabWidget(Customer_View_Main)
        self.Menu_Customer_View.setObjectName(u"Menu_Customer_View")
        self.Menu_Customer_View.setGeometry(QRect(72, 230, 887, 631))
        self.Menu_Customer_View.setMinimumSize(QSize(887, 631))
        self.Menu_Customer_View.setMaximumSize(QSize(887, 631))
        self.Menu_Customer_View.setStyleSheet(u"QWidget{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"Orbitron\";\n"
"}\n"
"QTabWidget::pane {\n"
"    	border: none;\n"
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
        self.Facture = QWidget()
        self.Facture.setObjectName(u"Facture")
        self.Facture_Frame = QFrame(self.Facture)
        self.Facture_Frame.setObjectName(u"Facture_Frame")
        self.Facture_Frame.setGeometry(QRect(0, 3, 887, 590))
        self.Facture_Frame.setMinimumSize(QSize(887, 590))
        self.Facture_Frame.setMaximumSize(QSize(887, 590))
        self.Facture_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Facture_Frame.setFrameShape(QFrame.StyledPanel)
        self.Facture_Frame.setFrameShadow(QFrame.Raised)
        self.Filter_Frame_View = QFrame(self.Facture_Frame)
        self.Filter_Frame_View.setObjectName(u"Filter_Frame_View")
        self.Filter_Frame_View.setGeometry(QRect(197, 10, 494, 47))
        self.Filter_Frame_View.setMinimumSize(QSize(494, 47))
        self.Filter_Frame_View.setMaximumSize(QSize(494, 47))
        self.Filter_Frame_View.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 73, 73);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Filter_Frame_View.setFrameShape(QFrame.StyledPanel)
        self.Filter_Frame_View.setFrameShadow(QFrame.Raised)
        self.FilterBy_Customer_Facture = QComboBox(self.Filter_Frame_View)
        icon = QIcon()
        icon.addFile(u":/Icons/Search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.FilterBy_Customer_Facture.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Facture_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/Icons/Facture_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Customer_Facture.addItem(icon1, "")
        self.FilterBy_Customer_Facture.addItem(icon1, "")
        self.FilterBy_Customer_Facture.addItem(icon1, "")
        self.FilterBy_Customer_Facture.setObjectName(u"FilterBy_Customer_Facture")
        self.FilterBy_Customer_Facture.setGeometry(QRect(71, 7, 120, 33))
        self.FilterBy_Customer_Facture.setMinimumSize(QSize(120, 33))
        self.FilterBy_Customer_Facture.setMaximumSize(QSize(120, 33))
        self.FilterBy_Customer_Facture.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid white;\n"
"	border-radius:6px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 12pt \"Acme\";\n"
"	padding-left: 15px;\n"
"	selection-background-color: #2980B9;\n"
"}")
        self.Ordre_Customer_Facture = QPushButton(self.Filter_Frame_View)
        self.Ordre_Customer_Facture.setObjectName(u"Ordre_Customer_Facture")
        self.Ordre_Customer_Facture.setGeometry(QRect(18, 7, 43, 33))
        self.Ordre_Customer_Facture.setMinimumSize(QSize(43, 33))
        self.Ordre_Customer_Facture.setMaximumSize(QSize(43, 33))
        font = QFont()
        font.setFamilies([u"Orbitron"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.Ordre_Customer_Facture.setFont(font)
        self.Ordre_Customer_Facture.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Ordre_Customer_Facture.setStyleSheet(u"QPushButton {\n"
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
        self.Ordre_Customer_Facture.setIconSize(QSize(20, 20))
        self.Ordre_Customer_Facture.setCheckable(True)
        self.Ordre_Customer_Facture.setChecked(True)
        self.Ordre_Customer_Facture.setAutoRepeat(False)
        self.Ordre_Customer_Facture.setAutoExclusive(False)
        self.Ordre_Customer_Facture.setAutoRepeatDelay(50)
        self.Ordre_Customer_Facture.setAutoRepeatInterval(10)
        self.Search_Customer_Facture = QLineEdit(self.Filter_Frame_View)
        self.Search_Customer_Facture.setObjectName(u"Search_Customer_Facture")
        self.Search_Customer_Facture.setGeometry(QRect(201, 7, 275, 33))
        self.Search_Customer_Facture.setMinimumSize(QSize(275, 33))
        self.Search_Customer_Facture.setMaximumSize(QSize(275, 31))
        self.Search_Customer_Facture.setStyleSheet(u"QLineEdit {\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	padding-left: 30px;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 8px;\n"
"	background-image: url(:/Icons/Search.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	font: 75 10pt \"Acme\";\n"
"}")
        self.FactureTabs = QTabWidget(self.Facture_Frame)
        self.FactureTabs.setObjectName(u"FactureTabs")
        self.FactureTabs.setGeometry(QRect(10, 65, 867, 520))
        self.FactureTabs.setMinimumSize(QSize(867, 520))
        self.FactureTabs.setMaximumSize(QSize(867, 520))
        self.FactureTabs.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}")
        self.View = QWidget()
        self.View.setObjectName(u"View")
        self.Frame_Customer_Facture_Advanced_2 = QFrame(self.View)
        self.Frame_Customer_Facture_Advanced_2.setObjectName(u"Frame_Customer_Facture_Advanced_2")
        self.Frame_Customer_Facture_Advanced_2.setGeometry(QRect(0, 3, 861, 475))
        self.Frame_Customer_Facture_Advanced_2.setMinimumSize(QSize(861, 475))
        self.Frame_Customer_Facture_Advanced_2.setMaximumSize(QSize(861, 475))
        self.Frame_Customer_Facture_Advanced_2.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Frame_Customer_Facture_Advanced_2.setFrameShape(QFrame.StyledPanel)
        self.Frame_Customer_Facture_Advanced_2.setFrameShadow(QFrame.Raised)
        self.Customer_FactureScrollBar = QScrollArea(self.Frame_Customer_Facture_Advanced_2)
        self.Customer_FactureScrollBar.setObjectName(u"Customer_FactureScrollBar")
        self.Customer_FactureScrollBar.setGeometry(QRect(5, 5, 851, 465))
        self.Customer_FactureScrollBar.setMinimumSize(QSize(851, 465))
        self.Customer_FactureScrollBar.setMaximumSize(QSize(851, 465))
        self.Customer_FactureScrollBar.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgba(0, 0, 0, 0);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Customer_FactureScrollBar.setWidgetResizable(True)
        self.SrollWidget_CustomerFactureScrollBar = QWidget()
        self.SrollWidget_CustomerFactureScrollBar.setObjectName(u"SrollWidget_CustomerFactureScrollBar")
        self.SrollWidget_CustomerFactureScrollBar.setGeometry(QRect(0, 0, 847, 461))
        self.gridLayoutWidget = QWidget(self.SrollWidget_CustomerFactureScrollBar)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 831, 441))
        self.GridLayout_Customer_Facture_View = QGridLayout(self.gridLayoutWidget)
        self.GridLayout_Customer_Facture_View.setObjectName(u"GridLayout_Customer_Facture_View")
        self.GridLayout_Customer_Facture_View.setContentsMargins(0, 0, 0, 0)
        self.Customer_FactureScrollBar.setWidget(self.SrollWidget_CustomerFactureScrollBar)
        self.FactureTabs.addTab(self.View, "")
        self.Advanced = QWidget()
        self.Advanced.setObjectName(u"Advanced")
        self.FacturesCustomesTable_Advanced = QTableWidget(self.Advanced)
        if (self.FacturesCustomesTable_Advanced.columnCount() < 4):
            self.FacturesCustomesTable_Advanced.setColumnCount(4)
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Customer_Whitre.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/Icons/Customer_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setIcon(icon2);
        self.FacturesCustomesTable_Advanced.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Calendar_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Icons/Calendar_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setIcon(icon3);
        self.FacturesCustomesTable_Advanced.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/TND_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/Icons/TND_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setIcon(icon4);
        self.FacturesCustomesTable_Advanced.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Actions_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/Icons/Actions_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setIcon(icon5);
        self.FacturesCustomesTable_Advanced.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.FacturesCustomesTable_Advanced.setObjectName(u"FacturesCustomesTable_Advanced")
        self.FacturesCustomesTable_Advanced.setGeometry(QRect(20, 10, 841, 400))
        self.FacturesCustomesTable_Advanced.setMinimumSize(QSize(841, 400))
        self.FacturesCustomesTable_Advanced.setMaximumSize(QSize(841, 400))
        self.FacturesCustomesTable_Advanced.setStyleSheet(u"QHeaderView::section{\n"
"	font: 75 13pt \"Acme\";\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(167, 164, 147);\n"
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
"	background-color:rgb(167, 164, 147);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.FacturesCustomesTable_Advanced.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.FacturesCustomesTable_Advanced.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.FacturesCustomesTable_Advanced.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.FacturesCustomesTable_Advanced.setTabKeyNavigation(True)
        self.FacturesCustomesTable_Advanced.setSortingEnabled(False)
        self.FacturesCustomesTable_Advanced.horizontalHeader().setCascadingSectionResizes(False)
        self.FacturesCustomesTable_Advanced.horizontalHeader().setDefaultSectionSize(205)
        self.FacturesCustomesTable_Advanced.horizontalHeader().setHighlightSections(True)
        self.FacturesCustomesTable_Advanced.horizontalHeader().setStretchLastSection(True)
        self.FacturesCustomesTable_Advanced.verticalHeader().setVisible(False)
        self.FacturesCustomesTable_Advanced.verticalHeader().setHighlightSections(False)
        self.ToolsFrame_Advanced = QFrame(self.Advanced)
        self.ToolsFrame_Advanced.setObjectName(u"ToolsFrame_Advanced")
        self.ToolsFrame_Advanced.setGeometry(QRect(20, 420, 841, 47))
        self.ToolsFrame_Advanced.setMinimumSize(QSize(841, 47))
        self.ToolsFrame_Advanced.setMaximumSize(QSize(841, 47))
        self.ToolsFrame_Advanced.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(167, 164, 147);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.ToolsFrame_Advanced.setFrameShape(QFrame.StyledPanel)
        self.ToolsFrame_Advanced.setFrameShadow(QFrame.Raised)
        self.Exporting_Frame = QFrame(self.ToolsFrame_Advanced)
        self.Exporting_Frame.setObjectName(u"Exporting_Frame")
        self.Exporting_Frame.setGeometry(QRect(709, 0, 132, 47))
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
        self.Export_PDF_Customers.setFont(font)
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
        self.Export_Exel_Customers.setFont(font)
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
        self.Exportation_CustomerFacture_Info = QLabel(self.ToolsFrame_Advanced)
        self.Exportation_CustomerFacture_Info.setObjectName(u"Exportation_CustomerFacture_Info")
        self.Exportation_CustomerFacture_Info.setGeometry(QRect(20, 3, 681, 41))
        self.Exportation_CustomerFacture_Info.setStyleSheet(u"QLabel {border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgbrgb(0, 174, 255);\n"
"font: 75 12pt \"Acme\";\n"
"}")
        self.Exportation_CustomerFacture_Info.setAlignment(Qt.AlignCenter)
        self.Exportation_CustomerFacture_Info.setWordWrap(True)
        self.FactureTabs.addTab(self.Advanced, "")
        self.Menu_Customer_View.addTab(self.Facture, "")
        self.Boughts = QWidget()
        self.Boughts.setObjectName(u"Boughts")
        self.Advanced_Frame = QFrame(self.Boughts)
        self.Advanced_Frame.setObjectName(u"Advanced_Frame")
        self.Advanced_Frame.setGeometry(QRect(0, 3, 887, 590))
        self.Advanced_Frame.setMinimumSize(QSize(887, 590))
        self.Advanced_Frame.setMaximumSize(QSize(887, 590))
        self.Advanced_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Advanced_Frame.setFrameShape(QFrame.StyledPanel)
        self.Advanced_Frame.setFrameShadow(QFrame.Raised)
        self.Boughts_Tabs = QTabWidget(self.Advanced_Frame)
        self.Boughts_Tabs.setObjectName(u"Boughts_Tabs")
        self.Boughts_Tabs.setGeometry(QRect(10, 5, 860, 565))
        self.Boughts_Tabs.setMinimumSize(QSize(860, 565))
        self.Boughts_Tabs.setMaximumSize(QSize(820, 565))
        self.Boughts_Tabs.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}")
        self.Rabbits = QWidget()
        self.Rabbits.setObjectName(u"Rabbits")
        self.Frame_CustomerRabbits_Facture_Advanced = QFrame(self.Rabbits)
        self.Frame_CustomerRabbits_Facture_Advanced.setObjectName(u"Frame_CustomerRabbits_Facture_Advanced")
        self.Frame_CustomerRabbits_Facture_Advanced.setGeometry(QRect(10, 66, 850, 465))
        self.Frame_CustomerRabbits_Facture_Advanced.setMinimumSize(QSize(850, 465))
        self.Frame_CustomerRabbits_Facture_Advanced.setMaximumSize(QSize(850, 465))
        self.Frame_CustomerRabbits_Facture_Advanced.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Frame_CustomerRabbits_Facture_Advanced.setFrameShape(QFrame.StyledPanel)
        self.Frame_CustomerRabbits_Facture_Advanced.setFrameShadow(QFrame.Raised)
        self.Customer_Rabbits_FactureScrollBar = QScrollArea(self.Frame_CustomerRabbits_Facture_Advanced)
        self.Customer_Rabbits_FactureScrollBar.setObjectName(u"Customer_Rabbits_FactureScrollBar")
        self.Customer_Rabbits_FactureScrollBar.setGeometry(QRect(5, 5, 840, 455))
        self.Customer_Rabbits_FactureScrollBar.setMinimumSize(QSize(840, 455))
        self.Customer_Rabbits_FactureScrollBar.setMaximumSize(QSize(840, 455))
        self.Customer_Rabbits_FactureScrollBar.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgba(0, 0, 0, 0);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Customer_Rabbits_FactureScrollBar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Customer_Rabbits_FactureScrollBar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Customer_Rabbits_FactureScrollBar.setWidgetResizable(True)
        self.Customer_Rabbits_FactureScrollBar_Content_7 = QWidget()
        self.Customer_Rabbits_FactureScrollBar_Content_7.setObjectName(u"Customer_Rabbits_FactureScrollBar_Content_7")
        self.Customer_Rabbits_FactureScrollBar_Content_7.setGeometry(QRect(0, 0, 836, 451))
        self.gridLayoutWidget_7 = QWidget(self.Customer_Rabbits_FactureScrollBar_Content_7)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(10, 10, 821, 431))
        self.GridLayout_Customer_Rabbits_FactureView = QGridLayout(self.gridLayoutWidget_7)
        self.GridLayout_Customer_Rabbits_FactureView.setObjectName(u"GridLayout_Customer_Rabbits_FactureView")
        self.GridLayout_Customer_Rabbits_FactureView.setContentsMargins(0, 0, 0, 0)
        self.Customer_Rabbits_FactureScrollBar.setWidget(self.Customer_Rabbits_FactureScrollBar_Content_7)
        self.Filter_Frame_View_2 = QFrame(self.Rabbits)
        self.Filter_Frame_View_2.setObjectName(u"Filter_Frame_View_2")
        self.Filter_Frame_View_2.setGeometry(QRect(131, 10, 620, 47))
        self.Filter_Frame_View_2.setMinimumSize(QSize(620, 47))
        self.Filter_Frame_View_2.setMaximumSize(QSize(620, 47))
        self.Filter_Frame_View_2.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 73, 73);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Filter_Frame_View_2.setFrameShape(QFrame.StyledPanel)
        self.Filter_Frame_View_2.setFrameShadow(QFrame.Raised)
        self.FilterGender_Rabbits = QComboBox(self.Filter_Frame_View_2)
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Gender_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/Icons/Gender_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterGender_Rabbits.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/Gender_Null_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/Icons/Gender_Null_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterGender_Rabbits.addItem(icon7, "")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/Gender_Male_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/Icons/Gender_Male_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterGender_Rabbits.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/Gender_Female_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/Icons/Gender_Female_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterGender_Rabbits.addItem(icon9, "")
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
        self.Ordre_Rabbits = QPushButton(self.Filter_Frame_View_2)
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
        self.Ordre_Rabbits.setChecked(True)
        self.Ordre_Rabbits.setAutoRepeat(False)
        self.Ordre_Rabbits.setAutoExclusive(False)
        self.Ordre_Rabbits.setAutoRepeatDelay(50)
        self.Ordre_Rabbits.setAutoRepeatInterval(10)
        self.Search_Rabbits = QLineEdit(self.Filter_Frame_View_2)
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
        self.FilterBy_Rabbits = QComboBox(self.Filter_Frame_View_2)
        self.FilterBy_Rabbits.addItem(icon, "")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/Rabbit_Tag.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/Icons/Rabbit_Tag.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon10, "")
        self.FilterBy_Rabbits.addItem(icon10, "")
        self.FilterBy_Rabbits.addItem(icon3, "")
        icon11 = QIcon()
        icon11.addFile(u":/Icons/Rabbit_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/Icons/Rabbit_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon11, "")
        icon12 = QIcon()
        icon12.addFile(u":/Icons/Rabbit_Tree_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon12.addFile(u":/Icons/Rabbit_Tree_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon12, "")
        self.FilterBy_Rabbits.addItem(icon12, "")
        self.FilterBy_Rabbits.addItem(icon12, "")
        icon13 = QIcon()
        icon13.addFile(u":/Icons/Settings_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/Icons/Settings_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon13, "")
        icon14 = QIcon()
        icon14.addFile(u":/Icons/Cages_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon14.addFile(u":/Icons/Cages_Green.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.FilterBy_Rabbits.addItem(icon14, "")
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
        self.Boughts_Tabs.addTab(self.Rabbits, "")
        self.Cages = QWidget()
        self.Cages.setObjectName(u"Cages")
        self.Frame_CustomerCages_Advanced = QFrame(self.Cages)
        self.Frame_CustomerCages_Advanced.setObjectName(u"Frame_CustomerCages_Advanced")
        self.Frame_CustomerCages_Advanced.setGeometry(QRect(10, 66, 850, 465))
        self.Frame_CustomerCages_Advanced.setMinimumSize(QSize(850, 465))
        self.Frame_CustomerCages_Advanced.setMaximumSize(QSize(850, 465))
        self.Frame_CustomerCages_Advanced.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Frame_CustomerCages_Advanced.setFrameShape(QFrame.StyledPanel)
        self.Frame_CustomerCages_Advanced.setFrameShadow(QFrame.Raised)
        self.Customer_CagesScrollBar = QScrollArea(self.Frame_CustomerCages_Advanced)
        self.Customer_CagesScrollBar.setObjectName(u"Customer_CagesScrollBar")
        self.Customer_CagesScrollBar.setGeometry(QRect(5, 5, 840, 455))
        self.Customer_CagesScrollBar.setMinimumSize(QSize(840, 455))
        self.Customer_CagesScrollBar.setMaximumSize(QSize(840, 455))
        self.Customer_CagesScrollBar.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgba(0, 0, 0, 0);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Customer_CagesScrollBar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Customer_CagesScrollBar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Customer_CagesScrollBar.setWidgetResizable(True)
        self.Customer_CagesScrollBar_Content = QWidget()
        self.Customer_CagesScrollBar_Content.setObjectName(u"Customer_CagesScrollBar_Content")
        self.Customer_CagesScrollBar_Content.setGeometry(QRect(0, 0, 836, 451))
        self.gridLayoutWidget_8 = QWidget(self.Customer_CagesScrollBar_Content)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(10, 10, 821, 441))
        self.GridLayout_Customer_Cages_View = QGridLayout(self.gridLayoutWidget_8)
        self.GridLayout_Customer_Cages_View.setObjectName(u"GridLayout_Customer_Cages_View")
        self.GridLayout_Customer_Cages_View.setContentsMargins(0, 0, 0, 0)
        self.Customer_CagesScrollBar.setWidget(self.Customer_CagesScrollBar_Content)
        self.Filter_Frame_View_3 = QFrame(self.Cages)
        self.Filter_Frame_View_3.setObjectName(u"Filter_Frame_View_3")
        self.Filter_Frame_View_3.setGeometry(QRect(131, 10, 620, 47))
        self.Filter_Frame_View_3.setMinimumSize(QSize(620, 47))
        self.Filter_Frame_View_3.setMaximumSize(QSize(620, 47))
        self.Filter_Frame_View_3.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(73, 73, 73);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Filter_Frame_View_3.setFrameShape(QFrame.StyledPanel)
        self.Filter_Frame_View_3.setFrameShadow(QFrame.Raised)
        self.FilterBy_Cages = QComboBox(self.Filter_Frame_View_3)
        self.FilterBy_Cages.addItem(icon, "")
        self.FilterBy_Cages.addItem(icon14, "")
        self.FilterBy_Cages.addItem(icon4, "")
        self.FilterBy_Cages.addItem(icon4, "")
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
        self.Ordre_Cages = QPushButton(self.Filter_Frame_View_3)
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
        self.Ordre_Cages.setChecked(True)
        self.Ordre_Cages.setAutoRepeat(False)
        self.Ordre_Cages.setAutoExclusive(False)
        self.Ordre_Cages.setAutoRepeatDelay(50)
        self.Ordre_Cages.setAutoRepeatInterval(10)
        self.Search_Cages = QLineEdit(self.Filter_Frame_View_3)
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
        self.FilterGender_Cages = QComboBox(self.Filter_Frame_View_3)
        self.FilterGender_Cages.addItem(icon6, "")
        self.FilterGender_Cages.addItem(icon8, "")
        self.FilterGender_Cages.addItem(icon9, "")
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
        self.Boughts_Tabs.addTab(self.Cages, "")
        self.Menu_Customer_View.addTab(self.Boughts, "")
        self.Infos_Frame = QFrame(Customer_View_Main)
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
        self.Customer_Name_Label = QLabel(self.Infos_Frame)
        self.Customer_Name_Label.setObjectName(u"Customer_Name_Label")
        self.Customer_Name_Label.setGeometry(QRect(50, 51, 311, 21))
        self.Customer_Name_Label.setMinimumSize(QSize(311, 21))
        self.Customer_Name_Label.setMaximumSize(QSize(311, 21))
        self.Customer_Name_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";")
        self.Customer_Phone_Label = QLabel(self.Infos_Frame)
        self.Customer_Phone_Label.setObjectName(u"Customer_Phone_Label")
        self.Customer_Phone_Label.setGeometry(QRect(50, 86, 141, 21))
        self.Customer_Phone_Label.setMinimumSize(QSize(141, 21))
        self.Customer_Phone_Label.setMaximumSize(QSize(141, 21))
        self.Customer_Phone_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";\n"
"}")
        self.Customer_Gender_Label = QLabel(self.Infos_Frame)
        self.Customer_Gender_Label.setObjectName(u"Customer_Gender_Label")
        self.Customer_Gender_Label.setGeometry(QRect(50, 121, 181, 21))
        self.Customer_Gender_Label.setMinimumSize(QSize(181, 21))
        self.Customer_Gender_Label.setMaximumSize(QSize(181, 21))
        self.Customer_Gender_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";\n"
"}")
        self.Customer_Address_Label = QLabel(self.Infos_Frame)
        self.Customer_Address_Label.setObjectName(u"Customer_Address_Label")
        self.Customer_Address_Label.setGeometry(QRect(50, 159, 681, 21))
        self.Customer_Address_Label.setMinimumSize(QSize(211, 21))
        self.Customer_Address_Label.setMaximumSize(QSize(681, 21))
        self.Customer_Address_Label.setStyleSheet(u"QLabel {\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Acme\";\n"
"}")
        self.Customer_Address_Label.setScaledContents(True)
        self.Customer_Address_Label.setWordWrap(False)
        self.Customer_Avatar_Frame = QFrame(self.Infos_Frame)
        self.Customer_Avatar_Frame.setObjectName(u"Customer_Avatar_Frame")
        self.Customer_Avatar_Frame.setGeometry(QRect(703, 10, 119, 161))
        self.Customer_Avatar_Frame.setMinimumSize(QSize(119, 161))
        self.Customer_Avatar_Frame.setMaximumSize(QSize(119, 161))
        self.Customer_Avatar_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #D9D9D9;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Customer_Avatar_Frame.setFrameShape(QFrame.StyledPanel)
        self.Customer_Avatar_Frame.setFrameShadow(QFrame.Raised)
        self.Customer_Avatar_Label = QLabel(self.Customer_Avatar_Frame)
        self.Customer_Avatar_Label.setObjectName(u"Customer_Avatar_Label")
        self.Customer_Avatar_Label.setGeometry(QRect(9, 10, 101, 141))
        self.Customer_Avatar_Label.setStyleSheet(u"border:none;")
        self.Customer_Avatar_Label.setPixmap(QPixmap(u":/Icons/Customer_Green.png"))
        self.Customer_Avatar_Label.setScaledContents(False)
        self.Customer_Avatar_Label.setAlignment(Qt.AlignCenter)
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
        self.Customer_Notes_PleinText = QPlainTextEdit(self.Infos_Frame)
        self.Customer_Notes_PleinText.setObjectName(u"Customer_Notes_PleinText")
        self.Customer_Notes_PleinText.setGeometry(QRect(445, 10, 251, 131))
        self.Customer_Notes_PleinText.setMinimumSize(QSize(251, 131))
        self.Customer_Notes_PleinText.setMaximumSize(QSize(251, 131))
        self.Customer_Notes_PleinText.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.UpArrowCursor))
        self.Customer_Notes_PleinText.setStyleSheet(u"QPlainTextEdit{\n"
"	background-color: rgb(69, 69, 69);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Customer_Notes_PleinText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Customer_Notes_PleinText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Customer_Notes_PleinText.setReadOnly(True)
        self.Notes_Label_Frame = QFrame(self.Infos_Frame)
        self.Notes_Label_Frame.setObjectName(u"Notes_Label_Frame")
        self.Notes_Label_Frame.setGeometry(QRect(400, 10, 41, 131))
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
        self.Activity_Frame = QFrame(Customer_View_Main)
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
        self.Exit_Customer_View = QPushButton(self.Activity_Frame)
        self.Exit_Customer_View.setObjectName(u"Exit_Customer_View")
        self.Exit_Customer_View.setEnabled(True)
        self.Exit_Customer_View.setGeometry(QRect(7, 20, 33, 33))
        self.Exit_Customer_View.setMinimumSize(QSize(33, 33))
        self.Exit_Customer_View.setMaximumSize(QSize(33, 33))
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
        self.Edit_Customer = QPushButton(self.Activity_Frame)
        self.Edit_Customer.setObjectName(u"Edit_Customer")
        self.Edit_Customer.setEnabled(True)
        self.Edit_Customer.setGeometry(QRect(7, 83, 33, 33))
        self.Edit_Customer.setMinimumSize(QSize(33, 33))
        self.Edit_Customer.setMaximumSize(QSize(33, 33))
        self.Edit_Customer.setFont(font)
        self.Edit_Customer.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Edit_Customer.setStyleSheet(u"QPushButton {\n"
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
        self.Edit_Customer.setIconSize(QSize(20, 20))
        self.Edit_Customer.setCheckable(False)
        self.Edit_Customer.setAutoRepeat(False)
        self.Edit_Customer.setAutoExclusive(False)
        self.Edit_Customer.setAutoRepeatDelay(50)
        self.Edit_Customer.setAutoRepeatInterval(10)
        self.Delete_Customer = QPushButton(self.Activity_Frame)
        self.Delete_Customer.setObjectName(u"Delete_Customer")
        self.Delete_Customer.setEnabled(True)
        self.Delete_Customer.setGeometry(QRect(7, 146, 33, 33))
        self.Delete_Customer.setMinimumSize(QSize(33, 33))
        self.Delete_Customer.setMaximumSize(QSize(33, 33))
        self.Delete_Customer.setFont(font)
        self.Delete_Customer.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Delete_Customer.setStyleSheet(u"QPushButton {\n"
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
        self.Delete_Customer.setIconSize(QSize(20, 20))
        self.Delete_Customer.setCheckable(False)
        self.Delete_Customer.setAutoRepeat(False)
        self.Delete_Customer.setAutoExclusive(False)
        self.Delete_Customer.setAutoRepeatDelay(50)
        self.Delete_Customer.setAutoRepeatInterval(10)
        self.Background = QFrame(Customer_View_Main)
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
        self.Background.raise_()
        self.Infos_Frame.raise_()
        self.Activity_Frame.raise_()
        self.Menu_Customer_View.raise_()

        self.retranslateUi(Customer_View_Main)
        self.Exit_Customer_View.clicked.connect(Customer_View_Main.close)

        self.Menu_Customer_View.setCurrentIndex(0)
        self.FactureTabs.setCurrentIndex(0)
        self.Boughts_Tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Customer_View_Main)
    # setupUi

    def retranslateUi(self, Customer_View_Main):
        Customer_View_Main.setWindowTitle(QCoreApplication.translate("Customer_View_Main", u"Dialog", None))
        self.FilterBy_Customer_Facture.setItemText(0, QCoreApplication.translate("Customer_View_Main", u"By", None))
        self.FilterBy_Customer_Facture.setItemText(1, QCoreApplication.translate("Customer_View_Main", u"ID", None))
        self.FilterBy_Customer_Facture.setItemText(2, QCoreApplication.translate("Customer_View_Main", u"Date", None))
        self.FilterBy_Customer_Facture.setItemText(3, QCoreApplication.translate("Customer_View_Main", u"Total", None))

        self.Ordre_Customer_Facture.setText("")
        self.Search_Customer_Facture.setInputMask("")
        self.Search_Customer_Facture.setText("")
        self.Search_Customer_Facture.setPlaceholderText(QCoreApplication.translate("Customer_View_Main", u"Search Facture...", None))
        self.FactureTabs.setTabText(self.FactureTabs.indexOf(self.View), QCoreApplication.translate("Customer_View_Main", u"View", None))
        ___qtablewidgetitem = self.FacturesCustomesTable_Advanced.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Customer_View_Main", u"ID", None));
        ___qtablewidgetitem1 = self.FacturesCustomesTable_Advanced.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Customer_View_Main", u"Date", None));
        ___qtablewidgetitem2 = self.FacturesCustomesTable_Advanced.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Customer_View_Main", u"Total", None));
        ___qtablewidgetitem3 = self.FacturesCustomesTable_Advanced.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Customer_View_Main", u"Actions", None));
        self.Export_PDF_Customers.setText("")
        self.Export_Exel_Customers.setText("")
        self.Exportation_CustomerFacture_Info.setText("")
        self.FactureTabs.setTabText(self.FactureTabs.indexOf(self.Advanced), QCoreApplication.translate("Customer_View_Main", u"Advanced", None))
        self.Menu_Customer_View.setTabText(self.Menu_Customer_View.indexOf(self.Facture), QCoreApplication.translate("Customer_View_Main", u"Facture", None))
        self.FilterGender_Rabbits.setItemText(0, QCoreApplication.translate("Customer_View_Main", u"Gender", None))
        self.FilterGender_Rabbits.setItemText(1, QCoreApplication.translate("Customer_View_Main", u"Null", None))
        self.FilterGender_Rabbits.setItemText(2, QCoreApplication.translate("Customer_View_Main", u"Male", None))
        self.FilterGender_Rabbits.setItemText(3, QCoreApplication.translate("Customer_View_Main", u"Female", None))

        self.Ordre_Rabbits.setText("")
        self.Search_Rabbits.setInputMask("")
        self.Search_Rabbits.setText("")
        self.Search_Rabbits.setPlaceholderText(QCoreApplication.translate("Customer_View_Main", u"Search Rabbit...", None))
        self.FilterBy_Rabbits.setItemText(0, QCoreApplication.translate("Customer_View_Main", u"By", None))
        self.FilterBy_Rabbits.setItemText(1, QCoreApplication.translate("Customer_View_Main", u"ID", None))
        self.FilterBy_Rabbits.setItemText(2, QCoreApplication.translate("Customer_View_Main", u"Breed", None))
        self.FilterBy_Rabbits.setItemText(3, QCoreApplication.translate("Customer_View_Main", u"Born", None))
        self.FilterBy_Rabbits.setItemText(4, QCoreApplication.translate("Customer_View_Main", u"Color", None))
        self.FilterBy_Rabbits.setItemText(5, QCoreApplication.translate("Customer_View_Main", u"Mother", None))
        self.FilterBy_Rabbits.setItemText(6, QCoreApplication.translate("Customer_View_Main", u"Father", None))
        self.FilterBy_Rabbits.setItemText(7, QCoreApplication.translate("Customer_View_Main", u"Generation", None))
        self.FilterBy_Rabbits.setItemText(8, QCoreApplication.translate("Customer_View_Main", u"Type", None))
        self.FilterBy_Rabbits.setItemText(9, QCoreApplication.translate("Customer_View_Main", u"CageID", None))

        self.Boughts_Tabs.setTabText(self.Boughts_Tabs.indexOf(self.Rabbits), QCoreApplication.translate("Customer_View_Main", u"Rabbits", None))
        self.FilterBy_Cages.setItemText(0, QCoreApplication.translate("Customer_View_Main", u"By", None))
        self.FilterBy_Cages.setItemText(1, QCoreApplication.translate("Customer_View_Main", u"ID", None))
        self.FilterBy_Cages.setItemText(2, QCoreApplication.translate("Customer_View_Main", u"Sold", None))
        self.FilterBy_Cages.setItemText(3, QCoreApplication.translate("Customer_View_Main", u"Bought", None))

        self.Ordre_Cages.setText("")
        self.Search_Cages.setInputMask("")
        self.Search_Cages.setText("")
        self.Search_Cages.setPlaceholderText(QCoreApplication.translate("Customer_View_Main", u"Search Facture...", None))
        self.FilterGender_Cages.setItemText(0, QCoreApplication.translate("Customer_View_Main", u"Gender", None))
        self.FilterGender_Cages.setItemText(1, QCoreApplication.translate("Customer_View_Main", u"Male", None))
        self.FilterGender_Cages.setItemText(2, QCoreApplication.translate("Customer_View_Main", u"Female", None))

        self.Boughts_Tabs.setTabText(self.Boughts_Tabs.indexOf(self.Cages), QCoreApplication.translate("Customer_View_Main", u"Cages", None))
        self.Menu_Customer_View.setTabText(self.Menu_Customer_View.indexOf(self.Boughts), QCoreApplication.translate("Customer_View_Main", u"Boughts", None))
        self.ID_Label.setText(QCoreApplication.translate("Customer_View_Main", u"ID : ", None))
        self.Customer_Name_Label.setText(QCoreApplication.translate("Customer_View_Main", u"Name : ", None))
        self.Customer_Phone_Label.setText(QCoreApplication.translate("Customer_View_Main", u"Phone : ", None))
        self.Customer_Gender_Label.setText(QCoreApplication.translate("Customer_View_Main", u"Gender : ", None))
        self.Customer_Address_Label.setText(QCoreApplication.translate("Customer_View_Main", u"Address : ", None))
        self.Customer_Avatar_Label.setText("")
        self.Customer_Name_Icon.setText("")
        self.Customer_Phone_Icon.setText("")
        self.Customer_Gender_Icon.setText("")
        self.Customer_Address_Icon.setText("")
        self.Notes_Text_Label.setText(QCoreApplication.translate("Customer_View_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">N</span></p></body></html>", None))
        self.Notes_Text_Label_2.setText(QCoreApplication.translate("Customer_View_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">O</span></p></body></html>", None))
        self.Notes_Text_Label_3.setText(QCoreApplication.translate("Customer_View_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">T</span></p></body></html>", None))
        self.Notes_Text_Label_4.setText(QCoreApplication.translate("Customer_View_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">E</span></p></body></html>", None))
        self.Notes_Text_Label_5.setText(QCoreApplication.translate("Customer_View_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">S</span></p></body></html>", None))
        self.Exit_Customer_View.setText("")
#if QT_CONFIG(shortcut)
        self.Exit_Customer_View.setShortcut(QCoreApplication.translate("Customer_View_Main", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.Edit_Customer.setText("")
        self.Delete_Customer.setText("")
#if QT_CONFIG(shortcut)
        self.Delete_Customer.setShortcut(QCoreApplication.translate("Customer_View_Main", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.Title.setText(QCoreApplication.translate("Customer_View_Main", u"Customer Viewer Window", None))
    # retranslateUi

