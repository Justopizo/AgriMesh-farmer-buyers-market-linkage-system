from loginandRegistrationDialog import Ui_loginOrregistrationDialog
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class LoginRegistrationDialog(QWidget):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_loginOrregistrationDialog()
        self.ui.setupUi(self)
        

from PyQt6 import QtWidgets, QtGui
app = QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon("projectImage.ico")) 
window = LoginRegistrationDialog()
window.setFixedSize(400, 340)
window.show()
app.exec()
