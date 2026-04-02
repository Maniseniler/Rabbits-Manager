#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Importations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

#All PySide6 Importation :
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog,QMessageBox
from PySide6.QtGui import QIcon,QPixmap

#Other Importation Of Packages :
import sqlite3
from pathlib import Path
import os

#Importation Of Interfaces :
from InterfacesPY import Ui_Facture_View_Main

#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Creating A DataBase With All The Columns ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

def getDBData(Importation,DBName,genderFilter,FilterBy,Search):
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()
        if(DBName == "customers" or DBName == "rabbits" or DBName == "cages"):
            query = f"SELECT {Importation} FROM {DBName} WHERE ('{genderFilter}' = 'Gender' OR Gender = '{genderFilter}')"
            if(FilterBy != 'By'):
                query = f"SELECT {Importation} FROM {DBName} WHERE ('{genderFilter}' = 'Gender' OR Gender = '{genderFilter}') AND ({FilterBy} LIKE '%{Search}%')"
        elif (DBName == "factures"):
            query = f"SELECT {Importation} FROM {DBName} WHERE CustomerID = '{genderFilter}'"
            if(FilterBy != 'By'):
                query = f"SELECT {Importation} FROM {DBName} WHERE (CustomerID = '{genderFilter}') AND ({FilterBy} LIKE '%{Search}%')"
        cursor.execute(query)
        Data = cursor.fetchall()
        
    return Data

def DeleteDBData(DBName,FilterBy,Search):
    with sqlite3.connect("ElevageInfos.db") as connection:
        connection.cursor().execute(f"DELETE FROM {DBName} WHERE {FilterBy} = ?", (Search,))
        connection.commit()
        

def Find_Image_SelectedView(SelectedPath,ID):
    appdata_path = os.getenv("APPDATA")  # Gets the %appdata% folder path
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

#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main Window Class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

class mainFacture(QDialog,Ui_Facture_View_Main):

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Clear Images ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def clear_images(self,Current):
        if(Current == "Rabbits"):
            while self.GridRabbits_ScrollArea.count():
                child = self.GridRabbits_ScrollArea.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
        elif(Current == "Cages"):
            while self.GridCages_ScrollArea.count():
                child = self.GridCages_ScrollArea.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Images Grid ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def ImagesGrid(self,Data,SelectedPath,mainCustomer,Number):
        from Index_MainWindow import ImageFrame
        if(SelectedPath == "Rabbits"):
            self.clear_images(SelectedPath)
            self.Facture_Rabbits_ScrollArea.setWidgetResizable(True)
            self.Facture_Rabbits_ScrollArea_Widget.setLayout(self.GridRabbits_ScrollArea)
            self.Facture_Rabbits_ScrollArea.setWidget(self.Facture_Rabbits_ScrollArea_Widget)
            self.GridRabbits_ScrollArea.setAlignment(Qt.AlignTop | Qt.AlignCenter)
            self.GridRabbits_ScrollArea.setSpacing(33)
        
        elif(SelectedPath == "Cages"):
            self.clear_images(SelectedPath)
            self.Facture_Cages_ScrollArea.setWidgetResizable(True)
            self.Facture_Cages_ScrollArea_Widget.setLayout(self.GridCages_ScrollArea)
            self.Facture_Cages_ScrollArea.setWidget(self.Facture_Cages_ScrollArea_Widget)
            self.GridCages_ScrollArea.setAlignment(Qt.AlignTop | Qt.AlignCenter)
            self.GridCages_ScrollArea.setSpacing(33)
        
        for index,Informations in enumerate(Data):
            row = index // Number
            col = index % Number
            ID = Informations[0]
            image_frame = ImageFrame(Find_Image_SelectedView(SelectedPath,ID), f"#{ID}",Informations,self.mainWindow,self,SelectedPath)
            if(SelectedPath == "Rabbits"):
                self.GridRabbits_ScrollArea.addWidget(image_frame, row, col)
            elif(SelectedPath == "Cages"):
                self.GridCages_ScrollArea.addWidget(image_frame, row, col)

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Data Base Importer ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def StartingMethode(self):

        pixmap = QPixmap(self.Avatar).scaled(536,767, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.Facture_Label.setPixmap(pixmap)
        self.Facture_Label.setAlignment(Qt.AlignCenter)

        self.ID_Label.setText(f"ID  :  {str(self.ID)}")
        self.Customer_ID_Label.setText(f"ID  :  {str(self.Data[0])}")
        self.Customer_Name_Label.setText(self.Data[1])
        self.Customer_Phone_Label.setText(self.Data[2])
        self.Customer_Gender_Label.setText(self.Data[4])
        self.Customer_Address_Label.setText(self.Data[3])

        self.ImagesGrid(getDBData("ID,Breed,Gender","rabbits","Gender","FactureID",self.ID),"Rabbits",self,1)
        self.ImagesGrid(getDBData("ID,Bought,Gender","cages","Gender","FactureID",self.ID),"Cages",self,1)


    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Initialize The Window ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def __init__(self,ID,Avatar,Data,mainCustomer,mainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Facture Details") #Title OF The Application
        self.setWindowIcon(QIcon(":/Icons/Logo.png")) #Icon In The Top Of The Application
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.mainWindow = mainWindow
        self.Data = Data
        self.ID = ID
        self.Avatar = Avatar
        self.mainCustomer = mainCustomer

        self.StartingMethode()

        #----------------------------#
        #Menu Buttons Fonctions
        #----------------------------#
        self.Delete_Facture.clicked.connect(self.DeleteButton_Clicked)
        #----------------------------#

    def DeleteButton_Clicked(self):
        message = QMessageBox.question(self,'Confirmation','Are You Sure You Want To Delete [ '+str(self.ID)+' ]?',QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if (message == QMessageBox.StandardButton.Yes):
            DeleteDBData("factures",'ID',self.ID)
            if(self.mainCustomer != "AlreadyCurrent"):
                self.mainCustomer.FactureCustomer_Widgets_Reload()
            else :
                self.mainWindow.Facture_Widgets_Reload()
            self.close()
            with sqlite3.connect("ElevageInfos.db") as connection:
                connection.cursor().execute(f"UPDATE rabbits SET CustomerID = NULL,FactureID = NULL,Sold=0 WHERE FactureID = ?", (self.ID,))
                connection.commit()
                
            with sqlite3.connect("ElevageInfos.db") as connection:
                connection.cursor().execute(f"UPDATE cages SET CustomerID = NULL,FactureID = NULL,Sold=0 WHERE FactureID = ?", (self.ID,))
                connection.commit()