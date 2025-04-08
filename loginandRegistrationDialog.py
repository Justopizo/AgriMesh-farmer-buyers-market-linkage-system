from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
import psycopg2
from datetime import datetime

class Ui_loginOrregistrationDialog(object):
    def setupUi(self, loginOrregistrationDialog):
        loginOrregistrationDialog.setObjectName("loginOrregistrationDialog")
        loginOrregistrationDialog.resize(400, 340)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginOrregistrationDialog.sizePolicy().hasHeightForWidth())
        loginOrregistrationDialog.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(parent=loginOrregistrationDialog)
        self.label.setGeometry(QtCore.QRect(80, 10, 231, 31))
        self.label.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=loginOrregistrationDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 331, 21))
        self.label_2.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=loginOrregistrationDialog)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 91, 31))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.usernamelineEdit = QtWidgets.QLineEdit(parent=loginOrregistrationDialog)
        self.usernamelineEdit.setGeometry(QtCore.QRect(120, 90, 271, 31))
        self.usernamelineEdit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.usernamelineEdit.setObjectName("usernamelineEdit")
        self.label_4 = QtWidgets.QLabel(parent=loginOrregistrationDialog)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 91, 41))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.passswordlinedit = QtWidgets.QLineEdit(parent=loginOrregistrationDialog)
        self.passswordlinedit.setGeometry(QtCore.QRect(120, 140, 271, 31))
        self.passswordlinedit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.passswordlinedit.setText("")
        self.passswordlinedit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passswordlinedit.setObjectName("passswordlinedit")
        self.label_5 = QtWidgets.QLabel(parent=loginOrregistrationDialog)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 91, 51))
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.rolecomboBox = QtWidgets.QComboBox(parent=loginOrregistrationDialog)
        self.rolecomboBox.setGeometry(QtCore.QRect(120, 200, 271, 31))
        self.rolecomboBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.rolecomboBox.setObjectName("rolecomboBox")
        self.rolecomboBox.addItem("")
        self.rolecomboBox.addItem("")
        self.rolecomboBox.addItem("")
        self.name=""
        self.LoginpushButton = QtWidgets.QPushButton(parent=loginOrregistrationDialog)
        self.LoginpushButton.setGeometry(QtCore.QRect(160, 260, 93, 28))
        self.LoginpushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.LoginpushButton.clicked.connect(self.LoginpushButtonclicked)
        self.LoginpushButton.setObjectName("LoginpushButton")
        self.registerPushButton = QtWidgets.QPushButton(parent=loginOrregistrationDialog)
        self.registerPushButton.setGeometry(QtCore.QRect(280, 260, 93, 28))
        self.registerPushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.registerPushButton.setObjectName("registerPushButton")
        
        self.registerPushButton.clicked.connect(self.registerPushButtonClicked)
        
        self.forgotpassword = QtWidgets.QLabel(parent=loginOrregistrationDialog)
        self.forgotpassword.setGeometry(QtCore.QRect(160, 290, 161, 41))
        self.forgotpassword.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.forgotpassword.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.forgotpassword.setObjectName("forgotpassword")
        self.forgotpassword.linkActivated.connect(self.forgotpasswordLinkActivated)

        self.retranslateUi(loginOrregistrationDialog)
        QtCore.QMetaObject.connectSlotsByName(loginOrregistrationDialog)
    
    #forgotpasswordLinkActivated
    def forgotpasswordLinkActivated(self):
        from resetpassword import Ui_forgotpasswordDialog
        self.reset = QtWidgets.QMainWindow()
        self.ui = Ui_forgotpasswordDialog()
        self.ui.setupUi(self.reset)
        self.reset.setFixedSize(347, 258)
        self.reset.show()
        
    
    #LoginpushButtonclicked
    def LoginpushButtonclicked(self):
        name=self.usernamelineEdit.text().lower()
        password=self.passswordlinedit.text()
        role=self.rolecomboBox.currentText()
        
        if not name or not password :
            
            QMessageBox.warning(None,"Error","All Fields Are Required!")
            
            return  
        elif len(password)>4: 
            QMessageBox.warning(None,"Error","Password must be less than 4 characters")
            self.passswordlinedit.setPlaceholderText("Password must be less than 4 characters") 
            return
        else:
            try:
                connection=psycopg2.connect(
                    host="localhost",
                    user="postgres",
                    password="3062",
                    database="agrimesh"
                    
                )
                cursor=connection.cursor()
                
                cursor.execute("SELECT * FROM userinfo WHERE name=%s;", (name,))
                useralreadyExists=cursor.fetchone()
                
                if useralreadyExists:
                    password2=useralreadyExists[1]
                    if password!=password2:
                            QMessageBox.information(None,"Wrong Password","Wrong Password")
                            return
                    
                    role2=useralreadyExists[2]
                    if role!=role2:
                        QMessageBox.information(None,"Wrong role","User Found, but Role Does Not Match!")
                        return
                    description = f"{name} logged into the system as {role} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                    cursor.execute("INSERT INTO loginlogs(description) VALUES(%s);",(description,))
                    connection.commit()
                    if role=="Farmer":
                        QMessageBox.information(None,"Success","Login Successfully\nWelcome Back Our Valued Farmer.Let's Grow Together!")
                         
                        from farmersDashboard import Ui_MainWindow
                        self.farmerdash = QtWidgets.QMainWindow()
                        self.ui = Ui_MainWindow()
                        self.ui.setupUi(self.farmerdash)
                        self.farmerdash.setFixedSize(953, 717)
                        self.farmerdash.show()
                        QtWidgets.QApplication.instance().activeWindow().close()
                        
                    elif role=="Buyer":
                        QMessageBox.information(None,"Success","Login Successfully\nWelcome Back Our Valued Buyer.Find The Best Deals Today!")
                        
                        from buyerDashboard import Ui_buyerDashboardDialog
                        self.buyerdash = QtWidgets.QMainWindow()
                        self.ui = Ui_buyerDashboardDialog()
                        self.ui.setupUi(self.buyerdash)
                        self.buyerdash.setFixedSize(954, 719)
                        self.buyerdash.show()
                        QtWidgets.QApplication.instance().activeWindow().close()
                
                        
                    else:
                        QMessageBox.information(None,"Success","Login Successfully\nWelcome Back Our Master Admin!")
                        from adminDashboard import Ui_admnidashboardDialog
                        self.admindash = QtWidgets.QMainWindow()
                        self.ui = Ui_admnidashboardDialog()
                        self.ui.setupUi(self.admindash)
                        self.admindash.setFixedSize(954, 713)
                        self.admindash.show()
                        QtWidgets.QApplication.instance().activeWindow().close()
                       
                else:
                    QMessageBox.information(None,"Error","User Doesn't Exist!\nPlease Register")
                connection.close()
                cursor.close()
            except psycopg2.Error as e:
                QMessageBox.warning(None,"Error",f"Error Occured {e}")
                
    #registerPushButtonClicked
    def registerPushButtonClicked(self):
        name=self.usernamelineEdit.text().lower()
        password=self.passswordlinedit.text()
        role=self.rolecomboBox.currentText()
        
        if not name or not password :
            QMessageBox.warning(None,"Error","All Fields Are Required!")
            self.passswordlinedit.setPlaceholderText("Password must be less than 4 characters")
            return
        elif len(password)>4:
            QMessageBox.warning(None,"Error","Password must be less than 4 characters")
            self.passswordlinedit.setPlaceholderText("Password must be less than 4 characters")
            return
        else:
            connection=psycopg2.connect(
                host="localhost",
                user="postgres",
                password="3062",
                database="agrimesh"
            )
            cursor=connection.cursor()
            cursor.execute("""
                               CREATE TABLE IF NOT EXISTS userinfo(
                                   name VARCHAR(20),
                                   password VARCHAR(20),
                                   role VARCHAR(20)
                               )
                               """)
            connection.commit()
            cursor.execute("SELECT * FROM userinfo WHERE name=%s;",(name,))
            useralreadyExists=cursor.fetchone()
            
            if useralreadyExists:
                QMessageBox.warning(None,"User Exists","UserName Already Exists.Please Choose a Different one!")
                
            else:
                cursor.execute("""
                               INSERT INTO userinfo(name,password,role) 
                               VALUES(%s,%s,%s) 
                               """,(name,password,role))
                connection.commit()
                QMessageBox.information(None,"Success","Registration Successful!")
                cursor.execute("CREATE TABLE IF NOT EXISTS loginlogs(description VARCHAR(1000))")
                description = f"{name} Registered into the system as {role} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                cursor.execute("INSERT INTO loginlogs(description) VALUES(%s);",(description,))
                connection.commit()
                if role=="Farmer":
                    
                    from farmersDashboard import Ui_MainWindow
                    self.farmerdash = QtWidgets.QMainWindow()
                    self.ui = Ui_MainWindow()
                    self.ui.setupUi(self.farmerdash)
                    self.farmerdash.setFixedSize(953, 717)
                    self.farmerdash.show()
                    QtWidgets.QApplication.instance().activeWindow().close()
                    self.name=self.usernamelineEdit.text().lower()
                   
                    
                elif role=="Buyer":
                    from buyerDashboard import Ui_buyerDashboardDialog
                    self.buyerdash = QtWidgets.QMainWindow()
                    self.ui = Ui_buyerDashboardDialog()
                    self.ui.setupUi(self.buyerdash)
                    self.buyerdash.setFixedSize(954, 719)
                    self.buyerdash.show()
                    QtWidgets.QApplication.instance().activeWindow().close()
                    
                else:
                    from adminDashboard import Ui_admnidashboardDialog
                    self.admindash = QtWidgets.QMainWindow()
                    self.ui = Ui_admnidashboardDialog()
                    self.ui.setupUi(self.admindash)
                    self.admindash.setFixedSize(954, 713)
                    self.admindash.show()
                    QtWidgets.QApplication.instance().activeWindow().close()
                                        
    

    def retranslateUi(self, loginOrregistrationDialog):
        _translate = QtCore.QCoreApplication.translate
        loginOrregistrationDialog.setWindowTitle(_translate("loginOrregistrationDialog", "LOGIN"))
        self.label.setText(_translate("loginOrregistrationDialog", "Welcome To AgriMesh"))
        self.label_2.setText(_translate("loginOrregistrationDialog", "A web Of Seamless Farm-To-Market Connections"))
        self.label_3.setText(_translate("loginOrregistrationDialog", "User Name"))
        self.usernamelineEdit.setPlaceholderText(_translate("loginOrregistrationDialog", "e.g justopizo01"))
        self.label_4.setText(_translate("loginOrregistrationDialog", "Password"))
        self.passswordlinedit.setPlaceholderText(_translate("loginOrregistrationDialog", "Enter Four Digit Password"))
        self.label_5.setText(_translate("loginOrregistrationDialog", "Role"))
        self.rolecomboBox.setItemText(0, _translate("loginOrregistrationDialog", "Farmer"))
        self.rolecomboBox.setItemText(1, _translate("loginOrregistrationDialog", "Buyer"))
        self.rolecomboBox.setItemText(2, _translate("loginOrregistrationDialog", "Admin"))
        self.LoginpushButton.setText(_translate("loginOrregistrationDialog", "Login"))
        self.registerPushButton.setText(_translate("loginOrregistrationDialog", "Register"))
        self.forgotpassword.setText(_translate("loginOrregistrationDialog", "<a href=\"#\">Forgot Password?</a>"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginOrregistrationDialog = QtWidgets.QDialog()
    ui = Ui_loginOrregistrationDialog()
    ui.setupUi(loginOrregistrationDialog)
    loginOrregistrationDialog.show()
    sys.exit(app.exec())
"""