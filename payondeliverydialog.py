

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *

class Ui_paymentonDeliveryDialog(object):
    def setupUi(self, paymentonDeliveryDialog):
        paymentonDeliveryDialog.setObjectName("paymentonDeliveryDialog")
        paymentonDeliveryDialog.resize(466, 162)
        self.label = QtWidgets.QLabel(parent=paymentonDeliveryDialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 161, 21))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.locationcomboBox = QtWidgets.QComboBox(parent=paymentonDeliveryDialog)
        self.locationcomboBox.setGeometry(QtCore.QRect(200, 40, 261, 22))
        self.locationcomboBox.setObjectName("locationcomboBox")
        self.submitLoccationpushButton = QtWidgets.QPushButton(parent=paymentonDeliveryDialog)
        self.submitLoccationpushButton.setGeometry(QtCore.QRect(360, 100, 93, 28))
        self.submitLoccationpushButton.setObjectName("submitLoccationpushButton")
        
        self.submitLoccationpushButton.clicked.connect(self.submitLoccationpushButtonclicked)
        self.updatecombobox()

        self.retranslateUi(paymentonDeliveryDialog)
        QtCore.QMetaObject.connectSlotsByName(paymentonDeliveryDialog)

    def retranslateUi(self, paymentonDeliveryDialog):
        _translate = QtCore.QCoreApplication.translate
        paymentonDeliveryDialog.setWindowTitle(_translate("paymentonDeliveryDialog", "PAY-ON-DELIVERY"))
        self.label.setText(_translate("paymentonDeliveryDialog", "Choose You Location"))
        self.submitLoccationpushButton.setText(_translate("paymentonDeliveryDialog", "Submit"))
        
        
    #updatecombobox
    def updatecombobox(self):
        kenyan_counties = [
    "Baringo", "Bomet", "Bungoma", "Busia", "Elgeyo Marakwet", "Embu", "Garissa", "Homa Bay", 
    "Isiolo", "Kajiado", "Kakamega", "Kericho", "Kiambu", "Kilifi", "Kirinyaga", "Kisii", 
    "Kisumu", "Kitui", "Kwale", "Laikipia", "Lamu", "Machakos", "Makueni", "Mandera", 
    "Marsabit", "Meru", "Migori", "Mombasa", "Murang'a", "Nairobi City", "Nakuru", 
    "Nandi", "Narok", "Nyamira", "Nyandarua", "Nyeri", "Samburu", "Siaya", "Taita Taveta", 
    "Tana River", "Tharaka Nithi", "Trans Nzoia", "Turkana", "Uasin Gishu", "Vihiga", 
    "Wajir", "West Pokot"
]
        self.locationcomboBox.addItems(kenyan_counties)
        
    #submitLoccationpushButtonclicked
    def submitLoccationpushButtonclicked(self):
        import random
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        random_day = random.choice(days_of_week)
        county=self.locationcomboBox.currentText()
        QMessageBox.information(None,"Success",f"You Order will be Delivered To {county} Agrimesh Official store\n On {random_day}")
        QtWidgets.QApplication.instance().activeWindow().close()
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    paymentonDeliveryDialog = QtWidgets.QDialog()
    ui = Ui_paymentonDeliveryDialog()
    ui.setupUi(paymentonDeliveryDialog)
    paymentonDeliveryDialog.show()
    sys.exit(app.exec())
