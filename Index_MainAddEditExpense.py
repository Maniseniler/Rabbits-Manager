#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Importations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

#All PySide6 Importation :
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon

#Other Importation Of Packages :
import sqlite3

#Importation Of Interfaces :
from InterfacesPY import Ui_AddExpense_Main 
from InterfacesPY import Ui_EditExpense_Main

#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Fonctions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

def VerifName(self,Title):
    self.Expense_Title.setText(Title)
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

#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ AddC Window Class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

class mainAddExpense(QDialog,Ui_AddExpense_Main):

    def AddCage(self):
        if(VerifName(self,"Add A New Expense")):
            Name = self.Name_Input.text().title()
            Total = float(self.Expense_Input.value())
            Notes = self.Notes_Input.toPlainText()

            with sqlite3.connect("ElevageInfos.db") as connection:
                sql = "INSERT INTO expenses (ID, Name, Total, Notes) VALUES (?, ?, ?, ?)"
                val = (self.ID, Name,Total, Notes)
                connection.cursor().execute(sql, val)
                connection.commit()
                    

            self.close()
            self.mainWindow.Expenses_Widgets_Reload()
            self.mainWindow.Exportation_ExpensesAdvanced_Info.setText(f"Expense ID [ {str(self.ID)} ] Added Successfully")
        else :
            self.Expense_Title.setText("Error Missing")

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Initialize The Window ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def __init__(self,mainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Add Expense") #Title OF The Application
        self.setWindowIcon(QIcon(":/Icons/Logo.png")) #Icon In The Top Of The Application
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.mainWindow = mainWindow
        with sqlite3.connect("ElevageInfos.db") as connection:
            cursor = connection.cursor()
            query = "SELECT ID FROM expenses ORDER BY ID DESC LIMIT 1"
            cursor.execute(query)
            Data = cursor.fetchone()

        if Data:
            self.ID = Data[0]+1
        else:
            self.ID = 1


        self.ID_Label.setText(f"ID  :  {str(self.ID)}")
        self.Add_Expense_Button.clicked.connect(lambda:self.AddCage())
        self.Name_Input.textChanged.connect(lambda:VerifName(self,"Add A New Expense"))



#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Edit Window Class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

class mainEditExpense(QDialog,Ui_EditExpense_Main):

    def EditExpense(self):
        if(VerifName(self,"Edit A Expense")):
            Name = self.Name_Input.text().title()
            Total = float(self.Expense_Input.value())
            Notes = self.Notes_Input.toPlainText()

            with sqlite3.connect("ElevageInfos.db") as connection:
                sql = "UPDATE expenses SET Name=? , Total=?, Notes=? WHERE ID = ?"
                val = (Name,Total,Notes,self.ID)
                connection.cursor().execute(sql, val)
                connection.commit()
                    

            self.close()
            self.mainWindow.Expenses_Widgets_Reload()
            self.mainWindow.Exportation_ExpensesAdvanced_Info.setText(f"Expense ID [ {str(self.ID)} ] Edited Successfully")
        else :
            self.Expense_Title.setText("Error Missing")

    # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Initialize The Window ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    def __init__(self,ID,mainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Edit Expense") #Title OF The Application
        self.setWindowIcon(QIcon(":/Icons/Logo.png")) #Icon In The Top Of The Application
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.mainWindow = mainWindow
        self.ID = ID

        with sqlite3.connect("ElevageInfos.db") as connection:
            cursor = connection.cursor()
            query = f"SELECT Name,Total,Notes FROM expenses WHERE ID={self.ID}"
            cursor.execute(query)
            Data = cursor.fetchone()

        self.ID_Label.setText(f"ID  :  {str(self.ID)}")
        self.Name_Input.setText(str(Data[0]))   
        self.Expense_Input.setValue(Data[1]) 
        self.Notes_Input.setPlainText(str(Data[2]))      

        self.Edit_Expense_Button.clicked.connect(lambda:self.EditExpense())
        self.Name_Input.textChanged.connect(lambda:VerifName(self,"Edit A Expense"))