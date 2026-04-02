#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Importations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

#All PySide6 Importation :
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow,QFrame,QLabel, QWidget,QTableWidgetItem,QHBoxLayout,QVBoxLayout,QPlainTextEdit,QPushButton,QFileDialog,QMessageBox,QGraphicsBlurEffect
from PySide6.QtGui import QIcon,QColor,QPixmap

#Other Importation Of Packages :
import sqlite3
from pathlib import Path
import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate,Table,TableStyle
from reportlab.lib import colors
from datetime import datetime

#Importation Of Interfaces :
from InterfacesPY import Ui_MainWindow

#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Creating A DataBase With All The Columns ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

def checkRabbitsTable():
    """
    Ensures the "rabbits" table exists in the "ElevageInfos.db" database.
    If the table does not exist, it creates it with the specified schema.
    """
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()
        
        create_table_query = "CREATE TABLE IF NOT EXISTS rabbits (ID INTEGER NOT NULL UNIQUE, Breed TEXT, Born TEXT, Gender TEXT DEFAULT 'Null', Color TEXT, Mother INTEGER, Father INTEGER, Generation INTEGER DEFAULT 0, Type TEXT DEFAULT 'None', CageID INTEGER, FactureID INTEGER, CustomerID INTEGER, Bought REAL DEFAULT 0, Sold REAL DEFAULT 0, Notes TEXT, PRIMARY KEY(ID));"
        
        cursor.execute(create_table_query)
        connection.commit()

def checkFacturesTable():
    """
    Ensures the "factures" table exists in the "ElevageInfos.db" database.
    If the table does not exist, it creates it with the specified schema.
    """
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()
        
        create_table_query = "CREATE TABLE IF NOT EXISTS factures (ID INTEGER NOT NULL UNIQUE, Date TEXT, CustomerID INTEGER, Total REAL DEFAULT 0, PRIMARY KEY(ID));"
        
        cursor.execute(create_table_query)
        connection.commit()

def checkExpensesTable():
    """
    Ensures the "expenses" table exists in the "ElevageInfos.db" database.
    If the table does not exist, it creates it with the specified schema.
    """
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()

        create_table_query = "CREATE TABLE IF NOT EXISTS expenses (ID INTEGER UNIQUE, Name TEXT, Total REAL, Notes TEXT, PRIMARY KEY(ID));"
        
        cursor.execute(create_table_query)
        connection.commit()

def checkCustomersTable():
    """
    Ensures the "customers" table exists in the "ElevageInfos.db" database.
    If the table does not exist, it creates it with the specified schema.
    """
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()
        
        create_table_query = "CREATE TABLE IF NOT EXISTS customers (ID INTEGER NOT NULL UNIQUE, Name TEXT, Phone TEXT, Address TEXT, Gender TEXT, Notes TEXT, PRIMARY KEY(ID));"
        
        cursor.execute(create_table_query)
        connection.commit()

def checkCagesTable():
    """
    Ensures the "cages" table exists in the "ElevageInfos.db" database.
    If the table does not exist, it creates it with the specified schema.
    """
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()

        create_table_query = "CREATE TABLE IF NOT EXISTS cages (ID INTEGER NOT NULL UNIQUE, Gender TEXT, Bought REAL DEFAULT 0, FactureID INTEGER, CustomerID INTEGER, Sold REAL DEFAULT 0, Notes TEXT, PRIMARY KEY(ID));"
        
        cursor.execute(create_table_query)
        connection.commit()


checkRabbitsTable()
checkExpensesTable()
checkCagesTable()
checkCustomersTable()
checkFacturesTable()


#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Get Specifique informations From Data Bases ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

def getDBData(Importation,DBName,genderFilter,FilterBy,Search,OrdreButtonChecked):
    DECR = "ORDER BY ID DESC"
    CR = "ORDER BY ID ASC"
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()
        if(DBName == "customers" or DBName == "rabbits" or DBName =="cages"):
            query = f"SELECT {Importation} FROM {DBName} WHERE ('{genderFilter}' = 'Gender' OR Gender = '{genderFilter}')"
            if(FilterBy != 'By'):
                query = f"SELECT {Importation} FROM {DBName} WHERE ('{genderFilter}' = 'Gender' OR Gender = '{genderFilter}') AND ({FilterBy} LIKE '%{Search}%')"
        if(DBName =="factures" or DBName =="expenses"):
            query = f"SELECT {Importation} FROM {DBName} "
            if(FilterBy != 'By'):
                query = f"SELECT {Importation} FROM {DBName} WHERE ({FilterBy} LIKE '%{Search}%')"
        if(OrdreButtonChecked):
            query += CR
        else :
            query += DECR

        cursor.execute(query)
        Data = cursor.fetchall()
    return Data


def DeleteDBData(DBName,FilterBy,Search):
    with sqlite3.connect("ElevageInfos.db") as connection:
        connection.execute("PRAGMA journal_mode=WAL;")
        connection.cursor().execute(f"DELETE FROM {DBName} WHERE {FilterBy} = ?", (Search,))
        connection.commit()


def Find_Image_SelectedView(SelectedPath,ID):
    appdata_path = os.getenv("APPDATA")
    if appdata_path is None:
        raise EnvironmentError("APPDATA environment variable is not set.")
    AvatarsFolder = Path(appdata_path) / "Rabbits_Manager" / SelectedPath
    AvatarsFolder.mkdir(parents=True, exist_ok=True)
    AvatarFile = ([f for f in os.listdir(AvatarsFolder) if f.startswith(f"{ID}.")])
    if(len(AvatarFile) == 0):
        AvatarFile=f"{AvatarsFolder}/Default.png"
    else :
        AvatarFile = AvatarFile[0]
    AvatarFile = os.path.join(AvatarsFolder,AvatarFile)
        
    return AvatarFile

def SearchFilter(FilterBy,SearchBar,Txt):
    Current_FilterBy = FilterBy.currentText()
    SearchBar.setReadOnly(True)
    SearchBar.setPlaceholderText("Pick Option From The Button [ By ]")
    SearchBar.setText("")
    if(Current_FilterBy != "By"):
        SearchBar.setReadOnly(False)
        SearchBar.setPlaceholderText(f"Search {Txt}...")
#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Image Frame Class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

class ImageFrame(QFrame):
    def __init__(self,Image_View,idString,Data,mainWindow,CurrentWindow,NewWindow, parent=None):
        super().__init__(parent)
        self.ID = Data[0]
        self.Image_View = Image_View
        self.mainWindow = mainWindow
        self.NewWindow = NewWindow
        self.CurrentWindow = CurrentWindow
        self.setFrameShape(QFrame.StyledPanel)
        self.setStyleSheet("border-radius: 10px; background-color: #444;")
        # Layout for the image frame
        VerticalConteiner = QVBoxLayout()
        VerticalConteiner.setContentsMargins(5, 5, 5, 5)
        VerticalConteiner.setSpacing(2)
        self.setFixedSize(118, 161)

        # Add the image button
        pixmap = QPixmap(Image_View).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        AvatarButton = QPushButton()
        AvatarButton.setStyleSheet("QPushButton:hover {border: 3px solid rgb(98, 114, 90);}")
        AvatarButton.setIcon(pixmap)
        AvatarButton.setIconSize(pixmap.size())
        AvatarButton.setFlat(True)
        AvatarButton.clicked.connect(lambda:self.open_DetailWindow_WithBlur(self.NewWindow))

        # Add the label below the image
        ID_TXT_Label = QLabel(idString)
        ID_TXT_Label.setAlignment(Qt.AlignCenter)

        Name_TXT_Label = QLabel(f"[ {Data[1]} ]")
        Name_TXT_Label.setAlignment(Qt.AlignCenter)

        Gender =""
        match self.NewWindow:
            case "Rabbits": Gender = Data[2]
            case "Customers": Gender = Data[4]
            case "Cages":Gender = Data[2]

        Color = {"Male": (0, 140, 179), "Female": (199, 0, 217),"Null": (182, 155, 0),"Kids": (182, 155, 0)}.get(Gender, (0, 104, 104))

        ID_TXT_Label.setStyleSheet(f'color: rgb(255, 255, 255);font: 75 15pt "Acme";background-color:rgb{Color};')
        Name_TXT_Label.setStyleSheet(f'color: rgb(255, 255, 255);font: 75 8pt "Acme";background-color:rgb{Color};')
        

        VerticalConteiner.addWidget(AvatarButton)
        VerticalConteiner.addWidget(ID_TXT_Label)
        VerticalConteiner.addWidget(Name_TXT_Label)
        self.setLayout(VerticalConteiner)

    def open_DetailWindow_WithBlur(self,WindowName):
        mainWindow_Geometry = self.mainWindow.geometry()
        if(WindowName == "Customers"):
            blurEffect = QGraphicsBlurEffect()
            blurEffect.setBlurRadius(10)
            self.mainWindow.Window.setGraphicsEffect(blurEffect)

            from Index_MainCustomerView import mainCustomer

            with sqlite3.connect("ElevageInfos.db") as connection:
                cursor = connection.cursor()
                query = f"SELECT ID,Name,Phone,Address,Gender,Notes FROM customers WHERE ID = '{self.ID}'"
                cursor.execute(query)
                Data = cursor.fetchall()[0]
        
            mainCustomerWindow = mainCustomer(self.Image_View,Data,self.mainWindow)
            Right = mainWindow_Geometry.x() + 241
            Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainCustomerWindow.height()) // 2 )
            mainCustomerWindow.move(Right, Centre)
            mainCustomerWindow.exec()
            self.mainWindow.Window.setGraphicsEffect(None)

        elif(WindowName == "Factures/PNG" and self.CurrentWindow == "AlreadyCurrent"):
            from Index_MainFactureView import mainFacture

            with sqlite3.connect("ElevageInfos.db") as connection:
                cursor = connection.cursor()
                query = f"SELECT CustomerID FROM factures WHERE ID = '{self.ID}'"
                cursor.execute(query)
                Data = cursor.fetchall()[0]
            with sqlite3.connect("ElevageInfos.db") as connection:
                cursor = connection.cursor()
                query = f"SELECT ID,Name,Phone,Address,Gender FROM customers WHERE ID = '{Data[0]}'"
                cursor.execute(query)
                Data = cursor.fetchall()[0]
                
            blurEffect = QGraphicsBlurEffect()
            blurEffect.setBlurRadius(10)
            self.mainWindow.Window.setGraphicsEffect(blurEffect)
            mainFactureWindow = mainFacture(self.ID,self.Image_View,Data,self.CurrentWindow,self.mainWindow)
            Right = mainWindow_Geometry.x() + 241
            Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainFactureWindow.height()) // 2 )
            mainFactureWindow.move(Right, Centre)
            mainFactureWindow.exec()
            self.mainWindow.Window.setGraphicsEffect(None)
        elif(WindowName == "Factures/PNG" and self.CurrentWindow != "AlreadyCurrent"):
            from Index_MainFactureView import mainFacture

            with sqlite3.connect("ElevageInfos.db") as connection:
                cursor = connection.cursor()
                query = f"SELECT CustomerID FROM factures WHERE ID = '{self.ID}'"
                cursor.execute(query)
                Data = cursor.fetchall()[0]
            with sqlite3.connect("ElevageInfos.db") as connection:
                cursor = connection.cursor()
                query = f"SELECT ID,Name,Phone,Address,Gender FROM customers WHERE ID = '{Data[0]}'"
                cursor.execute(query)
                Data = cursor.fetchall()[0]

            mainFactureWindow = mainFacture(self.ID,self.Image_View,Data,self.CurrentWindow,self.mainWindow)
            Right = mainWindow_Geometry.x() + 241
            Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainFactureWindow.height()) // 2 )
            mainFactureWindow.move(Right, Centre)
            mainFactureWindow.exec()
        elif(WindowName == "Rabbits" and self.CurrentWindow == "AlreadyCurrent"):
            blurEffect = QGraphicsBlurEffect()
            blurEffect.setBlurRadius(10)
            self.mainWindow.Window.setGraphicsEffect(blurEffect)
            from Index_MainRabbitView import mainRabbitView
            
            with sqlite3.connect("ElevageInfos.db") as connection:
                cursor = connection.cursor()
                query = f"SELECT ID,Breed,Born,Color,Gender,Father,Mother,Generation,CageID,Type,Bought,FactureID,CustomerID,Sold,Notes FROM rabbits WHERE ID = '{self.ID}'"
                cursor.execute(query)
                Data = cursor.fetchall()[0]

            mainRabbitWindow = mainRabbitView(self.Image_View,Data,self.mainWindow)
            Right = mainWindow_Geometry.x() + 241
            Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainRabbitWindow.height()) // 2 )
            mainRabbitWindow.move(Right, Centre)
            mainRabbitWindow.exec()
            self.mainWindow.Window.setGraphicsEffect(None)
        elif(WindowName == "Rabbits" and self.CurrentWindow != "AlreadyCurrent"):
            from Index_MainRabbitView import mainRabbitView

            with sqlite3.connect("ElevageInfos.db") as connection:
                cursor = connection.cursor()
                query = f"SELECT ID,Breed,Born,Color,Gender,Father,Mother,Generation,CageID,Type,Bought,FactureID,CustomerID,Sold,Notes FROM rabbits WHERE ID = '{self.ID}'"
                cursor.execute(query)
                Data = cursor.fetchall()[0]
            
            mainRabbitWindow = mainRabbitView(self.Image_View,Data,self.mainWindow)
            Right = mainWindow_Geometry.x() + 241
            Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainRabbitWindow.height()) // 2 )
            mainRabbitWindow.move(Right, Centre)
            mainRabbitWindow.exec()

        elif(WindowName == "Cages" and self.CurrentWindow == "AlreadyCurrent"):
            blurEffect = QGraphicsBlurEffect()
            blurEffect.setBlurRadius(10)
            self.mainWindow.Window.setGraphicsEffect(blurEffect)
            from Index_MainCageView import mainCage

            mainRabbitWindow = mainCage(self.Image_View,self.ID,self.mainWindow)
            Right = mainWindow_Geometry.x() + 241
            Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainRabbitWindow.height()) // 2 )
            mainRabbitWindow.move(Right, Centre)
            mainRabbitWindow.exec()
            self.mainWindow.Window.setGraphicsEffect(None)
        elif(WindowName == "Cages" and self.CurrentWindow != "AlreadyCurrent"):
            from Index_MainCageView import mainCage
            
            mainRabbitWindow = mainCage(self.Image_View,self.ID,self.mainWindow)
            Right = mainWindow_Geometry.x() + 241
            Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainRabbitWindow.height()) // 2 )
            mainRabbitWindow.move(Right, Centre)
            mainRabbitWindow.exec()
    
#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main Window Class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

class mainWindow(QMainWindow,Ui_MainWindow):
    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Switch Page ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def Switch_Page(self,Number):
        self.Menu_Pages.setCurrentIndex(Number) #Page Number
        #UnCheck All The Buttons
        self.Dashboard_Button.setChecked(False) 
        self.Customers_Button.setChecked(False)
        self.Rabbits_Button.setChecked(False)
        self.Cages_Button.setChecked(False)
        self.Factures_Button.setChecked(False)
        self.Expenses_Button.setChecked(False)
        self.Settings_Button.setChecked(False)
        self.Logout_Button.setChecked(False)
        #Check The Selected Button
        match Number:
            case 0:self.Dashboard_Button.setChecked(True)
            case 1:self.Customers_Button.setChecked(True)
            case 2:self.Rabbits_Button.setChecked(True)
            case 3:self.Cages_Button.setChecked(True)
            case 4:self.Factures_Button.setChecked(True)
            case 5:self.Expenses_Button.setChecked(True)
            case 6:self.Settings_Button.setChecked(True)
            case 7:self.Logout_Button.setChecked(True)

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Clear Images ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def clear_images(self,Current):
        if(Current == "Customers"):
            while self.GridLayout_Customers_View.count():
                child = self.GridLayout_Customers_View.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        if(Current == "Rabbits"):
            while self.GridLayout_Rabbits_View.count():
                child = self.GridLayout_Rabbits_View.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
        
        if(Current == "Cages"):
            while self.GridLayout_Cages_View.count():
                child = self.GridLayout_Cages_View.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
        
        if(Current == "Factures/PNG"):
            while self.GridLayout_Facture_View.count():
                child = self.GridLayout_Facture_View.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Images Grid ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def ImagesGrid(self,Data,SelectedPath):
        if(SelectedPath == "Customers"):
            self.clear_images(SelectedPath)
            self.Scroll_Customers_Area_View.setWidgetResizable(True)
            self.SrollWidget_Customers_View.setLayout(self.GridLayout_Customers_View)
            self.Scroll_Customers_Area_View.setWidget(self.SrollWidget_Customers_View)
            self.GridLayout_Customers_View.setAlignment(Qt.AlignTop | Qt.AlignCenter)
            self.GridLayout_Customers_View.setSpacing(33)

        elif(SelectedPath == "Rabbits"):
            self.clear_images(SelectedPath)
            self.Scroll_Rabbits_Area_View.setWidgetResizable(True)
            self.SrollWidget_Rabbits_View.setLayout(self.GridLayout_Rabbits_View)
            self.Scroll_Rabbits_Area_View.setWidget(self.SrollWidget_Rabbits_View)
            self.GridLayout_Rabbits_View.setAlignment(Qt.AlignTop | Qt.AlignCenter)
            self.GridLayout_Rabbits_View.setSpacing(33)

        elif(SelectedPath == "Cages"):
            self.clear_images(SelectedPath)
            self.Scroll_Cages_Area_View.setWidgetResizable(True)
            self.SrollWidget_Cages_View.setLayout(self.GridLayout_Cages_View)
            self.Scroll_Cages_Area_View.setWidget(self.SrollWidget_Cages_View)
            self.GridLayout_Cages_View.setAlignment(Qt.AlignTop | Qt.AlignCenter)
            self.GridLayout_Cages_View.setSpacing(33)

        elif(SelectedPath == "Factures/PNG"):
            self.clear_images(SelectedPath)
            self.Scroll_Facture_Area_View.setWidgetResizable(True)
            self.SrollWidget_Facture_View.setLayout(self.GridLayout_Facture_View)
            self.Scroll_Facture_Area_View.setWidget(self.SrollWidget_Facture_View)
            self.GridLayout_Facture_View.setAlignment(Qt.AlignTop | Qt.AlignCenter)
            self.GridLayout_Facture_View.setSpacing(33)

        for index,Informations in enumerate(Data):
            row = index // 6
            col = index % 6
            ID = Informations[0]
            image_frame = ImageFrame(Find_Image_SelectedView(SelectedPath,ID), f"#{ID}",Informations,self,"AlreadyCurrent",SelectedPath)
            
            if(SelectedPath == "Customers"):
                self.GridLayout_Customers_View.addWidget(image_frame, row, col)
            elif(SelectedPath == "Rabbits"):
                self.GridLayout_Rabbits_View.addWidget(image_frame, row, col)
            elif(SelectedPath == "Cages"):
                self.GridLayout_Cages_View.addWidget(image_frame, row, col)
            elif(SelectedPath == "Factures/PNG"):
                self.GridLayout_Facture_View.addWidget(image_frame, row, col)


    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Data Base Importer ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    def openAddCustomerWindow(self):
        from Index_MainAddEditCustomer import mainAddCustomer
        mainWindow_Geometry = self.geometry()
        blurEffect = QGraphicsBlurEffect()
        blurEffect.setBlurRadius(10)
        self.Window.setGraphicsEffect(blurEffect)
        mainAddCustomerWindow = mainAddCustomer(self)
        Right = mainWindow_Geometry.x() + 241 + 265
        Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainAddCustomerWindow.height()) // 2 ) - 10
        mainAddCustomerWindow.move(Right, Centre)
        mainAddCustomerWindow.exec()
        self.Window.setGraphicsEffect(None)

    def openRabbitsTreeWindow(self):
        from Index_MainViewRabbitTree import mainRabbitTree
        mainWindow_Geometry = self.geometry()
        blurEffect = QGraphicsBlurEffect()
        blurEffect.setBlurRadius(10)
        self.Window.setGraphicsEffect(blurEffect)
        mainRabbitTreeWindow = mainRabbitTree(self)
        Right = mainWindow_Geometry.x() + 241 + 15
        Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainRabbitTreeWindow.height()) // 2 )
        mainRabbitTreeWindow.move(Right, Centre)
        mainRabbitTreeWindow.exec()
        self.Window.setGraphicsEffect(None)

    def openAddRabbitsWindow(self):
        from Index_MainAddEditRabbit import mainAddRabbit
        mainWindow_Geometry = self.geometry()
        blurEffect = QGraphicsBlurEffect()
        blurEffect.setBlurRadius(10)
        self.Window.setGraphicsEffect(blurEffect)
        mainAddCustomerWindow = mainAddRabbit(self)
        Right = mainWindow_Geometry.x() + 241 + 265
        Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainAddCustomerWindow.height()) // 2 ) - 10
        mainAddCustomerWindow.move(Right, Centre)
        mainAddCustomerWindow.exec()
        self.Window.setGraphicsEffect(None)

    def openAddCagesWindow(self):
        from Index_MainAddEditCages import mainAddCage
        mainWindow_Geometry = self.geometry()
        blurEffect = QGraphicsBlurEffect()
        blurEffect.setBlurRadius(10)
        self.Window.setGraphicsEffect(blurEffect)
        mainAddCustomerWindow = mainAddCage(self)
        Right = mainWindow_Geometry.x() + 241 + 265
        Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainAddCustomerWindow.height()) // 2 ) - 10
        mainAddCustomerWindow.move(Right, Centre)
        mainAddCustomerWindow.exec()
        self.Window.setGraphicsEffect(None)

    def openCagesTreeWindow(self):
        from Index_MainViewCageTree import mainCageTree
        mainWindow_Geometry = self.geometry()
        blurEffect = QGraphicsBlurEffect()
        blurEffect.setBlurRadius(10)
        self.Window.setGraphicsEffect(blurEffect)
        mainRabbitTreeWindow = mainCageTree(self)
        Right = mainWindow_Geometry.x() + 241 + 15
        Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainRabbitTreeWindow.height()) // 2 )
        mainRabbitTreeWindow.move(Right, Centre)
        mainRabbitTreeWindow.exec()
        self.Window.setGraphicsEffect(None)

    def openAddExpensesWindow(self):
        from Index_MainAddEditExpense import mainAddExpense
        mainWindow_Geometry = self.geometry()
        blurEffect = QGraphicsBlurEffect()
        blurEffect.setBlurRadius(10)
        self.Window.setGraphicsEffect(blurEffect)
        mainRabbitTreeWindow = mainAddExpense(self)
        Right = mainWindow_Geometry.x() + 241 + 265
        Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainRabbitTreeWindow.height()) // 2 )
        mainRabbitTreeWindow.move(Right, Centre)
        mainRabbitTreeWindow.exec()
        self.Window.setGraphicsEffect(None)

    def openAddFactureWindow(self):
        from Index_MainAddFacture import mainAddFacture
        mainWindow_Geometry = self.geometry()
        blurEffect = QGraphicsBlurEffect()
        blurEffect.setBlurRadius(10)
        self.Window.setGraphicsEffect(blurEffect)
        mainRabbitTreeWindow = mainAddFacture(self)
        Right = mainWindow_Geometry.x() + 241
        Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainRabbitTreeWindow.height()) // 2 )
        mainRabbitTreeWindow.move(Right, Centre)
        mainRabbitTreeWindow.exec()
        self.Window.setGraphicsEffect(None)

    def LoadDashboard(self):
        with sqlite3.connect("ElevageInfos.db") as connection:
            cursor = connection.cursor()
            
            queries = {
                "TotalExpenses": "SELECT SUM(Total) FROM expenses",
                "TotalSells": "SELECT SUM(Total) FROM factures",
                "TotalRabbits": "SELECT COUNT(ID) FROM rabbits WHERE CustomerID IS NULL",
                "TotalCustomers": "SELECT COUNT(ID) FROM customers",
                "TotalCages": "SELECT COUNT(ID) FROM cages WHERE CustomerID IS NULL",
                "MaleRabbits": "SELECT COUNT(ID) FROM rabbits WHERE Gender = 'Male' AND CustomerID IS NULL",
                "FemaleRabbits": "SELECT COUNT(ID) FROM rabbits WHERE Gender = 'Female' AND CustomerID IS NULL",
                "NullGenderRabbits": "SELECT COUNT(ID) FROM rabbits WHERE Gender = 'Null' AND CustomerID IS NULL",
                "AllRabbits": "SELECT COUNT(ID) FROM rabbits",
                "MaleCages": "SELECT COUNT(ID) FROM cages WHERE Gender = 'Male' AND CustomerID IS NULL",
                "FemaleCages": "SELECT COUNT(ID) FROM cages WHERE Gender = 'Female' AND CustomerID IS NULL",
                "NullGenderCages": "SELECT COUNT(ID) FROM cages WHERE Gender = 'Null' AND CustomerID IS NULL",
                "AllCages": "SELECT COUNT(ID) FROM cages",
                "AvailableRabbits": "SELECT COUNT(ID) FROM rabbits WHERE CustomerID IS NULL",
                "SoldRabbits": "SELECT COUNT(ID) FROM rabbits WHERE FactureID IS NOT NULL",
                "OwnedRabbits": "SELECT COUNT(ID) FROM rabbits WHERE CustomerID = 0",
                "LostRabbits": "SELECT COUNT(ID) FROM rabbits WHERE CustomerID = -1"
            }
            
            results = {key: cursor.execute(query).fetchone()[0] or 0 for key, query in queries.items()}
            
            # Income and Expenses
            self.Income_Inter.setText(str(round(results["TotalSells"], 3)))
            self.Expenses_Inter.setText(str(round(results["TotalExpenses"], 3)))
            
            # Gain Calculation
            Gain = round(results["TotalSells"] - results["TotalExpenses"], 3)
            color = (137, 255, 141) if Gain > 0 else (255, 137, 137) if Gain < 0 else (251, 255, 146)
            self.Earning_Inter.setStyleSheet(f"border:none;background-color: rgba(0, 0, 0, 0);color:rgb{color};font: 75 15pt 'Acme';")
            self.Earning_Inter.setText(str(abs(Gain)))
            self.Earning_Text.setStyleSheet(f"border:none;background-color: rgba(0, 0, 0, 0);color:rgb{color};font: 75 25pt 'Acme';")
            
            # Updating UI Elements
            mappings = {
                "TotalRabbits": {"Count":self.Rabbits_Inter,"Text":self.Rabbits_Text,"Color":(137, 255, 141)},
                "TotalCustomers": {"Count":self.Customers_Inter,"Text":self.Customers_Text,"Color":(137, 255, 141)},
                "TotalCages": {"Count":self.Cages_Inter,"Text":self.Cages_Text,"Color":(137, 255, 141)},

                "MaleRabbits": {"Count":self.Rabbits_Males_Inter,"Text":self.Males_Text,"Color":(0, 140, 179)},
                "FemaleRabbits": {"Count":self.Rabbits_Females_Inter,"Text":self.Females_Text,"Color":(199, 0, 217)},
                "NullGenderRabbits": {"Count":self.Rabbits_Nulls_Inter,"Text":self.Nulls_Text,"Color":(182, 155, 0)},
                "AllRabbits": {"Count":self.Rabbits_All_Inter,"Text":self.All_Text_2,"Color":(137, 255, 141)},

                "MaleCages": {"Count":self.Cages_Males_Inter,"Text":self.Males_Text_2,"Color":(0, 140, 179)},
                "FemaleCages": {"Count":self.Cages_Females_Inter,"Text":self.Females_Text_2,"Color":(199, 0, 217)},
                "NullGenderCages": {"Count":self.Cages_Kids_Inter,"Text":self.Kids_Text,"Color":(182, 155, 0)},
                "AllCages": {"Count":self.Cages_All_Inter,"Text":self.All_Text,"Color":(137, 255, 141)},

                "AvailableRabbits": {"Count":self.Rabbits_Disponible_Inter,"Text":self.Disponible_Text,"Color":(85, 255, 127)},
                "SoldRabbits": {"Count":self.Rabbits_SoldOut_Inter,"Text":self.SoldOut_Text,"Color":(170, 0, 0)},
                "OwnedRabbits": {"Count":self.Rabbits_Owned_Inter,"Text":self.Owned_Text,"Color":(0, 170, 255)},
                "LostRabbits": {"Count":self.Rabbits_Dead_Inter,"Text":self.Dead_Text,"Color":(234, 66, 0)},
            }
            
            for key, widget in mappings.items():
                count = results[key]
                color = widget["Color"] if count > 0 else (255, 137, 137)
                widget["Text"].setStyleSheet(f"border:none;background-color: rgba(0, 0, 0, 0);color:rgb{color};font: 75 25pt 'Acme';")
                widget["Count"].setStyleSheet(f"border:none;background-color: rgba(0, 0, 0, 0);color:rgb{color};font: 75 15pt 'Acme';")
                widget["Count"].setText(str(count))

            # Get the Top Buyer
            cursor.execute("SELECT CustomerID, SUM(Total) AS TotalBuy FROM factures GROUP BY CustomerID ORDER BY TotalBuy DESC LIMIT 1")
            last = cursor.fetchone()
            if last:
                cursor.execute("SELECT ID, Name FROM customers WHERE ID = ?", (last[0],))
                customer = cursor.fetchone()
                msg_top_buyer = f"{customer[0]} | {customer[1]}" if customer else str(last)
            else:
                msg_top_buyer = "No data"

            self.TopBuyer_Inter.setText(msg_top_buyer)
            # Get the Last Income Date
            cursor.execute("SELECT Date FROM factures ORDER BY ID DESC LIMIT 1")
            last_income = cursor.fetchone()

            msg_last_income = last_income[0] if last_income else "No data"
            self.LastIncome_Inter.setText(msg_last_income)

            

            
            self.Dashboard_QText.setText("""🐰 Rabbit Manager Dashboard
Welcome to Rabbit Manager, the ultimate tool for managing your rabbit farm efficiently. This application helps you keep track of every rabbit, including breeding details, purchases, and sales, all in one place.

Key Features:
✅ Rabbit Management – Store and organize rabbit details, including breed, gender, and injection dates.
✅ Family Tree Generator – Visualize each rabbit’s lineage with an automatically generated family tree.
✅ Customer Tracking – Keep records of customer purchases, including contact details and transaction history.
✅ Invoice Generator – Automatically generate and store invoices for each sale.
✅ Smart Filtering & Search – Quickly find rabbits or customers based on ID, type, or purchase history.

🐇 Manage your farm with ease and efficiency!""")


        








    def StartingMethode(self):
        # | Initialize The Pages |
        self.Switch_Page(0) # MainMenu Dashboard First
        self.Customer_Windows.setCurrentIndex(0) # CustomersMenu View First

        self.LoadDashboard()

        #----------------------------#
        #Menu Buttons Fonctions
        #----------------------------#
        self.CustomersTable_Advanced.verticalHeader().setVisible(False) # Disable Counter VertHead
        self.CustomersTable_Advanced.setColumnWidth(0,80) # Customer Advanced ID
        self.CustomersTable_Advanced.setColumnWidth(1,150)   # Customer Advanced Name
        self.CustomersTable_Advanced.setColumnWidth(2,100)   # Customer Advanced Phone
        self.CustomersTable_Advanced.setColumnWidth(3,433)   # Customer Advanced Address
        self.CustomersTable_Advanced.setColumnWidth(4,150)   # Customer Advanced Activity
        self.Customer_Windows.setCurrentIndex(0)

        self.RabbitsTable_Advanced.verticalHeader().setVisible(False) # Disable Counter VertHead
        self.RabbitsTable_Advanced.setColumnWidth(0,80) # Rabbit Advanced ID
        self.RabbitsTable_Advanced.setColumnWidth(1,180)   # Rabbit Advanced Breed
        self.RabbitsTable_Advanced.setColumnWidth(2,100)   # Rabbit Advanced Born
        self.RabbitsTable_Advanced.setColumnWidth(3,120)   # Rabbit Advanced Generation
        self.RabbitsTable_Advanced.setColumnWidth(4,80)   # Rabbit Advanced Cage
        self.RabbitsTable_Advanced.setColumnWidth(5,180)   # Rabbit Advanced Color
        self.RabbitsTable_Advanced.setColumnWidth(6,150)   # Rabbit Advanced Activity
        self.Rabbit_Windows.setCurrentIndex(0)

        self.CagesTable_Advanced.verticalHeader().setVisible(False) # Disable Counter VertHead
        self.CagesTable_Advanced.setColumnWidth(0,100) # Cage Advanced ID
        self.CagesTable_Advanced.setColumnWidth(1,150)   # Cage Advanced Bought
        self.CagesTable_Advanced.setColumnWidth(2,450)   # Cage Advanced Notes
        self.CagesTable_Advanced.setColumnWidth(3,150)   # Cage Advanced Activity
        self.Cages_Windows.setCurrentIndex(0)

        self.FactureTable_Advanced.verticalHeader().setVisible(False) # Disable Counter VertHead
        self.Facture_Windows.setCurrentIndex(0)

        self.ExpensesTable_Advanced.verticalHeader().setVisible(False) # Disable Counter VertHead
        self.ExpensesTable_Advanced.setColumnWidth(0,100)  # Expenses Advanced ID
        self.ExpensesTable_Advanced.setColumnWidth(1,150)   # Expenses Advanced Name
        self.ExpensesTable_Advanced.setColumnWidth(2,150)   # Expenses Advanced Total
        self.ExpensesTable_Advanced.setColumnWidth(3,350)   # Expenses Advanced Notes
        self.ExpensesTable_Advanced.setColumnWidth(4,150)   # Expenses Advanced Activity
        #----------------------------#

        #----------------------------#
        #Disable Search Fonctions
        #----------------------------#
        self.Search_Customer.setReadOnly(True)
        self.Search_Customer.setText("")
        self.Search_Customer.setPlaceholderText("Pick Option From The Button [ By ]")

        self.Search_Rabbits.setReadOnly(True)
        self.Search_Rabbits.setText("")
        self.Search_Rabbits.setPlaceholderText("Pick Option From The Button [ By ]")

        self.Search_Cages.setReadOnly(True)
        self.Search_Cages.setText("")
        self.Search_Cages.setPlaceholderText("Pick Option From The Button [ By ]")

        self.Search_Facture.setReadOnly(True)
        self.Search_Facture.setText("")
        self.Search_Facture.setPlaceholderText("Pick Option From The Button [ By ]")

        self.Search_Expenses.setReadOnly(True)
        self.Search_Expenses.setText("")
        self.Search_Expenses.setPlaceholderText("Pick Option From The Button [ By ]")
        #----------------------------#

        
        self.Customers_Widgets_Reload()
        self.Rabbits_Widgets_Reload()
        self.Cages_Widgets_Reload()
        self.Facture_Widgets_Reload()
        self.Expenses_Widgets_Reload()

    def CustomerSearchFilter(self,FilterBy,SearchBar):
        SearchFilter(FilterBy,SearchBar,"Customer")
        self.Customers_Widgets_Reload

    def Customers_Widgets_Reload(self):
        Current_FilterGender = self.FilterGender_Customer.currentText()
        Current_FilterBy = self.FilterBy_Customer.currentText()
        CurrentTextSearch = self.Search_Customer.text()
        self.Load_CustomersAdvancedTable() # Customers Table Filled
        self.ImagesGrid(getDBData("ID,Name,Phone,Address,Gender,Notes","customers",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Customer.isChecked()),"Customers") # Customers View Filled
        self.LoadDashboard()
    
    def RabbitSearchFilter(self,FilterBy,SearchBar):
        SearchFilter(FilterBy,SearchBar,"Rabbit")
        self.Rabbits_Widgets_Reload
    
    def Rabbits_Widgets_Reload(self):
        Current_FilterGender = self.FilterGender_Rabbits.currentText()
        Current_FilterBy = self.FilterBy_Rabbits.currentText()
        CurrentTextSearch = self.Search_Rabbits.text()
        self.Load_RabbitsAdvancedTable()
        self.ImagesGrid(getDBData("ID,Breed,Gender","rabbits",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Rabbits.isChecked()),"Rabbits") # Customers View Filled
        self.LoadDashboard()

    def CageSearchFilter(self,FilterBy,SearchBar):
        SearchFilter(FilterBy,SearchBar,"Cage")
        self.Cages_Widgets_Reload

    def Cages_Widgets_Reload(self):
        Current_FilterGender = self.FilterGender_Cages.currentText()
        Current_FilterBy = self.FilterBy_Cages.currentText()
        CurrentTextSearch = self.Search_Cages.text()
        self.Load_CagesAdvancedTable()
        self.ImagesGrid(getDBData("ID,Bought,Gender","cages",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Cages.isChecked()),"Cages") # Customers View Filled
        self.LoadDashboard()

    def FactureSearchFilter(self,FilterBy,SearchBar):
        SearchFilter(FilterBy,SearchBar,"Facture")
        self.Facture_Widgets_Reload

    def Facture_Widgets_Reload(self):
        Current_FilterBy = self.FilterBy_Facture.currentText()
        CurrentTextSearch = self.Search_Facture.text()
        self.Load_FactureAdvancedTable()
        self.ImagesGrid(getDBData("ID,Date,Total","factures","Gender",Current_FilterBy,CurrentTextSearch,self.Ordre_Facture.isChecked()),"Factures/PNG")
        self.LoadDashboard()

    def ExpensesSearchFilter(self,FilterBy,SearchBar):
        SearchFilter(FilterBy,SearchBar,"Expense")
        self.Expenses_Widgets_Reload

    def Expenses_Widgets_Reload(self):
        self.Load_ExpensesAdvancedTable()
        self.LoadDashboard()
        
    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Initialize The Window ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Rabbits Manager Application [ By Ibrahim Bouchaala ]") #Title OF The Application
        self.setWindowIcon(QIcon(":/Icons/Logo.png")) #Icon In The Top Of The Application
        self.setWindowFlags(Qt.FramelessWindowHint) # Frameless Window
        self.setAttribute(Qt.WA_TranslucentBackground, True) # Transparent Background Window
        
        #----------------------------#
        #Menu Buttons Fonctions
        #----------------------------#
        self.Dashboard_Button.clicked.connect(lambda:self.Switch_Page(0))
        self.Customers_Button.clicked.connect(lambda:self.Switch_Page(1))
        self.Rabbits_Button.clicked.connect(lambda:self.Switch_Page(2))
        self.Cages_Button.clicked.connect(lambda:self.Switch_Page(3))
        self.Factures_Button.clicked.connect(lambda:self.Switch_Page(4))
        self.Expenses_Button.clicked.connect(lambda:self.Switch_Page(5))
        self.Settings_Button.clicked.connect(lambda:self.Switch_Page(6))
        self.Logout_Button.clicked.connect(lambda:self.Switch_Page(7))

        self.Export_Exel_Customers.clicked.connect(lambda:self.export_to_exel_Table(self.CustomersTable_Advanced,"Customers",self.Exportation_CustomerAdvanced_Info))
        self.Export_PDF_Customers.clicked.connect(lambda:self.export_to_pdf_Table(self.CustomersTable_Advanced,"Customers",self.Exportation_CustomerAdvanced_Info))
        
        self.Export_Exel_Rabbits.clicked.connect(lambda:self.export_to_exel_Table(self.RabbitsTable_Advanced,"Rabbits",self.Exportation_RabbitsAdvanced_Info))
        self.Export_PDF_Rabbits.clicked.connect(lambda:self.export_to_pdf_Table(self.RabbitsTable_Advanced,"Rabbits",self.Exportation_RabbitsAdvanced_Info))
        
        self.Export_Exel_Cages.clicked.connect(lambda:self.export_to_exel_Table(self.CagesTable_Advanced,"Cages",self.Exportation_CagesAdvanced_Info))
        self.Export_PDF_Cages.clicked.connect(lambda:self.export_to_pdf_Table(self.CagesTable_Advanced,"Cages",self.Exportation_CagesAdvanced_Info))
        
        self.Export_Exel_Facture.clicked.connect(lambda:self.export_to_exel_Table(self.FactureTable_Advanced,"Factures",self.Exportation_FactureAdvanced_Info))
        self.Export_PDF_Facture.clicked.connect(lambda:self.export_to_pdf_Table(self.FactureTable_Advanced,"Factures",self.Exportation_FactureAdvanced_Info))
        
        self.Export_Exel_Expenses.clicked.connect(lambda:self.export_to_exel_Table(self.ExpensesTable_Advanced,"Expenses",self.Exportation_ExpensesAdvanced_Info))
        self.Export_PDF_Expenses.clicked.connect(lambda:self.export_to_pdf_Table(self.ExpensesTable_Advanced,"Expenses",self.Exportation_ExpensesAdvanced_Info))
        
        self.Add_Customer_View.clicked.connect(self.openAddCustomerWindow)

        self.Add_Rabbit_View.clicked.connect(self.openAddRabbitsWindow)
        self.Rabbit_Tree.clicked.connect(self.openRabbitsTreeWindow)

        self.Add_Cage_View.clicked.connect(self.openAddCagesWindow)
        self.Cages_Tree.clicked.connect(self.openCagesTreeWindow)

        self.Add_Expenses_View.clicked.connect(self.openAddExpensesWindow)
        self.Add_Facture_View.clicked.connect(self.openAddFactureWindow)


        self.Logout_Button.clicked.connect(self.close)
        #----------------------------#

        #----------------------------#
        #Filter Buttons Fonctions
        #----------------------------#
        self.FilterGender_Customer.currentIndexChanged.connect(self.Customers_Widgets_Reload)
        self.FilterBy_Customer.currentIndexChanged.connect(lambda:self.CustomerSearchFilter(self.FilterBy_Customer,self.Search_Customer))
        self.Search_Customer.textChanged.connect(self.Customers_Widgets_Reload)
        self.Ordre_Customer.toggled.connect(self.Customers_Widgets_Reload)

        self.FilterGender_Rabbits.currentIndexChanged.connect(self.Rabbits_Widgets_Reload)
        self.FilterBy_Rabbits.currentIndexChanged.connect(lambda:self.RabbitSearchFilter(self.FilterBy_Rabbits,self.Search_Rabbits))
        self.Search_Rabbits.textChanged.connect(self.Rabbits_Widgets_Reload)
        self.Ordre_Rabbits.toggled.connect(self.Rabbits_Widgets_Reload)

        self.FilterGender_Cages.currentIndexChanged.connect(self.Cages_Widgets_Reload)
        self.FilterBy_Cages.currentIndexChanged.connect(lambda:self.CageSearchFilter(self.FilterBy_Cages,self.Search_Cages))
        self.Search_Cages.textChanged.connect(self.Cages_Widgets_Reload)
        self.Ordre_Cages.toggled.connect(self.Cages_Widgets_Reload)

        self.FilterBy_Expenses.currentIndexChanged.connect(lambda:self.ExpensesSearchFilter(self.FilterBy_Expenses,self.Search_Expenses))
        self.Search_Expenses.textChanged.connect(self.Expenses_Widgets_Reload)
        self.Ordre_Expenses.toggled.connect(self.Expenses_Widgets_Reload)
        #----------------------------#

        self.StartingMethode()

        #----------------------------#
        #Verify DataBase
        #----------------------------#
        checkRabbitsTable()
        checkExpensesTable()
        checkCagesTable()
        checkCustomersTable()
        checkFacturesTable()

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Initialize The Pages ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    
    def Load_CustomersAdvancedTable(self):
        self.CustomersTable_Advanced.clearContents()
        self.CustomersTable_Advanced.setRowCount(0)
        Current_FilterGender = self.FilterGender_Customer.currentText()
        Current_FilterBy = self.FilterBy_Customer.currentText()
        CurrentTextSearch = self.Search_Customer.text()
        data = getDBData("ID,Name,Phone,Address","customers",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Customer.isChecked())
        Gender = getDBData("Gender","customers",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Customer.isChecked())
        for (row_index,row_data) in enumerate(data):
            self.CustomersTable_Advanced.insertRow(row_index)
            for col_index,cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data),)
                item.setTextAlignment(Qt.AlignCenter)
                self.CustomersTable_Advanced.setItem(row_index,col_index,item)
                if(len(Gender)>0 and len(Gender[row_index])>0):
                    if(Gender[row_index][0]=="Null"):
                        self.CustomersTable_Advanced.item(row_index, col_index).setBackground(QColor(182, 155, 0))
                    if(Gender[row_index][0]=="Male"):
                        self.CustomersTable_Advanced.item(row_index, col_index).setBackground(QColor(0, 140, 179))
                    if(Gender[row_index][0]=="Female"):
                        self.CustomersTable_Advanced.item(row_index, col_index).setBackground(QColor(199, 0, 217))

            self.CustomersTable_Advanced.setCellWidget(row_index,4,DoubleButtonWidgets(row_index,row_data,"Customers","AlredyMain",self))
            self.CustomersTable_Advanced.setRowHeight(row_index,50)  

    def Load_RabbitsAdvancedTable(self):
        self.RabbitsTable_Advanced.clearContents()
        self.RabbitsTable_Advanced.setRowCount(0)
        Current_FilterGender = self.FilterGender_Rabbits.currentText()
        Current_FilterBy = self.FilterBy_Rabbits.currentText()
        CurrentTextSearch = self.Search_Rabbits.text()
        data = getDBData("ID,Breed,Born,Generation,CageID,Color","rabbits",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Rabbits.isChecked())
        Gender = getDBData("Gender","rabbits",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Rabbits.isChecked())
        Customer = getDBData("CustomerID","rabbits",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Rabbits.isChecked())

        for (row_index,row_data) in enumerate(data):
            self.RabbitsTable_Advanced.insertRow(row_index)
            for col_index,cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data),)
                item.setTextAlignment(Qt.AlignCenter)
                self.RabbitsTable_Advanced.setItem(row_index,col_index,item)
                if(len(Gender)>0 and len(Gender[row_index])>0):
                    if(Gender[row_index][0]=="Null"):
                        self.RabbitsTable_Advanced.item(row_index, col_index).setBackground(QColor(182, 155, 0))
                    elif(Gender[row_index][0]=="Male"):
                        self.RabbitsTable_Advanced.item(row_index, col_index).setBackground(QColor(0, 140, 179))
                    elif(Gender[row_index][0]=="Female"):
                        self.RabbitsTable_Advanced.item(row_index, col_index).setBackground(QColor(199, 0, 217))

            self.RabbitsTable_Advanced.setCellWidget(row_index,6,DoubleButtonWidgets(row_index,row_data,"Rabbits","AlredyMain",self))
            self.RabbitsTable_Advanced.setRowHeight(row_index,50)
            if(str(Customer[row_index][0]) == "0"):
                self.RabbitsTable_Advanced.item(row_index, 0).setBackground(QColor(0, 170, 255))
            elif(str(Customer[row_index][0]) == "-1"):
                self.RabbitsTable_Advanced.item(row_index, 0).setBackground(QColor(234, 66, 0))
            elif(Customer[row_index][0] is None):
                self.RabbitsTable_Advanced.item(row_index, 0).setBackground(QColor(85, 255, 127))
            elif(Customer[row_index][0] is not None):
                self.RabbitsTable_Advanced.item(row_index, 0).setBackground(QColor(170, 0, 0))

            




    def Load_CagesAdvancedTable(self):
        self.CagesTable_Advanced.clearContents()
        self.CagesTable_Advanced.setRowCount(0)
        Current_FilterGender = self.FilterGender_Cages.currentText()
        Current_FilterBy = self.FilterBy_Cages.currentText()
        CurrentTextSearch = self.Search_Cages.text()
        data = getDBData("ID,Bought,Notes","cages",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Cages.isChecked())
        Gender = getDBData("Gender","cages",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Cages.isChecked())
        Customer = getDBData("CustomerID","cages",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Cages.isChecked())


        for (row_index,row_data) in enumerate(data):
            self.CagesTable_Advanced.insertRow(row_index)
            for col_index,cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data),)
                item.setTextAlignment(Qt.AlignCenter)
                self.CagesTable_Advanced.setItem(row_index,col_index,item)
                if(len(Gender)>0 and len(Gender[row_index])>0):
                    if(Gender[row_index][0]=="Kids"):
                        self.CagesTable_Advanced.item(row_index, col_index).setBackground(QColor(182, 155, 0))
                    if(Gender[row_index][0]=="Male"):
                        self.CagesTable_Advanced.item(row_index, col_index).setBackground(QColor(0, 140, 179))
                    if(Gender[row_index][0]=="Female"):
                        self.CagesTable_Advanced.item(row_index, col_index).setBackground(QColor(199, 0, 217))

            self.CagesTable_Advanced.setCellWidget(row_index,3,DoubleButtonWidgets(row_index,row_data,"Cages","AlredyMain",self))
            self.CagesTable_Advanced.setCellWidget(row_index,2,NoteWidget(row_data[2],"Cages","AlredyMain",self))
            self.CagesTable_Advanced.setRowHeight(row_index,50) 

            if(str(Customer[row_index][0]) == "0"):
                self.CagesTable_Advanced.item(row_index, 0).setBackground(QColor(0, 170, 255))
            elif(str(Customer[row_index][0]) == "-1"):
                self.CagesTable_Advanced.item(row_index, 0).setBackground(QColor(234, 66, 0))
            elif(Customer[row_index][0] is None):
                self.CagesTable_Advanced.item(row_index, 0).setBackground(QColor(85, 255, 127))
            elif(Customer[row_index][0] is not None):
                self.CagesTable_Advanced.item(row_index, 0).setBackground(QColor(170, 0, 0)) 

    def Load_FactureAdvancedTable(self):
        self.FactureTable_Advanced.clearContents()
        self.FactureTable_Advanced.setRowCount(0)
        Current_FilterBy = self.FilterBy_Facture.currentText()
        CurrentTextSearch = self.Search_Facture.text()
        data = getDBData("*","factures","Gender",Current_FilterBy,CurrentTextSearch,self.Ordre_Facture.isChecked())

        for (row_index,row_data) in enumerate(data):
            self.FactureTable_Advanced.insertRow(row_index)
            for col_index,cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data),)
                item.setTextAlignment(Qt.AlignCenter)
                self.FactureTable_Advanced.setItem(row_index,col_index,item)
                self.FactureTable_Advanced.item(row_index, col_index).setBackground(QColor(137, 255, 141))

            self.FactureTable_Advanced.setCellWidget(row_index,4,DoubleButtonWidgets(row_index,row_data,"Factures","AlredyMain",self))
            self.FactureTable_Advanced.setRowHeight(row_index,50)  

    def Load_ExpensesAdvancedTable(self):
        self.ExpensesTable_Advanced.clearContents()
        self.ExpensesTable_Advanced.setRowCount(0)
        Current_FilterBy = self.FilterBy_Expenses.currentText()
        CurrentTextSearch = self.Search_Expenses.text()
        data = getDBData("*","expenses","Gender",Current_FilterBy,CurrentTextSearch,self.Ordre_Expenses.isChecked())

        for (row_index,row_data) in enumerate(data):
            self.ExpensesTable_Advanced.insertRow(row_index)
            for col_index,cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data),)
                item.setTextAlignment(Qt.AlignCenter)
                self.ExpensesTable_Advanced.setItem(row_index,col_index,item)

            self.ExpensesTable_Advanced.setCellWidget(row_index,3,NoteWidget(row_data[3],"Expenses","AlredyMain",self))
            self.ExpensesTable_Advanced.setCellWidget(row_index,4,DoubleButtonWidgets(row_index,row_data,"Expenses","AlredyMain",self))
            self.ExpensesTable_Advanced.setRowHeight(row_index,150)  

            self.ExpensesTable_Advanced.item(row_index, 3).setBackground(QColor(117, 58, 58))
            self.ExpensesTable_Advanced.item(row_index, 2).setBackground(QColor(156, 78, 78))
            self.ExpensesTable_Advanced.item(row_index, 1).setBackground(QColor(183, 92, 92))
            self.ExpensesTable_Advanced.item(row_index, 0).setBackground(QColor(255, 128, 128))


    
    def export_to_exel_Table(self,TableData,Type,SendMsg):
        data = []
        self.headers = [TableData.horizontalHeaderItem(col).text() for col in range(TableData.columnCount())]
        for row in range (TableData.rowCount()):
            row_data = [TableData.item(row,col).text() if TableData.item(row,col) is not None else "" for col in range(TableData.columnCount())]
            data.append(row_data)

        df =pd.DataFrame(data, columns=self.headers)
        df_filtered = df.iloc[:,:-1]
        default_folder = os.path.join(os.getcwd(), '0_EXEL')
        if not os.path.exists(default_folder):
            os.makedirs(default_folder)

        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self,"Save Exel File",os.path.join(default_folder,"["+Type+"_Table]_"+datetime.today().strftime("{%m-%d-%Y}_(%H-%M-%S)")),"Exel Files (*.xlsx);;All Files (*)")
        if file_path:
            df_filtered.to_excel(file_path,index=False)
            SendMsg.setText(f"Exel Table Exported To {file_path}")
    
    def export_to_pdf_Table(self,TableData,Type,SendMsg):
        default_folder = os.path.join(os.getcwd(), '0_PDF')
        if not os.path.exists(default_folder):
            os.makedirs(default_folder)
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self,"Save PDF File",os.path.join(default_folder,"["+Type+"_Table]_"+datetime.today().strftime("{%m-%d-%Y}_(%H-%M-%S)")),"PDF Files (*.pdf);;All Files (*)")
        if file_path:
            pdf_document = SimpleDocTemplate(file_path,pagesize=letter)
            n = TableData.columnCount()
            headers = [TableData.horizontalHeaderItem(col).text() for col in range(n-1)]
            data = [headers]

            for row in range(TableData.rowCount()):
                row_data = [TableData.item(row,col).text() if TableData.item(row,col) is not None else "" for col in range(n-1)]
                data.append(row_data)

            pdf_table = Table(data)
            style = TableStyle([
                ("ALIGN",(0,0),(-1,-1),"CENTER"),
                ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
                ("FONTSIZE",(0,0),(-1,-1),8),
                ("BOTTOMPADDING",(0,0),(-1,0),12),
                ("GRID",(0,0),(-1,0),1,colors.black)
            ])
            pdf_table.setStyle(style)
            pdf_document.build([pdf_table])
            SendMsg.setText(f"PDF Table Exported To {file_path}")


#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Buttons Customers Advanced Table Class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|
class NoteWidget(QWidget):
    def __init__(self,data,SelectedPath,Current,mainWindow):
        super().__init__()

        self.data = data
        self.SelectedPath = SelectedPath
        self.Current = Current
        self.mainWindow = mainWindow

        layout = QHBoxLayout(self)
        self.NotesPage = QPlainTextEdit("",self)    
        self.NotesPage.setPlainText(str(self.data))
        self.NotesPage.setReadOnly(True)
        self.NotesPage.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NotesPage.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NotesPage.setStyleSheet("QPlainTextEdit{font: 75 13pt 'Acme';background-color: rgb(69, 69, 69);color: rgb(255, 255, 255);border: 2px solid rgb(255, 255, 255);border-style: outset;	border-radius: 10px;}")

        layout.addWidget(self.NotesPage)

class DoubleButtonWidgets(QWidget):
    def __init__(self,row_index,row_data,SelectedPath,Current,mainWindow):
        super().__init__()

        self.row_index = row_index
        self.row_data = row_data
        self.SelectedPath = SelectedPath
        self.Current = Current
        self.mainWindow = mainWindow

        self.ID = self.row_data[0]

        layout = QHBoxLayout(self)

        if(self.SelectedPath != "Expenses"):
            self.AccessButton = QPushButton("",self)    
            self.AccessButton.setStyleSheet("QPushButton {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Monitor_Yellow.png);}QPushButton:hover {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Monitor_Mix.png);}QPushButton:pressed {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Monitor_White.png);}")
            self.AccessButton.setFixedSize(31,31)    
            self.AccessButton.clicked.connect(self.AccessButton_Clicked)
            layout.addWidget(self.AccessButton)
        
        if(self.SelectedPath == "Customers"):

            self.Edit_Button = QPushButton("",self)    
            self.Edit_Button.setStyleSheet("QPushButton {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Edit_Blue.png);}QPushButton:hover {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Edit_Mix.png);}QPushButton:pressed {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Edit_White.png);}")
            self.Edit_Button.setFixedSize(31,31)    
            self.Edit_Button.clicked.connect(self.EditButton_Clicked)
            layout.addWidget(self.Edit_Button)

            with sqlite3.connect("ElevageInfos.db") as connection:
                AllRabbitsBought = len(connection.cursor().execute(f"SELECT ID FROM factures WHERE CustomerID={self.ID}").fetchall())
            if(AllRabbitsBought == 0):
                self.DeleteButton = QPushButton("",self)    
                self.DeleteButton.setStyleSheet("QPushButton {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Pink.png);}QPushButton:hover {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Mix.png);}QPushButton:pressed {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_White.png);}")
                self.DeleteButton.setFixedSize(31,31)    
                self.DeleteButton.clicked.connect(self.DeleteButton_Clicked)
                layout.addWidget(self.DeleteButton)

        elif(self.SelectedPath == "Factures"):
            self.DeleteButton = QPushButton("",self)    
            self.DeleteButton.setStyleSheet("QPushButton {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Pink.png);}QPushButton:hover {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Mix.png);}QPushButton:pressed {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_White.png);}")
            self.DeleteButton.setFixedSize(31,31)    
            self.DeleteButton.clicked.connect(self.DeleteButton_Clicked)
            layout.addWidget(self.DeleteButton)
        
        elif(self.SelectedPath == "Rabbits"):
            self.Edit_Button = QPushButton("",self)    
            self.Edit_Button.setStyleSheet("QPushButton {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Edit_Blue.png);}QPushButton:hover {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Edit_Mix.png);}QPushButton:pressed {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Edit_White.png);}")
            self.Edit_Button.setFixedSize(31,31)    
            self.Edit_Button.clicked.connect(self.EditButton_Clicked)
            layout.addWidget(self.Edit_Button)

            with sqlite3.connect("ElevageInfos.db") as connection:
                AllSonsRabbits = len(connection.cursor().execute(f"SELECT ID FROM rabbits WHERE Mother={self.ID} OR Father ={self.ID} OR (ID={self.ID} AND (FactureID NOT NULL OR CustomerID NOT NULL))").fetchall())

            if(AllSonsRabbits == 0):
                self.DeleteButton = QPushButton("",self)    
                self.DeleteButton.setStyleSheet("QPushButton {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Pink.png);}QPushButton:hover {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Mix.png);}QPushButton:pressed {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_White.png);}")
                self.DeleteButton.setFixedSize(31,31)    
                self.DeleteButton.clicked.connect(self.DeleteButton_Clicked)
                layout.addWidget(self.DeleteButton)
        
        elif(self.SelectedPath == "Cages"):
            self.Edit_Button = QPushButton("",self)    
            self.Edit_Button.setStyleSheet("QPushButton {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Edit_Blue.png);}QPushButton:hover {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Edit_Mix.png);}QPushButton:pressed {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Edit_White.png);}")
            self.Edit_Button.setFixedSize(31,31)    
            self.Edit_Button.clicked.connect(self.EditButton_Clicked)
            layout.addWidget(self.Edit_Button)

            with sqlite3.connect("ElevageInfos.db") as connection:
                AllRabbitsInCage = len(connection.cursor().execute(f"SELECT ID FROM rabbits WHERE CageID={self.ID}").fetchall())

            if(AllRabbitsInCage == 0):
                self.DeleteButton = QPushButton("",self)    
                self.DeleteButton.setStyleSheet("QPushButton {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Pink.png);}QPushButton:hover {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Mix.png);}QPushButton:pressed {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_White.png);}")
                self.DeleteButton.setFixedSize(31,31)    
                self.DeleteButton.clicked.connect(self.DeleteButton_Clicked)
                layout.addWidget(self.DeleteButton)
        
        elif(self.SelectedPath == "Expenses"):

            self.Edit_Button = QPushButton("",self)    
            self.Edit_Button.setStyleSheet("QPushButton {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Edit_Blue.png);}QPushButton:hover {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Edit_Mix.png);}QPushButton:pressed {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Edit_White.png);}")
            self.Edit_Button.setFixedSize(50,50)    
            self.Edit_Button.clicked.connect(self.EditButton_Clicked)
            layout.addWidget(self.Edit_Button)

            self.DeleteButton = QPushButton("",self)    
            self.DeleteButton.setStyleSheet("QPushButton {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Pink.png);}QPushButton:hover {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Mix.png);}QPushButton:pressed {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_White.png);}")
            self.DeleteButton.setFixedSize(50,50)    
            self.DeleteButton.clicked.connect(self.DeleteButton_Clicked)
            layout.addWidget(self.DeleteButton)




        
    def AccessButton_Clicked(self):
        mainWindow_Geometry = self.mainWindow.geometry()
        if(self.SelectedPath == "Customers"):
            blurEffect = QGraphicsBlurEffect()
            blurEffect.setBlurRadius(10)
            self.mainWindow.Window.setGraphicsEffect(blurEffect)
            from Index_MainCustomerView import mainCustomer

            with sqlite3.connect("ElevageInfos.db") as connection:
                cursor = connection.cursor()
                query = f"SELECT ID,Name,Phone,Address,Gender,Notes FROM customers WHERE ID = '{self.ID}'"
                cursor.execute(query)
                Data = cursor.fetchall()[0]

            mainCustomerWindow = mainCustomer(Find_Image_SelectedView(self.SelectedPath,Data[0]),Data,self.mainWindow)
            Right = mainWindow_Geometry.x() + 241
            Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainCustomerWindow.height()) // 2 )
            mainCustomerWindow.move(Right, Centre)
            mainCustomerWindow.exec()
            self.mainWindow.Window.setGraphicsEffect(None)

        elif(self.SelectedPath == "Factures"):
            print(self.Current)
            from Index_MainFactureView import mainFacture

            with sqlite3.connect("ElevageInfos.db") as connection:
                cursor = connection.cursor()
                query = f"SELECT CustomerID FROM factures WHERE ID = '{self.ID}'"
                cursor.execute(query)
                Data = cursor.fetchall()[0]
            with sqlite3.connect("ElevageInfos.db") as connection:
                cursor = connection.cursor()
                query = f"SELECT ID,Name,Phone,Address,Gender FROM customers WHERE ID = '{Data[0]}'"
                cursor.execute(query)
                Data = cursor.fetchall()[0]
            
            if(self.Current == "AlredyMain"):
                blurEffect = QGraphicsBlurEffect()
                blurEffect.setBlurRadius(10)
                self.mainWindow.Window.setGraphicsEffect(blurEffect)
                mainFactureWindow = mainFacture(self.ID,Find_Image_SelectedView(f"{self.SelectedPath}/PNG",self.ID),Data,self.Current,self.mainWindow)
                Right = mainWindow_Geometry.x() + 241
                Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainFactureWindow.height()) // 2 )
                mainFactureWindow.move(Right, Centre)
                mainFactureWindow.exec()
                self.mainWindow.Window.setGraphicsEffect(None)
            
            else :

                mainFactureWindow = mainFacture(self.ID,Find_Image_SelectedView(f"{self.SelectedPath}/PNG",self.ID),Data,self.Current,self.mainWindow)
                Right = mainWindow_Geometry.x() + 241
                Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainFactureWindow.height()) // 2 )
                mainFactureWindow.move(Right, Centre)
                mainFactureWindow.exec()

        elif(self.SelectedPath == "Rabbits"):
            blurEffect = QGraphicsBlurEffect()
            blurEffect.setBlurRadius(10)
            self.mainWindow.Window.setGraphicsEffect(blurEffect)
            from Index_MainRabbitView import mainRabbitView

            with sqlite3.connect("ElevageInfos.db") as connection:
                cursor = connection.cursor()
                query = f"SELECT ID,Breed,Born,Color,Gender,Father,Mother,Generation,CageID,Type,Bought,FactureID,CustomerID,Sold,Notes FROM rabbits WHERE ID = '{self.ID}'"
                cursor.execute(query)
                Data = cursor.fetchall()[0]

            mainRabbitWindow = mainRabbitView(Find_Image_SelectedView(self.SelectedPath,Data[0]),Data,self.mainWindow)
            Right = mainWindow_Geometry.x() + 241
            Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainRabbitWindow.height()) // 2 )
            mainRabbitWindow.move(Right, Centre)
            mainRabbitWindow.exec()
            self.mainWindow.Window.setGraphicsEffect(None)
        

        elif(self.SelectedPath == "Cages"):
            blurEffect = QGraphicsBlurEffect()
            blurEffect.setBlurRadius(10)
            self.mainWindow.Window.setGraphicsEffect(blurEffect)
            from Index_MainCageView import mainCage

            mainRabbitWindow = mainCage(Find_Image_SelectedView(self.SelectedPath,self.ID),self.ID,self.mainWindow)
            Right = mainWindow_Geometry.x() + 241
            Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainRabbitWindow.height()) // 2 )
            mainRabbitWindow.move(Right, Centre)
            mainRabbitWindow.exec()
            self.mainWindow.Window.setGraphicsEffect(None)



        

    def EditButton_Clicked(self):
        if(self.SelectedPath == "Customers"):
            from Index_MainAddEditCustomer import mainEditCustomer
            mainWindow_Geometry = self.mainWindow.geometry()
            blurEffect = QGraphicsBlurEffect()
            blurEffect.setBlurRadius(10)
            self.mainWindow.Window.setGraphicsEffect(blurEffect)
            mainAddCustomerWindow = mainEditCustomer(self.ID,self.mainWindow)
            Right = mainWindow_Geometry.x() + 241 + 265
            Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainAddCustomerWindow.height()) // 2 ) - 10
            mainAddCustomerWindow.move(Right, Centre)
            mainAddCustomerWindow.exec()
            self.mainWindow.Window.setGraphicsEffect(None)

        elif(self.SelectedPath == "Rabbits"):
            from Index_MainAddEditRabbit import mainEditRabbit
            mainWindow_Geometry = self.mainWindow.geometry()
            blurEffect = QGraphicsBlurEffect()
            blurEffect.setBlurRadius(10)
            self.mainWindow.Window.setGraphicsEffect(blurEffect)
            mainRabbitTreeWindow = mainEditRabbit(self.ID,self.mainWindow)
            Right = mainWindow_Geometry.x() + 241 + 265
            Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainRabbitTreeWindow.height()) // 2 )
            mainRabbitTreeWindow.move(Right, Centre)
            mainRabbitTreeWindow.exec()
            self.mainWindow.Window.setGraphicsEffect(None)
        
        elif(self.SelectedPath == "Cages"):
            from Index_MainAddEditCages import mainEditCage
            mainWindow_Geometry = self.mainWindow.geometry()
            blurEffect = QGraphicsBlurEffect()
            blurEffect.setBlurRadius(10)
            self.mainWindow.Window.setGraphicsEffect(blurEffect)
            mainAddCustomerWindow = mainEditCage(self.ID,self.mainWindow)
            Right = mainWindow_Geometry.x() + 241 + 265
            Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainAddCustomerWindow.height()) // 2 ) - 10
            mainAddCustomerWindow.move(Right, Centre)
            mainAddCustomerWindow.exec()
            self.mainWindow.Window.setGraphicsEffect(None)
        
        elif(self.SelectedPath == "Expenses"):
            from Index_MainAddEditExpense import mainEditExpense
            mainWindow_Geometry = self.mainWindow.geometry()
            blurEffect = QGraphicsBlurEffect()
            blurEffect.setBlurRadius(10)
            self.mainWindow.Window.setGraphicsEffect(blurEffect)
            mainAddCustomerWindow = mainEditExpense(self.ID,self.mainWindow)
            Right = mainWindow_Geometry.x() + 241 + 265
            Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainAddCustomerWindow.height()) // 2 ) - 10
            mainAddCustomerWindow.move(Right, Centre)
            mainAddCustomerWindow.exec()
            self.mainWindow.Window.setGraphicsEffect(None)




    def DeleteButton_Clicked(self):
        message = QMessageBox.question(self,'Confirmation','Are You Sure You Want To Delete [ '+str(self.ID)+' ]?',QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if (message == QMessageBox.StandardButton.Yes):
            DeleteDBData((self.SelectedPath).lower(),'ID',self.ID)
            match self.SelectedPath:
                case "Customers":
                    self.mainWindow.Customers_Widgets_Reload()
                    self.mainWindow.Exportation_CustomerAdvanced_Info.setText(f"Customer ID [ {str(self.ID)} ] Deleted Successfully")
                    self.mainWindow.Exportation_CustomerView_Info.setText(f"Customer ID [ {str(self.ID)} ] Deleted Successfully")
                case "Factures":
                    if(self.Current != "AlredyMain"):
                       self.Current.FactureCustomer_Widgets_Reload()
                    else :
                        self.mainWindow.Facture_Widgets_Reload()
                    with sqlite3.connect("ElevageInfos.db") as connection:
                        connection.cursor().execute(f"UPDATE rabbits SET CustomerID = NULL,FactureID = NULL,Sold=0 WHERE FactureID = ?", (self.ID,))
                        connection.commit()
                    with sqlite3.connect("ElevageInfos.db") as connection:
                        connection.cursor().execute(f"UPDATE cages SET CustomerID = NULL,FactureID = NULL,Sold=0 WHERE FactureID = ?", (self.ID,))
                        connection.commit()
                case "Rabbits":
                    self.mainWindow.Rabbits_Widgets_Reload()
                    self.mainWindow.Exportation_RabbitsView_Info.setText(f"Rabbit ID [ {str(self.ID)} ] Deleted Successfully")
                    self.mainWindow.Exportation_RabbitsAdvanced_Info.setText(f"Rabbit ID [ {str(self.ID)} ] Deleted Successfully")
                case "Cages":
                    self.mainWindow.Cages_Widgets_Reload()
                    self.mainWindow.Exportation_CagesView_Info.setText(f"Cage ID [ {str(self.ID)} ] Deleted Successfully")
                    self.mainWindow.Exportation_CagesAdvanced_Info.setText(f"Cage ID [ {str(self.ID)} ] Deleted Successfully")
                case "Expenses":
                    self.mainWindow.Expenses_Widgets_Reload()
                    self.mainWindow.Exportation_ExpensesAdvanced_Info.setText(f"Expense ID [ {str(self.ID)} ] Deleted Successfully")




            
    
        