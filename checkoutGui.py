
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *

class Ui_checkOutDialog(object):
    def setupUi(self, checkOutDialog):
        checkOutDialog.setObjectName("checkOutDialog")
        checkOutDialog.resize(438, 591)
        self.label = QtWidgets.QLabel(parent=checkOutDialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=checkOutDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 91, 21))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=checkOutDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 91, 21))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=checkOutDialog)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 91, 21))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=checkOutDialog)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 91, 21))
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.imageOfProducelabel_checkoutdialog = QtWidgets.QLabel(parent=checkOutDialog)
        self.imageOfProducelabel_checkoutdialog.setGeometry(QtCore.QRect(150, 320, 200, 200))
        self.imageOfProducelabel_checkoutdialog.setStyleSheet("border: 1px solid black")
        self.imageOfProducelabel_checkoutdialog.setText("")
        self.imageOfProducelabel_checkoutdialog.setObjectName("imageOfProducelabel_checkoutdialog")
        self.label_6 = QtWidgets.QLabel(parent=checkOutDialog)
        self.label_6.setGeometry(QtCore.QRect(10, 300, 121, 21))
        self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=checkOutDialog)
        self.label_7.setGeometry(QtCore.QRect(10, 240, 121, 21))
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.checkoutpushButton = QtWidgets.QPushButton(parent=checkOutDialog)
        self.checkoutpushButton.setGeometry(QtCore.QRect(330, 540, 93, 28))
        self.checkoutpushButton.setObjectName("checkoutpushButton")
        self.buyerNamelineEdit = QtWidgets.QLineEdit(parent=checkOutDialog)
        self.buyerNamelineEdit.setGeometry(QtCore.QRect(110, 40, 311, 22))
        self.buyerNamelineEdit.setObjectName("buyerNamelineEdit")
        self.buyerphonenumberlineEdit = QtWidgets.QLineEdit(parent=checkOutDialog)
        self.buyerphonenumberlineEdit.setGeometry(QtCore.QRect(110, 80, 311, 22))
        self.buyerphonenumberlineEdit.setObjectName("buyerphonenumberlineEdit")
        self.productnamelineEdit = QtWidgets.QLineEdit(parent=checkOutDialog)
        self.productnamelineEdit.setGeometry(QtCore.QRect(110, 120, 311, 22))
        self.productnamelineEdit.setObjectName("productnamelineEdit")
        self.quantitylineeidtlineEdit = QtWidgets.QLineEdit(parent=checkOutDialog)
        self.quantitylineeidtlineEdit.setGeometry(QtCore.QRect(110, 160, 311, 22))
        self.quantitylineeidtlineEdit.setObjectName("quantitylineeidtlineEdit")
        self.pricelineEdit = QtWidgets.QLineEdit(parent=checkOutDialog)
        self.pricelineEdit.setGeometry(QtCore.QRect(110, 200, 311, 22))
        self.pricelineEdit.setObjectName("pricelineEdit")
        self.delierMethodcomboBox = QtWidgets.QComboBox(parent=checkOutDialog)
        self.delierMethodcomboBox.setGeometry(QtCore.QRect(150, 240, 271, 22))
        self.delierMethodcomboBox.setObjectName("delierMethodcomboBox")
        self.delierMethodcomboBox.addItem("")
        self.delierMethodcomboBox.addItem("")
        self.delierMethodcomboBox.addItem("")

        self.retranslateUi(checkOutDialog)
        QtCore.QMetaObject.connectSlotsByName(checkOutDialog)

    def retranslateUi(self, checkOutDialog):
        _translate = QtCore.QCoreApplication.translate
        checkOutDialog.setWindowTitle(_translate("checkOutDialog", "Check Out"))
        self.label.setText(_translate("checkOutDialog", "Your Name"))
        self.label_2.setText(_translate("checkOutDialog", "Phone No"))
        self.label_3.setText(_translate("checkOutDialog", "Product"))
        self.label_4.setText(_translate("checkOutDialog", "Quantity"))
        self.label_5.setText(_translate("checkOutDialog", "Price"))
        self.label_6.setText(_translate("checkOutDialog", "Product Image"))
        self.label_7.setText(_translate("checkOutDialog", "Delivery Method"))
        self.checkoutpushButton.setText(_translate("checkOutDialog", "Check Out"))
        self.delierMethodcomboBox.setItemText(0, _translate("checkOutDialog", "Payment On Delivery"))
        self.delierMethodcomboBox.setItemText(1, _translate("checkOutDialog", "Pay-Before-Delivery"))
        self.delierMethodcomboBox.setItemText(2, _translate("checkOutDialog", "As a Parcel"))
        
        #checkoutbuttonclicked
    def checkoutbuttonclicked(self,details):
        productname,quantity,price=details
        buyername=self.buyerNamelineEdit.text()
        phoneno=self.buyerphonenumberlineEdit.text()
        paymentmethod=self.delierMethodcomboBox.currentText().strip()
        import psycopg2
        if not buyername or not phoneno:
            QMessageBox.warning(None,"Error","All Fields Are Required!")
            return
        else:
            try:
                from farmersDashboard import Ui_MainWindow
                connection=Ui_MainWindow.connectagrimeshDB(self)
                
                cursor=connection.cursor()
                cursor.execute("""
                               CREATE TABLE IF NOT EXISTS vieworders(
                                   buyername VARCHAR(40),
                                   phoneno VARCHAR(20),
                                   productname VARCHAR(40) PRIMARY KEY,
                                   quantity VARCHAR(20),
                                   price INTEGER,
                                   paymentmethod VARCHAR(40)
                                   
                               )
                               
                               """)
                cursor.execute("""
                               INSERT INTO vieworders(buyername,phoneno,productname,quantity,price,paymentmethod)
                               VALUES(%s,%s,%s,%s,%s,%s) ON CONFLICT(productname) DO NOTHING;
                               """,(buyername,phoneno,productname,quantity,price,paymentmethod))
                
                connection.commit()
                if paymentmethod=="Payment On Delivery":
                    from payondeliverydialog import Ui_paymentonDeliveryDialog
                    
                    self.deliverygui=QtWidgets.QMainWindow()
                    self.ui = Ui_paymentonDeliveryDialog()
                    self.ui.setupUi(self.deliverygui)
                    self.deliverygui.setFixedSize(466, 162)
                    self.deliverygui.show()
                    
                    
                    
                elif paymentmethod=="Pay-Before-Delivery":
                    from paybeforDeliverydialog import Ui_paybeforedeliveryDialog
                    self.beforedelivery=QtWidgets.QMainWindow()
                    self.ui = Ui_paybeforedeliveryDialog()
                    self.ui.setupUi(self.beforedelivery)
                    self.beforedelivery.setFixedSize(495, 146)
                    self.beforedelivery.show()
                    
                    
                else:
                    QMessageBox.information(None,"Success","this is a parcel")
                
                
                cursor.close()
                connection.close()
            except psycopg2.Error as e:
                QMessageBox.warning(None,"Error",f"An Error Occurred {e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    checkOutDialog = QtWidgets.QDialog()
    ui = Ui_checkOutDialog()
    ui.setupUi(checkOutDialog)
    checkOutDialog.show()
    sys.exit(app.exec())
