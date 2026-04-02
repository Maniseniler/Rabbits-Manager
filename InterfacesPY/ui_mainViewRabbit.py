# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainViewRabbit.ui'
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
    QPlainTextEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QWidget)
import resources_rc

class Ui_Rabbit_View_Main(object):
    def setupUi(self, Rabbit_View_Main):
        if not Rabbit_View_Main.objectName():
            Rabbit_View_Main.setObjectName(u"Rabbit_View_Main")
        Rabbit_View_Main.resize(1031, 867)
        Rabbit_View_Main.setMinimumSize(QSize(1031, 867))
        Rabbit_View_Main.setMaximumSize(QSize(1031, 867))
        Rabbit_View_Main.setStyleSheet(u"")
        self.Background = QFrame(Rabbit_View_Main)
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
        self.Breeding_Info_Frame = QFrame(self.Background)
        self.Breeding_Info_Frame.setObjectName(u"Breeding_Info_Frame")
        self.Breeding_Info_Frame.setEnabled(True)
        self.Breeding_Info_Frame.setGeometry(QRect(310, 10, 331, 691))
        self.Breeding_Info_Frame.setMinimumSize(QSize(331, 691))
        self.Breeding_Info_Frame.setMaximumSize(QSize(331, 691))
        self.Breeding_Info_Frame.setMouseTracking(False)
        self.Breeding_Info_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"	font: 75 10pt \"Acme\";\n"
"}")
        self.Breeding_Info_Frame.setFrameShape(QFrame.StyledPanel)
        self.Breeding_Info_Frame.setFrameShadow(QFrame.Raised)
        self.YearSelection_Rabbit = QComboBox(self.Breeding_Info_Frame)
        icon = QIcon()
        icon.addFile(u":/Icons/Calendar_White.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.addItem(icon, "")
        self.YearSelection_Rabbit.setObjectName(u"YearSelection_Rabbit")
        self.YearSelection_Rabbit.setGeometry(QRect(27, 6, 120, 24))
        self.YearSelection_Rabbit.setMinimumSize(QSize(120, 24))
        self.YearSelection_Rabbit.setMaximumSize(QSize(120, 24))
        self.YearSelection_Rabbit.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid white;\n"
"	border-radius:6px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 15px;\n"
"	selection-background-color: #2980B9;\n"
"}")
        self.layoutWidget = QWidget(self.Breeding_Info_Frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(21, 38, 291, 638))
        self.Rabbit_Detail_Grid = QGridLayout(self.layoutWidget)
        self.Rabbit_Detail_Grid.setObjectName(u"Rabbit_Detail_Grid")
        self.Rabbit_Detail_Grid.setContentsMargins(0, 0, 0, 0)
        self.Rabbit_Detail_Table_10 = QTableWidget(self.layoutWidget)
        if (self.Rabbit_Detail_Table_10.columnCount() < 1):
            self.Rabbit_Detail_Table_10.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setIcon(icon);
        self.Rabbit_Detail_Table_10.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.Rabbit_Detail_Table_10.setObjectName(u"Rabbit_Detail_Table_10")
        self.Rabbit_Detail_Table_10.setMinimumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_10.setMaximumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_10.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-radius:10px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border:0px;\n"
"}")
        self.Rabbit_Detail_Table_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_10.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_10.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Rabbit_Detail_Table_10.horizontalHeader().setDefaultSectionSize(10)
        self.Rabbit_Detail_Table_10.horizontalHeader().setStretchLastSection(True)
        self.Rabbit_Detail_Table_10.verticalHeader().setVisible(False)

        self.Rabbit_Detail_Grid.addWidget(self.Rabbit_Detail_Table_10, 3, 0, 1, 1)

        self.Rabbit_Detail_Table_11 = QTableWidget(self.layoutWidget)
        if (self.Rabbit_Detail_Table_11.columnCount() < 1):
            self.Rabbit_Detail_Table_11.setColumnCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setIcon(icon);
        self.Rabbit_Detail_Table_11.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        self.Rabbit_Detail_Table_11.setObjectName(u"Rabbit_Detail_Table_11")
        self.Rabbit_Detail_Table_11.setMinimumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_11.setMaximumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_11.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-radius:10px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border:0px;\n"
"}")
        self.Rabbit_Detail_Table_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_11.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Rabbit_Detail_Table_11.horizontalHeader().setDefaultSectionSize(10)
        self.Rabbit_Detail_Table_11.horizontalHeader().setStretchLastSection(True)
        self.Rabbit_Detail_Table_11.verticalHeader().setVisible(False)

        self.Rabbit_Detail_Grid.addWidget(self.Rabbit_Detail_Table_11, 3, 1, 1, 1)

        self.Rabbit_Detail_Table_2 = QTableWidget(self.layoutWidget)
        if (self.Rabbit_Detail_Table_2.columnCount() < 1):
            self.Rabbit_Detail_Table_2.setColumnCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setIcon(icon);
        self.Rabbit_Detail_Table_2.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        self.Rabbit_Detail_Table_2.setObjectName(u"Rabbit_Detail_Table_2")
        self.Rabbit_Detail_Table_2.setMinimumSize(QSize(93, 156))
        self.Rabbit_Detail_Table_2.setMaximumSize(QSize(93, 156))
        self.Rabbit_Detail_Table_2.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-radius:10px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border:0px;\n"
"}")
        self.Rabbit_Detail_Table_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Rabbit_Detail_Table_2.horizontalHeader().setDefaultSectionSize(10)
        self.Rabbit_Detail_Table_2.horizontalHeader().setStretchLastSection(True)
        self.Rabbit_Detail_Table_2.verticalHeader().setVisible(False)

        self.Rabbit_Detail_Grid.addWidget(self.Rabbit_Detail_Table_2, 0, 1, 1, 1)

        self.Rabbit_Detail_Table_8 = QTableWidget(self.layoutWidget)
        if (self.Rabbit_Detail_Table_8.columnCount() < 1):
            self.Rabbit_Detail_Table_8.setColumnCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setIcon(icon);
        self.Rabbit_Detail_Table_8.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        self.Rabbit_Detail_Table_8.setObjectName(u"Rabbit_Detail_Table_8")
        self.Rabbit_Detail_Table_8.setMinimumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_8.setMaximumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_8.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-radius:10px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border:0px;\n"
"}")
        self.Rabbit_Detail_Table_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_8.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Rabbit_Detail_Table_8.horizontalHeader().setDefaultSectionSize(10)
        self.Rabbit_Detail_Table_8.horizontalHeader().setStretchLastSection(True)
        self.Rabbit_Detail_Table_8.verticalHeader().setVisible(False)

        self.Rabbit_Detail_Grid.addWidget(self.Rabbit_Detail_Table_8, 2, 1, 1, 1)

        self.Rabbit_Detail_Table_6 = QTableWidget(self.layoutWidget)
        if (self.Rabbit_Detail_Table_6.columnCount() < 1):
            self.Rabbit_Detail_Table_6.setColumnCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setIcon(icon);
        self.Rabbit_Detail_Table_6.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        self.Rabbit_Detail_Table_6.setObjectName(u"Rabbit_Detail_Table_6")
        self.Rabbit_Detail_Table_6.setMinimumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_6.setMaximumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_6.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-radius:10px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border:0px;\n"
"}")
        self.Rabbit_Detail_Table_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_6.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Rabbit_Detail_Table_6.horizontalHeader().setDefaultSectionSize(10)
        self.Rabbit_Detail_Table_6.horizontalHeader().setStretchLastSection(True)
        self.Rabbit_Detail_Table_6.verticalHeader().setVisible(False)

        self.Rabbit_Detail_Grid.addWidget(self.Rabbit_Detail_Table_6, 1, 2, 1, 1)

        self.Rabbit_Detail_Table_7 = QTableWidget(self.layoutWidget)
        if (self.Rabbit_Detail_Table_7.columnCount() < 1):
            self.Rabbit_Detail_Table_7.setColumnCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setIcon(icon);
        self.Rabbit_Detail_Table_7.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        self.Rabbit_Detail_Table_7.setObjectName(u"Rabbit_Detail_Table_7")
        self.Rabbit_Detail_Table_7.setMinimumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_7.setMaximumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_7.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-radius:10px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border:0px;\n"
"}")
        self.Rabbit_Detail_Table_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_7.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Rabbit_Detail_Table_7.horizontalHeader().setDefaultSectionSize(10)
        self.Rabbit_Detail_Table_7.horizontalHeader().setStretchLastSection(True)
        self.Rabbit_Detail_Table_7.verticalHeader().setVisible(False)

        self.Rabbit_Detail_Grid.addWidget(self.Rabbit_Detail_Table_7, 2, 0, 1, 1)

        self.Rabbit_Detail_Table_9 = QTableWidget(self.layoutWidget)
        if (self.Rabbit_Detail_Table_9.columnCount() < 1):
            self.Rabbit_Detail_Table_9.setColumnCount(1)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setIcon(icon);
        self.Rabbit_Detail_Table_9.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        self.Rabbit_Detail_Table_9.setObjectName(u"Rabbit_Detail_Table_9")
        self.Rabbit_Detail_Table_9.setMinimumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_9.setMaximumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_9.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-radius:10px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border:0px;\n"
"}")
        self.Rabbit_Detail_Table_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_9.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Rabbit_Detail_Table_9.horizontalHeader().setDefaultSectionSize(10)
        self.Rabbit_Detail_Table_9.horizontalHeader().setStretchLastSection(True)
        self.Rabbit_Detail_Table_9.verticalHeader().setVisible(False)

        self.Rabbit_Detail_Grid.addWidget(self.Rabbit_Detail_Table_9, 2, 2, 1, 1)

        self.Rabbit_Detail_Table_4 = QTableWidget(self.layoutWidget)
        if (self.Rabbit_Detail_Table_4.columnCount() < 1):
            self.Rabbit_Detail_Table_4.setColumnCount(1)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setIcon(icon);
        self.Rabbit_Detail_Table_4.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        self.Rabbit_Detail_Table_4.setObjectName(u"Rabbit_Detail_Table_4")
        self.Rabbit_Detail_Table_4.setMinimumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_4.setMaximumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_4.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-radius:10px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border:0px;\n"
"}")
        self.Rabbit_Detail_Table_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Rabbit_Detail_Table_4.horizontalHeader().setDefaultSectionSize(10)
        self.Rabbit_Detail_Table_4.horizontalHeader().setStretchLastSection(True)
        self.Rabbit_Detail_Table_4.verticalHeader().setVisible(False)

        self.Rabbit_Detail_Grid.addWidget(self.Rabbit_Detail_Table_4, 1, 0, 1, 1)

        self.Rabbit_Detail_Table_3 = QTableWidget(self.layoutWidget)
        if (self.Rabbit_Detail_Table_3.columnCount() < 1):
            self.Rabbit_Detail_Table_3.setColumnCount(1)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setIcon(icon);
        self.Rabbit_Detail_Table_3.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        self.Rabbit_Detail_Table_3.setObjectName(u"Rabbit_Detail_Table_3")
        self.Rabbit_Detail_Table_3.setMinimumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_3.setMaximumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_3.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-radius:10px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border:0px;\n"
"}")
        self.Rabbit_Detail_Table_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Rabbit_Detail_Table_3.horizontalHeader().setDefaultSectionSize(10)
        self.Rabbit_Detail_Table_3.horizontalHeader().setStretchLastSection(True)
        self.Rabbit_Detail_Table_3.verticalHeader().setVisible(False)

        self.Rabbit_Detail_Grid.addWidget(self.Rabbit_Detail_Table_3, 0, 2, 1, 1)

        self.Rabbit_Detail_Table_1 = QTableWidget(self.layoutWidget)
        if (self.Rabbit_Detail_Table_1.columnCount() < 1):
            self.Rabbit_Detail_Table_1.setColumnCount(1)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setIcon(icon);
        self.Rabbit_Detail_Table_1.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        self.Rabbit_Detail_Table_1.setObjectName(u"Rabbit_Detail_Table_1")
        self.Rabbit_Detail_Table_1.setMinimumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_1.setMaximumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_1.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-radius:10px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border:0px;\n"
"}")
        self.Rabbit_Detail_Table_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Rabbit_Detail_Table_1.horizontalHeader().setDefaultSectionSize(10)
        self.Rabbit_Detail_Table_1.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.Rabbit_Detail_Table_1.horizontalHeader().setStretchLastSection(True)
        self.Rabbit_Detail_Table_1.verticalHeader().setVisible(False)

        self.Rabbit_Detail_Grid.addWidget(self.Rabbit_Detail_Table_1, 0, 0, 1, 1)

        self.Rabbit_Detail_Table_5 = QTableWidget(self.layoutWidget)
        if (self.Rabbit_Detail_Table_5.columnCount() < 1):
            self.Rabbit_Detail_Table_5.setColumnCount(1)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setIcon(icon);
        self.Rabbit_Detail_Table_5.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        self.Rabbit_Detail_Table_5.setObjectName(u"Rabbit_Detail_Table_5")
        self.Rabbit_Detail_Table_5.setMinimumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_5.setMaximumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_5.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-radius:10px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border:0px;\n"
"}")
        self.Rabbit_Detail_Table_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Rabbit_Detail_Table_5.horizontalHeader().setDefaultSectionSize(10)
        self.Rabbit_Detail_Table_5.horizontalHeader().setStretchLastSection(True)
        self.Rabbit_Detail_Table_5.verticalHeader().setVisible(False)

        self.Rabbit_Detail_Grid.addWidget(self.Rabbit_Detail_Table_5, 1, 1, 1, 1)

        self.Rabbit_Detail_Table_12 = QTableWidget(self.layoutWidget)
        if (self.Rabbit_Detail_Table_12.columnCount() < 1):
            self.Rabbit_Detail_Table_12.setColumnCount(1)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setIcon(icon);
        self.Rabbit_Detail_Table_12.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        self.Rabbit_Detail_Table_12.setObjectName(u"Rabbit_Detail_Table_12")
        self.Rabbit_Detail_Table_12.setMinimumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_12.setMaximumSize(QSize(92, 156))
        self.Rabbit_Detail_Table_12.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-radius:10px;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(143, 143, 143);\n"
"	alternate-background-color: rgb(176, 237, 251);\n"
"	border:0px;\n"
"}")
        self.Rabbit_Detail_Table_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_12.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Detail_Table_12.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Rabbit_Detail_Table_12.horizontalHeader().setDefaultSectionSize(10)
        self.Rabbit_Detail_Table_12.horizontalHeader().setStretchLastSection(True)
        self.Rabbit_Detail_Table_12.verticalHeader().setVisible(False)

        self.Rabbit_Detail_Grid.addWidget(self.Rabbit_Detail_Table_12, 3, 2, 1, 1)

        self.Rabbit_Total_Bunnies_Label = QLabel(self.Breeding_Info_Frame)
        self.Rabbit_Total_Bunnies_Label.setObjectName(u"Rabbit_Total_Bunnies_Label")
        self.Rabbit_Total_Bunnies_Label.setGeometry(QRect(157, 7, 159, 21))
        self.Rabbit_Total_Bunnies_Label.setMinimumSize(QSize(159, 21))
        self.Rabbit_Total_Bunnies_Label.setMaximumSize(QSize(159, 21))
        self.Rabbit_Total_Bunnies_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Activity_Frame = QFrame(self.Background)
        self.Activity_Frame.setObjectName(u"Activity_Frame")
        self.Activity_Frame.setGeometry(QRect(790, 20, 207, 46))
        self.Activity_Frame.setMinimumSize(QSize(207, 46))
        self.Activity_Frame.setMaximumSize(QSize(207, 46))
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
        self.Exit_Customer_View.setGeometry(QRect(150, 6, 33, 33))
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
        self.Edit_Rabbit = QPushButton(self.Activity_Frame)
        self.Edit_Rabbit.setObjectName(u"Edit_Rabbit")
        self.Edit_Rabbit.setEnabled(True)
        self.Edit_Rabbit.setGeometry(QRect(90, 6, 33, 33))
        self.Edit_Rabbit.setMinimumSize(QSize(33, 33))
        self.Edit_Rabbit.setMaximumSize(QSize(33, 33))
        self.Edit_Rabbit.setFont(font)
        self.Edit_Rabbit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Edit_Rabbit.setStyleSheet(u"QPushButton {\n"
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
        self.Edit_Rabbit.setIconSize(QSize(20, 20))
        self.Edit_Rabbit.setCheckable(False)
        self.Edit_Rabbit.setAutoRepeat(False)
        self.Edit_Rabbit.setAutoExclusive(False)
        self.Edit_Rabbit.setAutoRepeatDelay(50)
        self.Edit_Rabbit.setAutoRepeatInterval(10)
        self.Delete_Rabbit = QPushButton(self.Activity_Frame)
        self.Delete_Rabbit.setObjectName(u"Delete_Rabbit")
        self.Delete_Rabbit.setEnabled(True)
        self.Delete_Rabbit.setGeometry(QRect(30, 6, 33, 33))
        self.Delete_Rabbit.setMinimumSize(QSize(33, 33))
        self.Delete_Rabbit.setMaximumSize(QSize(33, 33))
        self.Delete_Rabbit.setFont(font)
        self.Delete_Rabbit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Delete_Rabbit.setStyleSheet(u"QPushButton {\n"
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
        self.Delete_Rabbit.setIconSize(QSize(20, 20))
        self.Delete_Rabbit.setCheckable(False)
        self.Delete_Rabbit.setAutoRepeat(False)
        self.Delete_Rabbit.setAutoExclusive(False)
        self.Delete_Rabbit.setAutoRepeatDelay(50)
        self.Delete_Rabbit.setAutoRepeatInterval(10)
        self.General_Info_Frame = QFrame(self.Background)
        self.General_Info_Frame.setObjectName(u"General_Info_Frame")
        self.General_Info_Frame.setGeometry(QRect(30, 50, 271, 780))
        self.General_Info_Frame.setMinimumSize(QSize(271, 780))
        self.General_Info_Frame.setMaximumSize(QSize(271, 780))
        self.General_Info_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.General_Info_Frame.setFrameShape(QFrame.StyledPanel)
        self.General_Info_Frame.setFrameShadow(QFrame.Raised)
        self.Breed_Frame = QFrame(self.General_Info_Frame)
        self.Breed_Frame.setObjectName(u"Breed_Frame")
        self.Breed_Frame.setGeometry(QRect(20, 20, 230, 40))
        self.Breed_Frame.setMinimumSize(QSize(230, 40))
        self.Breed_Frame.setMaximumSize(QSize(230, 40))
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
        self.Rabbit_Breed_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Breed_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Breed_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Breed_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Breed_Icon.setPixmap(QPixmap(u":/Icons/Rabbit_Tag.png"))
        self.Rabbit_Breed_Icon.setScaledContents(True)
        self.Rabbit_Breed_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Breed_Icon.setWordWrap(False)
        self.Rabbit_Breed_Label = QLabel(self.Breed_Frame)
        self.Rabbit_Breed_Label.setObjectName(u"Rabbit_Breed_Label")
        self.Rabbit_Breed_Label.setGeometry(QRect(50, 9, 169, 21))
        self.Rabbit_Breed_Label.setMinimumSize(QSize(169, 21))
        self.Rabbit_Breed_Label.setMaximumSize(QSize(169, 21))
        self.Rabbit_Breed_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Born_Frame = QFrame(self.General_Info_Frame)
        self.Born_Frame.setObjectName(u"Born_Frame")
        self.Born_Frame.setGeometry(QRect(20, 70, 230, 40))
        self.Born_Frame.setMinimumSize(QSize(230, 40))
        self.Born_Frame.setMaximumSize(QSize(230, 40))
        self.Born_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Born_Frame.setFrameShape(QFrame.StyledPanel)
        self.Born_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Born_Icon = QLabel(self.Born_Frame)
        self.Rabbit_Born_Icon.setObjectName(u"Rabbit_Born_Icon")
        self.Rabbit_Born_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Born_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Born_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Born_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Born_Icon.setPixmap(QPixmap(u":/Icons/Calendar_White.png"))
        self.Rabbit_Born_Icon.setScaledContents(True)
        self.Rabbit_Born_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Born_Icon.setWordWrap(False)
        self.Rabbit_Born_Label = QLabel(self.Born_Frame)
        self.Rabbit_Born_Label.setObjectName(u"Rabbit_Born_Label")
        self.Rabbit_Born_Label.setGeometry(QRect(50, 9, 169, 21))
        self.Rabbit_Born_Label.setMinimumSize(QSize(169, 21))
        self.Rabbit_Born_Label.setMaximumSize(QSize(169, 21))
        self.Rabbit_Born_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Color_Frame = QFrame(self.General_Info_Frame)
        self.Color_Frame.setObjectName(u"Color_Frame")
        self.Color_Frame.setGeometry(QRect(20, 170, 230, 40))
        self.Color_Frame.setMinimumSize(QSize(230, 40))
        self.Color_Frame.setMaximumSize(QSize(230, 40))
        self.Color_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Color_Frame.setFrameShape(QFrame.StyledPanel)
        self.Color_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Color_Icon = QLabel(self.Color_Frame)
        self.Rabbit_Color_Icon.setObjectName(u"Rabbit_Color_Icon")
        self.Rabbit_Color_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Color_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Color_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Color_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Color_Icon.setPixmap(QPixmap(u":/Icons/Rabbit_White.png"))
        self.Rabbit_Color_Icon.setScaledContents(True)
        self.Rabbit_Color_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Color_Icon.setWordWrap(False)
        self.Rabbit_Color_Label = QLabel(self.Color_Frame)
        self.Rabbit_Color_Label.setObjectName(u"Rabbit_Color_Label")
        self.Rabbit_Color_Label.setGeometry(QRect(50, 9, 169, 21))
        self.Rabbit_Color_Label.setMinimumSize(QSize(169, 21))
        self.Rabbit_Color_Label.setMaximumSize(QSize(169, 21))
        self.Rabbit_Color_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Father_Frame = QFrame(self.General_Info_Frame)
        self.Father_Frame.setObjectName(u"Father_Frame")
        self.Father_Frame.setGeometry(QRect(20, 270, 230, 40))
        self.Father_Frame.setMinimumSize(QSize(230, 40))
        self.Father_Frame.setMaximumSize(QSize(230, 40))
        self.Father_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Father_Frame.setFrameShape(QFrame.StyledPanel)
        self.Father_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Father_Icon = QLabel(self.Father_Frame)
        self.Rabbit_Father_Icon.setObjectName(u"Rabbit_Father_Icon")
        self.Rabbit_Father_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Father_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Father_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Father_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Father_Icon.setPixmap(QPixmap(u":/Icons/Rabbit_Tree_White.png"))
        self.Rabbit_Father_Icon.setScaledContents(True)
        self.Rabbit_Father_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Father_Icon.setWordWrap(False)
        self.Rabbit_Father_Label = QLabel(self.Father_Frame)
        self.Rabbit_Father_Label.setObjectName(u"Rabbit_Father_Label")
        self.Rabbit_Father_Label.setGeometry(QRect(50, 9, 169, 21))
        self.Rabbit_Father_Label.setMinimumSize(QSize(169, 21))
        self.Rabbit_Father_Label.setMaximumSize(QSize(169, 21))
        self.Rabbit_Father_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Bunnies_Frame = QFrame(self.General_Info_Frame)
        self.Bunnies_Frame.setObjectName(u"Bunnies_Frame")
        self.Bunnies_Frame.setGeometry(QRect(20, 470, 230, 40))
        self.Bunnies_Frame.setMinimumSize(QSize(230, 40))
        self.Bunnies_Frame.setMaximumSize(QSize(230, 40))
        self.Bunnies_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Bunnies_Frame.setFrameShape(QFrame.StyledPanel)
        self.Bunnies_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Bunnies_Icon = QLabel(self.Bunnies_Frame)
        self.Rabbit_Bunnies_Icon.setObjectName(u"Rabbit_Bunnies_Icon")
        self.Rabbit_Bunnies_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Bunnies_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Bunnies_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Bunnies_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Bunnies_Icon.setPixmap(QPixmap(u":/Icons/Rabbits_White.png"))
        self.Rabbit_Bunnies_Icon.setScaledContents(True)
        self.Rabbit_Bunnies_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Bunnies_Icon.setWordWrap(False)
        self.Rabbit_Bunnies_Label = QLabel(self.Bunnies_Frame)
        self.Rabbit_Bunnies_Label.setObjectName(u"Rabbit_Bunnies_Label")
        self.Rabbit_Bunnies_Label.setGeometry(QRect(50, 9, 169, 21))
        self.Rabbit_Bunnies_Label.setMinimumSize(QSize(169, 21))
        self.Rabbit_Bunnies_Label.setMaximumSize(QSize(169, 21))
        self.Rabbit_Bunnies_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Facture_Frame = QFrame(self.General_Info_Frame)
        self.Facture_Frame.setObjectName(u"Facture_Frame")
        self.Facture_Frame.setGeometry(QRect(20, 620, 230, 40))
        self.Facture_Frame.setMinimumSize(QSize(230, 40))
        self.Facture_Frame.setMaximumSize(QSize(230, 40))
        self.Facture_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Facture_Frame.setFrameShape(QFrame.StyledPanel)
        self.Facture_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Facture_Icon = QLabel(self.Facture_Frame)
        self.Rabbit_Facture_Icon.setObjectName(u"Rabbit_Facture_Icon")
        self.Rabbit_Facture_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Facture_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Facture_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Facture_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Facture_Icon.setPixmap(QPixmap(u":/Icons/Facture_White.png"))
        self.Rabbit_Facture_Icon.setScaledContents(True)
        self.Rabbit_Facture_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Facture_Icon.setWordWrap(False)
        self.Rabbit_Facture_Label = QLabel(self.Facture_Frame)
        self.Rabbit_Facture_Label.setObjectName(u"Rabbit_Facture_Label")
        self.Rabbit_Facture_Label.setGeometry(QRect(50, 9, 169, 21))
        self.Rabbit_Facture_Label.setMinimumSize(QSize(169, 21))
        self.Rabbit_Facture_Label.setMaximumSize(QSize(169, 21))
        self.Rabbit_Facture_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Customer_Frame = QFrame(self.General_Info_Frame)
        self.Customer_Frame.setObjectName(u"Customer_Frame")
        self.Customer_Frame.setGeometry(QRect(20, 670, 230, 40))
        self.Customer_Frame.setMinimumSize(QSize(230, 40))
        self.Customer_Frame.setMaximumSize(QSize(230, 40))
        self.Customer_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Customer_Frame.setFrameShape(QFrame.StyledPanel)
        self.Customer_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Customer_Icon = QLabel(self.Customer_Frame)
        self.Rabbit_Customer_Icon.setObjectName(u"Rabbit_Customer_Icon")
        self.Rabbit_Customer_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Customer_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Customer_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Customer_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Customer_Icon.setPixmap(QPixmap(u":/Icons/Customer_Whitre.png"))
        self.Rabbit_Customer_Icon.setScaledContents(True)
        self.Rabbit_Customer_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Customer_Icon.setWordWrap(False)
        self.Rabbit_Customer_Label = QLabel(self.Customer_Frame)
        self.Rabbit_Customer_Label.setObjectName(u"Rabbit_Customer_Label")
        self.Rabbit_Customer_Label.setGeometry(QRect(50, 9, 169, 21))
        self.Rabbit_Customer_Label.setMinimumSize(QSize(169, 21))
        self.Rabbit_Customer_Label.setMaximumSize(QSize(169, 21))
        self.Rabbit_Customer_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Bought_Frame = QFrame(self.General_Info_Frame)
        self.Bought_Frame.setObjectName(u"Bought_Frame")
        self.Bought_Frame.setGeometry(QRect(20, 570, 230, 40))
        self.Bought_Frame.setMinimumSize(QSize(230, 40))
        self.Bought_Frame.setMaximumSize(QSize(230, 40))
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
        self.Rabbit_Bought_Icon = QLabel(self.Bought_Frame)
        self.Rabbit_Bought_Icon.setObjectName(u"Rabbit_Bought_Icon")
        self.Rabbit_Bought_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Bought_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Bought_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Bought_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Bought_Icon.setPixmap(QPixmap(u":/Icons/TND_White.png"))
        self.Rabbit_Bought_Icon.setScaledContents(True)
        self.Rabbit_Bought_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Bought_Icon.setWordWrap(False)
        self.Rabbit_Bought_Label = QLabel(self.Bought_Frame)
        self.Rabbit_Bought_Label.setObjectName(u"Rabbit_Bought_Label")
        self.Rabbit_Bought_Label.setGeometry(QRect(50, 9, 169, 21))
        self.Rabbit_Bought_Label.setMinimumSize(QSize(169, 21))
        self.Rabbit_Bought_Label.setMaximumSize(QSize(169, 21))
        self.Rabbit_Bought_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Sold_Frame = QFrame(self.General_Info_Frame)
        self.Sold_Frame.setObjectName(u"Sold_Frame")
        self.Sold_Frame.setGeometry(QRect(20, 720, 230, 40))
        self.Sold_Frame.setMinimumSize(QSize(230, 40))
        self.Sold_Frame.setMaximumSize(QSize(230, 40))
        self.Sold_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Sold_Frame.setFrameShape(QFrame.StyledPanel)
        self.Sold_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Sold_Icon = QLabel(self.Sold_Frame)
        self.Rabbit_Sold_Icon.setObjectName(u"Rabbit_Sold_Icon")
        self.Rabbit_Sold_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Sold_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Sold_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Sold_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Sold_Icon.setPixmap(QPixmap(u":/Icons/TND_White.png"))
        self.Rabbit_Sold_Icon.setScaledContents(True)
        self.Rabbit_Sold_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Sold_Icon.setWordWrap(False)
        self.Rabbit_Sold_Label = QLabel(self.Sold_Frame)
        self.Rabbit_Sold_Label.setObjectName(u"Rabbit_Sold_Label")
        self.Rabbit_Sold_Label.setGeometry(QRect(50, 9, 169, 21))
        self.Rabbit_Sold_Label.setMinimumSize(QSize(169, 21))
        self.Rabbit_Sold_Label.setMaximumSize(QSize(169, 21))
        self.Rabbit_Sold_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Age_Frame = QFrame(self.General_Info_Frame)
        self.Age_Frame.setObjectName(u"Age_Frame")
        self.Age_Frame.setGeometry(QRect(20, 120, 230, 40))
        self.Age_Frame.setMinimumSize(QSize(230, 40))
        self.Age_Frame.setMaximumSize(QSize(230, 40))
        self.Age_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Age_Frame.setFrameShape(QFrame.StyledPanel)
        self.Age_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Age_Icon = QLabel(self.Age_Frame)
        self.Rabbit_Age_Icon.setObjectName(u"Rabbit_Age_Icon")
        self.Rabbit_Age_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Age_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Age_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Age_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Age_Icon.setPixmap(QPixmap(u":/Icons/Calendar_White.png"))
        self.Rabbit_Age_Icon.setScaledContents(True)
        self.Rabbit_Age_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Age_Icon.setWordWrap(False)
        self.Rabbit_Age_Label = QLabel(self.Age_Frame)
        self.Rabbit_Age_Label.setObjectName(u"Rabbit_Age_Label")
        self.Rabbit_Age_Label.setGeometry(QRect(50, 9, 169, 21))
        self.Rabbit_Age_Label.setMinimumSize(QSize(169, 21))
        self.Rabbit_Age_Label.setMaximumSize(QSize(169, 21))
        self.Rabbit_Age_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Siblings_Frame = QFrame(self.General_Info_Frame)
        self.Siblings_Frame.setObjectName(u"Siblings_Frame")
        self.Siblings_Frame.setGeometry(QRect(20, 420, 230, 40))
        self.Siblings_Frame.setMinimumSize(QSize(230, 40))
        self.Siblings_Frame.setMaximumSize(QSize(230, 40))
        self.Siblings_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Siblings_Frame.setFrameShape(QFrame.StyledPanel)
        self.Siblings_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Siblings_Icon = QLabel(self.Siblings_Frame)
        self.Rabbit_Siblings_Icon.setObjectName(u"Rabbit_Siblings_Icon")
        self.Rabbit_Siblings_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Siblings_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Siblings_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Siblings_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Siblings_Icon.setPixmap(QPixmap(u":/Icons/Rabbits_White.png"))
        self.Rabbit_Siblings_Icon.setScaledContents(True)
        self.Rabbit_Siblings_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Siblings_Icon.setWordWrap(False)
        self.Rabbit_Siblings_Label = QLabel(self.Siblings_Frame)
        self.Rabbit_Siblings_Label.setObjectName(u"Rabbit_Siblings_Label")
        self.Rabbit_Siblings_Label.setGeometry(QRect(50, 9, 169, 21))
        self.Rabbit_Siblings_Label.setMinimumSize(QSize(169, 21))
        self.Rabbit_Siblings_Label.setMaximumSize(QSize(169, 21))
        self.Rabbit_Siblings_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Mother_Frame = QFrame(self.General_Info_Frame)
        self.Mother_Frame.setObjectName(u"Mother_Frame")
        self.Mother_Frame.setGeometry(QRect(20, 320, 230, 40))
        self.Mother_Frame.setMinimumSize(QSize(230, 40))
        self.Mother_Frame.setMaximumSize(QSize(230, 40))
        self.Mother_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Mother_Frame.setFrameShape(QFrame.StyledPanel)
        self.Mother_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Mother_Icon = QLabel(self.Mother_Frame)
        self.Rabbit_Mother_Icon.setObjectName(u"Rabbit_Mother_Icon")
        self.Rabbit_Mother_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Mother_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Mother_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Mother_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Mother_Icon.setPixmap(QPixmap(u":/Icons/Rabbit_Tree_White.png"))
        self.Rabbit_Mother_Icon.setScaledContents(True)
        self.Rabbit_Mother_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Mother_Icon.setWordWrap(False)
        self.Rabbit_Mother_Label = QLabel(self.Mother_Frame)
        self.Rabbit_Mother_Label.setObjectName(u"Rabbit_Mother_Label")
        self.Rabbit_Mother_Label.setGeometry(QRect(50, 9, 169, 21))
        self.Rabbit_Mother_Label.setMinimumSize(QSize(169, 21))
        self.Rabbit_Mother_Label.setMaximumSize(QSize(169, 21))
        self.Rabbit_Mother_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Gender_Frame = QFrame(self.General_Info_Frame)
        self.Gender_Frame.setObjectName(u"Gender_Frame")
        self.Gender_Frame.setGeometry(QRect(20, 220, 230, 40))
        self.Gender_Frame.setMinimumSize(QSize(230, 40))
        self.Gender_Frame.setMaximumSize(QSize(230, 40))
        self.Gender_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Gender_Frame.setFrameShape(QFrame.StyledPanel)
        self.Gender_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Gender_Icon = QLabel(self.Gender_Frame)
        self.Rabbit_Gender_Icon.setObjectName(u"Rabbit_Gender_Icon")
        self.Rabbit_Gender_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Gender_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Gender_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Gender_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Gender_Icon.setPixmap(QPixmap(u":/Icons/Gender_White.png"))
        self.Rabbit_Gender_Icon.setScaledContents(True)
        self.Rabbit_Gender_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Gender_Icon.setWordWrap(False)
        self.Rabbit_Gender_Label = QLabel(self.Gender_Frame)
        self.Rabbit_Gender_Label.setObjectName(u"Rabbit_Gender_Label")
        self.Rabbit_Gender_Label.setGeometry(QRect(50, 9, 169, 21))
        self.Rabbit_Gender_Label.setMinimumSize(QSize(169, 21))
        self.Rabbit_Gender_Label.setMaximumSize(QSize(169, 21))
        self.Rabbit_Gender_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Cage_Frame = QFrame(self.General_Info_Frame)
        self.Cage_Frame.setObjectName(u"Cage_Frame")
        self.Cage_Frame.setGeometry(QRect(20, 520, 230, 40))
        self.Cage_Frame.setMinimumSize(QSize(230, 40))
        self.Cage_Frame.setMaximumSize(QSize(230, 40))
        self.Cage_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Cage_Frame.setFrameShape(QFrame.StyledPanel)
        self.Cage_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Cage_Icon = QLabel(self.Cage_Frame)
        self.Rabbit_Cage_Icon.setObjectName(u"Rabbit_Cage_Icon")
        self.Rabbit_Cage_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Cage_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Cage_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Cage_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Cage_Icon.setPixmap(QPixmap(u":/Icons/Cages_White.png"))
        self.Rabbit_Cage_Icon.setScaledContents(True)
        self.Rabbit_Cage_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Cage_Icon.setWordWrap(False)
        self.Rabbit_Cage_Label = QLabel(self.Cage_Frame)
        self.Rabbit_Cage_Label.setObjectName(u"Rabbit_Cage_Label")
        self.Rabbit_Cage_Label.setGeometry(QRect(50, 9, 169, 21))
        self.Rabbit_Cage_Label.setMinimumSize(QSize(169, 21))
        self.Rabbit_Cage_Label.setMaximumSize(QSize(169, 21))
        self.Rabbit_Cage_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Generation_Frame = QFrame(self.General_Info_Frame)
        self.Generation_Frame.setObjectName(u"Generation_Frame")
        self.Generation_Frame.setGeometry(QRect(20, 370, 230, 40))
        self.Generation_Frame.setMinimumSize(QSize(230, 40))
        self.Generation_Frame.setMaximumSize(QSize(230, 40))
        self.Generation_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Generation_Frame.setFrameShape(QFrame.StyledPanel)
        self.Generation_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Generation_Icon = QLabel(self.Generation_Frame)
        self.Rabbit_Generation_Icon.setObjectName(u"Rabbit_Generation_Icon")
        self.Rabbit_Generation_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Generation_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Generation_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Generation_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Generation_Icon.setPixmap(QPixmap(u":/Icons/Rabbit_Tree_White.png"))
        self.Rabbit_Generation_Icon.setScaledContents(True)
        self.Rabbit_Generation_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Generation_Icon.setWordWrap(False)
        self.Rabbit_Generation_Label = QLabel(self.Generation_Frame)
        self.Rabbit_Generation_Label.setObjectName(u"Rabbit_Generation_Label")
        self.Rabbit_Generation_Label.setGeometry(QRect(50, 9, 169, 21))
        self.Rabbit_Generation_Label.setMinimumSize(QSize(169, 21))
        self.Rabbit_Generation_Label.setMaximumSize(QSize(169, 21))
        self.Rabbit_Generation_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.ID_Frame = QFrame(self.Background)
        self.ID_Frame.setObjectName(u"ID_Frame")
        self.ID_Frame.setEnabled(True)
        self.ID_Frame.setGeometry(QRect(30, 20, 158, 44))
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
        self.Notes_Frame = QFrame(self.Background)
        self.Notes_Frame.setObjectName(u"Notes_Frame")
        self.Notes_Frame.setGeometry(QRect(340, 690, 271, 141))
        self.Notes_Frame.setMinimumSize(QSize(271, 141))
        self.Notes_Frame.setMaximumSize(QSize(271, 141))
        self.Notes_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(143, 143, 143);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Notes_Frame.setFrameShape(QFrame.StyledPanel)
        self.Notes_Frame.setFrameShadow(QFrame.Raised)
        self.Notes_Label_Frame = QFrame(self.Notes_Frame)
        self.Notes_Label_Frame.setObjectName(u"Notes_Label_Frame")
        self.Notes_Label_Frame.setGeometry(QRect(3, 6, 41, 131))
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
        self.Rabbit_Notes_PleinText = QPlainTextEdit(self.Notes_Frame)
        self.Rabbit_Notes_PleinText.setObjectName(u"Rabbit_Notes_PleinText")
        self.Rabbit_Notes_PleinText.setGeometry(QRect(48, 6, 220, 131))
        self.Rabbit_Notes_PleinText.setMinimumSize(QSize(220, 131))
        self.Rabbit_Notes_PleinText.setMaximumSize(QSize(220, 131))
        self.Rabbit_Notes_PleinText.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.UpArrowCursor))
        self.Rabbit_Notes_PleinText.setStyleSheet(u"QPlainTextEdit{\n"
"	background-color: rgb(69, 69, 69);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Rabbit_Notes_PleinText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Notes_PleinText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Rabbit_Notes_PleinText.setReadOnly(True)
        self.Rabbit_Tree_Frame = QFrame(self.Background)
        self.Rabbit_Tree_Frame.setObjectName(u"Rabbit_Tree_Frame")
        self.Rabbit_Tree_Frame.setGeometry(QRect(650, 270, 351, 561))
        self.Rabbit_Tree_Frame.setMinimumSize(QSize(351, 561))
        self.Rabbit_Tree_Frame.setMaximumSize(QSize(351, 561))
        self.Rabbit_Tree_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Rabbit_Tree_Frame.setFrameShape(QFrame.StyledPanel)
        self.Rabbit_Tree_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Detail_Tree = QTreeWidget(self.Rabbit_Tree_Frame)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        self.Rabbit_Detail_Tree.setHeaderItem(__qtreewidgetitem)
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.NoBrush)
        brush1 = QBrush(QColor(0, 91, 44, 255))
        brush1.setStyle(Qt.SolidPattern)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.NoBrush)
        brush3 = QBrush(QColor(99, 92, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        __qtreewidgetitem1 = QTreeWidgetItem(self.Rabbit_Detail_Tree)
        __qtreewidgetitem1.setTextAlignment(0, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem1.setBackground(0, brush1);
        __qtreewidgetitem1.setForeground(0, brush);
        __qtreewidgetitem2 = QTreeWidgetItem(self.Rabbit_Detail_Tree)
        __qtreewidgetitem2.setBackground(0, brush3);
        __qtreewidgetitem2.setForeground(0, brush2);
        self.Rabbit_Detail_Tree.setObjectName(u"Rabbit_Detail_Tree")
        self.Rabbit_Detail_Tree.setGeometry(QRect(5, 10, 341, 541))
        self.Rabbit_Detail_Tree.setMinimumSize(QSize(341, 541))
        self.Rabbit_Detail_Tree.setMaximumSize(QSize(341, 541))
        self.Rabbit_Detail_Tree.setLayoutDirection(Qt.LeftToRight)
        self.Rabbit_Detail_Tree.setStyleSheet(u"QHeaderView::section{\n"
"	font: 75 10pt \"Orbitron\";\n"
"	font-weight:bold;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid #6c6c6c;\n"
"	border-color: rgb(108, 108, 108);\n"
"	border-top-color: rgb(108, 108, 108);\n"
"	border-right-color: rgb(108, 108, 108);\n"
"	border-bottom-color: rgb(108, 108, 108);\n"
"	border-left-color: rgb(108, 108, 108);\n"
"	border-radius:10px;\n"
"}\n"
"QHeaderView::section:checked{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"QTreeWidget{\n"
"	font: 75 10pt \"Segoe UI\";\n"
"	background-color: rgb(108, 108, 108);\n"
"	border:0px;\n"
"	text-align: center;\n"
"}\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"	border-image: url(:/Icons/Better_Tree/vline.png) 0;\n"
"}\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"	border-image: url(:/Icons/Better_Tree/branch-more.png);\n"
"}\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"	border-image: url(:/Icons/Better_Tree/branch-en"
                        "d.png);\n"
"}\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"	border-image: none;\n"
"	image: url(:/Icons/Better_Tree/branch-closed.png);\n"
"}\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"	border-image: none;\n"
"	image: url(:/Icons/Better_Tree/branch-open.png);\n"
"}")
        self.Rabbit_Detail_Tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Rabbit_Detail_Tree.setTabKeyNavigation(True)
        self.Rabbit_Detail_Tree.setProperty(u"showDropIndicator", True)
        self.Rabbit_Detail_Tree.setDragEnabled(False)
        self.Rabbit_Detail_Tree.setDragDropOverwriteMode(True)
        self.Rabbit_Detail_Tree.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.Rabbit_Detail_Tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.Rabbit_Detail_Tree.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.Rabbit_Detail_Tree.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.Rabbit_Detail_Tree.setRootIsDecorated(True)
        self.Rabbit_Detail_Tree.setUniformRowHeights(False)
        self.Rabbit_Detail_Tree.setItemsExpandable(True)
        self.Rabbit_Detail_Tree.setSortingEnabled(False)
        self.Rabbit_Detail_Tree.setAnimated(True)
        self.Rabbit_Detail_Tree.setHeaderHidden(False)
        self.Rabbit_Detail_Tree.header().setCascadingSectionResizes(False)
        self.Rabbit_Detail_Tree.header().setHighlightSections(False)
        self.Rabbit_Detail_Tree.header().setProperty(u"showSortIndicator", False)
        self.Photos_Infos_Frame = QFrame(self.Background)
        self.Photos_Infos_Frame.setObjectName(u"Photos_Infos_Frame")
        self.Photos_Infos_Frame.setGeometry(QRect(650, 79, 351, 181))
        self.Photos_Infos_Frame.setMinimumSize(QSize(351, 181))
        self.Photos_Infos_Frame.setMaximumSize(QSize(351, 181))
        self.Photos_Infos_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Photos_Infos_Frame.setFrameShape(QFrame.StyledPanel)
        self.Photos_Infos_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Avatar_Frame = QFrame(self.Photos_Infos_Frame)
        self.Rabbit_Avatar_Frame.setObjectName(u"Rabbit_Avatar_Frame")
        self.Rabbit_Avatar_Frame.setGeometry(QRect(220, 10, 119, 161))
        self.Rabbit_Avatar_Frame.setMinimumSize(QSize(119, 161))
        self.Rabbit_Avatar_Frame.setMaximumSize(QSize(119, 161))
        self.Rabbit_Avatar_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #D9D9D9;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Rabbit_Avatar_Frame.setFrameShape(QFrame.StyledPanel)
        self.Rabbit_Avatar_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Avatar_Label = QLabel(self.Rabbit_Avatar_Frame)
        self.Rabbit_Avatar_Label.setObjectName(u"Rabbit_Avatar_Label")
        self.Rabbit_Avatar_Label.setGeometry(QRect(9, 10, 101, 141))
        self.Rabbit_Avatar_Label.setStyleSheet(u"border:none;")
        self.Rabbit_Avatar_Label.setPixmap(QPixmap(u":/Icons/Rabbit_Green.png"))
        self.Rabbit_Avatar_Label.setScaledContents(False)
        self.Rabbit_Avatar_Label.setAlignment(Qt.AlignCenter)
        self.Type_Frame = QFrame(self.Photos_Infos_Frame)
        self.Type_Frame.setObjectName(u"Type_Frame")
        self.Type_Frame.setGeometry(QRect(10, 11, 200, 40))
        self.Type_Frame.setMinimumSize(QSize(200, 40))
        self.Type_Frame.setMaximumSize(QSize(200, 40))
        self.Type_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Type_Frame.setFrameShape(QFrame.StyledPanel)
        self.Type_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Type_Icon = QLabel(self.Type_Frame)
        self.Rabbit_Type_Icon.setObjectName(u"Rabbit_Type_Icon")
        self.Rabbit_Type_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Type_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Type_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Type_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Type_Icon.setPixmap(QPixmap(u":/Icons/Settings_White.png"))
        self.Rabbit_Type_Icon.setScaledContents(True)
        self.Rabbit_Type_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Type_Icon.setWordWrap(False)
        self.Rabbit_Type_Label = QLabel(self.Type_Frame)
        self.Rabbit_Type_Label.setObjectName(u"Rabbit_Type_Label")
        self.Rabbit_Type_Label.setGeometry(QRect(50, 9, 139, 21))
        self.Rabbit_Type_Label.setMinimumSize(QSize(139, 21))
        self.Rabbit_Type_Label.setMaximumSize(QSize(139, 21))
        self.Rabbit_Type_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Status_Frame = QFrame(self.Photos_Infos_Frame)
        self.Status_Frame.setObjectName(u"Status_Frame")
        self.Status_Frame.setGeometry(QRect(10, 71, 200, 40))
        self.Status_Frame.setMinimumSize(QSize(200, 40))
        self.Status_Frame.setMaximumSize(QSize(200, 40))
        self.Status_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: #5C5C5C;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 18pt \"Acme\";\n"
"	border: 2px solid #ffffff;\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"}")
        self.Status_Frame.setFrameShape(QFrame.StyledPanel)
        self.Status_Frame.setFrameShadow(QFrame.Raised)
        self.Rabbit_Status_Icon = QLabel(self.Status_Frame)
        self.Rabbit_Status_Icon.setObjectName(u"Rabbit_Status_Icon")
        self.Rabbit_Status_Icon.setGeometry(QRect(20, 8, 21, 21))
        self.Rabbit_Status_Icon.setMinimumSize(QSize(21, 21))
        self.Rabbit_Status_Icon.setMaximumSize(QSize(21, 21))
        self.Rabbit_Status_Icon.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Acme\";")
        self.Rabbit_Status_Icon.setPixmap(QPixmap(u":/Icons/Actions_White.png"))
        self.Rabbit_Status_Icon.setScaledContents(True)
        self.Rabbit_Status_Icon.setAlignment(Qt.AlignCenter)
        self.Rabbit_Status_Icon.setWordWrap(False)
        self.Rabbit_Status_Label = QLabel(self.Status_Frame)
        self.Rabbit_Status_Label.setObjectName(u"Rabbit_Status_Label")
        self.Rabbit_Status_Label.setGeometry(QRect(50, 9, 139, 21))
        self.Rabbit_Status_Label.setMinimumSize(QSize(139, 21))
        self.Rabbit_Status_Label.setMaximumSize(QSize(139, 21))
        self.Rabbit_Status_Label.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Acme\";")
        self.Gallery_Button = QPushButton(self.Photos_Infos_Frame)
        self.Gallery_Button.setObjectName(u"Gallery_Button")
        self.Gallery_Button.setEnabled(True)
        self.Gallery_Button.setGeometry(QRect(18, 133, 33, 33))
        self.Gallery_Button.setMinimumSize(QSize(33, 33))
        self.Gallery_Button.setMaximumSize(QSize(33, 33))
        self.Gallery_Button.setFont(font)
        self.Gallery_Button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.Gallery_Button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Gallery_White.png);\n"
"}\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Gallery_Mix.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: none;\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	image: url(:/Icons/Gallery_Green.png);\n"
"}")
        self.Gallery_Button.setIconSize(QSize(20, 20))
        self.Gallery_Button.setCheckable(False)
        self.Gallery_Button.setAutoRepeat(False)
        self.Gallery_Button.setAutoExclusive(False)
        self.Gallery_Button.setAutoRepeatDelay(50)
        self.Gallery_Button.setAutoRepeatInterval(10)
        self.Male_Info_Frame = QFrame(self.Background)
        self.Male_Info_Frame.setObjectName(u"Male_Info_Frame")
        self.Male_Info_Frame.setGeometry(QRect(310, 10, 331, 691))
        self.Male_Info_Frame.setMinimumSize(QSize(331, 691))
        self.Male_Info_Frame.setMaximumSize(QSize(331, 691))
        self.Male_Info_Frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(49, 49, 49);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    	border-radius: 20px;\n"
"	font: 75 10pt \"Acme\";\n"
"}")
        self.Male_Info_Frame.setFrameShape(QFrame.StyledPanel)
        self.Male_Info_Frame.setFrameShadow(QFrame.Raised)
        self.Breeding_Info_Frame.raise_()
        self.Activity_Frame.raise_()
        self.General_Info_Frame.raise_()
        self.ID_Frame.raise_()
        self.Rabbit_Tree_Frame.raise_()
        self.Photos_Infos_Frame.raise_()
        self.Male_Info_Frame.raise_()
        self.Notes_Frame.raise_()
        QWidget.setTabOrder(self.Exit_Customer_View, self.Edit_Rabbit)
        QWidget.setTabOrder(self.Edit_Rabbit, self.Delete_Rabbit)
        QWidget.setTabOrder(self.Delete_Rabbit, self.Rabbit_Notes_PleinText)
        QWidget.setTabOrder(self.Rabbit_Notes_PleinText, self.Rabbit_Detail_Tree)
        QWidget.setTabOrder(self.Rabbit_Detail_Tree, self.YearSelection_Rabbit)
        QWidget.setTabOrder(self.YearSelection_Rabbit, self.Rabbit_Detail_Table_10)
        QWidget.setTabOrder(self.Rabbit_Detail_Table_10, self.Rabbit_Detail_Table_11)
        QWidget.setTabOrder(self.Rabbit_Detail_Table_11, self.Rabbit_Detail_Table_2)
        QWidget.setTabOrder(self.Rabbit_Detail_Table_2, self.Rabbit_Detail_Table_8)
        QWidget.setTabOrder(self.Rabbit_Detail_Table_8, self.Rabbit_Detail_Table_6)
        QWidget.setTabOrder(self.Rabbit_Detail_Table_6, self.Rabbit_Detail_Table_7)
        QWidget.setTabOrder(self.Rabbit_Detail_Table_7, self.Rabbit_Detail_Table_9)
        QWidget.setTabOrder(self.Rabbit_Detail_Table_9, self.Rabbit_Detail_Table_4)
        QWidget.setTabOrder(self.Rabbit_Detail_Table_4, self.Rabbit_Detail_Table_3)
        QWidget.setTabOrder(self.Rabbit_Detail_Table_3, self.Rabbit_Detail_Table_1)
        QWidget.setTabOrder(self.Rabbit_Detail_Table_1, self.Rabbit_Detail_Table_5)
        QWidget.setTabOrder(self.Rabbit_Detail_Table_5, self.Rabbit_Detail_Table_12)

        self.retranslateUi(Rabbit_View_Main)
        self.Exit_Customer_View.clicked.connect(Rabbit_View_Main.close)

        QMetaObject.connectSlotsByName(Rabbit_View_Main)
    # setupUi

    def retranslateUi(self, Rabbit_View_Main):
        Rabbit_View_Main.setWindowTitle(QCoreApplication.translate("Rabbit_View_Main", u"Dialog", None))
        self.YearSelection_Rabbit.setItemText(0, QCoreApplication.translate("Rabbit_View_Main", u"2024", None))
        self.YearSelection_Rabbit.setItemText(1, QCoreApplication.translate("Rabbit_View_Main", u"2025", None))
        self.YearSelection_Rabbit.setItemText(2, QCoreApplication.translate("Rabbit_View_Main", u"2026", None))
        self.YearSelection_Rabbit.setItemText(3, QCoreApplication.translate("Rabbit_View_Main", u"2027", None))
        self.YearSelection_Rabbit.setItemText(4, QCoreApplication.translate("Rabbit_View_Main", u"2028", None))
        self.YearSelection_Rabbit.setItemText(5, QCoreApplication.translate("Rabbit_View_Main", u"2029", None))
        self.YearSelection_Rabbit.setItemText(6, QCoreApplication.translate("Rabbit_View_Main", u"2030", None))
        self.YearSelection_Rabbit.setItemText(7, QCoreApplication.translate("Rabbit_View_Main", u"2031", None))
        self.YearSelection_Rabbit.setItemText(8, QCoreApplication.translate("Rabbit_View_Main", u"2032", None))
        self.YearSelection_Rabbit.setItemText(9, QCoreApplication.translate("Rabbit_View_Main", u"2033", None))
        self.YearSelection_Rabbit.setItemText(10, QCoreApplication.translate("Rabbit_View_Main", u"2034", None))
        self.YearSelection_Rabbit.setItemText(11, QCoreApplication.translate("Rabbit_View_Main", u"2035", None))
        self.YearSelection_Rabbit.setItemText(12, QCoreApplication.translate("Rabbit_View_Main", u"2036", None))
        self.YearSelection_Rabbit.setItemText(13, QCoreApplication.translate("Rabbit_View_Main", u"2037", None))
        self.YearSelection_Rabbit.setItemText(14, QCoreApplication.translate("Rabbit_View_Main", u"2038", None))
        self.YearSelection_Rabbit.setItemText(15, QCoreApplication.translate("Rabbit_View_Main", u"2039", None))
        self.YearSelection_Rabbit.setItemText(16, QCoreApplication.translate("Rabbit_View_Main", u"2040", None))

        ___qtablewidgetitem = self.Rabbit_Detail_Table_10.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Rabbit_View_Main", u"October", None));
        ___qtablewidgetitem1 = self.Rabbit_Detail_Table_11.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Rabbit_View_Main", u"November", None));
        ___qtablewidgetitem2 = self.Rabbit_Detail_Table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Rabbit_View_Main", u"February", None));
        ___qtablewidgetitem3 = self.Rabbit_Detail_Table_8.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Rabbit_View_Main", u"August", None));
        ___qtablewidgetitem4 = self.Rabbit_Detail_Table_6.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Rabbit_View_Main", u"June", None));
        ___qtablewidgetitem5 = self.Rabbit_Detail_Table_7.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Rabbit_View_Main", u"July", None));
        ___qtablewidgetitem6 = self.Rabbit_Detail_Table_9.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Rabbit_View_Main", u"September", None));
        ___qtablewidgetitem7 = self.Rabbit_Detail_Table_4.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Rabbit_View_Main", u"April", None));
        ___qtablewidgetitem8 = self.Rabbit_Detail_Table_3.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Rabbit_View_Main", u"March", None));
        ___qtablewidgetitem9 = self.Rabbit_Detail_Table_1.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Rabbit_View_Main", u" January", None));
        ___qtablewidgetitem10 = self.Rabbit_Detail_Table_5.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Rabbit_View_Main", u"May", None));
        ___qtablewidgetitem11 = self.Rabbit_Detail_Table_12.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Rabbit_View_Main", u"December", None));
        self.Rabbit_Total_Bunnies_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Total", None))
        self.Exit_Customer_View.setText("")
#if QT_CONFIG(shortcut)
        self.Exit_Customer_View.setShortcut(QCoreApplication.translate("Rabbit_View_Main", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.Edit_Rabbit.setText("")
        self.Delete_Rabbit.setText("")
#if QT_CONFIG(shortcut)
        self.Delete_Rabbit.setShortcut(QCoreApplication.translate("Rabbit_View_Main", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.Rabbit_Breed_Icon.setText("")
        self.Rabbit_Breed_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Breed", None))
        self.Rabbit_Born_Icon.setText("")
        self.Rabbit_Born_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Born", None))
        self.Rabbit_Color_Icon.setText("")
        self.Rabbit_Color_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Color", None))
        self.Rabbit_Father_Icon.setText("")
        self.Rabbit_Father_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Father", None))
        self.Rabbit_Bunnies_Icon.setText("")
        self.Rabbit_Bunnies_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Bunnies", None))
        self.Rabbit_Facture_Icon.setText("")
        self.Rabbit_Facture_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Facture", None))
        self.Rabbit_Customer_Icon.setText("")
        self.Rabbit_Customer_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Customer", None))
        self.Rabbit_Bought_Icon.setText("")
        self.Rabbit_Bought_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Bought", None))
        self.Rabbit_Sold_Icon.setText("")
        self.Rabbit_Sold_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Sold", None))
        self.Rabbit_Age_Icon.setText("")
        self.Rabbit_Age_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Age", None))
        self.Rabbit_Siblings_Icon.setText("")
        self.Rabbit_Siblings_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Siblings", None))
        self.Rabbit_Mother_Icon.setText("")
        self.Rabbit_Mother_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Mother", None))
        self.Rabbit_Gender_Icon.setText("")
        self.Rabbit_Gender_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Gender", None))
        self.Rabbit_Cage_Icon.setText("")
        self.Rabbit_Cage_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Cage", None))
        self.Rabbit_Generation_Icon.setText("")
        self.Rabbit_Generation_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Generation", None))
        self.ID_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"ID : ", None))
        self.Notes_Text_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">N</span></p></body></html>", None))
        self.Notes_Text_Label_2.setText(QCoreApplication.translate("Rabbit_View_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">O</span></p></body></html>", None))
        self.Notes_Text_Label_3.setText(QCoreApplication.translate("Rabbit_View_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">T</span></p></body></html>", None))
        self.Notes_Text_Label_4.setText(QCoreApplication.translate("Rabbit_View_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">E</span></p></body></html>", None))
        self.Notes_Text_Label_5.setText(QCoreApplication.translate("Rabbit_View_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Acme'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">S</span></p></body></html>", None))
        ___qtreewidgetitem = self.Rabbit_Detail_Tree.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("Rabbit_View_Main", u"Father", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Rabbit_View_Main", u"Mother", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Rabbit_View_Main", u"Born", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Rabbit_View_Main", u"ID", None));

        __sortingEnabled = self.Rabbit_Detail_Tree.isSortingEnabled()
        self.Rabbit_Detail_Tree.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.Rabbit_Detail_Tree.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Rabbit_View_Main", u"Siblings", None));
        ___qtreewidgetitem2 = self.Rabbit_Detail_Tree.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Rabbit_View_Main", u"Bunnies", None));
        self.Rabbit_Detail_Tree.setSortingEnabled(__sortingEnabled)

        self.Rabbit_Avatar_Label.setText("")
        self.Rabbit_Type_Icon.setText("")
        self.Rabbit_Type_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Type", None))
        self.Rabbit_Status_Icon.setText("")
        self.Rabbit_Status_Label.setText(QCoreApplication.translate("Rabbit_View_Main", u"Status : ", None))
        self.Gallery_Button.setText("")
    # retranslateUi

