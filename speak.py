import sys
import pyttsx3
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class AccessibleApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize text-to-speech engine before UI
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 150)
        except Exception as e:
            print(f"Error initializing pyttsx3: {e}")
            self.engine = None

        self.initUI()  # Now it's safe to call UI setup

    def initUI(self):
        self.setWindowTitle("Accessible User Interface")
        self.setGeometry(300, 200, 400, 200)

        # Create layout
        layout = QVBoxLayout()

        # Create label
        self.label = QLabel("Welcome to the Accessible User Interface. Please select an option.")
        layout.addWidget(self.label)

        # Create buttons
        self.option_one_button = QPushButton("Option One")
        self.option_one_button.clicked.connect(self.option_one)
        layout.addWidget(self.option_one_button)

        self.option_two_button = QPushButton("Option Two")
        self.option_two_button.clicked.connect(self.option_two)
        layout.addWidget(self.option_two_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.exit_app)
        layout.addWidget(self.exit_button)

        self.setLayout(layout)

        # Speak welcome message (only if engine is available)
        if self.engine:
            self.speak("Welcome to the Accessible User Interface. Please select an option.")

    def speak(self, text):
        """Speak the given text using pyttsx3"""
        if self.engine:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                print(f"Speech Error: {e}")

    def option_one(self):
        self.speak("You have selected Option One.")
        self.label.setText("You are now in Option One.")

    def option_two(self):
        self.speak("You have selected Option Two.")
        self.label.setText("You are now in Option Two.")

    def exit_app(self):
        self.speak("Exiting the application. Goodbye!")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AccessibleApp()
    window.show()
    sys.exit(app.exec())
