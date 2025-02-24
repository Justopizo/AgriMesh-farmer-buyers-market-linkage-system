
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *

class Ui_deleteaccountdialog(object):
    def setupUi(self, deleteaccountdialog):
        deleteaccountdialog.setObjectName("deleteaccountdialog")
        deleteaccountdialog.resize(375, 146)
        self.label = QtWidgets.QLabel(parent=deleteaccountdialog)
        self.label.setGeometry(QtCore.QRect(90, 0, 161, 31))
        self.label.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=deleteaccountdialog)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 91, 16))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.username_deleteaccountlinedit = QtWidgets.QLineEdit(parent=deleteaccountdialog)
        self.username_deleteaccountlinedit.setGeometry(QtCore.QRect(120, 60, 251, 22))
        self.username_deleteaccountlinedit.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.username_deleteaccountlinedit.setObjectName("username_deleteaccountlinedit")
        self.deleteaccountpushbuttton = QtWidgets.QPushButton(parent=deleteaccountdialog)
        self.deleteaccountpushbuttton.setGeometry(QtCore.QRect(230, 100, 131, 28))
        self.deleteaccountpushbuttton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.deleteaccountpushbuttton.setObjectName("deleteaccountpushbuttton")
        self.connectagrimeshDB()
        self.deleteaccountpushbuttton.clicked.connect(self.deleteaccountpushbutttonclicked)

        self.retranslateUi(deleteaccountdialog)
        QtCore.QMetaObject.connectSlotsByName(deleteaccountdialog)

    def retranslateUi(self, deleteaccountdialog):
        _translate = QtCore.QCoreApplication.translate
        deleteaccountdialog.setWindowTitle(_translate("deleteaccountdialog", "Delete Account"))
        self.label.setText(_translate("deleteaccountdialog", "Delete Account"))
        self.label_3.setText(_translate("deleteaccountdialog", "Username"))
        self.deleteaccountpushbuttton.setText(_translate("deleteaccountdialog", "Delete"))
        
    #deleteaccountpushbutttonclicked
    def deleteaccountpushbutttonclicked(self):
        name=self.username_deleteaccountlinedit.text().lower()
        if not name:
            QMessageBox.information(None,"Error","Please Fill in The user Name!")
            return
        connection=self.connectagrimeshDB()
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM userinfo WHERE name=%s ;",(name,))
        exists=cursor.fetchone()
        
        if exists:
            from plyer import notification
            notification.notify(
                title="Account Deleted Successfully!!!",
                message="IT is Sad To see You Leave!",
                app_name="AgriMesh Company",
                timeout=600
            )
            cursor.execute("DELETE FROM userinfo WHERE name=%s;", (name,))
            connection.commit()
            QMessageBox.information(None,"Error","Account deleted successfully")
            
            from loginandRegistrationDialog import Ui_loginOrregistrationDialog
            self.loginwindow = QtWidgets.QMainWindow()
            self.ui = Ui_loginOrregistrationDialog()
            self.ui.setupUi(self.loginwindow)
            self.loginwindow.setFixedSize(400, 340)
            self.loginwindow.show()
            QtWidgets.QApplication.instance().activeWindow().close()
            
        else:
            QMessageBox.information(None,"Error","You have put a wrong Username!")
        
    def connectagrimeshDB(self):
        import psycopg2
        connection=psycopg2.connect(
                host="localhost",
                user="postgres",
                password="3062",
                database="agrimesh"
        )
        return connection
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deleteaccountdialog = QtWidgets.QDialog()
    ui = Ui_deleteaccountdialog()
    ui.setupUi(deleteaccountdialog)
    deleteaccountdialog.show()
    sys.exit(app.exec())
