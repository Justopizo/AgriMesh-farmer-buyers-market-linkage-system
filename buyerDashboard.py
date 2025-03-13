
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import *
import psycopg2
from functools import partial
from farmersDashboard import Ui_MainWindow
from PyQt6.QtGui import QIcon

class Ui_buyerDashboardDialog(object):
    def setupUi(self, buyerDashboardDialog):
        buyerDashboardDialog.setObjectName("buyerDashboardDialog")
        buyerDashboardDialog.resize(954, 719)
        
        self.widget = QtWidgets.QWidget(parent=buyerDashboardDialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 261, 711))
        self.widget.setStyleSheet("background-color: rgb(31, 0, 93);")
        self.widget.setObjectName("widget")
        self.widget1 = QtWidgets.QWidget(parent=self.widget)
        self.widget1.setGeometry(QtCore.QRect(0, 10, 251, 681))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dashboardwidgetpushButton = QtWidgets.QPushButton(parent=self.widget1)
        self.dashboardwidgetpushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.dashboardwidgetpushButton.setObjectName("dashboardwidgetpushButton")
        self.dashboardwidgetpushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.verticalLayout.addWidget(self.dashboardwidgetpushButton)
        self.browseproductspushbutton = QtWidgets.QPushButton(parent=self.widget1)
        self.browseproductspushbutton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.browseproductspushbutton.setObjectName("browseproductspushbutton")
        self.browseproductspushbutton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.verticalLayout.addWidget(self.browseproductspushbutton)
        self.myorderspushbutton = QtWidgets.QPushButton(parent=self.widget1)
        self.myorderspushbutton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.myorderspushbutton.setObjectName("myorderspushbutton")
        self.myorderspushbutton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.verticalLayout.addWidget(self.myorderspushbutton)
        self.cartpushbutton = QtWidgets.QPushButton(parent=self.widget1)
        self.cartpushbutton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.cartpushbutton.setObjectName("cartpushbutton")
        self.cartpushbutton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.verticalLayout.addWidget(self.cartpushbutton)
        self.paymentpushbutton = QtWidgets.QPushButton(parent=self.widget1)
        self.paymentpushbutton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.paymentpushbutton.setObjectName("paymentpushbutton")
        self.paymentpushbutton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.verticalLayout.addWidget(self.paymentpushbutton)
        self.profilepushbutton = QtWidgets.QPushButton(parent=self.widget1)
        self.profilepushbutton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.profilepushbutton.setObjectName("profilepushbutton")
        self.verticalLayout.addWidget(self.profilepushbutton)
        self.profilepushbutton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.settingspushbutton = QtWidgets.QPushButton(parent=self.widget1)
        self.settingspushbutton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.settingspushbutton.setObjectName("settingspushbutton")
        self.verticalLayout.addWidget(self.settingspushbutton)
        self.settingspushbutton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.logoutbutton = QtWidgets.QPushButton(parent=self.widget1)
        self.logoutbutton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.logoutbutton.setObjectName("logoutbutton")
        self.logoutbutton.clicked.connect(self.logoutbuttonclicked)
        self.verticalLayout.addWidget(self.logoutbutton)
        self.widget_2 = QtWidgets.QWidget(parent=buyerDashboardDialog)
        self.widget_2.setGeometry(QtCore.QRect(260, 0, 691, 711))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_2.setObjectName("widget_2")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget_2)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 671, 701))
        self.stackedWidget.setObjectName("stackedWidget")
        self.dashboardpage = QtWidgets.QWidget()
        self.dashboardpage.setObjectName("dashboardpage")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.dashboardpage)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 0, 361, 231))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_26 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_26.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_26.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_26.setObjectName("label_26")
        self.totalorderslcdNumber = QtWidgets.QLCDNumber(parent=self.groupBox_3)
        self.totalorderslcdNumber.setGeometry(QtCore.QRect(10, 60, 64, 31))
        self.totalorderslcdNumber.setObjectName("totalorderslcdNumber")
        self.label_27 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_27.setGeometry(QtCore.QRect(150, 30, 121, 16))
        self.label_27.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_27.setObjectName("label_27")
        self.ordersInCartLCDnumber = QtWidgets.QLCDNumber(parent=self.groupBox_3)
        self.ordersInCartLCDnumber.setGeometry(QtCore.QRect(160, 60, 64, 31))
        self.ordersInCartLCDnumber.setObjectName("ordersInCartLCDnumber")
        self.label_28 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_28.setGeometry(QtCore.QRect(10, 120, 111, 16))
        self.label_28.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_28.setObjectName("label_28")
        self.cancelledordersLCDdisplay = QtWidgets.QLCDNumber(parent=self.groupBox_3)
        self.cancelledordersLCDdisplay.setGeometry(QtCore.QRect(10, 140, 64, 31))
        self.cancelledordersLCDdisplay.setObjectName("cancelledordersLCDdisplay")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.dashboardpage)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 240, 361, 231))
        self.groupBox_4.setObjectName("groupBox_4")
        self.settingscommandLinkButton_dashboard = QtWidgets.QCommandLinkButton(parent=self.groupBox_4)
        self.settingscommandLinkButton_dashboard.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.settingscommandLinkButton_dashboard.setGeometry(QtCore.QRect(10, 20, 222, 48))
        self.settingscommandLinkButton_dashboard.setObjectName("settingscommandLinkButton_dashboard")
        self.profilecommandLinkButton = QtWidgets.QCommandLinkButton(parent=self.groupBox_4)
        self.profilecommandLinkButton.setGeometry(QtCore.QRect(10, 80, 222, 48))
        self.profilecommandLinkButton.setObjectName("profilecommandLinkButton")
        self.profilecommandLinkButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.cartCommandlinkbutton = QtWidgets.QCommandLinkButton(parent=self.groupBox_4)
        self.cartCommandlinkbutton.setGeometry(QtCore.QRect(10, 140, 222, 48))
        self.cartCommandlinkbutton.setObjectName("cartCommandlinkbutton")
        self.cartCommandlinkbutton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.label_2 = QtWidgets.QLabel(parent=self.dashboardpage)
        self.label_2.setGeometry(QtCore.QRect(30, 680, 271, 21))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.dashboardpage)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 480, 361, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.helpandsupporttextEdit = QtWidgets.QTextEdit(parent=self.groupBox_2)
        self.helpandsupporttextEdit.setGeometry(QtCore.QRect(0, 10, 361, 171))
        self.helpandsupporttextEdit.setObjectName("helpandsupporttextEdit")
        self.stackedWidget.addWidget(self.dashboardpage)
        self.browseproductspage = QtWidgets.QWidget()
        
        self.browseproductspage.setObjectName("browseproductspage")
        self.browseproductsTableWidget = QtWidgets.QTableWidget(parent=self.browseproductspage)
        self.browseproductsTableWidget.setGeometry(QtCore.QRect(0, 10, 681, 411))
        self.browseproductsTableWidget.setObjectName("browseproductsTableWidget")
        self.browseproductsTableWidget.setColumnCount(6)
        self.browseproductsTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.browseproductsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.browseproductsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.browseproductsTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.browseproductsTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.browseproductsTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.browseproductsTableWidget.setHorizontalHeaderItem(5, item)
        self.label_12 = QtWidgets.QLabel(parent=self.browseproductspage)
        self.label_12.setGeometry(QtCore.QRect(10, 460, 241, 21))
        self.label_12.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.searchproductLinedit = QtWidgets.QLineEdit(parent=self.browseproductspage)
        self.searchproductLinedit.setGeometry(QtCore.QRect(260, 460, 331, 22))
        self.searchproductLinedit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        
        self.searchproductLinedit.textChanged.connect(self.searchproductLinedittextchabged)
        
        self.searchproductLinedit.setObjectName("searchproductLinedit")
        self.stackedWidget.addWidget(self.browseproductspage)
        self.myorderspage = QtWidgets.QWidget()
        self.myorderspage.setObjectName("myorderspage")
        self.browseproductsTableWidget_2 = QtWidgets.QTableWidget(parent=self.myorderspage)
        self.browseproductsTableWidget_2.setGeometry(QtCore.QRect(0, 10, 681, 411))
        self.browseproductsTableWidget_2.setObjectName("browseproductsTableWidget_2")
        self.browseproductsTableWidget_2.setColumnCount(4)
        self.browseproductsTableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.browseproductsTableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.browseproductsTableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.browseproductsTableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.browseproductsTableWidget_2.setHorizontalHeaderItem(3, item)
        self.stackedWidget.addWidget(self.myorderspage)
        self.cartpage = QtWidgets.QWidget()
        self.cartpage.setObjectName("cartpage")
        self.cart_table_Widget = QtWidgets.QTableWidget(parent=self.cartpage)
        self.cart_table_Widget.setGeometry(QtCore.QRect(0, 10, 681, 411))
        self.cart_table_Widget.setObjectName("cart_table_Widget")
        self.cart_table_Widget.setColumnCount(5)
        self.cart_table_Widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cart_table_Widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cart_table_Widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cart_table_Widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.cart_table_Widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.cart_table_Widget.setHorizontalHeaderItem(4, item)
        self.productsinCartLabel = QtWidgets.QLabel(parent=self.cartpage)
        self.productsinCartLabel.setGeometry(QtCore.QRect(20, 470, 181, 20))
        self.productsinCartLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.productsinCartLabel.setObjectName("productsinCartLabel")
        self.stackedWidget.addWidget(self.cartpage)
        self.paymentspage = QtWidgets.QWidget()
        self.paymentspage.setObjectName("paymentspage")
        self.cart_table_Widget_2 = QtWidgets.QTableWidget(parent=self.paymentspage)
        self.cart_table_Widget_2.setGeometry(QtCore.QRect(0, 10, 681, 411))
        self.cart_table_Widget_2.setObjectName("cart_table_Widget_2")
        self.cart_table_Widget_2.setColumnCount(3)
        self.cart_table_Widget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cart_table_Widget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cart_table_Widget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cart_table_Widget_2.setHorizontalHeaderItem(2, item)
        self.totalmoneyspentLabel_paymentpagelabel = QtWidgets.QLabel(parent=self.paymentspage)
        self.totalmoneyspentLabel_paymentpagelabel.setGeometry(QtCore.QRect(10, 450, 171, 20))
        self.totalmoneyspentLabel_paymentpagelabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.totalmoneyspentLabel_paymentpagelabel.setObjectName("totalmoneyspentLabel_paymentpagelabel")
        self.stackedWidget.addWidget(self.paymentspage)
        self.profilepage = QtWidgets.QWidget()
        self.profilepage.setObjectName("profilepage")
        self.groupBox = QtWidgets.QGroupBox(parent=self.profilepage)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 431, 251))
        self.groupBox.setObjectName("groupBox")
        self.label_19 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(10, 40, 51, 20))
        self.label_19.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.label_20.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(10, 120, 71, 20))
        self.label_21.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_21.setObjectName("label_21")
        self.namelineEdit_seettingspage = QtWidgets.QLineEdit(parent=self.groupBox)
        self.namelineEdit_seettingspage.setGeometry(QtCore.QRect(90, 40, 331, 22))
        self.namelineEdit_seettingspage.setObjectName("namelineEdit_seettingspage")
        self.locationlineEdit_seettingspage_2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.locationlineEdit_seettingspage_2.setGeometry(QtCore.QRect(90, 80, 331, 22))
        self.locationlineEdit_seettingspage_2.setObjectName("locationlineEdit_seettingspage_2")
        self.phoneNoineEdit_seettingspage_2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.phoneNoineEdit_seettingspage_2.setGeometry(QtCore.QRect(90, 120, 331, 22))
        self.phoneNoineEdit_seettingspage_2.setObjectName("phoneNoineEdit_seettingspage_2")
        self.updateprofilebutton = QtWidgets.QPushButton(parent=self.groupBox)
        self.updateprofilebutton.setGeometry(QtCore.QRect(320, 160, 93, 28))
        self.updateprofilebutton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.updateprofilebutton.setObjectName("updateprofilebutton")
        self.stackedWidget.addWidget(self.profilepage)
        self.settingspage = QtWidgets.QWidget()
        self.settingspage.setObjectName("settingspage")
        self.accountsettingsgroupBox = QtWidgets.QGroupBox(parent=self.settingspage)
        self.accountsettingsgroupBox.setGeometry(QtCore.QRect(10, 10, 371, 251))
        self.accountsettingsgroupBox.setObjectName("accountsettingsgroupBox")
        self.label_22 = QtWidgets.QLabel(parent=self.accountsettingsgroupBox)
        self.label_22.setGeometry(QtCore.QRect(10, 30, 131, 16))
        self.label_22.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(parent=self.accountsettingsgroupBox)
        self.label_23.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(parent=self.accountsettingsgroupBox)
        self.label_24.setGeometry(QtCore.QRect(10, 100, 91, 16))
        self.label_24.setObjectName("label_24")
        self.oldpasswordlineEdit_settings = QtWidgets.QLineEdit(parent=self.accountsettingsgroupBox)
        self.oldpasswordlineEdit_settings.setGeometry(QtCore.QRect(110, 60, 221, 22))
        self.oldpasswordlineEdit_settings.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.oldpasswordlineEdit_settings.setObjectName("oldpasswordlineEdit_settings")
        self.newpasswordlinedit_settings = QtWidgets.QLineEdit(parent=self.accountsettingsgroupBox)
        self.newpasswordlinedit_settings.setGeometry(QtCore.QRect(110, 100, 221, 22))
        self.newpasswordlinedit_settings.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.newpasswordlinedit_settings.setObjectName("newpasswordlinedit_settings")
        self.changePasswordpushButton = QtWidgets.QPushButton(parent=self.accountsettingsgroupBox)
        self.changePasswordpushButton.setGeometry(QtCore.QRect(110, 150, 93, 28))
        self.changePasswordpushButton.clicked.connect(self.changePasswordpushButtonClicked)
        self.changePasswordpushButton.setObjectName("changePasswordpushButton")
        self.stackedWidget.addWidget(self.settingspage)

        self.retranslateUi(buyerDashboardDialog)
        QtCore.QMetaObject.connectSlotsByName(buyerDashboardDialog)

    def retranslateUi(self, buyerDashboardDialog):
        _translate = QtCore.QCoreApplication.translate
        buyerDashboardDialog.setWindowTitle(_translate("buyerDashboardDialog", "Buyer-Agrimesh Company"))
        self.dashboardwidgetpushButton.setText(_translate("buyerDashboardDialog", "Dashboard"))
        self.browseproductspushbutton.setText(_translate("buyerDashboardDialog", "Market Place"))
        self.myorderspushbutton.setText(_translate("buyerDashboardDialog", "Orders History"))
        self.cartpushbutton.setText(_translate("buyerDashboardDialog", "Cart"))
        self.paymentpushbutton.setText(_translate("buyerDashboardDialog", "Payment History"))
        self.profilepushbutton.setText(_translate("buyerDashboardDialog", "Profile"))
        self.settingspushbutton.setText(_translate("buyerDashboardDialog", "Settings"))
        self.logoutbutton.setText(_translate("buyerDashboardDialog", "Logout"))
        self.groupBox_3.setTitle(_translate("buyerDashboardDialog", "Key Metrics"))
        self.label_26.setText(_translate("buyerDashboardDialog", "Total orders"))
        self.label_27.setText(_translate("buyerDashboardDialog", "orders in Cart"))
        self.label_28.setText(_translate("buyerDashboardDialog", "Cancelled Orders"))
        self.groupBox_4.setTitle(_translate("buyerDashboardDialog", "Quick Actions"))
        self.settingscommandLinkButton_dashboard.setText(_translate("buyerDashboardDialog", "Settings"))
        self.profilecommandLinkButton.setText(_translate("buyerDashboardDialog", "profile"))
        self.cartCommandlinkbutton.setText(_translate("buyerDashboardDialog", "Cart"))
        self.label_2.setText(_translate("buyerDashboardDialog", "WE ARE PROUD TO SERVE YOU"))
        self.groupBox_2.setTitle(_translate("buyerDashboardDialog", "HELP AND SUPPORT"))
        item = self.browseproductsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("buyerDashboardDialog", "Product Name"))
        item = self.browseproductsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("buyerDashboardDialog", "Category"))
        item = self.browseproductsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("buyerDashboardDialog", "Quantity"))
        item = self.browseproductsTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("buyerDashboardDialog", "Price"))
        item = self.browseproductsTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("buyerDashboardDialog", "Location"))
        item = self.browseproductsTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("buyerDashboardDialog", "Action"))
        self.label_12.setText(_translate("buyerDashboardDialog", "Search Your Preffered Product"))
        self.searchproductLinedit.setPlaceholderText(_translate("buyerDashboardDialog", "Type some words"))
        item = self.browseproductsTableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("buyerDashboardDialog", "Product Name"))
        item = self.browseproductsTableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("buyerDashboardDialog", "Quantity"))
        item = self.browseproductsTableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("buyerDashboardDialog", "Price"))
        item = self.browseproductsTableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("buyerDashboardDialog", "Action"))
        item = self.cart_table_Widget.horizontalHeaderItem(0)
        item.setText(_translate("buyerDashboardDialog", "Product Name"))
        item = self.cart_table_Widget.horizontalHeaderItem(1)
        item.setText(_translate("buyerDashboardDialog", "Quantity"))
        item = self.cart_table_Widget.horizontalHeaderItem(2)
        item.setText(_translate("buyerDashboardDialog", "Price"))
        item = self.cart_table_Widget.horizontalHeaderItem(3)
        item.setText(_translate("buyerDashboardDialog", "Action 1"))
        item = self.cart_table_Widget.horizontalHeaderItem(4)
        item.setText(_translate("buyerDashboardDialog", "Action 2"))
        self.productsinCartLabel.setText(_translate("buyerDashboardDialog", "Products in The Cart: "))
        item = self.cart_table_Widget_2.horizontalHeaderItem(0)
        item.setText(_translate("buyerDashboardDialog", "Product Name"))
        item = self.cart_table_Widget_2.horizontalHeaderItem(1)
        item.setText(_translate("buyerDashboardDialog", "Quantity"))
        item = self.cart_table_Widget_2.horizontalHeaderItem(2)
        item.setText(_translate("buyerDashboardDialog", "Price"))
        self.totalmoneyspentLabel_paymentpagelabel.setText(_translate("buyerDashboardDialog", "Total money Spent: "))
        self.groupBox.setTitle(_translate("buyerDashboardDialog", "Personal info"))
        self.label_19.setText(_translate("buyerDashboardDialog", "Name"))
        self.label_20.setText(_translate("buyerDashboardDialog", "Location"))
        self.label_21.setText(_translate("buyerDashboardDialog", "PhoneNo."))
        self.updateprofilebutton.setText(_translate("buyerDashboardDialog", "Update"))
        self.accountsettingsgroupBox.setTitle(_translate("buyerDashboardDialog", "Account Settings"))
        self.label_22.setText(_translate("buyerDashboardDialog", "Change Password"))
        self.label_23.setText(_translate("buyerDashboardDialog", "Old Password"))
        self.label_24.setText(_translate("buyerDashboardDialog", "New Password"))
        self.changePasswordpushButton.setText(_translate("buyerDashboardDialog", "Change"))
        
        self.updateprofilebutton.clicked.connect(self.updateprofilebuttonClicked)
        self.newpasswordlinedit_settings.setPlaceholderText("Less than 4 Characters")
        self.oldpasswordlineEdit_settings.setPlaceholderText("Less than 4 Characters")
        self.canceledoRders=0
        self.totalitemInCart=0
        self.totalorders=0
        
        
        self.updatepaymentTableWidget()
        self.updatebrowseproductsTableWidget2()
        self.updatebrowseproductsTableWidget()
        self.updatecart_TableWidget()
        self.timer = QTimer()
        self.timer.timeout.connect(self.updatebrowseproductsTableWidget)
        self.timer.timeout.connect(self.updatecart_TableWidget)
        self.timer.timeout.connect(self.updatebrowseproductsTableWidget2)
        self.timer.timeout.connect(self.scrollHelpAndSupportText)
        self.timer.timeout.connect(self.checkForCancelledOrders)
        #self.timer.timeout.connect(self.updatepaymentTableWidget)
        
        self.updateqlcdDisplays()
        
        self.timer.start(500) 
        self.cancelledordersLCDdisplay.display(self.canceledoRders)
        self.totalorderslcdNumber.display(self.totalorders)
        self.ordersInCartLCDnumber.display(self.totalitemInCart)

        self.help_text = """
<html>
<head>
    <style>
        body { text-align: center; font-family: Arial, sans-serif; }
        h2, h3 { margin: 5px; }
        p { margin: 2px; }
    </style>
</head>
<body>
    <h2>Help Line</h2>
    <p>Phone No: 07930312 69</p>
    <p>Email: justopizo01@gmail.com</p>
    <h3>Credits</h3>
    <p>Senior Developer and Designer: Justin Omare</p>
    <p>Team Members:</p>
    <p>Manyasa Elton - System Tester & Documentation</p>
    <p>Jerry Scotch - Frontend Designer</p>
    <p>Gloria Mongasi - Backend Developer</p>
    <p>Solomon Nyongesa - Database Administrator</p>
    <p>Godwin Kimutai - Python Developer</p>
    <p><em>Motto: Software that has no limits</em></p>
</body>
</html>
"""




        self.helpandsupporttextEdit.setHtml(self.help_text)
        self.helpandsupporttextEdit.setReadOnly(True)  






    def scrollHelpAndSupportText(self):
    
         scrollbar = self.helpandsupporttextEdit.verticalScrollBar()
         scrollbar.setValue(scrollbar.value() + 1)


         if scrollbar.value() >= scrollbar.maximum():
                scrollbar.setValue(0)
                
     

    def checkForCancelledOrders(self):
     try:
        connection = Ui_MainWindow.connectagrimeshDB(self)
        cursor = connection.cursor()
        
        cursor.execute("SELECT buyername, productname FROM vieworders WHERE status = 'Cancelled';")
        cancelled_orders = cursor.fetchall()

        if cancelled_orders:
            for order in cancelled_orders:
                buyername, productname = order
                message=f"Order for {productname} has been cancelled By The Farmer!."
                self.showNotification(message)
            
            cursor.execute("DELETE FROM vieworders WHERE status = 'Cancelled';")
            connection.commit()
        
        cursor.close()
        connection.close()
     except psycopg2.Error as e:
        print(f"Database Error: {e}")

    def showNotification(self, message):
         QMessageBox.warning(None, "Order Cancelled",message)


           


    #updateqlcdDisplays
    def updateqlcdDisplays(self):
        self.cancelledordersLCDdisplay.display(self.canceledoRders)
        self.totalorderslcdNumber.display(self.totalorders)
        self.ordersInCartLCDnumber.display(self.totalitemInCart)
            
    #changePasswordpushButtonClicked
    def changePasswordpushButtonClicked(self):
            oldpassword=self.oldpasswordlineEdit_settings.text()
            newpassword=self.newpasswordlinedit_settings.text()
            
            if not oldpassword or not newpassword:
                QMessageBox.information(None,"Error","All Fields are required!")
                return
            elif len(oldpassword)>4 or len(newpassword)>4:
                QMessageBox.information(None,"Error","Password Must be Below 4 Characters!")
                return
                    
            else:
                    try:
                        
                        connection=Ui_MainWindow.connectagrimeshDB(self)
                        cursor=connection.cursor()
                        cursor.execute("SELECT 1 FROM userinfo WHERE password=%s;",(oldpassword,))
                        userexists=cursor.fetchone()
                        if userexists:
                                cursor.execute("UPDATE userinfo SET password=%s WHERE password=%s;",(newpassword,oldpassword))
                                connection.commit()
                                QMessageBox.information(None,"Error","Passsword Changed Successfully!")
                        else:
                             QMessageBox.information(None,"Error","Incorrect Password!\nDoesnt exist in Our Database")   
                             return
                        cursor.close()
                        connection.close()
                    except psycopg2.Error as e:
                        QMessageBox.information(None,"Error",f"Error  Occured: {e}")
                    

    #updateprofilebuttonClicked
    def updateprofilebuttonClicked(self):
            name=self.namelineEdit_seettingspage.text().lower()
            location=self.locationlineEdit_seettingspage_2.text()
            phoneno=self.phoneNoineEdit_seettingspage_2.text()
            
            if not name or not location or not phoneno:
                    QMessageBox.information(None,"Error","All Fields are required!")
                    return
            else:
                    try:
                            connection=Ui_MainWindow.connectagrimeshDB(self)
                            cursor=connection.cursor()
                            cursor.execute("""CREATE TABLE IF NOT EXISTS buyerinfo(
                                    name VARCHAR(40),
                                    location VARCHAR(40),
                                    phoneno VARCHAR(20)
                                    )""")
                            cursor.execute("SELECT 1 FROM buyerinfo WHERE name=%s;",(name,))
                            connection.commit()
                            buyerexist=cursor.fetchone()
                            
                            if buyerexist:
                                QMessageBox.information(None,"Error","You had already Updated Your Profile!")
                            else:
                                    cursor.execute("INSERT INTO buyerinfo(name,location,phoneno) VALUES(%s,%s,%s);",(name,location,phoneno))
                                    QMessageBox.information(None,"Error","Profile Updated successfully!")
                                    connection.commit()
                            
                            
                            cursor.close()
                            connection.close()
                            
                    except psycopg2.Error as e:
                        QMessageBox.information(None,"Error",f"Error  Occured: {e}")

    #updatepaymentTableWidget
    def updatepaymentTableWidget(self):
            try:
                        connection = Ui_MainWindow.connectagrimeshDB(self)
                        cursor = connection.cursor()
                        cursor.execute(" SELECT productname,quantity,price  FROM vieworders")
                        results=cursor.fetchall()
                        total_price=0
                        self.cart_table_Widget_2.setRowCount(0)
                        for rowID,rowData in enumerate(results):
                                self.cart_table_Widget_2.insertRow(rowID)
                                for colID,colData in enumerate(rowData):
                                        self.cart_table_Widget_2.setItem(rowID,colID,QTableWidgetItem(str(colData)))
                        
                                total_price +=  int(rowData[2])  
                                total_row = self.cart_table_Widget_2.rowCount()
                                self.cart_table_Widget_2.insertRow(total_row)
                        self.cart_table_Widget_2.setItem(total_row, 0, QTableWidgetItem("Total Spent"))
                        self.cart_table_Widget_2.setItem(total_row, 2, QTableWidgetItem(str(total_price)))
                        self.totalmoneyspentLabel_paymentpagelabel.setText("Total Money Spent:  "+str(total_price))
 

                
                        cursor.close()
                        connection.close()

            except psycopg2.Error as e:
                   QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    #cancelorderbuttonClicked
    def cancelorderbuttonClicked(self,row):
        self.canceledoRders+=1
        details = []
        
        for col in range(3):  
            item = self.browseproductsTableWidget_2.item(row, col)
            details.append(item.text() if item else "")
        try:
            connection = Ui_MainWindow.connectagrimeshDB(self)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM vieworders WHERE productname=%s AND quantity=%s;", (details[0], details[1]))

            connection.commit()
            QMessageBox.information(None, "Success", "Order Cancelled successsfully Successfully!")
            
            self.updatebrowseproductsTableWidget2()
            self.updatecart_TableWidget()

            cursor.close()
            connection.close()

        except psycopg2.Error as e:
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")


       #updatebrowseproductsTableWidget2
    def updatebrowseproductsTableWidget2(self):
            try:
                connection=Ui_MainWindow.connectagrimeshDB(self)
                cursor=connection.cursor()
                cursor.execute("SELECT productname,quantity,price FROM vieworders")
                results=cursor.fetchall()
                
                self.browseproductsTableWidget_2.setRowCount(0)
                
                for rowID,rowData in enumerate(results):
                        self.browseproductsTableWidget_2.insertRow(rowID)
                        self.totalorders+=1
                        for colID,colData in enumerate(rowData):
                                self.browseproductsTableWidget_2.setItem(rowID,colID,QTableWidgetItem(str(colData)))
                                button=QPushButton("Cancel Order")
                                self.browseproductsTableWidget_2.setCellWidget(rowID,3,button)
                                button.clicked.connect(lambda _, r=rowID: self.cancelorderbuttonClicked(r))
                
                cursor.close()
                connection.close()
                
            except psycopg2.Error as e:
                    QMessageBox.information(None,"Error",f"Error {e}")

    #searchproductLinedittextchabged
    def searchproductLinedittextchabged(self,text):
        
        for row in range(self.browseproductsTableWidget.rowCount()):
            match = False
            for column in range(self.browseproductsTableWidget.columnCount()):
                item = self.browseproductsTableWidget.item(row, column)
                if item and text.lower() in item.text().lower():
                    match = True
                    break
            self.browseproductsTableWidget.setRowHidden(row, not match)
            
            
    #updatecart_TableWidget
    def updatecart_TableWidget(self):
        try:
            totalitem=0
            connection = Ui_MainWindow.connectagrimeshDB(self)
            cursor = connection.cursor()
            cursor.execute("SELECT productname, quantity, price FROM cart")
            results = cursor.fetchall()

            self.cart_table_Widget.setRowCount(0)

            if results:
                for rowID, rowData in enumerate(results):
                    self.cart_table_Widget.insertRow(rowID)
                    totalitem+=1
                    self.totalitemInCart+=1
                    for colID, colData in enumerate(rowData):
                        self.cart_table_Widget.setItem(rowID, colID, QTableWidgetItem(str(colData)))
                        

                    # Check Out Button
                    btn_edit = QPushButton("Check Out")
                    btn_edit.clicked.connect(partial(self.checkOut, rowID))
                    self.cart_table_Widget.setCellWidget(rowID, 3, btn_edit)

                    # Remove Product Button
                    removebtn = QPushButton("Remove Product")
                    removebtn.clicked.connect(partial(self.removeFromCart, rowID))
                    self.cart_table_Widget.setCellWidget(rowID, 4, removebtn)
           
            else:
                pass

            connection.commit()
            totalitem  =str(totalitem)     
            self.productsinCartLabel.setText(f"Products In Cart: {totalitem}")
            self.productsinCartLabel.setStyleSheet("font-size: 20px;")
            cursor.close()
            connection.close()

        except psycopg2.Error as e:
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    # Remove From Cart
    def removeFromCart(self, row):
        try:
            # Ensure row is valid
            if row >= self.cart_table_Widget.rowCount():
                QMessageBox.warning(None, "Error", "Invalid row selected!")
                return

            
            details = []
            for col in range(3):
                item = self.cart_table_Widget.item(row, col)
                details.append(item.text() if item else "")

            connection = Ui_MainWindow.connectagrimeshDB(self)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM cart WHERE productname=%s AND quantity=%s;", (details[0], details[1]))

            connection.commit()
            QMessageBox.information(None, "Success", "Product Removed Successfully!")
            self.updatecart_TableWidget()

            cursor.close()
            connection.close()

        except psycopg2.Error as e:
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    # Checkout Function
    def checkOut(self, row):
        try:
            if row >= self.cart_table_Widget.rowCount():
                QMessageBox.warning(None, "Error", "Invalid row selected!")
                return

            details = []
            for col in range(3):  
                item = self.cart_table_Widget.item(row, col)
                details.append(item.text() if item else "")

            connection = Ui_MainWindow.connectagrimeshDB(self)
            cursor = connection.cursor()

            from checkoutGui import Ui_checkOutDialog
            self.checkoutdialog = QtWidgets.QMainWindow()
            self.ui = Ui_checkOutDialog()
            self.ui.setupUi(self.checkoutdialog)
            self.checkoutdialog.setFixedSize(438, 591)
            self.checkoutdialog.show()
            self.ui.productnamelineEdit.setText(details[0])
            self.ui.quantitylineeidtlineEdit.setText(details[1])
            self.ui.pricelineEdit.setText(details[2])
            cursor.execute("""
    SELECT cart.productname, cart.quantity, cart.price, produce.imagepath 
    FROM cart 
    JOIN produce ON cart.productname = produce.productname
""")
            results = cursor.fetchall()
            
            
            for rowID, rowData in enumerate(results):
                        product_name, quantity, price, image_path = rowData
                        from PyQt6.QtGui import QPixmap
                        pixmap = QPixmap(image_path)
                        self.ui.imageOfProducelabel_checkoutdialog.setPixmap(pixmap)
                        self.ui.imageOfProducelabel_checkoutdialog.setScaledContents(True)
             
                        self.ui.checkoutpushButton.clicked.connect(lambda: self.ui.checkoutbuttonclicked(details))
                     
                        
            self.ui.productnamelineEdit.setReadOnly(True)
            self.ui.quantitylineeidtlineEdit.setReadOnly(True)
            self.ui.pricelineEdit.setReadOnly(True)

            cursor.close()
            connection.close()

        except psycopg2.Error as e:
            QMessageBox.warning(None, "Error", f"An error occurred: {e}")

    # Update Browse Products Table
    def updatebrowseproductsTableWidget(self):
        self.browseproductsTableWidget.setColumnCount(7)
        self.browseproductsTableWidget.setHorizontalHeaderLabels(
            ["Product Name", "Category", "Quantity", "Price", "Location", "Image", "Actions"]
        )
        try:
            connection = Ui_MainWindow.connectagrimeshDB(self)
            cursor = connection.cursor()
            cursor.execute("SELECT productname, category, quantity, price, location,imagepath FROM produce")
            results = cursor.fetchall()

            self.browseproductsTableWidget.setRowCount(0)

            for rowID, rowData in enumerate(results):
                self.browseproductsTableWidget.insertRow(rowID)
                for columnID in range(5):
                    self.browseproductsTableWidget.setItem(rowID, columnID, QTableWidgetItem(str(rowData[columnID])))

                image_path = rowData[5]
                imagebtn = QPushButton("View Image")
                imagebtn.clicked.connect(partial(self.displayproductimage, image_path))
                self.browseproductsTableWidget.setCellWidget(rowID, 5, imagebtn)
                btn_add = QPushButton("Add To Cart")
                btn_add.clicked.connect(partial(self.addToCart, rowID))
                self.browseproductsTableWidget.setCellWidget(rowID, 6, btn_add)
            self.searchproductLinedittextchabged(self.searchproductLinedit.text())
            cursor.close()
            connection.close()

        except psycopg2.Error as e:
            QMessageBox.warning(None, "Error", f"Error Occurred: {e}")
            
    #displayproductimage
    def displayproductimage(self,imagepath):
        from beforeaddingtoCart_displayimage import Ui_productimageDialog
        self.produceimagedilog = QtWidgets.QMainWindow()
        self.ui = Ui_productimageDialog()
        self.ui.setupUi(self.produceimagedilog)
        self.ui.imagelabelSetImage(imagepath)
        self.produceimagedilog.setFixedSize(319, 300)
        self.produceimagedilog.show()
            
    def addToCart(self,row):
        
        from farmersDashboard import Ui_MainWindow
        details = [self.browseproductsTableWidget.item(row, col).text() for col in range(5)]
        connection=Ui_MainWindow.connectagrimeshDB(self)
        cursor=connection.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS cart(
                               productname VARCHAR(200) PRIMARY KEY,
                               quantity VARCHAR(200),
                               price INTEGER
                               
                       )
                       """)
       
        productname=details[0]
        quantity=details[2]
        price=int(details[3])
        cursor.execute("""
                       INSERT INTO cart(productname,quantity,price)
                       VALUES(%s,%s,%s) ON CONFLICT(productname) DO NOTHING
                       """,(productname,quantity,price))
        connection.commit()
        QMessageBox.information(None,"Success","Product Added To Cart Successfully!")
        cursor.close()
        connection.close()
        
        
    
    #logoutbuttonclicked
    def logoutbuttonclicked(self):
        QMessageBox.information(None,"Logout","Are you sure you want to logout?")
        from loginandRegistrationDialog import Ui_loginOrregistrationDialog
        self.loginwindow = QtWidgets.QMainWindow()
        self.ui = Ui_loginOrregistrationDialog()
        self.ui.setupUi(self.loginwindow)
        self.loginwindow.setFixedSize(400, 340)
        self.loginwindow.show()
        QtWidgets.QApplication.instance().activeWindow().close()
        QMessageBox.information(None,"Loggout Successfully","LOGGED OUT SUCCESSFULLY!")
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    buyerDashboardDialog = QtWidgets.QDialog()
    ui = Ui_buyerDashboardDialog()
    ui.setupUi(buyerDashboardDialog)
    buyerDashboardDialog.show()
  
    sys.exit(app.exec())
