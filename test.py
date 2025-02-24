from PyQt6 import QtCore, QtWidgets
import psycopg2


DB_HOST = "localhost"
DB_USER = "postgres"
DB_PASSWORD = "3062"
TARGET_DB = "quickrideCompany"

def create_table_if_not_exists():
  
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=TARGET_DB
        )
        cur = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS userLogin (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL,
            role VARCHAR(20) NOT NULL
        )
        """
        cur.execute(create_table_query)
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error creating table: {e}")

class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        loginDialog.setObjectName("loginDialog")
        loginDialog.resize(369, 308)

        self.label = QtWidgets.QLabel(parent=loginDialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 341, 41))
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label.setText("Welcome to QuickRide Bus Company")

        self.label_2 = QtWidgets.QLabel(parent=loginDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 91, 21))
        self.label_2.setText("User Name")

        self.label_3 = QtWidgets.QLabel(parent=loginDialog)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 91, 31))
        self.label_3.setText("Password")

        self.usernamelineEdit = QtWidgets.QLineEdit(parent=loginDialog)
        self.usernamelineEdit.setGeometry(QtCore.QRect(130, 80, 221, 22))

        self.passwordLinedit = QtWidgets.QLineEdit(parent=loginDialog)
        self.passwordLinedit.setGeometry(QtCore.QRect(130, 120, 221, 22))
        self.passwordLinedit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.label_4 = QtWidgets.QLabel(parent=loginDialog)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 91, 31))
        self.label_4.setText("Role")

        self.adminCheckBox = QtWidgets.QCheckBox(parent=loginDialog)
        self.adminCheckBox.setGeometry(QtCore.QRect(130, 170, 95, 20))
        self.adminCheckBox.setText("Admin")

        self.travellerCheckBox = QtWidgets.QCheckBox(parent=loginDialog)
        self.travellerCheckBox.setGeometry(QtCore.QRect(220, 170, 95, 20))
        self.travellerCheckBox.setText("Traveller")

        self.loginButton = QtWidgets.QPushButton(parent=loginDialog)
        self.loginButton.setGeometry(QtCore.QRect(130, 220, 93, 28))
        self.loginButton.setText("Login")

        self.registerButton = QtWidgets.QPushButton(parent=loginDialog)
        self.registerButton.setGeometry(QtCore.QRect(230, 220, 93, 28))
        self.registerButton.setText("Register")

        self.commandLinkButton = QtWidgets.QCommandLinkButton(parent=loginDialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(120, 250, 222, 48))
        self.commandLinkButton.setText("Forgot Password?")

        self.retranslateUi(loginDialog)
        QtCore.QMetaObject.connectSlotsByName(loginDialog)

        self.loginButton.clicked.connect(self.login_user)
        self.registerButton.clicked.connect(self.registerButtonClicked)
        self.commandLinkButton.clicked.connect(self.commandLinkButtonClicked)

        self.adminCheckBox.stateChanged.connect(self.role_selection_changed)
        self.travellerCheckBox.stateChanged.connect(self.role_selection_changed)

    def retranslateUi(self, loginDialog):
        loginDialog.setWindowTitle("LOGIN")

    def role_selection_changed(self):
       
        if self.adminCheckBox.isChecked() and self.travellerCheckBox.isChecked():
            
            if self.adminCheckBox.hasFocus():
                self.travellerCheckBox.setChecked(False)
            elif self.travellerCheckBox.hasFocus():
                self.adminCheckBox.setChecked(False)

    def get_selected_role(self):
       
        if self.adminCheckBox.isChecked():
            return "Admin"
        elif self.travellerCheckBox.isChecked():
            return "Traveller"
        return None

    def login_user(self):
        username = self.usernamelineEdit.text().strip().lower()  
        password = self.passwordLinedit.text().strip()
        role = self.get_selected_role()

        if not username or not password:
            QtWidgets.QMessageBox.critical(None, "Input Error", "Username and Password cannot be empty.")
            return

        if not role:
            QtWidgets.QMessageBox.critical(None, "Input Error", "Please select a role.")
            return

        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=TARGET_DB
            )
            cur = conn.cursor()
            cur.execute("SELECT password, role FROM userLogin WHERE username = %s", (username,))
            result = cur.fetchone()

            if result:
                stored_password, stored_role = result
                if stored_password == password:
                    if role == stored_role:
                        QtWidgets.QMessageBox.information(None, "Login Successful", f"Welcome, {role}!")
                        
                        if role == "Admin":
                            pass
                        else:
                            from travellerDashboard import Ui_MainWindow
                            self.travellerwindow = QtWidgets.QMainWindow()
                            self.ui = Ui_MainWindow()
                            self.ui.setupUi(self.travellerwindow)
                            self.travellerwindow.setFixedSize(1021, 806)
                            self.travellerwindow.show()
                            
                            QtWidgets.QApplication.instance().activeWindow().close()
                        
                    else:
                        QtWidgets.QMessageBox.warning(None, "Login Failed", "Role mismatch.")
                else:
                    QtWidgets.QMessageBox.warning(None, "Login Failed", "Incorrect password.")
            else:
                QtWidgets.QMessageBox.warning(None, "Login Failed", "User does not exist! Please register.")

            cur.close()
            conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Database Error", f"Error logging in: {e}")

    def registerButtonClicked(self):
        username = self.usernamelineEdit.text().strip().lower()  
        password = self.passwordLinedit.text().strip() 
        role = self.get_selected_role()

        if not username or not password:
            QtWidgets.QMessageBox.critical(None, "Error", "All fields are required!")
            return

        if not role:
            QtWidgets.QMessageBox.critical(None, "Error", "Please select a role.")
            return

        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=TARGET_DB
            )
            cur = conn.cursor()
            cur.execute("SELECT username FROM userLogin WHERE username = %s", (username,))
            result = cur.fetchone()

            if result:
                QtWidgets.QMessageBox.information(None, "Error", "User already exists. Please log in!")
            else:
                cur.execute("INSERT INTO userLogin (username, password, role) VALUES (%s, %s, %s)", 
                            (username, password, role))
                conn.commit()
                QtWidgets.QMessageBox.information(None, "Success", "Registration successful!")
                
                if role == "Admin":
                    pass
                else:
                    from travellerDashboard import Ui_MainWindow
                    self.travellerwindow = QtWidgets.QMainWindow()
                    self.ui = Ui_MainWindow()
                    self.ui.setupUi(self.travellerwindow)
                    self.travellerwindow.setFixedSize(1021, 806)
                    self.travellerwindow.show()
                            
                    QtWidgets.QApplication.instance().activeWindow().close()

            cur.close()
            conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Database Error", f"Error registering: {e}")
    
    def commandLinkButtonClicked(self):
        from forgotpassword import Ui_ChangePasswordDialog
        self.resetWindow = QtWidgets.QMainWindow()
        self.ui = Ui_ChangePasswordDialog()
        self.ui.setupUi(self.resetWindow)
        self.resetWindow.setFixedSize(248, 257)
        self.resetWindow.show()
  
if __name__ == "__main__":
    import sys
    create_table_if_not_exists()
    app = QtWidgets.QApplication(sys.argv)
    loginDialog = QtWidgets.QDialog()
    ui = Ui_loginDialog()
    ui.setupUi(loginDialog)
    loginDialog.show()
    sys.exit(app.exec())
