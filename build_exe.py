import PyInstaller.__main__
import sys

separator = ";" if sys.platform == "win32" else ":"

PyInstaller.__main__.run([
    '--name=RabbitsManager',
    '--noconsole',
    '--onedir',
    '--icon=InterfacesPY/QTInterfaces/Icons/Icon.ico',
    f'--add-data=ElevageInfos.db{separator}.',
    f'--add-data=Default/Cage.png{separator}.',
    f'--add-data=Default/Customer.png{separator}.',
    f'--add-data=Default/Facture.png{separator}.',
    f'--add-data=Default/Rabbit.png{separator}.',
    f'--add-data=InterfacesPY;InterfacesPY',
    '--hidden-import=pandas',
    '--hidden-import=sqlite3',
    '--hidden-import=datetime',
    '--hidden-import=PySide6',
    '--hidden-import=reportlab',
    '--hidden-import=openpyxl',
    '--hidden-import=xlsxwriter',
    '--hidden-import=os',
    'main.py'
])
