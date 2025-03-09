


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(292, 166)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 111, 51))
        self.label.setObjectName("label")
        self.agelineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.agelineEdit.setGeometry(QtCore.QRect(140, 40, 113, 31))
        self.agelineEdit.setObjectName("agelineEdit")
        self.CalculateagepushButton = QtWidgets.QPushButton(parent=Dialog)
        self.CalculateagepushButton.setGeometry(QtCore.QRect(160, 100, 93, 28))
        self.CalculateagepushButton.setObjectName("CalculateagepushButton")
        
        self.CalculateagepushButton.clicked.connect(self.CalculateagepushButtonclicked)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AGE CALCULATOR"))
        self.label.setText(_translate("Dialog", "ENTER YOUR YOB"))
        self.CalculateagepushButton.setText(_translate("Dialog", "CALCULATE"))
        
    #CalculateagepushButtonclicked
    def CalculateagepushButtonclicked(self):
        yob=self.agelineEdit.text()
        
        if not yob:
            QMessageBox.critical(None,"Error","YOB field cannot be empty!")
            return
        else:
            yob=int(yob)
            age=2025-yob
            QMessageBox.information(None,"Age",f"You are {age} years old")
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
