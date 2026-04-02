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
from InterfacesPY import Ui_Cage_View_Main

#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Creating A DataBase With All The Columns ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

def select_Cage(ID):
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()
        query = f"SELECT * FROM cages WHERE ID = {ID}"
        cursor.execute(query)
        Data = cursor.fetchone()
        connection.commit()
    return Data

def getDBData(Importation,DBName,genderFilter,FilterBy,Search,OrdreButtonChecked,CageID):
    DECR = "ORDER BY ID DESC"
    CR = "ORDER BY ID ASC"
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()

        query = f"SELECT {Importation} FROM {DBName} WHERE ('{genderFilter}' = 'Gender' OR Gender = '{genderFilter}') AND CageID = '{CageID}'"
        if(FilterBy != 'By'):
            query = f"SELECT {Importation} FROM {DBName} WHERE ('{genderFilter}' = 'Gender' OR Gender = '{genderFilter}') AND ({FilterBy} LIKE '%{Search}%') AND CageID = '{CageID}'"

        if(OrdreButtonChecked):
            query += CR
        else :
            query += DECR

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

class mainCage(QDialog,Ui_Cage_View_Main):

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Clear Images ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def clear_images(self):
        while self.GridRabbits_ScrollArea.count():
            child = self.GridRabbits_ScrollArea.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Images Grid ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def ImagesGrid(self,Data,SelectedPath,mainCustomer,Number):
        from Index_MainWindow import ImageFrame
        self.mainCustomer = mainCustomer
        
        self.clear_images()
        self.Cage_Rabbits_ScrollArea.setWidgetResizable(True)
        self.Cage_Rabbits_ScrollArea_Widget.setLayout(self.GridRabbits_ScrollArea)
        self.Cage_Rabbits_ScrollArea.setWidget(self.Cage_Rabbits_ScrollArea_Widget)
        self.GridRabbits_ScrollArea.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.GridRabbits_ScrollArea.setSpacing(33)
        
        for index,Informations in enumerate(Data):
            row = index // Number
            col = index % Number
            ID = Informations[0]
            image_frame = ImageFrame(Find_Image_SelectedView(SelectedPath,ID), f"#{ID}",Informations,self.mainWindow,self,SelectedPath)
            self.GridRabbits_ScrollArea.addWidget(image_frame, row, col)

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Data Base Importer ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    
    def Reload_Avatar(self):
        pixmap = QPixmap(Find_Image_SelectedView("Cages",self.ID)).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.Cage_Avatar_Label.setPixmap(pixmap)
        self.Cage_Avatar_Label.setAlignment(Qt.AlignCenter)

    def ReloadInformations(self):
        self.Data = select_Cage(self.ID)
        self.ID_Label.setText(f"ID  :  {str(self.ID)}")
        self.Cage_Gender_Label.setText(f"Gender : {str(self.Data[1])}")
        self.Cage_Bought_Label.setText(f"Bought : {str(self.Data[2])}")
        self.Cage_Facture_Label.setText(f"Facture : {str(self.Data[3])}")
        self.Cage_Customer_Label.setText(f"Customer : {str(self.Data[4])}")
        self.Cage_Sold_Label.setText(f"{str(self.Data[5])}")
        self.Cage_Notes_PleinText.setPlainText(f"{str(self.Data[6])}")
        if(self.Data[4] is None):
            self.Selled_Frame.hide()
            self.Cage_Gender_Icon.move(20,86)
            self.Cage_Gender_Label.move(50,86)

            self.Cage_Brought_Icon.move(20,121)
            self.Cage_Bought_Label.move(50,121)

    
    def StartingMethode(self):
        self.ReloadInformations()
        self.DeleteButtonCheck()
        pixmap = QPixmap(self.Avatar).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.Cage_Avatar_Label.setPixmap(pixmap)
        self.Cage_Avatar_Label.setAlignment(Qt.AlignCenter)
        #----------------------------#
        #Disable Search Fonctions
        #----------------------------#
        self.Search_Rabbits.setReadOnly(True)
        self.Search_Rabbits.setText("")
        self.Search_Rabbits.setPlaceholderText("Pick Option From The Button [ By ]")
        #----------------------------#

        #----------------------------#
        #Pages Fill Fonctions
        #----------------------------#
        self.RabbitCustomer_Widgets_Reload()
        #----------------------------#



    def DeleteButtonCheck(self):
        with sqlite3.connect("ElevageInfos.db") as connection:
            AllRabbitsInCage = len(connection.cursor().execute(f"SELECT ID FROM rabbits WHERE CageID={self.ID}").fetchall())
            if(AllRabbitsInCage != 0):
                self.Delete_Cage.setEnabled(False)
                self.Delete_Cage.setStyleSheet("QPushButton {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Pink_Locked.png);}")
            else :
                self.Delete_Cage.setEnabled(True)
                self.Delete_Cage.setStyleSheet("QPushButton {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Pink.png);}QPushButton:hover {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Mix.png);}QPushButton:pressed {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_White.png);}")

        

    def RabbitCustomerSearchFilter(self):
        Current_FilterBy = self.FilterBy_Rabbits.currentText()
        self.Search_Rabbits.setReadOnly(True)
        self.Search_Rabbits.setPlaceholderText("Pick Option From The Button [ By ]")
        self.Search_Rabbits.setText("")
        if(Current_FilterBy != "By"):
            self.Search_Rabbits.setReadOnly(False)
            self.Search_Rabbits.setPlaceholderText("Search Rabbit...")
        self.RabbitCustomer_Widgets_Reload

    
    def RabbitCustomer_Widgets_Reload(self):
        Current_FilterGender = self.FilterGender_Rabbits.currentText()
        Current_FilterBy = self.FilterBy_Rabbits.currentText()
        CurrentTextSearch = self.Search_Rabbits.text()
        self.ImagesGrid(getDBData("ID,Breed,Gender","rabbits",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Rabbits.isChecked(),self.ID),"Rabbits",self,5)     

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Initialize The Window ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def __init__(self,Avatar,ID,mainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Cage Details") #Title OF The Application
        self.setWindowIcon(QIcon(":/Icons/Logo.png")) #Icon In The Top Of The Application
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.mainWindow = mainWindow
        self.Avatar = Avatar
        self.ID = ID

        #----------------------------#
        #Menu Buttons Fonctions
        #----------------------------#
        self.Delete_Cage.clicked.connect(self.DeleteButton_Clicked)
        self.Edit_Cage.clicked.connect(self.EditButton_Clicked)
        #----------------------------#

        #----------------------------#
        #Filter Buttons Fonctions
        #----------------------------#
        self.FilterBy_Rabbits.currentIndexChanged.connect(self.RabbitCustomerSearchFilter)
        self.Search_Rabbits.textChanged.connect(self.RabbitCustomer_Widgets_Reload)
        self.Ordre_Rabbits.toggled.connect(self.RabbitCustomer_Widgets_Reload)
        self.FilterGender_Rabbits.currentIndexChanged.connect(self.RabbitCustomer_Widgets_Reload)
        #----------------------------#

        self.StartingMethode()

             

    def DeleteButton_Clicked(self):
        message = QMessageBox.question(self,'Confirmation','Are You Sure You Want To Delete [ '+str(self.ID)+' ]?',QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if (message == QMessageBox.StandardButton.Yes):
            DeleteDBData("cages",'ID',self.ID)
            self.mainWindow.Cages_Widgets_Reload()
            self.mainWindow.Exportation_CagesAdvanced_Info.setText(f"Cage ID [ {str(self.ID)} ] Deleted Successfully")
            self.mainWindow.Exportation_CagesView_Info.setText(f"Cage ID [ {str(self.ID)} ] Deleted Successfully")
            self.close()

    def EditButton_Clicked(self):
        from Index_MainAddEditCages import mainEditCage
        mainWindow_Geometry = self.mainWindow.geometry()
        mainAddCustomerWindow = mainEditCage(self.ID,self.mainWindow)
        Right = mainWindow_Geometry.x() + 241 + 265
        Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainAddCustomerWindow.height()) // 2 ) - 10
        mainAddCustomerWindow.move(Right, Centre)
        mainAddCustomerWindow.exec()
        self.mainWindow.Exportation_CagesAdvanced_Info.setText(f"Cage ID [ {str(self.ID)} ] Edited Successfully")
        self.mainWindow.Exportation_CagesView_Info.setText(f"Cage ID [ {str(self.ID)} ] Edited Successfully")
        self.ReloadInformations()
        self.Reload_Avatar()

    