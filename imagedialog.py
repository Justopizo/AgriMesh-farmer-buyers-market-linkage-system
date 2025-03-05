


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_imageDialog_admin(object):
    def setupUi(self, imageDialog_admin):
        imageDialog_admin.setObjectName("imageDialog_admin")
        imageDialog_admin.resize(264, 265)
        self.imagelabel = QtWidgets.QLabel(parent=imageDialog_admin)
        self.imagelabel.setGeometry(QtCore.QRect(0, 0, 251, 261))
        self.imagelabel.setText("")
        self.imagelabel.setObjectName("imagelabel")

        self.retranslateUi(imageDialog_admin)
        QtCore.QMetaObject.connectSlotsByName(imageDialog_admin)

    def retranslateUi(self, imageDialog_admin):
        _translate = QtCore.QCoreApplication.translate
        imageDialog_admin.setWindowTitle(_translate("imageDialog_admin", "Product Image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    imageDialog_admin = QtWidgets.QDialog()
    ui = Ui_imageDialog_admin()
    ui.setupUi(imageDialog_admin)
    imageDialog_admin.show()
    sys.exit(app.exec())
