#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Importations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

#All PySide6 Importation :
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog,QTableWidgetItem,QFileDialog,QMessageBox
from PySide6.QtGui import QIcon,QPixmap

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
from InterfacesPY import Ui_Customer_View_Main

#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Creating A DataBase With All The Columns ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

def select_Customer(ID):
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()
        query = f"SELECT * FROM customers WHERE ID = {ID}"
        cursor.execute(query)
        Data = cursor.fetchone()
        connection.commit()
    return Data

def getDBData(Importation,DBName,genderFilter,FilterBy,Search,OrdreButtonChecked,CustomerID):
    DECR = "ORDER BY ID DESC"
    CR = "ORDER BY ID ASC"
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()
        if(DBName == "customers" or DBName == "rabbits" or DBName == "cages"):
            if(CustomerID != 0):
                query = f"SELECT {Importation} FROM {DBName} WHERE ('{genderFilter}' = 'Gender' OR Gender = '{genderFilter}') AND CustomerID = '{CustomerID}'"
                if(FilterBy != 'By'):
                    query = f"SELECT {Importation} FROM {DBName} WHERE ('{genderFilter}' = 'Gender' OR Gender = '{genderFilter}') AND ({FilterBy} LIKE '%{Search}%') AND CustomerID = '{CustomerID}'"
            else :
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

class mainCustomer(QDialog,Ui_Customer_View_Main):

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Clear Images ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def clear_images(self,Current):
        if(Current == "Factures/PNG"):
            while self.GridLayout_Customer_Facture_View.count():
                child = self.GridLayout_Customer_Facture_View.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
        elif(Current == "Rabbits"):
            while self.GridLayout_Customer_Rabbits_FactureView.count():
                child = self.GridLayout_Customer_Rabbits_FactureView.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
        elif(Current == "Cages"):
            while self.GridLayout_Customer_Cages_View.count():
                child = self.GridLayout_Customer_Cages_View.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
        

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Images Grid ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def ImagesGrid(self,Data,SelectedPath,mainCustomer,Number):
        from Index_MainWindow import ImageFrame
        self.mainCustomer = mainCustomer
        if(SelectedPath == "Factures/PNG"):
            self.clear_images(SelectedPath)
            self.Customer_FactureScrollBar.setWidgetResizable(True)
            self.SrollWidget_CustomerFactureScrollBar.setLayout(self.GridLayout_Customer_Facture_View)
            self.Customer_FactureScrollBar.setWidget(self.SrollWidget_CustomerFactureScrollBar)
            self.GridLayout_Customer_Facture_View.setAlignment(Qt.AlignTop | Qt.AlignCenter)
            self.GridLayout_Customer_Facture_View.setSpacing(33)
        
        elif(SelectedPath == "Rabbits"):
            self.clear_images(SelectedPath)
            self.Customer_Rabbits_FactureScrollBar.setWidgetResizable(True)
            self.Customer_Rabbits_FactureScrollBar_Content_7.setLayout(self.GridLayout_Customer_Rabbits_FactureView)
            self.Customer_Rabbits_FactureScrollBar.setWidget(self.Customer_Rabbits_FactureScrollBar_Content_7)
            self.GridLayout_Customer_Rabbits_FactureView.setAlignment(Qt.AlignTop | Qt.AlignCenter)
            self.GridLayout_Customer_Rabbits_FactureView.setSpacing(33)
        
        elif(SelectedPath == "Cages"):
            self.clear_images(SelectedPath)
            self.Customer_CagesScrollBar.setWidgetResizable(True)
            self.Customer_CagesScrollBar_Content.setLayout(self.GridLayout_Customer_Cages_View)
            self.Customer_CagesScrollBar.setWidget(self.Customer_CagesScrollBar_Content)
            self.GridLayout_Customer_Cages_View.setAlignment(Qt.AlignTop | Qt.AlignCenter)
            self.GridLayout_Customer_Cages_View.setSpacing(33)
        
        for index,Informations in enumerate(Data):
            row = index // Number
            col = index % Number
            ID = Informations[0]
            image_frame = ImageFrame(Find_Image_SelectedView(SelectedPath,ID), f"#{ID}",Informations,self.mainWindow,self,SelectedPath)

            if(SelectedPath == "Factures/PNG"):
                self.GridLayout_Customer_Facture_View.addWidget(image_frame, row, col)
            elif(SelectedPath == "Rabbits"):
                self.GridLayout_Customer_Rabbits_FactureView.addWidget(image_frame, row, col)
            elif(SelectedPath == "Cages"):
                self.GridLayout_Customer_Cages_View.addWidget(image_frame, row, col)

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Data Base Importer ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    
    def Reload_Avatar(self):
        pixmap = QPixmap(Find_Image_SelectedView("Customers",self.Data[0])).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.Customer_Avatar_Label.setPixmap(pixmap)
        self.Customer_Avatar_Label.setAlignment(Qt.AlignCenter)
    def ReloadInformations(self):
        self.Data = select_Customer(self.Data[0])
        self.ID_Label.setText(f"ID  :  {str(self.Data[0])}")
        self.Customer_Name_Label.setText(self.Data[1])
        self.Customer_Phone_Label.setText(self.Data[2])
        self.Customer_Gender_Label.setText(self.Data[4])
        self.Customer_Address_Label.setText(self.Data[3])
        self.Customer_Notes_PleinText.setPlainText(self.Data[5])
    
    def StartingMethode(self):
        self.ReloadInformations()
        pixmap = QPixmap(self.Avatar).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.Customer_Avatar_Label.setPixmap(pixmap)
        self.Customer_Avatar_Label.setAlignment(Qt.AlignCenter)
        #----------------------------#
        #Disable Search Fonctions
        #----------------------------#
        self.Search_Customer_Facture.setReadOnly(True)
        self.Search_Customer_Facture.setText("")
        self.Search_Customer_Facture.setPlaceholderText("Pick Option From The Button [ By ]")
        self.Search_Rabbits.setReadOnly(True)
        self.Search_Rabbits.setText("")
        self.Search_Rabbits.setPlaceholderText("Pick Option From The Button [ By ]")
        self.Search_Cages.setReadOnly(True)
        self.Search_Cages.setText("")
        self.Search_Cages.setPlaceholderText("Pick Option From The Button [ By ]")
        #----------------------------#

        #----------------------------#
        #Pages Fill Fonctions
        #----------------------------#
        self.FactureCustomer_Widgets_Reload()
        self.RabbitCustomer_Widgets_Reload()
        self.CagesCustomer_Widgets_Reload()
        #----------------------------#



    def DeleteButtonCheck(self):
        with sqlite3.connect("ElevageInfos.db") as connection:
            AllRabbitsBought = len(connection.cursor().execute(f"SELECT ID FROM factures WHERE CustomerID={self.Data[0]}").fetchall())
            if(AllRabbitsBought != 0):
                self.Delete_Customer.setEnabled(False)
                self.Delete_Customer.setStyleSheet("QPushButton {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Pink_Locked.png);}")
            else :
                self.Delete_Customer.setEnabled(True)
                self.Delete_Customer.setStyleSheet("QPushButton {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Pink.png);}QPushButton:hover {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_Mix.png);}QPushButton:pressed {border: none;background-color:rgba(0, 0, 0, 0);image: url(:/Icons/Delete_White.png);}")

        

    def CustomerSearchFilter(self):
        Current_FilterBy = self.FilterBy_Customer_Facture.currentText()
        self.Search_Customer_Facture.setReadOnly(True)
        self.Search_Customer_Facture.setPlaceholderText("Pick Option From The Button [ By ]")
        self.Search_Customer_Facture.setText("")
        if(Current_FilterBy != "By"):
            self.Search_Customer_Facture.setReadOnly(False)
            self.Search_Customer_Facture.setPlaceholderText("Search Facture...")
        self.FactureCustomer_Widgets_Reload

    def RabbitCustomerSearchFilter(self):
        Current_FilterBy = self.FilterBy_Rabbits.currentText()
        self.Search_Rabbits.setReadOnly(True)
        self.Search_Rabbits.setPlaceholderText("Pick Option From The Button [ By ]")
        self.Search_Rabbits.setText("")
        if(Current_FilterBy != "By"):
            self.Search_Rabbits.setReadOnly(False)
            self.Search_Rabbits.setPlaceholderText("Search Rabbit...")
        self.RabbitCustomer_Widgets_Reload

    def CagesCustomerSearchFilter(self):
        Current_FilterBy = self.FilterBy_Cages.currentText()
        self.Search_Cages.setReadOnly(True)
        self.Search_Cages.setPlaceholderText("Pick Option From The Button [ By ]")
        self.Search_Cages.setText("")
        if(Current_FilterBy != "By"):
            self.Search_Cages.setReadOnly(False)
            self.Search_Cages.setPlaceholderText("Search Cage...")
        self.CagesCustomer_Widgets_Reload

    def FactureCustomer_Widgets_Reload(self):
        Current_FilterBy = self.FilterBy_Customer_Facture.currentText()
        CurrentTextSearch = self.Search_Customer_Facture.text()
        self.ImagesGrid(getDBData("ID,Date,Total","factures",self.Data[0],Current_FilterBy,CurrentTextSearch,self.Ordre_Customer_Facture.isChecked(),0),"Factures/PNG",self,5)
        self.Load_CustomersFacturesTable()
        self.DeleteButtonCheck()
    
    def RabbitCustomer_Widgets_Reload(self):
        Current_FilterGender = self.FilterGender_Rabbits.currentText()
        Current_FilterBy = self.FilterBy_Rabbits.currentText()
        CurrentTextSearch = self.Search_Rabbits.text()
        self.ImagesGrid(getDBData("ID,Breed,Gender","rabbits",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Rabbits.isChecked(),self.Data[0]),"Rabbits",self,5)
    
    def CagesCustomer_Widgets_Reload(self):
        Current_FilterGender = self.FilterGender_Cages.currentText()
        Current_FilterBy = self.FilterBy_Cages.currentText()
        CurrentTextSearch = self.Search_Cages.text()
        self.ImagesGrid(getDBData("ID,Bought,Gender","cages",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Rabbits.isChecked(),self.Data[0]),"Cages",self,5)
    

        

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Initialize The Window ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def __init__(self,Avatar,Data,mainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Customer Details") #Title OF The Application
        self.setWindowIcon(QIcon(":/Icons/Logo.png")) #Icon In The Top Of The Application
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.Menu_Customer_View.setCurrentIndex(0)

        self.mainWindow = mainWindow
        self.Avatar = Avatar
        self.Data = Data

        #----------------------------#
        #Menu Buttons Fonctions
        #----------------------------#
        self.Delete_Customer.clicked.connect(self.DeleteButton_Clicked)
        self.Edit_Customer.clicked.connect(self.EditButton_Clicked)
        self.Export_Exel_Customers.clicked.connect(lambda:self.export_to_exel_Table(self.FacturesCustomesTable_Advanced,"Factures",self.Exportation_CustomerFacture_Info))
        self.Export_PDF_Customers.clicked.connect(lambda:self.export_to_pdf_Table(self.FacturesCustomesTable_Advanced,"Factures",self.Exportation_CustomerFacture_Info))
        #----------------------------#

        #----------------------------#
        #Filter Buttons Fonctions
        #----------------------------#
        self.FilterBy_Customer_Facture.currentIndexChanged.connect(self.CustomerSearchFilter)
        self.Search_Customer_Facture.textChanged.connect(self.FactureCustomer_Widgets_Reload)
        self.Ordre_Customer_Facture.toggled.connect(self.FactureCustomer_Widgets_Reload)

        self.FilterGender_Rabbits.currentIndexChanged.connect(self.RabbitCustomer_Widgets_Reload)
        self.FilterBy_Rabbits.currentIndexChanged.connect(self.RabbitCustomerSearchFilter)
        self.Search_Rabbits.textChanged.connect(self.RabbitCustomer_Widgets_Reload)
        self.Ordre_Rabbits.toggled.connect(self.RabbitCustomer_Widgets_Reload)

        self.FilterBy_Cages.currentIndexChanged.connect(self.CagesCustomerSearchFilter)
        self.Search_Cages.textChanged.connect(self.CagesCustomer_Widgets_Reload)
        self.Ordre_Cages.toggled.connect(self.CagesCustomer_Widgets_Reload)
        self.FilterGender_Cages.currentIndexChanged.connect(self.CagesCustomer_Widgets_Reload)
        #----------------------------#

        self.StartingMethode()

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Initialize The Pages ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def Load_CustomersFacturesTable(self):
        self.FacturesCustomesTable_Advanced.clearContents()
        self.FacturesCustomesTable_Advanced.setRowCount(0)
        Current_FilterBy = self.FilterBy_Customer_Facture.currentText()
        CurrentTextSearch = self.Search_Customer_Facture.text()
        data = getDBData("ID,Date,Total","factures",self.Data[0],Current_FilterBy,CurrentTextSearch,self.Ordre_Customer_Facture.isChecked(),0)
        from Index_MainWindow import DoubleButtonWidgets

        for (row_index,row_data) in enumerate(data):
            self.FacturesCustomesTable_Advanced.insertRow(row_index)
            for col_index,cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data),)
                item.setTextAlignment(Qt.AlignCenter)
                self.FacturesCustomesTable_Advanced.setItem(row_index,col_index,item)
                
            self.FacturesCustomesTable_Advanced.setCellWidget(row_index,3, DoubleButtonWidgets(row_index,row_data,"Factures",self,self.mainWindow))
            self.FacturesCustomesTable_Advanced.setRowHeight(row_index,50)

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
             

    def DeleteButton_Clicked(self):
        message = QMessageBox.question(self,'Confirmation','Are You Sure You Want To Delete [ '+str(self.Data[0])+' ]?',QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if (message == QMessageBox.StandardButton.Yes):
            DeleteDBData("customers",'ID',self.Data[0])
            self.mainWindow.Customers_Widgets_Reload()
            self.mainWindow.Exportation_CustomerAdvanced_Info.setText(f"Customer ID [ {str(self.Data[0])} ] Deleted Successfully")
            self.mainWindow.Exportation_CustomerView_Info.setText(f"Customer ID [ {str(self.Data[0])} ] Deleted Successfully")
            self.close()

    def EditButton_Clicked(self):
        from Index_MainAddEditCustomer import mainEditCustomer
        mainWindow_Geometry = self.mainWindow.geometry()
        mainAddCustomerWindow = mainEditCustomer(self.Data[0],self.mainWindow)
        Right = mainWindow_Geometry.x() + 241 + 265
        Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainAddCustomerWindow.height()) // 2 ) - 10
        mainAddCustomerWindow.move(Right, Centre)
        mainAddCustomerWindow.exec()
        self.mainWindow.Exportation_CustomerAdvanced_Info.setText(f"Customer ID [ {str(self.Data[0])} ] Edited Successfully")
        self.mainWindow.Exportation_CustomerView_Info.setText(f"Customer ID [ {str(self.Data[0])} ] Edited Successfully")
        self.ReloadInformations()
        self.Reload_Avatar()

    