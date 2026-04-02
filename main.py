import os
import sys
import uuid
import ctypes
import time
import shutil
import winreg
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar, QMessageBox, QDialog, QLineEdit, QPushButton)
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QIcon
import pyotp  # For 2FA code verification
from Index_MainWindow import mainWindow


# Global QApplication instance
app = None

# 2FA Secret Key (Replace with your actual secret key)
# This should be securely shared with the user (e.g., via QR code for Google Authenticator)
TOTP_SECRET = "JBSWY3DPEHPK3PXP"  # Example secret key

def get_application_instance():
    """Ensure a QApplication instance exists."""
    global app
    if app is None:
        app = QApplication(sys.argv)
    return app

def show_message_box(title, message):
    """Display a message box with a title, message, and an OK button."""
    get_application_instance()  # Ensure QApplication exists
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setWindowIcon(QIcon(":/Icons/Logo.png")) #Icon In The Top Of The Application
    msg_box.setText(message)
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec()

def is_admin():
    """Check if the application is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

# ---------------------- 1. Security: Prevent Copying & Unauthorized Use ----------------------
def get_hardware_id():
    """Get unique machine ID (HDD serial + MAC address)."""
    try:
        mac_address = ':'.join(hex(uuid.getnode())[2:].zfill(12)[i:i+2] for i in range(0, 12, 2))
        return f"{mac_address}"
    except Exception:
        return "UNKNOWN"

def check_license():
    """Check if the application is running on the authorized PC."""
    registry_path = r"SOFTWARE\RabbitManager"
    try:
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        key = winreg.OpenKey(reg, registry_path, 0, winreg.KEY_READ)
        stored_hardware_id, _ = winreg.QueryValueEx(key, "HardwareID")
        winreg.CloseKey(key)

        if stored_hardware_id != get_hardware_id():
            show_message_box("License Error", "This application is licensed for another machine.")
            sys.exit()
    except FileNotFoundError:
        # If hardware ID is not stored, prompt for 2FA code
        prompt_2fa_code()
        sys.exit()


def store_hardware_id():
    """Store the machine's hardware ID in the registry."""
    registry_path = r"SOFTWARE\RabbitManager"
    try:
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        key = winreg.CreateKey(reg, registry_path)
        winreg.SetValueEx(key, "HardwareID", 0, winreg.REG_SZ, get_hardware_id())
        winreg.CloseKey(key)
    except Exception as e:
        show_message_box("Error", f"Error saving license: {e}")

# ---------------------- 2. 2FA Code Verification ----------------------
def verify_2fa_code(code):
    """Verify the 2FA code using the TOTP secret."""
    totp = pyotp.TOTP(TOTP_SECRET)
    return totp.verify(code)

def prompt_2fa_code():
    """Show a dialog to enter the 2FA code."""
    get_application_instance()  # Ensure QApplication exists
    dialog = QDialog()
    dialog.setWindowIcon(QIcon(":/Icons/Logo.png")) #Icon In The Top Of The Application

    dialog.setWindowTitle("2FA Verification")
    dialog.setFixedSize(300, 150)

    layout = QVBoxLayout()

    label = QLabel("Enter 2FA Code:")
    layout.addWidget(label)

    code_input = QLineEdit()
    layout.addWidget(code_input)

    submit_button = QPushButton("Submit")
    layout.addWidget(submit_button)

    def on_submit():
        code = code_input.text()
        if verify_2fa_code(code):
            store_hardware_id()
            dialog.close()

        else:
            show_message_box("Error", "Invalid 2FA code. Please try again.")

    submit_button.clicked.connect(on_submit)
    dialog.setLayout(layout)
    dialog.exec()

# ---------------------- 3. Security: Detect Debugging ----------------------
def is_debugger_present():
    """Detect if a debugger is attached."""
    return ctypes.windll.kernel32.IsDebuggerPresent() != 0

def detect_debugger():
    """Exit if debugging is detected."""
    if is_debugger_present():
        show_message_box("Debugging Detected", "Debugging detected! Exiting...")
        sys.exit()
        
# ---------------------- 5. Create Required Folders & Copy Default Images ----------------------
def check_folders(selected_path, file_path):
    appdata_path = os.getenv("APPDATA")
    if appdata_path is None:
        raise EnvironmentError("APPDATA environment variable is not set.")
    avatars_folder = Path(appdata_path) / "Rabbits_Manager" / selected_path
    avatars_folder.mkdir(parents=True, exist_ok=True)
    avatar_file = "Default.png"
    copy_avatar = os.path.join(avatars_folder, avatar_file)
    try:
        shutil.copy(file_path, copy_avatar)
    except Exception as e:
        show_message_box("Error", f"Error copying file {file_path} to {copy_avatar}: {e}")

check_folders("Customers", "_internal/Customer.png")
check_folders("Rabbits", "_internal/Rabbit.png")
check_folders("Cages", "_internal/Cage.png")
check_folders("Factures/PNG", "_internal/Facture.png")
check_folders("Factures/PDF", "_internal/Facture.png")

# ---------------------- 6. Loading Screen ----------------------
class LoadingScreen(QWidget):
    """Loading screen shown while the main window loads."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loading...")
        self.setFixedSize(300, 120)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        
        layout = QVBoxLayout()
        self.label = QLabel("Initializing...")
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        
        layout.addWidget(self.label)
        layout.addWidget(self.progress)
        self.setLayout(layout)

    def update_message(self, message):
        """Updates the loading message."""
        self.label.setText(message)

class LoadThread(QThread):
    """Background thread to load the main window with messages."""
    progress_update = Signal(int)  # Signal to update progress bar
    message_update = Signal(str)  # Signal to update loading message
    loading_finished = Signal()  # Signal when loading is done

    def run(self):
        """Simulates a loading process with progress updates."""
        messages = [
            "Checking system integrity...",
            "Verifying license...",
            "Initializing database...",
            "Loading user interface...",
            "Finalizing setup...",
            "Launching application..."
        ]
        
        for i, message in zip(range(0, 101, 20), messages):
            self.message_update.emit(message)
            time.sleep(0.5)
            self.progress_update.emit(i)
        
        self.loading_finished.emit()

# ---------------------- 7. Main Application Execution ----------------------
if __name__ == "__main__":
    # Initialize QApplication at the very beginning
    app = get_application_instance()

    # Security checks
    detect_debugger()
    check_license()

    # Start application
    loading_screen = LoadingScreen()
    loading_screen.show()

    loader = LoadThread()
    loader.progress_update.connect(loading_screen.progress.setValue)
    loader.message_update.connect(loading_screen.update_message)
    loader.loading_finished.connect(loading_screen.close)

    def show_main_window():
        """Show the main window after loading is complete."""
        Window = mainWindow()
        Window.show()

    loader.loading_finished.connect(show_main_window)
    loader.start()

    sys.exit(app.exec())