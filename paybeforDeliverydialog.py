


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *

class Ui_paybeforedeliveryDialog(object):
    def setupUi(self, paybeforedeliveryDialog):
        paybeforedeliveryDialog.setObjectName("paybeforedeliveryDialog")
        paybeforedeliveryDialog.resize(495, 146)
        self.label = QtWidgets.QLabel(parent=paybeforedeliveryDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.paypushbutton = QtWidgets.QPushButton(parent=paybeforedeliveryDialog)
        self.paypushbutton.setGeometry(QtCore.QRect(400, 70, 93, 28))
        self.paypushbutton.setObjectName("paypushbutton")
        self.mpesaPhoneNolinedit = QtWidgets.QLineEdit(parent=paybeforedeliveryDialog)
        self.mpesaPhoneNolinedit.setGeometry(QtCore.QRect(230, 20, 251, 22))
        self.mpesaPhoneNolinedit.setObjectName("mpesaPhoneNolinedit")
        
        self.paypushbutton.clicked.connect(self.paypushbuttonclicked)
        self.mpesaPhoneNolinedit.setPlaceholderText("e.g 254793031269")
        self.is_connected()



        self.retranslateUi(paybeforedeliveryDialog)
        QtCore.QMetaObject.connectSlotsByName(paybeforedeliveryDialog)

    def retranslateUi(self, paybeforedeliveryDialog):
        _translate = QtCore.QCoreApplication.translate
        paybeforedeliveryDialog.setWindowTitle(_translate("paybeforedeliveryDialog", "PAY-BEFORE DELIVERY"))
        self.label.setText(_translate("paybeforedeliveryDialog", "M-PESA PHONE NUMBER"))
        self.paypushbutton.setText(_translate("paybeforedeliveryDialog", "Pay"))
        
        
        #cconnect to internet
    def is_connected(self):
        import socket
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=5)
            return True
        except (OSError, socket.error):  
            return False
    
        
    #paypushbuttonclicked
    def paypushbuttonclicked(self):
        phoneno=self.mpesaPhoneNolinedit.text()
        
        if not phoneno:
             QMessageBox.information(None,"Error","Phone Number Cannot be Empty")
             return
        
        if phoneno.startswith("254"):
            if not self.is_connected():
                    QMessageBox.warning(None, "Network Error", "No internet connection detected! Please check your connection.")
                    return

            if self.is_connected():
                import access_token
                access_token.LipanaMpesaPpassword.phoneno=phoneno
                import mpesa
                mpesa.lipa_na_mpesa_online(access_token.request)
            
            else:
                QMessageBox.information(None,"Internet Error","Please consider connecting to Internet (wifi or data connection) !!")
                return
        else:
            QMessageBox.information(None,"Error","Phone Number must Start With This Format : 254XXXX")
            return
            
       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    paybeforedeliveryDialog = QtWidgets.QDialog()
    ui = Ui_paybeforedeliveryDialog()
    ui.setupUi(paybeforedeliveryDialog)
    paybeforedeliveryDialog.show()
    sys.exit(app.exec())
