from PyQt6.QtWidgets import QApplication, QSystemTrayIcon
from PyQt6.QtGui import QIcon
import resources  # Ensure this imports the generated resources.py

# Initialize the application
app = QApplication([])

# Set the application name
app.setApplicationName("AgriMesh")

# Create the system tray icon
tray_icon = QSystemTrayIcon(app)
tray_icon.setIcon(QIcon(":/homeICON.ico"))  # Use the resource path
tray_icon.setToolTip("AgriMesh")
tray_icon.show()

# Show a notification
tray_icon.showMessage(
    "Notification",
    "This is a test message",
    QSystemTrayIcon.MessageIcon.Information
)

# Execute the application
app.exec()
