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
from InterfacesPY import Ui_AddCustomer_Main 
from InterfacesPY import Ui_EditCustomer_Main 

#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Fonctions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

def VerifName(self,Title):
    self.Customer_Title.setText(Title)
    i = 0
    Name = self.Name_Input.text()
    Msg = "The Name is Correct"
    if(len(Name) > 0 and Name.find("  ") == -1):
        while (i<len(Name) and ("A" <= Name[i].upper() <= "Z" or Name[i]==" ")):
            i+=1
        if(i != len(Name)):
            Msg="Must Be All Alphabetic"
    else :
        Msg="Name Contains One Separating Space"
    self.Name_Infos.setText(Msg)
    return (i == len(Name) and len(Name) > 0)
    
def VerifNumber(self,Title):
    self.Customer_Title.setText(Title)
    Phone = self.Phone_Input.text()
    Msg = "Must Contain 8 Digits"
    Verif = False
    if(len(Phone) > 0 and Phone[0] in ('2', '3', '4', '5', '7', '9') and Phone.find(" ") == -1):
        i=1
        while(i<len(Phone) and "0"<= Phone[0]<= "9"):
            i+=1
        if(i==len(Phone)):
            if(len(Phone) == 8):
                Msg = "The Phone Number is Correct"
                Verif = True
        else :
            Msg = "Must Be All Numeric"
    else :
        Msg = "Must Start With (2,3,4,5,9,7)"
    self.Phone_Infos.setText(Msg)
    return Verif
    
def VerifAddress(self,Title):
    self.Customer_Title.setText(Title)
    Address = self.Address_Input.text()
    Msg = "The Address is Correct"
    if(len(Address)==0):
        Msg = "The customer's residential or business address." 
    if(Address.find("  ") != -1):
        Msg="Name Contains One Separating Space"
    self.Address_Infos.setText(Msg)
    return ((Address.find("  ") == -1) and (len(Address)>0))
    
def SelectAvatar(self):
    FileDialog = QFileDialog()
    FileDialog.setWindowIcon(QIcon(":/Icons/Logo.png"))
    FilePath, _ = FileDialog.getOpenFileName(self, "Select Customer Avatar", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
    if FilePath:
        _, ext = os.path.splitext(FilePath)
        pixmap = QPixmap(FilePath).scaled(111, 151, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.Customer_Avatar_Button.setIcon(pixmap)
        self.Customer_Avatar_Button.setStyleSheet("QPushButton:hover {border: 3px solid rgb(98, 114, 90);}")
        self.Customer_Avatar_Button.setIcon(pixmap)
        self.Customer_Avatar_Button.setIconSize(pixmap.size())
        self.Customer_Avatar_Button.setFlat(True)
        self.Customer_Avatar_Button.setText("")
        appdata_path = os.getenv("APPDATA")  # Gets the %appdata% folder path
        if appdata_path is None:
            raise EnvironmentError("APPDATA environment variable is not set.")
        AvatarsFolder = Path(appdata_path) / "Rabbits_Manager" / "Customers"
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

class mainAddCustomer(QDialog,Ui_AddCustomer_Main):

    def AddCustomer(self):
        if((VerifName(self,"Add A New Customer")) and (VerifNumber(self,"Add A New Customer")) and (VerifAddress(self,"Add A New Customer"))):
            Name = self.Name_Input.text().title()
            Phone = self.Phone_Input.text()
            Address = self.Address_Input.text()
            Gender = self.Gender_Input.currentText()
            Notes = self.Notes_Input.toPlainText()

            with sqlite3.connect("ElevageInfos.db") as connection:
                sql = "INSERT INTO customers (ID, Name, Phone, Address, Gender, Notes) VALUES (?, ?, ?, ?, ?, ?)"
                val = (self.ID, Name, Phone, Address, Gender, Notes)
                connection.cursor().execute(sql, val)
                connection.commit()
                

            self.close()
            self.mainWindow.Customers_Widgets_Reload()
            self.mainWindow.Exportation_CustomerAdvanced_Info.setText(f"Customer ID [ {str(self.ID)} ] Added Successfully")
            self.mainWindow.Exportation_CustomerView_Info.setText(f"Customer ID [ {str(self.ID)} ] Added Successfully")
        else:
            self.Customer_Title.setText("Error Missing")

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Initialize The Window ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def __init__(self,mainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Add Customer") #Title OF The Application
        self.setWindowIcon(QIcon(":/Icons/Logo.png")) #Icon In The Top Of The Application
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.mainWindow = mainWindow
        with sqlite3.connect("ElevageInfos.db") as connection:
            cursor = connection.cursor()
            query = "SELECT ID FROM customers ORDER BY ID DESC LIMIT 1"
            cursor.execute(query)
            Data = cursor.fetchone()

        if Data:
            self.ID = Data[0]+1
        else:
            self.ID = 1

            

        self.ID_Label.setText(f"ID  :  {str(self.ID)}")
        self.Name_Input.textChanged.connect(lambda:VerifName(self,"Add A New Customer"))
        self.Phone_Input.textChanged.connect(lambda:VerifNumber(self,"Add A New Customer"))
        self.Address_Input.textChanged.connect(lambda:VerifAddress(self,"Add A New Customer"))
        self.Customer_Avatar_Button.clicked.connect(lambda:SelectAvatar(self))
        self.Add_Customer_Button.clicked.connect(lambda:self.AddCustomer())

#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Edit Window Class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

class mainEditCustomer(QDialog,Ui_EditCustomer_Main):
    def EditCustomer(self):
        if((VerifName(self,"Edit Customer")) and (VerifNumber(self,"Edit Customer")) and (VerifAddress(self,"Edit Customer"))):
            Name = self.Name_Input.text().title()
            Phone = self.Phone_Input.text()
            Address = self.Address_Input.text()
            Gender = self.Gender_Input.currentText()
            Notes = self.Notes_Input.toPlainText()

            with sqlite3.connect("ElevageInfos.db") as connection:
                cursor = connection.cursor()
                sql = "UPDATE customers SET Name = ?, Phone = ?, Address = ?, Gender = ?, Notes = ? WHERE ID = ?"
                val = (Name, Phone, Address, Gender, Notes,self.ID)
                cursor.execute(sql, val)
                connection.commit()
                
            self.close()
            self.mainWindow.Customers_Widgets_Reload()
            self.mainWindow.Exportation_CustomerAdvanced_Info.setText(f"Customer ID [ {str(self.ID)} ] Edited Successfully")
            self.mainWindow.Exportation_CustomerView_Info.setText(f"Customer ID [ {str(self.ID)} ] Edited Successfully")
        else:
            self.Customer_Title.setText("Error Missing")

    def select_Customer(self,ID):
        with sqlite3.connect("ElevageInfos.db") as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM customers WHERE ID = {ID}"
            cursor.execute(query)
            Data = cursor.fetchone()
            
        return Data
    
    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Initialize The Window ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def __init__(self,ID,mainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Edit Customer") #Title OF The Application
        self.setWindowIcon(QIcon(":/Icons/Logo.png")) #Icon In The Top Of The Application
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.mainWindow = mainWindow
        self.ID = ID

        Informations = self.select_Customer(self.ID)
        self.Name_Input.setText(Informations[1])
        self.Phone_Input.setText(Informations[2])
        self.Gender_Input.setCurrentText(Informations[4])
        self.Address_Input.setText(Informations[3])
        self.Notes_Input.setPlainText(Informations[5])

        appdata_path = os.getenv("APPDATA")  # Gets the %appdata% folder path
        if appdata_path is None:
            raise EnvironmentError("APPDATA environment variable is not set.")
        AvatarsFolder = Path(appdata_path) / "Rabbits_Manager" / "Customers"
        AvatarsFolder.mkdir(parents=True, exist_ok=True)
        AvatarFile = ([f for f in os.listdir(AvatarsFolder) if f.startswith(f"{ID}.")])
        if(len(AvatarFile) != 0):
            AvatarFile = AvatarFile[0]
            AvatarFile = os.path.join(AvatarsFolder,AvatarFile)
            pixmap = QPixmap(AvatarFile).scaled(111, 151, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.Customer_Avatar_Button.setIcon(pixmap)
            self.Customer_Avatar_Button.setStyleSheet("QPushButton:hover {border: 3px solid rgb(98, 114, 90);}")
            self.Customer_Avatar_Button.setIcon(pixmap)
            self.Customer_Avatar_Button.setIconSize(pixmap.size())
            self.Customer_Avatar_Button.setFlat(True)
            self.Customer_Avatar_Button.setText("")

        self.ID_Label.setText(f"ID  :  {str(self.ID)}")
        self.Name_Input.textChanged.connect(lambda:VerifName(self,"Edit Customer"))
        self.Phone_Input.textChanged.connect(lambda:VerifNumber(self,"Edit Customer"))
        self.Address_Input.textChanged.connect(lambda:VerifAddress(self,"Edit Customer"))
        self.Customer_Avatar_Button.clicked.connect(lambda:SelectAvatar(self))
        self.Edit_Customer_Button.clicked.connect(lambda:self.EditCustomer())       