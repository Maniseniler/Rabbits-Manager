#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Importations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

#All PySide6 Importation :
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog,QFrame,QLabel,QVBoxLayout,QPushButton
from PySide6.QtGui import QIcon,QPixmap

#Other Importation Of Packages :
import fitz  # PyMuPDF
import sqlite3
from pathlib import Path
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

#Importation Of Interfaces :
from InterfacesPY import Ui_Facture_Add_Main 

#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Get Specifique informations From Data Bases ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

def getDBData(Importation,DBName,genderFilter,FilterBy,Search,OrdreButtonChecked):
    DECR = "ORDER BY ID DESC"
    CR = "ORDER BY ID ASC"
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()
        if(DBName == "customers"):
            query = f"SELECT {Importation} FROM {DBName} WHERE ('{genderFilter}' = 'Gender' OR Gender = '{genderFilter}')"
            if(FilterBy != 'By'):
                query = f"SELECT {Importation} FROM {DBName} WHERE (('{genderFilter}' = 'Gender' OR Gender = '{genderFilter}') AND ({FilterBy} LIKE '%{Search}%'))"
        
        elif(DBName == "rabbits" or DBName =="cages"):
            query = f"SELECT {Importation} FROM {DBName} WHERE (CustomerID IS NULL AND FactureID IS NULL) AND ('{genderFilter}' = 'Gender' OR Gender = '{genderFilter}')"
            if(FilterBy != 'By'):
                query = f"SELECT {Importation} FROM {DBName} WHERE (CustomerID IS NULL AND FactureID IS NULL) AND ('{genderFilter}' = 'Gender' OR Gender = '{genderFilter}') AND ({FilterBy} LIKE '%{Search}%') "
        
        if(OrdreButtonChecked):
            query += CR
        else :
            query += DECR

        cursor.execute(query)
        Data = cursor.fetchall()
    return Data

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

def Find_Folder_Path(SelectedPath):
    appdata_path = os.getenv("APPDATA")  # Gets the %appdata% folder path
    if appdata_path is None:
        raise EnvironmentError("APPDATA environment variable is not set.")
    AvatarsFolder = Path(appdata_path) / "Rabbits_Manager" / SelectedPath
    AvatarsFolder.mkdir(parents=True, exist_ok=True)
    return AvatarsFolder

def SearchFilter(FilterBy,SearchBar,Txt):
    Current_FilterBy = FilterBy.currentText()
    SearchBar.setReadOnly(True)
    SearchBar.setPlaceholderText("Pick Option From The Button [ By ]")
    SearchBar.setText("")
    if(Current_FilterBy != "By"):
        SearchBar.setReadOnly(False)
        SearchBar.setPlaceholderText(f"Search {Txt}...")


Items = []  # List to store items

def create_facture(ID, CustomerID, output_pdf, output_png, data):
    # Create a PDF canvas
    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, height - 100, "Facture")

    # Customer details
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 140, f"Client: {data['client_name']}")
    c.drawString(100, height - 160, f"Date: {data['date']}")

    # Add table headers
    c.drawString(100, height - 200, "Category")
    c.drawString(300, height - 200, "ID")
    c.drawString(400, height - 200, "Price")

    # Add table rows
    y = height - 220
    for item in data["items"]:
        c.drawString(100, y, item["Category"])
        c.drawString(300, y, str(item["ID"]))
        c.drawString(400, y, f"{item['Price']:.3f} TND")
        y -= 20

    # Total
    total = sum(item["Price"] for item in data["items"])
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y - 20, f"Total: {total:.3f} TND")

    # Save the PDF
    c.save()

    # Convert PDF to high-resolution PNG using PyMuPDF
    pdf_document = fitz.open(output_pdf)
    for page in pdf_document:
        matrix = fitz.Matrix(4, 4)  # 4x scaling for high resolution (≈ 300 DPI)
        pix = page.get_pixmap(matrix=matrix, alpha=False)  # No transparency
        pix.save(output_png)  # Save as PNG
    pdf_document.close()

    # Save invoice data to database
    with sqlite3.connect("ElevageInfos.db") as connection:
        sql = "INSERT INTO factures (ID, Date, CustomerID, Total) VALUES (?, ?, ?, ?)"
        val = (ID, data['date'], CustomerID, total)
        connection.cursor().execute(sql, val)
        connection.commit()


#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Image Frame Class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

class ImageFrame(QFrame):
    def __init__(self, Image_View, idString, Data, mainWindow, CurrentWindow, NewWindow, parent=None):
        super().__init__(parent)
        global Items
        self.ID = Data[0]
        self.Image_View = Image_View
        self.mainWindow = mainWindow
        self.NewWindow = NewWindow
        self.CurrentWindow = CurrentWindow
        self.setFrameShape(QFrame.StyledPanel)
        self.setStyleSheet("border-radius: 10px; background-color: #444;")
        self.selected = False

        # Initialize selected frames storage if it doesn't exist
        if not hasattr(self.mainWindow, "selected_frames"):
            self.mainWindow.selected_frames = set()

        # Layout for the image frame
        VerticalContainer = QVBoxLayout()
        VerticalContainer.setContentsMargins(5, 5, 5, 5)
        VerticalContainer.setSpacing(2)
        self.setFixedSize(118, 161)

        # Add the image button
        pixmap = QPixmap(Image_View).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        AvatarButton = QPushButton()
        AvatarButton.setStyleSheet("QPushButton:hover {border: 3px solid rgb(98, 114, 90);}")
        AvatarButton.setIcon(pixmap)
        AvatarButton.setIconSize(pixmap.size())
        AvatarButton.setFlat(True)
        AvatarButton.clicked.connect(lambda: self.toggle_selection(self.NewWindow))

        # Store last selected frame in mainWindow
        self.mainWindow.Exit_Sell_Button.clicked.connect(self.unselect_last_frame)

        # Add the label below the image
        ID_TXT_Label = QLabel(idString)
        ID_TXT_Label.setAlignment(Qt.AlignCenter)

        Name_TXT_Label = QLabel(f"[ {Data[1]} ]")
        Name_TXT_Label.setAlignment(Qt.AlignCenter)

        Gender = ""
        match self.NewWindow:
            case "Rabbits": Gender = Data[2]
            case "Customers": Gender = Data[4]
            case "Cages": Gender = Data[2]

        Color = {"Male": (0, 140, 179), "Female": (199, 0, 217), "Null": (182, 155, 0), "Kids": (182, 155, 0)}.get(Gender, (0, 104, 104))

        ID_TXT_Label.setStyleSheet(f'color: rgb(255, 255, 255); font: 75 15pt "Acme"; background-color: rgb{Color};')
        Name_TXT_Label.setStyleSheet(f'color: rgb(255, 255, 255); font: 75 8pt "Acme"; background-color: rgb{Color};')

        VerticalContainer.addWidget(AvatarButton)
        VerticalContainer.addWidget(ID_TXT_Label)
        VerticalContainer.addWidget(Name_TXT_Label)
        self.setLayout(VerticalContainer)

        # Restore selection if this frame was previously selected
        if self.ID in self.mainWindow.selected_frames:
            self.set_selected(True)

    def unselect_last_frame(self):
        """Unselect only the last selected ImageFrame without affecting others"""
        if hasattr(self.mainWindow, "last_selected_frame") and self.mainWindow.last_selected_frame:
            self.mainWindow.last_selected_frame.set_selected(False)
            self.mainWindow.last_selected_frame = None

    def toggle_selection(self, WindowName):
        """Toggle selection for this frame independently"""
        global Items
        if WindowName == "Customers":
            with sqlite3.connect("ElevageInfos.db") as connection:
                cursor = connection.cursor()
                query = f"SELECT ID, Name, Phone, Address, Gender FROM customers WHERE ID = '{self.ID}'"
                cursor.execute(query)
                Data = cursor.fetchall()[0]

            self.mainWindow.Sell_Windows.setCurrentIndex(1)
            self.mainWindow.Return_Page.setHidden(False)

            self.mainWindow.Customer_ID_Label.setText(f"ID  :  {str(Data[0])}")
            self.mainWindow.Customer_Name_Label.setText(Data[1])
            self.mainWindow.Customer_Phone_Label.setText(Data[2])
            self.mainWindow.Customer_Gender_Label.setText(Data[4])
            self.mainWindow.Customer_Address_Label.setText(Data[3])
        else:
            if not self.selected:
                self.mainWindow.Sell_Item_Frame.setHidden(False)
                self.mainWindow.Block_Frame.setHidden(False)

                self.mainWindow.Item_ID_Label.setText(f"ID  :  {str(self.ID)}")
                self.mainWindow.Item_Type_Label.setText(f"Type  :  {str(WindowName)}")
                pixmap = QPixmap(self.Image_View).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.mainWindow.Item_Avatar_Label.setPixmap(pixmap)
                self.mainWindow.Item_Sold_Input.setValue(0.000)
            else : 
                Items = [item for item in Items if not (item["ID"] == str(self.ID) and item["Category"] == WindowName)] 
                self.mainWindow.print_items()

            self.selected = not self.selected
            self.set_selected(self.selected)

            # Update selected frames list
            if self.selected:
                self.mainWindow.selected_frames.add(self.ID)
                self.mainWindow.last_selected_frame = self
            else:
                self.mainWindow.selected_frames.discard(self.ID)

    def set_selected(self, state):
        """Apply selection style based on state"""
        self.selected = state
        if self.selected:
            self.setStyleSheet("border: 2px solid #00FF00; border-radius: 10px; background-color: #444;")
        else:
            self.setStyleSheet("border-radius: 10px; background-color: #444;")


#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ AddC Window Class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

class mainAddFacture(QDialog,Ui_Facture_Add_Main):

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

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Images Grid ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def ImagesGrid(self,Data,SelectedPath,Num):
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

        for index,Informations in enumerate(Data):
            row = index // Num
            col = index % Num
            ID = Informations[0]
            image_frame = ImageFrame(Find_Image_SelectedView(SelectedPath,ID), f"#{ID}",Informations,self,"AlreadyCurrent",SelectedPath)
            
            if(SelectedPath == "Customers"):
                self.GridLayout_Customers_View.addWidget(image_frame, row, col)
            elif(SelectedPath == "Rabbits"):
                self.GridLayout_Rabbits_View.addWidget(image_frame, row, col)
            elif(SelectedPath == "Cages"):
                self.GridLayout_Cages_View.addWidget(image_frame, row, col)

    def openAddCustomerWindow(self):
        from Index_MainAddEditCustomer import mainAddCustomer
        mainWindow_Geometry = self.geometry()
        mainAddCustomerWindow = mainAddCustomer(self)
        Right = (mainWindow_Geometry.x() + (mainWindow_Geometry.width() - mainAddCustomerWindow.width()) // 2 )
        Centre = (mainWindow_Geometry.y() + (mainWindow_Geometry.height() - mainAddCustomerWindow.height()) // 2 ) - 10
        mainAddCustomerWindow.move(Right, Centre)
        mainAddCustomerWindow.exec()

    def CustomerSearchFilter(self,FilterBy,SearchBar):
        SearchFilter(FilterBy,SearchBar,"Customer")
        self.Customers_Widgets_Reload

    def Customers_Widgets_Reload(self):
        Current_FilterGender = self.FilterGender_Customer.currentText()
        Current_FilterBy = self.FilterBy_Customer.currentText()
        CurrentTextSearch = self.Search_Customer.text()
        self.ImagesGrid(getDBData("ID,Name,Phone,Address,Gender,Notes","customers",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Customer.isChecked()),"Customers",6) # Customers View Filled
        self.mainWindow.LoadDashboard()
        self.mainWindow.Customers_Widgets_Reload()
    
    def RabbitSearchFilter(self,FilterBy,SearchBar):
        SearchFilter(FilterBy,SearchBar,"Rabbit")
        self.Rabbits_Widgets_Reload
    
    def Rabbits_Widgets_Reload(self):
        Current_FilterGender = self.FilterGender_Rabbits.currentText()
        Current_FilterBy = self.FilterBy_Rabbits.currentText()
        CurrentTextSearch = self.Search_Rabbits.text()
        self.ImagesGrid(getDBData("ID,Breed,Gender","rabbits",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Rabbits.isChecked()),"Rabbits",3) # Customers View Filled

    def CageSearchFilter(self,FilterBy,SearchBar):
        SearchFilter(FilterBy,SearchBar,"Cage")
        self.Cages_Widgets_Reload

    def Cages_Widgets_Reload(self):
        Current_FilterGender = self.FilterGender_Cages.currentText()
        Current_FilterBy = self.FilterBy_Cages.currentText()
        CurrentTextSearch = self.Search_Cages.text()
        self.ImagesGrid(getDBData("ID,Bought,Gender","cages",Current_FilterGender,Current_FilterBy,CurrentTextSearch,self.Ordre_Cages.isChecked()),"Cages",3) # Customers View Filled

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Initialize The Window ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    def print_items(self):
        self.AllItems.clear()
        if(len(Items)>0):
            self.Add_Facture.setHidden(False)
        else : 
            self.Add_Facture.setHidden(True)

        for item in Items:
            self.AllItems.append(f"Type : {item["Category"]} ; ID : {item["ID"]} ; Price : {item["Price"]} TND")

    def add_item(self):
        global Items
        item_id = self.Item_ID_Label.text()[7::]
        item_type = self.Item_Type_Label.text()[9::]
        price = self.Item_Sold_Input.value()

        Items.append({"Category":item_type,"ID":item_id,"Price":price})
        self.print_items()
        self.Sell_Item_Frame.hide()
        self.Block_Frame.hide()

    def Start(self):
        global Items
        self.Sell_Windows.setCurrentIndex(0)

        self.Sell_Item_Frame.setHidden(True)
        self.Block_Frame.setHidden(True)
        self.Return_Page.setHidden(True)
        self.Add_Facture.setHidden(True)

        self.Sell_Item_Frame.move(315,228)

        Items=[]
    
    def AddFacture(self):
        global Items
        facture_data = {
            "client_name": self.Customer_Name_Label.text(),
            "date": datetime.today().strftime("%m/%d/%Y"),
            "items": Items,
        }
        CustomerID = int(self.Customer_ID_Label.text()[7::])
        for item in Items:
            if(item["Category"] == "Rabbits"):
                with sqlite3.connect("ElevageInfos.db") as connection:
                    sql = "UPDATE rabbits SET CustomerID=?,FactureID=?,Sold=? WHERE ID = ?"
                    val = (CustomerID,self.ID,item["Price"],item["ID"])
                    connection.cursor().execute(sql, val)
                    connection.commit()
            if(item["Category"] == "Cages"):
                with sqlite3.connect("ElevageInfos.db") as connection:
                    sql = "UPDATE cages SET CustomerID=?,FactureID=?,Sold=? WHERE ID = ?"
                    val = (CustomerID,self.ID,item["Price"],item["ID"])
                    connection.cursor().execute(sql, val)
                    connection.commit()

        create_facture(self.ID,CustomerID,f"{Find_Folder_Path("Factures/PDF")}/{self.ID}.pdf", f"{Find_Folder_Path("Factures/PNG")}/{self.ID}.png", facture_data)
        self.close()
        self.mainWindow.Facture_Widgets_Reload()
        self.mainWindow.Exportation_FactureAdvanced_Info.setText(f"Facture ID [ {str(self.ID)} ] Added Successfully")
        self.mainWindow.Exportation_FactureView_Info.setText(f"Facture ID [ {str(self.ID)} ] Added Successfully")

    def __init__(self,mainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Add Facture") #Title OF The Application
        self.setWindowIcon(QIcon(":/Icons/Logo.png")) #Icon In The Top Of The Application
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.mainWindow = mainWindow

        #----------------------------#
        #Menu Buttons Fonctions
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

        self.Add_Customer_View.clicked.connect(self.openAddCustomerWindow)
        self.Customers_Widgets_Reload()
        self.Rabbits_Widgets_Reload()
        self.Cages_Widgets_Reload()

        self.Start()

        self.Return_Page.clicked.connect(self.Start)
        self.Exit_Sell_Button.clicked.connect(lambda : self.Block_Frame.hide())


        self.Sell_Button.clicked.connect(self.add_item)




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


        with sqlite3.connect("ElevageInfos.db") as connection:
            cursor = connection.cursor()
            query = "SELECT ID FROM factures ORDER BY ID DESC LIMIT 1"
            cursor.execute(query)
            Data = cursor.fetchone()

        if Data:
            self.ID = Data[0]+1
        else:
            self.ID = 1

        self.Add_Facture.clicked.connect(self.AddFacture)


