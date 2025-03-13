import sys
import pyttsx3
import threading
import queue
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont, QColor, QPalette


class VisuallyImpairedAssistant(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize text-to-speech (TTS) engine
        self.tts = pyttsx3.init()
        self.tts.setProperty('rate', 150)

        # Speech queue
        self.speech_queue = queue.Queue()
        self.speech_thread = threading.Thread(target=self.process_speech_queue, daemon=True)
        self.speech_thread.start()

        # Window settings
        self.setWindowTitle("Keyboard Voice Assistant")
        self.setGeometry(200, 200, 600, 300)
        self.setStyleSheet("background-color: #222831; color: #EEEEEE;")

        # Layout
        layout = QVBoxLayout()

        # Label for instructions
        self.label = QLabel("🖊️ Start typing... Press ESC to exit.", self)
        self.label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.label.setStyleSheet("color: #FFD369;")  # Highlighted color
        layout.addWidget(self.label)

        # Line Edit for user input
        self.input_field = QLineEdit(self)
        self.input_field.setFont(QFont("Arial", 16))
        self.input_field.setStyleSheet("background-color: #393E46; color: #00ADB5; padding: 8px; border-radius: 5px;")
        layout.addWidget(self.input_field)

        # Connect key press event
        self.input_field.keyPressEvent = self.handle_key_press

        # Timer for reading full text after inactivity
        self.idle_timer = QTimer(self)
        self.idle_timer.setInterval(5000)  # 5 seconds delay
        self.idle_timer.timeout.connect(self.read_full_text)

        self.setLayout(layout)

        # Store typed text
        self.typed_text = ""

    def handle_key_press(self, event):
        key = event.key()
        key_text = self.get_key_name(event)

        if key == Qt.Key.Key_Escape:  # Exit on ESC key
            self.speech_queue.put("Exiting system.")
            QApplication.quit()
            return

        self.speech_queue.put(key_text)  # Speak the pressed key
        self.typed_text += key_text if len(key_text) == 1 else " "  # Store text

        self.idle_timer.start()  # Restart idle timer
        QLineEdit.keyPressEvent(self.input_field, event)  # Pass event to default handler

    def get_key_name(self, event):
        """Return the readable name of the pressed key."""
        key_mapping = {
            Qt.Key.Key_Backspace: "Backspace",
            Qt.Key.Key_Return: "Enter",
            Qt.Key.Key_Space: "Space",
            Qt.Key.Key_Shift: "Shift",
            Qt.Key.Key_Control: "Control",
            Qt.Key.Key_Alt: "Alt",
            Qt.Key.Key_Tab: "Tab",
            Qt.Key.Key_CapsLock: "Caps Lock",
            Qt.Key.Key_Delete: "Delete",
            Qt.Key.Key_Up: "Arrow Up",
            Qt.Key.Key_Down: "Arrow Down",
            Qt.Key.Key_Left: "Arrow Left",
            Qt.Key.Key_Right: "Arrow Right",
        }
        return key_mapping.get(event.key(), event.text())

    def read_full_text(self):
        """Read the full typed sentence after 5 seconds of inactivity."""
        if self.typed_text.strip():
            self.speech_queue.put(f"You typed: {self.typed_text}")
        self.idle_timer.stop()

    def process_speech_queue(self):
        """Continuously process speech requests from the queue."""
        while True:
            text = self.speech_queue.get()
            self.tts.say(text)
            self.tts.runAndWait()
            self.speech_queue.task_done()


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VisuallyImpairedAssistant()
    window.show()
    sys.exit(app.exec())
