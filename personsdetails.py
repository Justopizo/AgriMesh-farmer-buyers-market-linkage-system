


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(405, 241)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 55, 41))
        self.label.setObjectName("label")
        self.namelinedit = QtWidgets.QLineEdit(parent=Dialog)
        self.namelinedit.setGeometry(QtCore.QRect(70, 40, 311, 22))
        self.namelinedit.setObjectName("namelinedit")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 51, 16))
        self.label_2.setObjectName("label_2")
        self.GENDERCOMBOBOX = QtWidgets.QComboBox(parent=Dialog)
        self.GENDERCOMBOBOX.setGeometry(QtCore.QRect(70, 90, 311, 22))
        self.GENDERCOMBOBOX.setObjectName("GENDERCOMBOBOX")
        self.submitbutton = QtWidgets.QPushButton(parent=Dialog)
        self.submitbutton.setGeometry(QtCore.QRect(290, 160, 93, 28))
        self.submitbutton.setObjectName("submitbutton")
        self.submitbutton.clicked.connect(self.submitbuttonclicked)
        self.gender=("Male","Female")
        self.GENDERCOMBOBOX.addItems(self.gender)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "details"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "GENDER"))
        self.submitbutton.setText(_translate("Dialog", "SUBMIT"))
        
    #submitbuttonclicked
    def submitbuttonclicked(self):
        name=self.namelinedit.text()
        gender=self.GENDERCOMBOBOX.currentText()
        
        if not name:
            QMessageBox.information(None,"Error","Name is required!")
            return
        else:
            QMessageBox.information(None,"Hi",f"welcome {name}\n You Are a {gender}")
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
