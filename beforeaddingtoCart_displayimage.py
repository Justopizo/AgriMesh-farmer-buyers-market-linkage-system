
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox
import os
class Ui_productimageDialog(object):
    def setupUi(self, productimageDialog):
        productimageDialog.setObjectName("productimageDialog")
        productimageDialog.resize(319, 300)
        self.imagelabel = QtWidgets.QLabel(parent=productimageDialog)
        self.imagelabel.setGeometry(QtCore.QRect(0, 0, 311, 281))
        self.imagelabel.setText("")
        self.imagelabel.setObjectName("imagelabel")


        self.retranslateUi(productimageDialog)
        QtCore.QMetaObject.connectSlotsByName(productimageDialog)

    def retranslateUi(self, productimageDialog):
        _translate = QtCore.QCoreApplication.translate
        productimageDialog.setWindowTitle(_translate("productimageDialog", "Product Image"))
        
    
    def imagelabelSetImage(self,imagepath):
        if not imagepath or not os.path.exists(imagepath):
            QMessageBox.warning(None, "Error", "Image not found!")
            return

        pixmap = QPixmap(imagepath)
        self.imagelabel.setPixmap(pixmap)
        self.imagelabel.setScaledContents(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    productimageDialog = QtWidgets.QDialog()
    ui = Ui_productimageDialog()
    ui.setupUi(productimageDialog)
    productimageDialog.show()
    sys.exit(app.exec())
