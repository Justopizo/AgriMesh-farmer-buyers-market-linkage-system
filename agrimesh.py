from loginandRegistrationDialog import Ui_loginOrregistrationDialog
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class LoginRegistrationDialog(QWidget):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_loginOrregistrationDialog()
        self.ui.setupUi(self)


app = QApplication(sys.argv)
window = LoginRegistrationDialog()
window.show()
app.exec()
