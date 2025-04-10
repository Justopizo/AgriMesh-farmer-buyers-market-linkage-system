from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
import psycopg2

class Ui_forgotpasswordDialog(object):
    def setupUi(self, forgotpasswordDialog):
        forgotpasswordDialog.setObjectName("forgotpasswordDialog")
        forgotpasswordDialog.resize(347, 258)
        self.label = QtWidgets.QLabel(parent=forgotpasswordDialog)
        self.label.setGeometry(QtCore.QRect(100, 10, 181, 31))
        self.label.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=forgotpasswordDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.usernamePaasswordresetlinedit = QtWidgets.QLineEdit(parent=forgotpasswordDialog)
        self.usernamePaasswordresetlinedit.setGeometry(QtCore.QRect(100, 70, 241, 22))
        self.usernamePaasswordresetlinedit.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.usernamePaasswordresetlinedit.setObjectName("usernamePaasswordresetlinedit")
        self.usernamePaasswordresetlinedit.textChanged.connect(self.usernamePaasswordresetlinedittextChanged)
        self.label_3 = QtWidgets.QLabel(parent=forgotpasswordDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 111, 31))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.newpasswordlineit = QtWidgets.QLineEdit(parent=forgotpasswordDialog)
        self.newpasswordlineit.setGeometry(QtCore.QRect(130, 120, 211, 22))
        self.newpasswordlineit.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.newpasswordlineit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.newpasswordlineit.setObjectName("newpasswordlineit")
        self.label_4 = QtWidgets.QLabel(parent=forgotpasswordDialog)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 91, 21))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.resetcodeLinEdit = QtWidgets.QLineEdit(parent=forgotpasswordDialog)
        self.resetcodeLinEdit.setGeometry(QtCore.QRect(110, 170, 231, 22))
        self.resetcodeLinEdit.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.resetcodeLinEdit.setObjectName("resetcodeLinEdit")
        self.resetpushButton = QtWidgets.QPushButton(parent=forgotpasswordDialog)
        self.resetpushButton.setGeometry(QtCore.QRect(240, 210, 93, 28))
        self.resetpushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.resetpushButton.setObjectName("resetpushButton")
        self.resetpushButton.clicked.connect(self.resetpushButtonclicked)

        self.retranslateUi(forgotpasswordDialog)
        QtCore.QMetaObject.connectSlotsByName(forgotpasswordDialog)

    def retranslateUi(self, forgotpasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        forgotpasswordDialog.setWindowTitle(_translate("forgotpasswordDialog", "Reset Password"))
        self.label.setText(_translate("forgotpasswordDialog", "Reset Password"))
        self.label_2.setText(_translate("forgotpasswordDialog", "UserName"))
        self.usernamePaasswordresetlinedit.setPlaceholderText(_translate("forgotpasswordDialog", "e.g justo"))
        self.label_3.setText(_translate("forgotpasswordDialog", "new password"))
        self.newpasswordlineit.setPlaceholderText(_translate("forgotpasswordDialog", "four digit password"))
        self.label_4.setText(_translate("forgotpasswordDialog", "Reset Code"))
        self.resetpushButton.setText(_translate("forgotpasswordDialog", "Reset"))
        
    #usernamePaasswordresetlinedittextChanged
    def usernamePaasswordresetlinedittextChanged(self):
        self.resetcodeLinEdit.setReadOnly(True)
        if not self.resetcodeLinEdit.text():
            import random
            code=str(random.randint(1000,9999))
            self.resetcodeLinEdit.setText(code)
        
    
    
    #resetpushButtonclicked
    def resetpushButtonclicked(self):
        try:
            usernamReset=self.usernamePaasswordresetlinedit.text().lower()
            newpassword=self.newpasswordlineit.text()
            resetcode=self.resetcodeLinEdit.text()
           
            if not usernamReset or not newpassword or not resetcode:
                QMessageBox.warning(None,"Error","All Fields Are Required!")
                return
                
            if len(newpassword)>4:
                QMessageBox.warning(None,"Error","Password Must Be below 4 characters!")
                return
                    
            connection=psycopg2.connect(
                host="localhost",
                user="postgres",
                password="3062",
                database="agrimesh"
            )
            cursor=connection.cursor()
            cursor.execute("SELECT 1 FROM userinfo WHERE name=%s; ",(usernamReset,))
            itExist=cursor.fetchone()
            
            if itExist:
                    cursor.execute("SELECT password FROM userinfo WHERE name=%s; ",(usernamReset,))
                    findsamepass=cursor.fetchone()
                    if findsamepass and findsamepass[0] == newpassword:
                        QMessageBox.information(None,"Error","You can't Use Your Old password as New Password!")
                        return
                        
                    cursor.execute("UPDATE userinfo SET password=%s WHERE name=%s;",(newpassword,usernamReset))
                    QMessageBox.information(None,"Success","Password Reset Successful!")
                    connection.commit()
                    QtWidgets.QApplication.instance().activeWindow().close()
            else:
                QMessageBox.warning(None,"Error","User Doesn't Exist !")
            
            connection.commit()
            connection.close()
            cursor.close()
        except psycopg2.Error as e :
            QMessageBox.warning(None,"Error",f"An error occured {e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    forgotpasswordDialog = QtWidgets.QDialog()
    ui = Ui_forgotpasswordDialog()
    ui.setupUi(forgotpasswordDialog)
    forgotpasswordDialog.show()
    sys.exit(app.exec())
