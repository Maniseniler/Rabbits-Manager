#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Importations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

# All PySide6 Importation :
from PySide6.QtWidgets import QDialog,QFileDialog, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget, QFrame, QVBoxLayout, QGridLayout, QHBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QPixmap, QPainter, QIcon
from PySide6.QtCore import Qt

# Other Importation Of Packages :
import sqlite3
from pathlib import Path
import os
from datetime import datetime

# Importation Of Interfaces :
from InterfacesPY import Ui_Rabbits_Tree_View_Main

MainWindow = ""

#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Get Specifique informations From Data Bases ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

def fetch_rabbits_from_db():
    with sqlite3.connect("ElevageInfos.db") as connection:
        cursor = connection.cursor()
        # Fetch all rabbits
        cursor.execute("SELECT ID, Breed, Father, Mother, Gender FROM rabbits")
        rows = cursor.fetchall()

        # Convert data into dictionary format
        rabbits = {}
        for row in rows:
            rabbit_id, name, father, mother, gender = row
            rabbits[rabbit_id] = {
                "id": rabbit_id,
                "name": name,
                "father": father if father else None,  # Convert None values properly
                "mother": mother if mother else None,
                "gender": gender
            }
        return rabbits

#-------------------------------------------------------------------------------------------------------------------------------------------|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main Window Class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#-------------------------------------------------------------------------------------------------------------------------------------------|

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
# Global variables to store family groups
Family_Members_Groups = {}
Father_Groups = {}
Families_Frame = []

def ReloadRabbitsTree(rabbits, father_id,mainWindow):
    if father_id and (father_id not in Father_Groups):
        father_frame = VerticalFrame([ImageFrame(Find_Image_SelectedView("Rabbits",rabbits[father_id]["id"]), str(rabbits[father_id]["id"]), rabbits[father_id]["gender"],rabbits[father_id]["name"],mainWindow)], (221, 242, 255))
        Father_Groups[father_id] = father_frame

        Wifes = []
        for index in rabbits:
            if rabbits[index]["father"] == father_id and rabbits[index]["mother"] not in Wifes:
                Wifes.append(rabbits[index]["mother"])

        if len(Wifes) > 0:
            Wifesfamilies = []
            for Wife in Wifes:
                mother_frame = VerticalFrame([ImageFrame(Find_Image_SelectedView("Rabbits",rabbits[Wife]["id"]), str(rabbits[Wife]["id"]), rabbits[Wife]["gender"],rabbits[Wife]["name"],mainWindow)], (253, 221, 255))
                parent_key = (father_id, Wife)
                if parent_key not in Family_Members_Groups:

                    FchildrenImages = [ImageFrame(Find_Image_SelectedView("Rabbits",rabbits[r]["id"]), str(rabbits[r]["id"]), rabbits[r]["gender"],rabbits[r]["name"],mainWindow) for r in rabbits if (rabbits[r]["father"], rabbits[r]["mother"]) == parent_key and ((rabbits[r]["gender"] == "Female") or (rabbits[r]["gender"] == "Null"))]
                    MchildrenImages = []
                    MchildrenIDS = [int(rabbits[r]["id"]) for r in rabbits if (rabbits[r]["father"], rabbits[r]["mother"]) == parent_key and rabbits[r]["gender"] == "Male"]

                    if MchildrenIDS:
                        for index in rabbits:
                            if (rabbits[index]["father"] in MchildrenIDS):
                                MchildrenImages.append(ReloadRabbitsTree(rabbits, rabbits[index]["father"],mainWindow))
                                MchildrenIDS.remove(rabbits[index]["father"])

                        if (len(MchildrenIDS) > 0):
                            for MchildID in MchildrenIDS:
                                FchildrenImages.append(ImageFrame(Find_Image_SelectedView("Rabbits",rabbits[MchildID]["id"]), str(rabbits[MchildID]["id"]), rabbits[MchildID]["gender"],rabbits[father_id]["name"],mainWindow))

                    children = []

                    if FchildrenImages:
                        children.append(GridFrame(FchildrenImages, 4))

                    if MchildrenImages:
                        children.append(GridFrame(MchildrenImages, 4))

                    if children:
                        Wifesfamilies.append(VerticalFrame([mother_frame, VerticalFrame(children)]))
            return HorizentalFrame([VerticalFrame([father_frame, HorizentalFrame(Wifesfamilies)])], (92, 92, 92), 20)
        else:
            return ImageFrame(Find_Image_SelectedView("Rabbits",rabbits[father_id]["id"]), str(rabbits[father_id]["id"]), rabbits[father_id]["gender"],rabbits[father_id]["name"],mainWindow)

class ImageFrame(QFrame):
    def __init__(self, image_path, id, gender, name,mainWindow, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.StyledPanel)
        self.setStyleSheet("""
            QFrame {
                border-radius: 10px;
                background-color: #444;
            }
            QPushButton {
                border: none;
                background-color: transparent;
            }
            QPushButton:hover {
                border: 3px solid rgb(98, 114, 90);
                background-color: rgba(98, 114, 90, 0.5);
            }
        """)

        self.mainWindow = mainWindow
        self.ID = id
        self.Image_View = image_path

        # Layout for the image frame
        VerticalConteiner = QVBoxLayout()
        VerticalConteiner.setContentsMargins(5, 5, 5, 5)
        VerticalConteiner.setSpacing(2)
        self.setFixedSize(118, 161)

        # Load image
        pixmap = QPixmap(image_path).scaled(90, 90, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        AvatarButton = QPushButton()
        AvatarButton.setIcon(pixmap)
        AvatarButton.setIconSize(pixmap.size())
        AvatarButton.setFlat(True)

        # Labels
        ID_TXT_Label = QLabel(id)
        ID_TXT_Label.setAlignment(Qt.AlignCenter)

        Name_TXT_Label = QLabel(f"[ {name} ]")
        Name_TXT_Label.setAlignment(Qt.AlignCenter)

        color = {"Male": (0, 140, 179), "Female": (199, 0, 217),"Null": (182, 155, 0)}.get(gender, (0, 104, 104))
        ID_TXT_Label.setStyleSheet(f'color: rgb(255, 255, 255); font: 75 10pt "Acme"; background-color:rgb{color};')
        Name_TXT_Label.setStyleSheet(f'color: rgb(255, 255, 255);font: 75 8pt "Acme";background-color:rgb{color};')

        VerticalConteiner.addWidget(AvatarButton)
        VerticalConteiner.addWidget(ID_TXT_Label)
        VerticalConteiner.addWidget(Name_TXT_Label)
        self.setLayout(VerticalConteiner)

        AvatarButton.clicked.connect(self.open_DetailWindow_WithBlur)

    def open_DetailWindow_WithBlur(self):
        mainWindow_Geometry = self.mainWindow.geometry()
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

class VerticalFrame(QFrame):
    def __init__(self, Widgets, Color=(92, 92, 92), Pad=10, parent=None):
        super().__init__(parent)
        self.setStyleSheet(f"border-radius: 10px; background-color: rgb{Color}; padding: 5px;")
        layout = QVBoxLayout()
        layout.setSpacing(Pad)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        for Widget in Widgets:
            if Widget:
                layout.addWidget(Widget)
        self.setLayout(layout)

class HorizentalFrame(QFrame):
    def __init__(self, Widgets, Color=(221, 242, 255), Pad=10, Main=False, parent=None):
        super().__init__(parent)
        self.setStyleSheet(f"border-radius: 10px; background-color: rgb{Color}; padding: 5px;")
        if Main:
            self.setStyleSheet("QWidget{background-color: #5C5C5C;color: rgb(255, 255, 255);font: 75 18pt 'Acme';border: 2px solid #ffffff;border-style: outset;border-radius: 20px;}")

        layout = QHBoxLayout()
        layout.setSpacing(Pad)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        for Widget in Widgets:
            if Widget:
                layout.addWidget(Widget)
        self.setLayout(layout)

class GridFrame(QFrame):
    def __init__(self, avatars, Number, Pad=10, parent=None):
        super().__init__(parent)
        self.setStyleSheet("border-radius: 10px; background-color: rgba(0, 0, 0, 0); padding: 5px;")
        layout = QGridLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        layout.setSpacing(Pad)
        for avatar in avatars:
            index = avatars.index(avatar)
            row = index // Number
            col = index % Number
            if avatar:
                layout.addWidget(avatar, row, col)
        self.setLayout(layout)

class RabbitTreeWindow(QGraphicsView):

    def refresh_tree(self):
        # Reset global variables
        global Family_Members_Groups, Father_Groups, Families_Frame
        Family_Members_Groups = {}
        Father_Groups = {}
        Families_Frame = []

        rabbits = fetch_rabbits_from_db()
        self.draw_tree(rabbits)

    def __init__(self,mainWindow):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.setSceneRect(-10000, -10000, 20000, 20000)  # Set a large scene size for infinite scrolling
        self.setDragMode(QGraphicsView.ScrollHandDrag)  # Enable scrolling
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)

        self.setStyleSheet("background-color: rgba(0, 0, 0, 0); border:none;")

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scale_factor = 1.0

        self.mainWindow = mainWindow

    def wheelEvent(self, event):
        # Zoom in/out with mouse wheel
        zoom_in_factor = 1.1
        zoom_out_factor = 1 / zoom_in_factor

        if event.angleDelta().y() > 0:
            zoom_factor = zoom_in_factor
        else:
            zoom_factor = zoom_out_factor

        self.scale_factor *= zoom_factor

        # Apply the zoom factor
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.scale(zoom_factor, zoom_factor)

    def draw_tree(self, rabbits):
        AllFathers_Frames = []
        family_proxy = QGraphicsProxyWidget()
        for id, data in rabbits.items():
            father_id = data["father"]
            if father_id and rabbits[father_id]["father"] is None and (father_id not in Father_Groups):
                AllFathers_Frames.append(ReloadRabbitsTree(rabbits, father_id,self.mainWindow))
                
        if AllFathers_Frames:
            family_proxy = QGraphicsProxyWidget()
            family_proxy.setWidget(HorizentalFrame(AllFathers_Frames, (92, 92, 92), 50))
            self.scene.clear()  # Clear previous items
            self.scene.addItem(family_proxy)
            self.centerOn(family_proxy)

    def take_screenshot(self):
        if not isinstance(self, QGraphicsView) or self.scene is None:
            return
        
        default_folder = os.path.join(os.getcwd(), 'Screenshots')
        if not os.path.exists(default_folder):
            os.makedirs(default_folder)
        
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self,"Save PNG File",os.path.join(default_folder,"[Rabbit_Tree]_"+datetime.today().strftime("{%m-%d-%Y}_(%H-%M-%S)")),"PNG Files (*.png);;All Files (*)")
        if file_path:

            scene = self.scene  # Get the QGraphicsScene object
            scene_rect = scene.sceneRect()  # Get the full bounding rectangle of the scene

            # Set high resolution without zooming
            screenshot = QPixmap(int(scene_rect.width()) * 3.5, int(scene_rect.height()) * 3.5)
            screenshot.fill(Qt.transparent)

            # Render without scaling to avoid zoom-in
            painter = QPainter(screenshot)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            scene.render(painter)  # Render directly onto the pixmap
            painter.end()

            # Save the screenshot with a timestamped filename 
            screenshot.save(file_path)



class mainRabbitTree(QDialog, Ui_Rabbits_Tree_View_Main):

    def __init__(self,mainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Rabbits Tree")  # Title OF The Application
        self.setWindowIcon(QIcon(":/Icons/Logo.png"))  # Icon In The Top Of The Application
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.mainWindow = mainWindow

        self.tree_view = RabbitTreeWindow(self.mainWindow)
        self.tree_view.setFixedSize(1031, 767)
        self.TreeVerticalLayout.addWidget(self.tree_view)

        self.tree_view.refresh_tree()

        self.ScreenShot_Button.clicked.connect(self.tree_view.take_screenshot)

    def showEvent(self, event):
        super().showEvent(event)
        # Adjust the window size to fit all frames
        self.adjustSize()
        # Fit the view to the drawn content
        self.tree_view.fitInView(self.tree_view.scene.itemsBoundingRect(), Qt.KeepAspectRatio)

    def closeEvent(self, event):
        # Reset global variables when the window is closed
        global Family_Members_Groups, Father_Groups, Families_Frame
        Family_Members_Groups = {}
        Father_Groups = {}
        Families_Frame = []
        event.accept()
