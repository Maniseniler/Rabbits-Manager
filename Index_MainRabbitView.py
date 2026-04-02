#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Importations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

#All PySide6 Importation :
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog,QTableWidgetItem,QTreeWidgetItem,QMessageBox
from PySide6.QtGui import QIcon,QColor,QPixmap

#Other Importation Of Packages :
import sqlite3
from pathlib import Path
import os
from datetime import datetime

#Importation Of Interfaces :
from InterfacesPY import Ui_Rabbit_View_Main 

#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Get Specifique informations From Data Bases ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

def getDBData(Importation,DBName,genderFilter,FilterBy,Search,OrdreButtonChecked):
    DECR = "ORDER BY ID DESC"
    CR = "ORDER BY ID ASC"
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()
        if(DBName == "customers" or DBName == "rabbits"):
            query = f"SELECT {Importation} FROM {DBName} WHERE ('{genderFilter}' = 'Gender' OR Gender = '{genderFilter}')"
            if(FilterBy != 'By'):
                query = f"SELECT {Importation} FROM {DBName} WHERE ('{genderFilter}' = 'Gender' OR Gender = '{genderFilter}') AND ({FilterBy} LIKE '%{Search}%')"
        elif (DBName == "factures"):
            query = f"SELECT {Importation} FROM {DBName} WHERE CustomerID = '{genderFilter}' OR  '{genderFilter}' = 'CustomerID'"
            if(FilterBy != 'By'):
                query = f"SELECT {Importation} FROM {DBName} WHERE (CustomerID = '{genderFilter}' OR  '{genderFilter}' = 'CustomerID') AND ({FilterBy} LIKE '%{Search}%')"

        if(OrdreButtonChecked):
            query += CR
        else :
            query += DECR

        cursor.execute(query)
        Data = cursor.fetchall()
    return Data

def Age_Calculated(Year,Month,Day):
    Age_Year = datetime.today().year - Year
    Age_Month = datetime.today().month - Month
    Age_Day = datetime.today().day - Day
    Msg = ""
    if(Age_Year==0 and Age_Month==0 and Age_Day==0):
        Msg = "New Born"
    else :
        if(Age_Year!=0):
            Msg += f"{Age_Year} Year"
        if(Age_Month!=0):
            Msg += f"{Age_Month} Month"
        if(Age_Day!=0):
            Msg += f"{Age_Day} Day"
    return Msg
    
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

def DeleteDBData(DBName,FilterBy,Search):
    with sqlite3.connect("ElevageInfos.db") as connection:
        connection.execute("PRAGMA journal_mode=WAL;")
        connection.cursor().execute(f"DELETE FROM {DBName} WHERE {FilterBy} = ?", (Search,))
        connection.commit()
#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ AddC Window Class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

class mainRabbitView(QDialog,Ui_Rabbit_View_Main):

    def Reload_Avatar(self):
        pixmap = QPixmap(Find_Image_SelectedView("Rabbits",self.Data[0])).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.Rabbit_Avatar_Label.setPixmap(pixmap)
        self.Rabbit_Avatar_Label.setAlignment(Qt.AlignCenter)
    
    def GetBunniesInfo(self,ID):
        yearFilter = int(self.YearSelection_Rabbit.currentText())

        with sqlite3.connect("ElevageInfos.db") as connection:
            cursor = connection.cursor()
            query = f"SELECT ID,Gender,Born FROM rabbits WHERE Mother = '{ID}'"
            cursor.execute(query)
            Data = cursor.fetchall()

        Months = {i: [] for i in range(1, 13)}
        i=0
        Bunnies=0
        for Information in Data:
            Color = {"Male": QColor(0, 140, 179), "Female": QColor(199, 0, 217),"Null": QColor(182, 155, 0)}.get(Information[1], QColor(0, 104, 104))
            Month, year = int(Information[2][:2]), int(Information[2][6:])
            if year == yearFilter and 1 <= Month <= 12:
                Months[Month].append([Information[0],Color])
                Bunnies+=1
            i+=1
        
        self.Rabbit_Total_Bunnies_Label.setText("Total : "+str(Bunnies))
        
        self.LoadData(self.Rabbit_Detail_Table_1,Months[1])
        self.LoadData(self.Rabbit_Detail_Table_2,Months[2])
        self.LoadData(self.Rabbit_Detail_Table_3,Months[3])
        self.LoadData(self.Rabbit_Detail_Table_4,Months[4])
        self.LoadData(self.Rabbit_Detail_Table_5,Months[5])
        self.LoadData(self.Rabbit_Detail_Table_6,Months[6])
        self.LoadData(self.Rabbit_Detail_Table_7,Months[7])
        self.LoadData(self.Rabbit_Detail_Table_8,Months[8])
        self.LoadData(self.Rabbit_Detail_Table_9,Months[9])
        self.LoadData(self.Rabbit_Detail_Table_10,Months[10])
        self.LoadData(self.Rabbit_Detail_Table_11,Months[11])
        self.LoadData(self.Rabbit_Detail_Table_12,Months[12])
    
    def LoadData(self,Table,Data):
        Table.setRowCount(0)
        count = 0
        if(len(Data)):
            Table.insertRow(count)
            item = QTableWidgetItem(f"T : {str(len(Data))}",)
            item.setTextAlignment(Qt.AlignCenter)
            Table.setItem(count,0,item)
            Table.setRowHeight(count,20)
            Table.item(count, 0).setBackground(QColor(185, 175, 255))
            count+=1
        for ID,Color in Data:
            Table.insertRow(count)
            item = QTableWidgetItem(str(ID),)
            item.setTextAlignment(Qt.AlignCenter)
            Table.setItem(count,0,item)
            Table.setRowHeight(count,20)
            Table.item(count, 0).setBackground(Color)
            count+=1


    def Remize_Zero_Detailed_Tree(self):
        self.Rabbit_Detail_Tree.clear()
        self.Rabbit_Detail_Tree.addTopLevelItem(QTreeWidgetItem(["Siblings"]))
        self.Rabbit_Detail_Tree.topLevelItem(0).setBackground(0, QColor("#005b2c"))
        self.Rabbit_Detail_Tree.addTopLevelItem(QTreeWidgetItem(["Bunnies"]))
        self.Rabbit_Detail_Tree.topLevelItem(1).setBackground(0, QColor("#635c00"))       
        
    def load_data_Siblings(self):

        with sqlite3.connect("ElevageInfos.db") as connection:
            cursor = connection.cursor()
            query = f"SELECT ID,Born,Mother,Father FROM rabbits WHERE ((Mother = '{self.Data[6]}' OR Father = '{self.Data[5]}') AND ID != '{self.Data[0]}')"
            cursor.execute(query)
            Siblings = cursor.fetchall()


        with sqlite3.connect("ElevageInfos.db") as connection:
            cursor = connection.cursor()
            query = f"SELECT Gender FROM rabbits WHERE ((Mother = '{self.Data[6]}' OR Father = '{self.Data[5]}') AND ID != '{self.Data[0]}')"
            cursor.execute(query)
            SiblingsGender = cursor.fetchall()
        
        for i in range(len(Siblings)):
            Siblings_Color = QColor(0, 104, 104)
            if(SiblingsGender[i][0] == "Male"):
                Siblings_Color = QColor(0, 140, 179)
            elif(SiblingsGender[i][0] != "Female"):
                Siblings_Color = QColor(199, 0, 217)
            elif(SiblingsGender[i][0] != "Null"):
                Siblings_Color = QColor(182, 155, 0)
            self.Rabbit_Detail_Tree.topLevelItem(0).addChild(QTreeWidgetItem(tuple(map(str, Siblings[i]))))
            if (Siblings_Color.isValid()):
                for col in range(self.Rabbit_Detail_Tree.columnCount()):
                    self.Rabbit_Detail_Tree.topLevelItem(0).child(i).setBackground(col, Siblings_Color)
        self.Rabbit_Detail_Tree.expandAll()

        return len(Siblings)
    
    def load_data_Bunnies(self):
        with sqlite3.connect("ElevageInfos.db") as connection:
            cursor = connection.cursor()
            query = f"SELECT ID,Born,Mother,Father FROM rabbits WHERE Mother = '{self.Data[0]}' OR Father = '{self.Data[0]}'"
            cursor.execute(query)
            Bunnies = cursor.fetchall()

        with sqlite3.connect("ElevageInfos.db") as connection:
            cursor = connection.cursor()
            query = f"SELECT Gender FROM rabbits WHERE Mother = '{self.Data[0]}' OR Father = '{self.Data[0]}'"
            cursor.execute(query)
            BunniesGender = cursor.fetchall()

        for i in range(len(Bunnies)):
            Bunnies_Color = QColor(0, 104, 104)
            if(BunniesGender[i][0] == "Male"):
                Bunnies_Color = QColor(0, 140, 179)
            elif(BunniesGender[i][0] != "Female"):
                Bunnies_Color = QColor(199, 0, 217)
            elif(BunniesGender[i][0] != "Null"):
                Bunnies_Color = QColor(182, 155, 0)

            self.Rabbit_Detail_Tree.topLevelItem(1).addChild(QTreeWidgetItem(tuple(map(str, Bunnies[i]))))
            if (Bunnies_Color.isValid()):
                for col in range(self.Rabbit_Detail_Tree.columnCount()):
                    self.Rabbit_Detail_Tree.topLevelItem(1).child(i).setBackground(col, Bunnies_Color)
        self.Rabbit_Detail_Tree.expandAll()

        return len(Bunnies)

    def ReloadInformations(self):

        with sqlite3.connect("ElevageInfos.db") as connection:
            cursor = connection.cursor()
            query = f"SELECT ID,Breed,Born,Color,Gender,Father,Mother,Generation,CageID,Type,Bought,FactureID,CustomerID,Sold,Notes FROM rabbits WHERE ID = '{self.ID}'"
            cursor.execute(query)
            self.Data = cursor.fetchall()[0]

        self.ID_Label.setText("ID : "+str(self.Data[0]))
        self.Reload_Avatar()
        self.Rabbit_Breed_Label.setText("Breed : "+str(self.Data[1]))

        Born = self.Data[2]
        self.Rabbit_Born_Label.setText("Born : "+str(Born))
        self.Rabbit_Age_Label.setText("Age : "+Age_Calculated(int(Born[6:]),int(Born[0:2]),int(Born[3:5])))

        self.Rabbit_Color_Label.setText("Color : "+str(self.Data[3]))
        self.Rabbit_Gender_Label.setText("Gender : "+str(self.Data[4]))
        if(str(self.Data[4]) == "Female"):
            self.Male_Info_Frame.hide()
            self.GetBunniesInfo(self.Data[0])
        else :
            self.Breeding_Info_Frame.hide()
        self.Rabbit_Father_Label.setText("Father : "+str(self.Data[5]))
        self.Rabbit_Mother_Label.setText("Mother : "+str(self.Data[6]))
        self.Rabbit_Generation_Label.setText("Generation : "+str(self.Data[7]))
        self.Rabbit_Cage_Label.setText("Cage : "+str(self.Data[8]))
        self.Rabbit_Type_Label.setText("Type : "+str(self.Data[9]))
        self.Rabbit_Bought_Label.setText("Bought : "+str(self.Data[10])+" TND")


        if(self.Data[11] != None):
            self.Rabbit_Facture_Label.setText("Facture : "+str(self.Data[11]))
            self.Rabbit_Customer_Label.setText("Customer : "+str(self.Data[12]))
            self.Rabbit_Sold_Label.setText("Sold : "+str(self.Data[13])+" TND")
            self.Rabbit_Status_Label.setText("Sold Out")
            self.Rabbit_Status_Label.setStyleSheet("border: none;background-color: rgba(0, 0, 0, 0);font: 75 13pt 'Acme';color:rgb(170, 0, 0);")
        else :
            self.Facture_Frame.hide()
            self.Customer_Frame.hide()
            self.Sold_Frame.hide()
            self.General_Info_Frame.setFixedHeight(630)
            self.Notes_Frame.move(30,690)
            self.Breeding_Info_Frame.move(310,50)
            self.Male_Info_Frame.move(310,50)
            if(str(self.Data[12]) == "0"):
                self.Rabbit_Status_Label.setText("Owned")
                self.Rabbit_Status_Label.setStyleSheet("border: none;background-color: rgba(0, 0, 0, 0);font: 75 13pt 'Acme';color:rgb(0, 170, 255)")
            elif(str(self.Data[12]) == "-1"):
                self.Rabbit_Status_Label.setText("Dead")
                self.Rabbit_Status_Label.setStyleSheet("border: none;background-color: rgba(0, 0, 0, 0);font: 75 13pt 'Acme';color:rgb(234, 66, 0);")
            elif(self.Data[12] is None):
                self.Rabbit_Status_Label.setText("Disponible")
                self.Rabbit_Status_Label.setStyleSheet("border: none;background-color: rgba(0, 0, 0, 0);font: 75 13pt 'Acme';color:rgb(85, 255, 127);")
        
        self.Rabbit_Notes_PleinText.setPlainText(str(self.Data[14]))

       #----------------------------#
        #Menu Buttons Fonctions
        #----------------------------#
        self.Rabbit_Detail_Tree.setColumnWidth(0,80) # Customer Advanced ID
        self.Rabbit_Detail_Tree.setColumnWidth(1,100)   # Customer Advanced Born
        self.Rabbit_Detail_Tree.setColumnWidth(2,80)   # Customer Advanced Mother
        self.Rabbit_Detail_Tree.setColumnWidth(3,80)   # Customer Advanced Father
        #----------------------------#
            
        self.Rabbit_Siblings_Label.setText("Siblings : "+str(self.load_data_Siblings()))
        self.Rabbit_Bunnies_Label.setText("Bunnies : "+str(self.load_data_Bunnies()))

        with sqlite3.connect("ElevageInfos.db") as connection:
            AllSonsRabbits = len(connection.cursor().execute(f"SELECT ID FROM rabbits WHERE Mother={self.Data[0]} OR Father ={self.Data[0]} OR (ID={self.Data[0]} AND (FactureID NOT NULL OR CustomerID NOT NULL))").fetchall())

        if(AllSonsRabbits > 0):
            self.Delete_Rabbit.setEnabled(False)
            self.Delete_Rabbit.setStyleSheet("QPushButton {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Pink_Locked.png);}")
        else :
            self.Delete_Rabbit.setEnabled(True)
            self.Delete_Rabbit.setStyleSheet("QPushButton {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Pink.png);}QPushButton:hover {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Mix.png);}QPushButton:pressed {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_White.png);}")



        self.Rabbit_Notes_PleinText.setPlainText(str(self.Data[14]))

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Initialize The Window ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def __init__(self,Avatar,Data,mainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Rabbit View") #Title OF The Application
        self.setWindowIcon(QIcon(":/Icons/Logo.png")) #Icon In The Top Of The Application
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.mainWindow = mainWindow
        self.Avatar = Avatar
        self.ID = Data[0]

        

        self.ReloadInformations()
        
        self.YearSelection_Rabbit.currentIndexChanged.connect(lambda : self.GetBunniesInfo(self.Data[0]))
        self.Delete_Rabbit.clicked.connect(self.DeleteButton_Clicked)
        self.Edit_Rabbit.clicked.connect(self.EditButton_Clicked)
    
    def DeleteButton_Clicked(self):
        message = QMessageBox.question(self,'Confirmation','Are You Sure You Want To Delete [ '+str(self.Data[0])+' ]?',QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if (message == QMessageBox.StandardButton.Yes):
            DeleteDBData("rabbits",'ID',self.Data[0])
            self.mainWindow.Rabbits_Widgets_Reload()
            self.mainWindow.Exportation_RabbitsView_Info.setText(f"Rabbit ID [ {str(self.Data[0])} ] Deleted Successfully")
            self.mainWindow.Exportation_RabbitsAdvanced_Info.setText(f"Rabbit ID [ {str(self.Data[0])} ] Deleted Successfully")
            self.close()

    def EditButton_Clicked(self):
        from Index_MainAddEditRabbit import mainEditRabbit
        mainWindow_Geometry = self.mainWindow.geometry()
        mainRabbitTreeWindow = mainEditRabbit(self.Data[0],self.mainWindow)
        Right = mainWindow_Geometry.x() + 241 + 265
        Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainRabbitTreeWindow.height()) // 2 )
        mainRabbitTreeWindow.move(Right, Centre)
        mainRabbitTreeWindow.exec()
        self.mainWindow.Exportation_RabbitsView_Info.setText(f"Rabbit ID [ {str(self.Data[0])} ] Edited Successfully")
        self.mainWindow.Exportation_RabbitsAdvanced_Info.setText(f"Rabbit ID [ {str(self.Data[0])} ] Edited Successfully")
        self.ReloadInformations()
        self.Reload_Avatar()

        




