import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QLineEdit, QStackedWidget, QDialog, QMessageBox, QGridLayout
)
from PyQt6.QtGui import QFont, QPalette, QColor
from PyQt6.QtCore import Qt

# Define age-specific themes: background color, text color, and font.
themes = {
    "Under 10": {
        "bg": "#FFDD00",     # Bright yellow for attention and engagement
        "fg": "#000000",
        "font": QFont("Comic Sans MS", 12)
    },
    "Teenager": {
        "bg": "#333333",     # Dark background with neon accents for modern look
        "fg": "#00FFFF",
        "font": QFont("Helvetica", 12)
    },
    "Youth": {
        "bg": "#F0F0F0",     # Neutral, balanced palette for clarity
        "fg": "#000000",
        "font": QFont("Arial", 12)
    },
    "Middle Age": {
        "bg": "#ADD8E6",     # Soft blue for comfort and readability
        "fg": "#000000",
        "font": QFont("Verdana", 12)
    },
    "Elderly": {
        "bg": "#FFFFFF",     # High contrast (white background with dark text)
        "fg": "#000000",
        "font": QFont("Arial", 14)
    }
}

class AgeSelectionDialog(QDialog):
    """Dialog to select an age group.
       HCI Rationale: Personalizes the experience with age-appropriate themes."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Select Age Group")
        self.selected_age = None
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        label = QLabel("Select Your Age Group:")
        label.setFont(QFont("Arial", 12))
        layout.addWidget(label)
        
        # Create buttons for each age group
        for age in themes.keys():
            btn = QPushButton(age)
            btn.setFont(QFont("Arial", 12))
            btn.clicked.connect(lambda _, a=age: self.select_age(a))
            layout.addWidget(btn)
            
        self.setLayout(layout)
        
    def select_age(self, age):
        self.selected_age = age
        self.accept()

class HomePage(QWidget):
    """Home/Entry Window.
       HCI Rationale: Clear, welcoming message with a consistent layout."""
    def __init__(self, theme):
        super().__init__()
        self.theme = theme
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        label = QLabel("Welcome to the Home Page!")
        label.setFont(self.theme["font"])
        label.setStyleSheet(f"color: {self.theme['fg']};")
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

class ProfilePage(QWidget):
    """Profile/Registration Window.
       HCI Rationale: Simple and clear form for user data entry."""
    def __init__(self, theme):
        super().__init__()
        self.theme = theme
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        title = QLabel("Profile / Registration")
        title.setFont(self.theme["font"])
        title.setStyleSheet(f"color: {self.theme['fg']};")
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        
        grid = QGridLayout()
        grid.addWidget(QLabel("Name:"), 0, 0)
        self.name_edit = QLineEdit()
        grid.addWidget(self.name_edit, 0, 1)
        
        grid.addWidget(QLabel("Age:"), 1, 0)
        self.age_edit = QLineEdit()
        grid.addWidget(self.age_edit, 1, 1)
        
        layout.addLayout(grid)
        submit_btn = QPushButton("Submit")
        submit_btn.clicked.connect(self.submit_profile)
        layout.addWidget(submit_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(layout)
        
    def submit_profile(self):
        # Confirmation dialog box for profile submission
        QMessageBox.information(self, "Confirmation", "Profile Saved!")

class ContentPage(QWidget):
    """Content/Activity Window.
       HCI Rationale: Minimalistic and engaging layout for interactive tasks."""
    def __init__(self, theme):
        super().__init__()
        self.theme = theme
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        label = QLabel("Content / Activity")
        label.setFont(self.theme["font"])
        label.setStyleSheet(f"color: {self.theme['fg']};")
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        activity_btn = QPushButton("Start Activity")
        activity_btn.clicked.connect(self.start_activity)
        layout.addWidget(activity_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(layout)
        
    def start_activity(self):
        # Informational dialog box for activity start
        QMessageBox.information(self, "Information", "Activity Started!")

class SettingsPage(QWidget):
    """Settings/Preferences Window.
       HCI Rationale: Provides consistency and reduces cognitive load through clear options."""
    def __init__(self, theme):
        super().__init__()
        self.theme = theme
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        label = QLabel("Settings / Preferences")
        label.setFont(self.theme["font"])
        label.setStyleSheet(f"color: {self.theme['fg']};")
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        theme_btn = QPushButton("Change Theme (Not Implemented)")
        theme_btn.clicked.connect(self.theme_not_implemented)
        layout.addWidget(theme_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(layout)
        
    def theme_not_implemented(self):
        # Warning dialog box
        QMessageBox.warning(self, "Warning", "Theme change not implemented.")

class HelpPage(QWidget):
    """Help/Support Window.
       HCI Rationale: Provides accessible support with FAQs and contact information."""
    def __init__(self, theme):
        super().__init__()
        self.theme = theme
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        label = QLabel("Help / Support")
        label.setFont(self.theme["font"])
        label.setStyleSheet(f"color: {self.theme['fg']};")
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        faq_btn = QPushButton("FAQ")
        faq_btn.clicked.connect(lambda: QMessageBox.information(self, "FAQ", "Frequently Asked Questions..."))
        contact_btn = QPushButton("Contact Support")
        contact_btn.clicked.connect(lambda: QMessageBox.information(self, "Contact", "Support Contact: support@example.com"))
        layout.addWidget(faq_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(contact_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(layout)

class MainWindow(QMainWindow):
    """Main application window with navigation.
       HCI Rationale: Consistency, clear navigation, and immediate feedback through dialog boxes."""
    def __init__(self, theme):
        super().__init__()
        self.theme = theme
        self.setWindowTitle("Multi-Age Interface Application")
        self.resize(600, 400)
        self.apply_theme()
        self.init_ui()
        
    def apply_theme(self):
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(self.theme["bg"]))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(self.theme["fg"]))
        self.setPalette(palette)
        
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Navigation bar
        nav_layout = QHBoxLayout()
        btn_home = QPushButton("Home")
        btn_home.clicked.connect(lambda: self.display_page(0))
        btn_profile = QPushButton("Profile")
        btn_profile.clicked.connect(lambda: self.display_page(1))
        btn_content = QPushButton("Content")
        btn_content.clicked.connect(lambda: self.display_page(2))
        btn_settings = QPushButton("Settings")
        btn_settings.clicked.connect(lambda: self.display_page(3))
        btn_help = QPushButton("Help")
        btn_help.clicked.connect(lambda: self.display_page(4))
        
        # Set font for navigation buttons
        for btn in [btn_home, btn_profile, btn_content, btn_settings, btn_help]:
            btn.setFont(self.theme["font"])
        
        nav_layout.addWidget(btn_home)
        nav_layout.addWidget(btn_profile)
        nav_layout.addWidget(btn_content)
        nav_layout.addWidget(btn_settings)
        nav_layout.addWidget(btn_help)
        main_layout.addLayout(nav_layout)
        
        # Stacked widget to hold different pages
        self.stack = QStackedWidget()
        self.stack.addWidget(HomePage(self.theme))
        self.stack.addWidget(ProfilePage(self.theme))
        self.stack.addWidget(ContentPage(self.theme))
        self.stack.addWidget(SettingsPage(self.theme))
        self.stack.addWidget(HelpPage(self.theme))
        main_layout.addWidget(self.stack)
        
    def display_page(self, index):
        self.stack.setCurrentIndex(index)

def main():
    app = QApplication(sys.argv)
    
    # Launch the Age Selection Dialog
    age_dialog = AgeSelectionDialog()
    if age_dialog.exec() == QDialog.DialogCode.Accepted and age_dialog.selected_age:
        chosen_age = age_dialog.selected_age
        theme = themes[chosen_age]
    else:
        sys.exit()  # Exit if no age group is selected
    
    # Create and show the main window with the chosen theme
    window = MainWindow(theme)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
