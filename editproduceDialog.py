
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
import psycopg2

class Ui_editproduceDialog(object):
    def setupUi(self, editproduceDialog):
        editproduceDialog.setObjectName("editproduceDialog")
        editproduceDialog.resize(384, 300)
        self.label = QtWidgets.QLabel(parent=editproduceDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.productnamelineEdit_editproduce = QtWidgets.QLineEdit(parent=editproduceDialog)
        self.productnamelineEdit_editproduce.setGeometry(QtCore.QRect(130, 10, 241, 22))
        self.productnamelineEdit_editproduce.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.productnamelineEdit_editproduce.setObjectName("productnamelineEdit_editproduce")
        self.label_2 = QtWidgets.QLabel(parent=editproduceDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 16))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.quantitylinedit_editproduce = QtWidgets.QLineEdit(parent=editproduceDialog)
        self.quantitylinedit_editproduce.setGeometry(QtCore.QRect(130, 50, 241, 22))
        self.quantitylinedit_editproduce.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.quantitylinedit_editproduce.setObjectName("quantitylinedit_editproduce")
        self.label_3 = QtWidgets.QLabel(parent=editproduceDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 111, 16))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.pricelinedit_editproduce = QtWidgets.QLineEdit(parent=editproduceDialog)
        self.pricelinedit_editproduce.setGeometry(QtCore.QRect(130, 100, 241, 22))
        self.pricelinedit_editproduce.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.pricelinedit_editproduce.setObjectName("pricelinedit_editproduce")
        self.label_4 = QtWidgets.QLabel(parent=editproduceDialog)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 111, 16))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.locationlinedit_editproduce = QtWidgets.QLineEdit(parent=editproduceDialog)
        self.locationlinedit_editproduce.setGeometry(QtCore.QRect(130, 150, 241, 22))
        self.locationlinedit_editproduce.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.locationlinedit_editproduce.setObjectName("locationlinedit_editproduce")
        self.editandsavepushButton_editproduce = QtWidgets.QPushButton(parent=editproduceDialog)
        self.editandsavepushButton_editproduce.setGeometry(QtCore.QRect(130, 190, 131, 28))
        self.editandsavepushButton_editproduce.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.editandsavepushButton_editproduce.setObjectName("editandsavepushButton_editproduce")

        

        self.retranslateUi(editproduceDialog)
        QtCore.QMetaObject.connectSlotsByName(editproduceDialog)
        
    #fill in the line edits
    def fillInLineEdits(self,details):
        product_name, category, quantity, price, location = details

        self.productnamelineEdit_editproduce.setText(details[0])
        self.quantitylinedit_editproduce.setText(details[2])
        self.pricelinedit_editproduce.setText(details[3])
        self.locationlinedit_editproduce.setText(details[4])
        
    #editandsavepushButton_editproduceClicked
    def editandsavepushButton_editproduceClicked(self,details):
        try:
            connection=psycopg2.connect(
                
                user="postgres",
                host="localhost",
                password="3062",
                database="agrimesh"
            )
            if not self.productnamelineEdit_editproduce.text() or not self.quantitylinedit_editproduce.text() or not self.pricelinedit_editproduce.text() or not self.locationlinedit_editproduce.text():
                QMessageBox.information(None,"Error","All Fields Are Required!")
                return
            cursor=connection.cursor()
            cursor.execute("""
                           UPDATE produce SET productname=%s,quantity=%s,price=%s,location=%s 
                           WHERE productname=%s;
                           """,(self.productnamelineEdit_editproduce.text(),self.quantitylinedit_editproduce.text(),int(self.pricelinedit_editproduce.text()),self.locationlinedit_editproduce.text(),details[0]))
            
            
            
            connection.commit()
            QMessageBox.information(None,"Success","Produce Edited And Saved Successfully!")
            
            QtWidgets.QApplication.instance().activeWindow().close()
            cursor.close()
            connection.close()
        except psycopg2.Error as e:
            QMessageBox.warning(None,"Error",f"Error Occurred: {e}")

    def retranslateUi(self, editproduceDialog):
        _translate = QtCore.QCoreApplication.translate
        editproduceDialog.setWindowTitle(_translate("editproduceDialog", "Edit Produce"))
        self.label.setText(_translate("editproduceDialog", "Product Name"))
        self.label_2.setText(_translate("editproduceDialog", "Quantity"))
        self.label_3.setText(_translate("editproduceDialog", "Price"))
        self.label_4.setText(_translate("editproduceDialog", "Location"))
        self.editandsavepushButton_editproduce.setText(_translate("editproduceDialog", "Edit and Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editproduceDialog = QtWidgets.QDialog()
    ui = Ui_editproduceDialog()
    ui.setupUi(editproduceDialog)
    editproduceDialog.show()
    sys.exit(app.exec())
