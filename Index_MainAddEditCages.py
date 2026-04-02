#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Importations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

#All PySide6 Importation :
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog,QFileDialog
from PySide6.QtGui import QIcon,QPixmap

#Other Importation Of Packages :
import sqlite3
from pathlib import Path
import os
import shutil

#Importation Of Interfaces :
from InterfacesPY import Ui_AddCage_Main 
from InterfacesPY import Ui_EditCage_Main 

#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Fonctions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

def SelectAvatar(self):
    FileDialog = QFileDialog()
    FileDialog.setWindowIcon(QIcon(":/Icons/Logo.png"))
    FilePath, _ = FileDialog.getOpenFileName(self, "Select Customer Avatar", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
    if FilePath:
        _, ext = os.path.splitext(FilePath)
        pixmap = QPixmap(FilePath).scaled(111, 151, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.Cage_Avatar_Button.setIcon(pixmap)
        self.Cage_Avatar_Button.setStyleSheet("QPushButton:hover {border: 3px solid rgb(98, 114, 90);}")
        self.Cage_Avatar_Button.setIcon(pixmap)
        self.Cage_Avatar_Button.setIconSize(pixmap.size())
        self.Cage_Avatar_Button.setFlat(True)
        self.Cage_Avatar_Button.setText("")
        appdata_path = os.getenv("APPDATA")  # Gets the %appdata% folder path
        if appdata_path is None:
            raise EnvironmentError("APPDATA environment variable is not set.")
        AvatarsFolder = Path(appdata_path) / "Rabbits_Manager" / "Cages"
        AvatarsFolder.mkdir(parents=True, exist_ok=True)
        AvatarFile = f"{self.ID}{ext}"
        CopyAvatar = os.path.join(AvatarsFolder, AvatarFile)
        for file in os.listdir(AvatarsFolder):
            if file.startswith(f"{self.ID}."):
                os.remove(os.path.join(AvatarsFolder, file))
        shutil.copy(FilePath, CopyAvatar)

#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ AddC Window Class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

class mainAddCage(QDialog,Ui_AddCage_Main):

    def AddCage(self):
        Bought = float(self.Bought_Input.value())
        Gender = self.Gender_Input.currentText()
        Notes = self.Notes_Input.toPlainText()

        with sqlite3.connect("ElevageInfos.db") as connection:
            sql = "INSERT INTO cages (ID, Bought, Gender, Notes) VALUES (?, ?, ?, ?)"
            val = (self.ID, Bought,Gender, Notes)
            connection.cursor().execute(sql, val)
            connection.commit()
                

        self.close()
        self.mainWindow.Cages_Widgets_Reload()
        self.mainWindow.Exportation_CagesAdvanced_Info.setText(f"Cage ID [ {str(self.ID)} ] Added Successfully")
        self.mainWindow.Exportation_CagesView_Info.setText(f"Cage ID [ {str(self.ID)} ] Added Successfully")

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Initialize The Window ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def __init__(self,mainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Add Cage") #Title OF The Application
        self.setWindowIcon(QIcon(":/Icons/Logo.png")) #Icon In The Top Of The Application
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.mainWindow = mainWindow
        with sqlite3.connect("ElevageInfos.db") as connection:
            cursor = connection.cursor()
            query = "SELECT ID FROM cages ORDER BY ID DESC LIMIT 1"
            cursor.execute(query)
            Data = cursor.fetchone()

        if Data:
            self.ID = Data[0]+1
        else:
            self.ID = 1


        self.ID_Label.setText(f"ID  :  {str(self.ID)}")
        self.Cage_Avatar_Button.clicked.connect(lambda:SelectAvatar(self))
        self.Add_Cage_Button.clicked.connect(lambda:self.AddCage())


#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Edit Window Class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

class mainEditCage(QDialog,Ui_EditCage_Main):

    def EditCage(self):
        Bought = float(self.Bought_Input.value())
        Gender = self.Gender_Input.currentText()
        Notes = self.Notes_Input.toPlainText()

        with sqlite3.connect("ElevageInfos.db") as connection:
            sql = "UPDATE cages SET Bought=? , Gender=?, Notes=? WHERE ID = ?"
            val = (Bought,Gender,Notes,self.ID)
            connection.cursor().execute(sql, val)
            connection.commit()
                

        self.close()
        self.mainWindow.Cages_Widgets_Reload()
        self.mainWindow.Exportation_CagesAdvanced_Info.setText(f"Cage ID [ {str(self.ID)} ] Edited Successfully")
        self.mainWindow.Exportation_CagesView_Info.setText(f"Cage ID [ {str(self.ID)} ] Edited Successfully")

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Initialize The Window ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def __init__(self,ID,mainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Edit Cage") #Title OF The Application
        self.setWindowIcon(QIcon(":/Icons/Logo.png")) #Icon In The Top Of The Application
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.mainWindow = mainWindow
        self.ID = ID

        with sqlite3.connect("ElevageInfos.db") as connection:
            cursor = connection.cursor()
            query = f"SELECT Bought,Gender,Notes FROM cages WHERE ID={self.ID}"
            cursor.execute(query)
            Data = cursor.fetchone()

        appdata_path = os.getenv("APPDATA")  # Gets the %appdata% folder path
        if appdata_path is None:
            raise EnvironmentError("APPDATA environment variable is not set.")
        AvatarsFolder = Path(appdata_path) / "Rabbits_Manager" / "Cages"
        AvatarsFolder.mkdir(parents=True, exist_ok=True)
        AvatarFile = ([f for f in os.listdir(AvatarsFolder) if f.startswith(f"{ID}.")])
        if(len(AvatarFile) != 0):
            AvatarFile = AvatarFile[0]
            AvatarFile = os.path.join(AvatarsFolder,AvatarFile)
            pixmap = QPixmap(AvatarFile).scaled(111, 151, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.Cage_Avatar_Button.setIcon(pixmap)
            self.Cage_Avatar_Button.setStyleSheet("QPushButton:hover {border: 3px solid rgb(98, 114, 90);}")
            self.Cage_Avatar_Button.setIcon(pixmap)
            self.Cage_Avatar_Button.setIconSize(pixmap.size())
            self.Cage_Avatar_Button.setFlat(True)
            self.Cage_Avatar_Button.setText("")

        self.ID_Label.setText(f"ID  :  {str(self.ID)}")
        self.Bought_Input.setValue(Data[0])    
        self.Gender_Input.setCurrentText(str(Data[1]))      
        self.Notes_Input.setPlainText(str(Data[2]))      

        self.Cage_Avatar_Button.clicked.connect(lambda:SelectAvatar(self))
        self.Edit_Cage_Button.clicked.connect(lambda:self.EditCage())