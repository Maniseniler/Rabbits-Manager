#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Importations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

#All PySide6 Importation :
from PySide6.QtCore import Qt,QDate
from PySide6.QtWidgets import QDialog,QFileDialog
from PySide6.QtGui import QIcon,QPixmap

#Other Importation Of Packages :
import sqlite3
from pathlib import Path
import os
import shutil
from datetime import datetime

#Importation Of Interfaces :
from InterfacesPY import Ui_AddRabbitr_Main 
from InterfacesPY import Ui_EditRabbit_Main 

#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Fonctions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

def ExistCage(ID):
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT ID FROM cages WHERE ID = ?", (ID,))
        existing_id = cursor.fetchone()
    return existing_id

def ExistRabbit(ID):
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM rabbits WHERE ID = ?", (ID,))
        existing_id = cursor.fetchone()
    return existing_id

def IdGender(ID,GENDER):
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT ID FROM rabbits WHERE ID = ? AND Gender = ?", (ID, GENDER))
        existing_id = cursor.fetchone()
    return existing_id

def IdGeneration(ID):
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT Generation FROM rabbits WHERE ID = ?", (ID,))
        existing_id = cursor.fetchone()
    return existing_id

def Date_Regulator(Date):
    Month = Date[0:Date.find("/")]
    Date = Date[Date.find("/")+1::]
    Day = Date[0:Date.find("/")]
    Year = Date[Date.find("/")+1::]
    if(len(Month)<2):
        Month="0"+Month
    if(len(Day)<2):
        Day="0"+Day
    return Month+"/"+Day+"/"+Year

def VerifBreed(self,Title):
    self.Rabbit_Title.setText(Title)
    i = 0
    Name = self.Breed_Input.text()
    Msg = "The Name is Correct"
    if(len(Name) > 0 and Name.find("  ") == -1):
        while (i<len(Name) and ("A" <= Name[i].upper() <= "Z" or Name[i]==" ")):
            i+=1
        if(i != len(Name)):
            Msg="Must Be All Alphabetic"
    else :
        Msg="Name Contains One Separating Space"
    self.Breed_Infos.setText(Msg)
    return (i == len(Name) and len(Name) > 0)

def verifFemaleID(self,Title):
    self.Rabbit_Title.setText(Title)
    MotherID = self.Mother_Input.text()
    if(MotherID == "0"):
        return True
    Msg = "The ID is Correct"
    i=0
    if(len(MotherID) > 0 and MotherID.find(" ") == -1):
        while (i<len(MotherID) and ("0" <= MotherID[i] <= "9")):
            i+=1
        if(i != len(MotherID)):
            Msg="Must Be All Numeric"
        elif(ExistRabbit(MotherID) == None):
            Msg="ID Not Found"
        elif(IdGender(MotherID,"Female") == None):
            Msg = "ID Of a Null or a Male Rabbit"

    else :
        Msg="ID Contains 0 Separating Space"
    self.Mother_Infos.setText(Msg)
    return ((len(MotherID) == 0) or (len(MotherID)>0 and i == len(MotherID) and ExistRabbit(MotherID) != None and IdGender(MotherID,"Female") != None))

def verifMaleID(self,Title):
    self.Rabbit_Title.setText(Title)
    FatherID = self.Father_Input.text()
    if(FatherID == "0"):
        return True
    Msg = "The ID is Correct"
    i=0
    if(len(FatherID) > 0 and FatherID.find(" ") == -1):
        while (i<len(FatherID) and ("0" <= FatherID[i] <= "9")):
            i+=1
        if(i != len(FatherID)):
            Msg="Must Be All Numeric"
        elif(ExistRabbit(FatherID) == None):
            Msg="ID Not Found"
        elif(IdGender(FatherID,"Male") == None):
            Msg = "ID Of a Null or a Female Rabbit"

    else :
        Msg="ID Contains 0 Separating Space"
    self.Father_Infos.setText(Msg)
    return ((len(FatherID) == 0) or (len(FatherID)>0 and i == len(FatherID) and ExistRabbit(FatherID) != None and IdGender(FatherID,"Male") != None))

def VerifColor(self,Title):
    self.Rabbit_Title.setText(Title)
    i = 0
    Color = self.Color_Input.text()
    Msg = "The Name is Correct"
    if(len(Color) > 0 and Color.find("  ") == -1):
        while (i<len(Color) and ("A" <= Color[i].upper() <= "Z" or Color[i]==" ")):
            i+=1
        if(i != len(Color)):
            Msg="Must Be All Alphabetic"
    else :
        Msg="Name Contains One Separating Space"
    self.Color_Infos.setText(Msg)
    return (len(Color) > 0 and i == len(Color))

def verifCageID(self,Title):
    self.Rabbit_Title.setText(Title)
    CageID = self.Cage_Input.text()
    Msg = "The ID is Correct"
    i=0
    if(len(CageID) > 0 and CageID.find(" ") == -1):
        while (i<len(CageID) and ("0" <= CageID[i] <= "9")):
            i+=1
        if(i != len(CageID)):
            Msg="Must Be All Numeric"
        elif(ExistCage(CageID) == None):
            Msg="ID Not Found"
    else :
        Msg="ID Contains 0 Separating Space"
    self.Cage_Infos.setText(Msg)
    return (len(CageID)>0 and i == len(CageID) and ExistCage(CageID) != None)

def verifBorn(self,Title):
    self.Rabbit_Title.setText(Title)
    TodayTime=datetime.today().strftime("%m/%d/%Y")
    day=TodayTime[3:5]
    month=TodayTime[0:2]
    year=TodayTime[6:]

    Born = self.Born_Input.text()
    Born = Date_Regulator(Born)
    Verif = True
    Msg = "The Date is Correct"
    if(int(year)<int(Born[6:])):
        Verif = False
        Msg="Year Must Be ≤ "+year
    elif(int(year)==int(Born[6:]) and int(month)<int(Born[0:2])):
        Verif = False
        Msg="Month Must Be ≤ "+month
    elif(int(year)==int(Born[6:]) and int(month)==int(Born[0:2]) and int(day)< int(Born[3:5]) ):
        Verif = False
        Msg="Day Must Be ≤ "+day
    
    self.Born_Infos.setText(Msg)
    return Verif

def VerifGender(self,Title):
    self.Rabbit_Title.setText(Title)
    Gender = self.Gender_Input.currentText()
    match Gender :
        case "Null": self.Gender_Infos.setText("You Choose Null")
        case "Male": self.Gender_Infos.setText("You Choose Male")
        case "Female": self.Gender_Infos.setText("You Choose Female")
    return True

def VerifType(self,Title):
    self.Rabbit_Title.setText(Title)
    Type = self.Type_Input.currentText()
    match Type :
        case "Meat": self.Type_Infos.setText("You Choose Meat")
        case "Breeding": self.Type_Infos.setText("You Choose Breeding")
    return True


    
def SelectAvatar(self):
    FileDialog = QFileDialog()
    FileDialog.setWindowIcon(QIcon(":/Icons/Logo.png"))
    FilePath, _ = FileDialog.getOpenFileName(self, "Select Customer Avatar", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
    if FilePath:
        _, ext = os.path.splitext(FilePath)
        pixmap = QPixmap(FilePath).scaled(111, 151, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.Rabbit_Avatar_Button.setIcon(pixmap)
        self.Rabbit_Avatar_Button.setStyleSheet("QPushButton:hover {border: 3px solid rgb(98, 114, 90);}")
        self.Rabbit_Avatar_Button.setIcon(pixmap)
        self.Rabbit_Avatar_Button.setIconSize(pixmap.size())
        self.Rabbit_Avatar_Button.setFlat(True)
        self.Rabbit_Avatar_Button.setText("")
        appdata_path = os.getenv("APPDATA")  # Gets the %appdata% folder path
        if appdata_path is None:
            raise EnvironmentError("APPDATA environment variable is not set.")
        AvatarsFolder = Path(appdata_path) / "Rabbits_Manager" / "Rabbits"
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

class mainAddRabbit(QDialog,Ui_AddRabbitr_Main):

    def AddRabbit(self):
        if(VerifType(self,"Add A New Rabbit") and VerifGender(self,"Add A New Rabbit") and VerifBreed(self,"Add A New Rabbit") and verifFemaleID(self,"Add A New Rabbit") and verifMaleID(self,"Add A New Rabbit")and VerifColor(self,"Add A New Rabbit")and verifCageID(self,"Add A New Rabbit")and verifBorn(self,"Add A New Rabbit")):
            
            Mother = self.Mother_Input.text()
            if(Mother == "0"):
                Mother = None
            else:
                Mother = int(Mother)
            Father = self.Father_Input.text()
            
            if(Father == "0"):
                Father = None
            else:
                Father = int(Father)

            if((Mother == None)and(Father == None) or (Mother != None)and(Father != None) or (Mother != None)and(Father == None)):
                Breed = self.Breed_Input.text().title()
                Color = self.Color_Input.text().title()
                Born = Date_Regulator(self.Born_Input.text())
                Gender = self.Gender_Input.currentText()
                Type = self.Type_Input.currentText()
                CageID = int(self.Cage_Input.text())
                Bought = float(self.Bought_Input.value())
                Notes = self.Notes_Input.toPlainText()

                Generation = 0
                if((Mother != None)and(Father != None)):
                    GenMother = IdGeneration(Mother)[0]
                    GenFather = IdGeneration(Father)[0]
                
                    if(GenMother == 0 and GenFather == 0):
                        Generation = 1
                    else :
                        Generation = GenMother + GenFather

                with sqlite3.connect("ElevageInfos.db") as connection:
                    sql = "INSERT INTO rabbits (ID, Breed, Mother, Father, Color ,Born,Generation,Gender,Type,CageID,Bought,Notes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
                    val = (self.ID, Breed, Mother, Father, Color, Born,Generation,Gender,Type,CageID,Bought,Notes)
                    connection.cursor().execute(sql, val)
                    connection.commit()
                    

                self.close()
                self.mainWindow.Rabbits_Widgets_Reload()
                self.mainWindow.Exportation_RabbitsAdvanced_Info.setText(f"Rabbit ID [ {str(self.ID)} ] Added Successfully")
                self.mainWindow.Exportation_RabbitsView_Info.setText(f"Rabbit ID [ {str(self.ID)} ] Added Successfully")
            else :
                self.Rabbit_Title.setText("Error Parents")
        else:
            self.Rabbit_Title.setText("Error Missing")

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Initialize The Window ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def __init__(self,mainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Add Rabbit") #Title OF The Application
        self.setWindowIcon(QIcon(":/Icons/Logo.png")) #Icon In The Top Of The Application
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.mainWindow = mainWindow
        with sqlite3.connect("ElevageInfos.db") as connection:
            cursor = connection.cursor()
            query = "SELECT ID FROM rabbits ORDER BY ID DESC LIMIT 1"
            cursor.execute(query)
            Data = cursor.fetchone()

        if Data:
            self.ID = Data[0]+1
        else:
            self.ID = 1

        self.Born_Input.setDate(QDate.fromString(datetime.today().strftime("%Y-%m-%d"),"yyyy-MM-dd"))
        self.ID_Label.setText(f"ID  :  {str(self.ID)}")
        self.Breed_Input.textChanged.connect(lambda:VerifBreed(self,"Add A New Rabbit"))
        self.Mother_Input.textChanged.connect(lambda:verifFemaleID(self,"Add A New Rabbit"))
        self.Father_Input.textChanged.connect(lambda:verifMaleID(self,"Add A New Rabbit"))
        self.Color_Input.textChanged.connect(lambda:VerifColor(self,"Add A New Rabbit"))
        self.Born_Input.dateTimeChanged.connect(lambda:verifBorn(self,"Add A New Rabbit"))
        self.Cage_Input.textChanged.connect(lambda:verifCageID(self,"Add A New Rabbit"))
        self.Gender_Input.currentTextChanged.connect(lambda:VerifGender(self,"Add A New Rabbit"))
        self.Type_Input.currentTextChanged.connect(lambda:VerifType(self,"Add A New Rabbit"))
        self.Rabbit_Avatar_Button.clicked.connect(lambda:SelectAvatar(self))
        self.Add_Rabbit_Button.clicked.connect(lambda:self.AddRabbit())


#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Edit Window Class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

class mainEditRabbit(QDialog,Ui_EditRabbit_Main):
    def EditRabbit(self):
        if(VerifType(self,"Add A New Rabbit") and VerifBreed(self,"Add A New Rabbit") and VerifColor(self,"Add A New Rabbit")and verifCageID(self,"Add A New Rabbit")and verifBorn(self,"Add A New Rabbit")):

            Breed = self.Breed_Input.text().title()
            Color = self.Color_Input.text().title()
            Born = Date_Regulator(self.Born_Input.text())
            Gender = self.Gender_Input.currentText()
            Type = self.Type_Input.currentText()
            CageID = int(self.Cage_Input.text())
            Bought = float(self.Bought_Input.value())
            Notes = self.Notes_Input.toPlainText()

            with sqlite3.connect("ElevageInfos.db") as connection:
                sql = "UPDATE rabbits SET Breed= ?, Color= ? ,Born= ?,Gender= ?,Type= ?,CageID= ?,Bought= ?,Notes= ? WHERE ID = ?"
                val = ( Breed, Color, Born,Gender,Type,CageID,Bought,Notes,self.ID)
                connection.cursor().execute(sql, val)
                connection.commit()
                    

            self.close()
            self.mainWindow.Rabbits_Widgets_Reload()
            self.mainWindow.Exportation_RabbitsAdvanced_Info.setText(f"Rabbit ID [ {str(self.ID)} ] Edited Successfully")
            self.mainWindow.Exportation_RabbitsView_Info.setText(f"Rabbit ID [ {str(self.ID)} ] Edited Successfully")
        else:
            self.Rabbit_Title.setText("Error Missing")


    def load_Rabbit_Info_Into_Dialog(self,Data):
        date_object=QDate.fromString(Data[2],"MM/dd/yyyy")
        
        self.Breed_Input.setText(str(Data[1]))
        self.Born_Input.setDate(date_object)

        Mother = Data[5]
        if(Mother == None):
            Mother = 0
        self.Mother_Input.setValue(Mother)
        self.Mother_Input.setReadOnly(True)

        Father = Data[6]
        if(Father == None):
            Father = 0

        self.Father_Input.setValue(Father)
        self.Father_Input.setReadOnly(True)

        self.Color_Input.setText(str(Data[4]))
        self.Cage_Input.setValue(Data[9])

        self.Gender_Input.setCurrentText(str(Data[3]))
        self.Type_Input.setCurrentText(str(Data[8]))

        self.Bought_Input.setValue(Data[12])

    def __init__(self,ID,mainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Add Rabbit") #Title OF The Application
        self.setWindowIcon(QIcon(":/Icons/Logo.png")) #Icon In The Top Of The Application
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.mainWindow = mainWindow
        self.ID = ID

        appdata_path = os.getenv("APPDATA")  # Gets the %appdata% folder path
        if appdata_path is None:
            raise EnvironmentError("APPDATA environment variable is not set.")
        AvatarsFolder = Path(appdata_path) / "Rabbits_Manager" / "Rabbits"
        AvatarsFolder.mkdir(parents=True, exist_ok=True)
        AvatarFile = ([f for f in os.listdir(AvatarsFolder) if f.startswith(f"{ID}.")])
        if(len(AvatarFile) != 0):
            AvatarFile = AvatarFile[0]
            AvatarFile = os.path.join(AvatarsFolder,AvatarFile)
            pixmap = QPixmap(AvatarFile).scaled(111, 151, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.Rabbit_Avatar_Button.setIcon(pixmap)
            self.Rabbit_Avatar_Button.setStyleSheet("QPushButton:hover {border: 3px solid rgb(98, 114, 90);}")
            self.Rabbit_Avatar_Button.setIcon(pixmap)
            self.Rabbit_Avatar_Button.setIconSize(pixmap.size())
            self.Rabbit_Avatar_Button.setFlat(True)
            self.Rabbit_Avatar_Button.setText("")

        self.load_Rabbit_Info_Into_Dialog(ExistRabbit(self.ID))
        self.ID_Label.setText(f"ID  :  {str(self.ID)}")

        self.Born_Input.setDate(QDate.fromString(datetime.today().strftime("%Y-%m-%d"),"yyyy-MM-dd"))
        self.Breed_Input.textChanged.connect(lambda:VerifBreed(self,"Add A New Rabbit"))
        self.Mother_Input.textChanged.connect(lambda:verifFemaleID(self,"Add A New Rabbit"))
        self.Father_Input.textChanged.connect(lambda:verifMaleID(self,"Add A New Rabbit"))
        self.Color_Input.textChanged.connect(lambda:VerifColor(self,"Add A New Rabbit"))
        self.Born_Input.dateTimeChanged.connect(lambda:verifBorn(self,"Add A New Rabbit"))
        self.Cage_Input.textChanged.connect(lambda:verifCageID(self,"Add A New Rabbit"))
        self.Gender_Input.currentTextChanged.connect(lambda:VerifGender(self,"Add A New Rabbit"))
        self.Type_Input.currentTextChanged.connect(lambda:VerifType(self,"Add A New Rabbit"))
        self.Rabbit_Avatar_Button.clicked.connect(lambda:SelectAvatar(self))
        self.Edit_Rabbit_Button.clicked.connect(lambda:self.EditRabbit())