

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import  *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 91, 16))
        self.label.setObjectName("label")
        self.usernamelineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.usernamelineEdit.setGeometry(QtCore.QRect(180, 40, 191, 22))
        self.usernamelineEdit.setObjectName("usernamelineEdit")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 91, 16))
        self.label_2.setObjectName("label_2")
        self.passwordlineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.passwordlineEdit.setGeometry(QtCore.QRect(180, 120, 191, 22))
        self.passwordlineEdit.setObjectName("passwordlineEdit")
        self.agecomboBox = QtWidgets.QComboBox(parent=Dialog)
        self.agecomboBox.setGeometry(QtCore.QRect(180, 180, 73, 22))
        self.agecomboBox.setObjectName("agecomboBox")
        self.agecomboBox.addItem("")
        self.agecomboBox.addItem("")
        self.LOGINpushButton = QtWidgets.QPushButton(parent=Dialog)
        self.LOGINpushButton.setGeometry(QtCore.QRect(180, 240, 93, 28))
        self.LOGINpushButton.setObjectName("LOGINpushButton")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 131, 20))
        self.label_3.setObjectName("label_3")
        self.LOGINpushButton.clicked.connect(self.LOGINpushButtonclicked)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LOGIN PAGE"))
        self.label.setText(_translate("Dialog", "username"))
        self.label_2.setText(_translate("Dialog", "password"))
        self.agecomboBox.setItemText(0, _translate("Dialog", "Over 18"))
        self.agecomboBox.setItemText(1, _translate("Dialog", "Under 18"))
        self.LOGINpushButton.setText(_translate("Dialog", "LOGIN"))
        self.label_3.setText(_translate("Dialog", "Age"))
        
    def LOGINpushButtonclicked(self):
        username=self.usernamelineEdit.text()
        password=self.passwordlineEdit.text()
        age=self.agecomboBox.currentText()
        
        if not username or not password:
            QMessageBox.warning(None,"Error","All Fields are required")
            
        else:
            from farmersDashboard import Ui_MainWindow
            connection=Ui_MainWindow.connectagrimeshDB(self)
            cursor=connection.cursor()
            cursor.execute("""
                           
                           CREATE TABLE IF NOT EXISTS eltonlogin(
                               name VARCHAR(30),
                               password VARCHAR(20),
                               age VARCHAR(20)
                           )
                           """)
            
            cursor.execute("""
                           INSERT INTO eltonlogin(name,password,age) VALUES(%s,%s,%s);
                           
                           """,(username,password,age))
            connection.commit()
            QMessageBox.warning(None,"Success","Logged in successfully!")
            connection.close()
            cursor.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
