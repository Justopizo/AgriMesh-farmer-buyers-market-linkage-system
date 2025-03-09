
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import *
import psycopg2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(953, 717)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 261, 731))
        self.widget.setStyleSheet("background-color: rgb(31, 0, 93);")
        self.widget.setObjectName("widget")
        self.widget1 = QtWidgets.QWidget(parent=self.widget)
        self.widget1.setGeometry(QtCore.QRect(20, 50, 221, 651))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dashboardwidgetpushButton = QtWidgets.QPushButton(parent=self.widget1)
        self.dashboardwidgetpushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        
        self.createdatabaseConnection()
        self.dashboardwidgetpushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
       
        self.dashboardwidgetpushButton.setObjectName("dashboardwidgetpushButton")
        self.verticalLayout.addWidget(self.dashboardwidgetpushButton)
        self.managefarmproducePushButton = QtWidgets.QPushButton(parent=self.widget1)
        self.managefarmproducePushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.managefarmproducePushButton.setObjectName("managefarmproducePushButton")
        self.managefarmproducePushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.verticalLayout.addWidget(self.managefarmproducePushButton)
        self.viewordersPushButton = QtWidgets.QPushButton(parent=self.widget1)
        self.viewordersPushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.viewordersPushButton.setObjectName("viewordersPushButton")
        self.viewordersPushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.verticalLayout.addWidget(self.viewordersPushButton)
        self.profilepushButton = QtWidgets.QPushButton(parent=self.widget1)
        self.profilepushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.profilepushButton.setObjectName("profilepushButton")
        self.profilepushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.verticalLayout.addWidget(self.profilepushButton)
        self.salespushbutton = QtWidgets.QPushButton(parent=self.widget1)
        self.salespushbutton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.salespushbutton.setObjectName("salespushbutton")
        self.salespushbutton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.verticalLayout.addWidget(self.salespushbutton)
        self.settingspushbutton = QtWidgets.QPushButton(parent=self.widget1)
        self.settingspushbutton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.settingspushbutton.setObjectName("settingspushbutton")
        self.settingspushbutton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.verticalLayout.addWidget(self.settingspushbutton)
        self.logoutpushbutton = QtWidgets.QPushButton(parent=self.widget1)
        self.logoutpushbutton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.logoutpushbutton.setObjectName("logoutpushbutton")
        self.logoutpushbutton.clicked.connect(self.logoutpushbuttonClicked)
        self.verticalLayout.addWidget(self.logoutpushbutton)
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(270, 0, 681, 731))
        self.widget_2.setObjectName("widget_2")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget_2)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 681, 711))
        self.stackedWidget.setObjectName("stackedWidget")
        self.dashboardPagewidget = QtWidgets.QWidget()
        self.dashboardPagewidget.setObjectName("dashboardPagewidget")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.dashboardPagewidget)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 60, 311, 231))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_26 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_26.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_26.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_26.setObjectName("label_26")
        self.totalsaleslcdNumber = QtWidgets.QLCDNumber(parent=self.groupBox_3)
        self.totalsaleslcdNumber.setGeometry(QtCore.QRect(10, 60, 64, 31))
        self.totalsaleslcdNumber.setObjectName("totalsaleslcdNumber")
        self.label_27 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_27.setGeometry(QtCore.QRect(150, 30, 101, 16))
        self.label_27.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_27.setObjectName("label_27")
        self.pendingordersLCDnumber = QtWidgets.QLCDNumber(parent=self.groupBox_3)
        self.pendingordersLCDnumber.setGeometry(QtCore.QRect(160, 60, 64, 31))
        self.pendingordersLCDnumber.setObjectName("pendingordersLCDnumber")
        self.label_28 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_28.setGeometry(QtCore.QRect(10, 120, 111, 16))
        self.label_28.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_28.setObjectName("label_28")
        self.availableproduceLCDnumber = QtWidgets.QLCDNumber(parent=self.groupBox_3)
        self.availableproduceLCDnumber.setGeometry(QtCore.QRect(10, 140, 64, 31))
        self.availableproduceLCDnumber.setObjectName("availableproduceLCDnumber")
        self.label_25 = QtWidgets.QLabel(parent=self.dashboardPagewidget)
        self.label_25.setGeometry(QtCore.QRect(20, 10, 331, 41))
        self.label_25.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_25.setObjectName("label_25")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.dashboardPagewidget)
        self.groupBox_4.setGeometry(QtCore.QRect(320, 60, 361, 231))
        self.groupBox_4.setObjectName("groupBox_4")
        self.settingscommandLinkButton_dashboard = QtWidgets.QCommandLinkButton(parent=self.groupBox_4)
        self.settingscommandLinkButton_dashboard.setGeometry(QtCore.QRect(10, 20, 222, 48))
        self.settingscommandLinkButton_dashboard.setObjectName("settingscommandLinkButton_dashboard")
        
        self.settingscommandLinkButton_dashboard.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        
        self.profilecommandLinkButton = QtWidgets.QCommandLinkButton(parent=self.groupBox_4)
        self.profilecommandLinkButton.setGeometry(QtCore.QRect(10, 80, 222, 48))
        self.profilecommandLinkButton.setObjectName("profilecommandLinkButton")
        
        self.profilecommandLinkButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        
        self.viewOrderscommandLinkButton = QtWidgets.QCommandLinkButton(parent=self.groupBox_4)
        self.viewOrderscommandLinkButton.setGeometry(QtCore.QRect(10, 140, 222, 48))
        self.viewOrderscommandLinkButton.setObjectName("viewOrderscommandLinkButton")
        
        
       
        self.viewOrderscommandLinkButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateviewProduceTableWidget)
        self.timer.timeout.connect(self.updateeditproduceTablewidget)
        self.timer.timeout.connect(self.updateviewProducepageTableWidget)
        self.timer.timeout.connect(self.updatesalestableWidget_sales)
        self.timer.timeout.connect(self.salesbycategoryGraphicsviewepdate)
        self.timer.timeout.connect(self.salesbyProductnamegraphicsviewupdate)
        
        self.timer.start(500) 
        
        
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.dashboardPagewidget)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 310, 681, 411))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_29 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_29.setGeometry(QtCore.QRect(20, 30, 111, 16))
        self.label_29.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_30.setGeometry(QtCore.QRect(410, 20, 111, 16))
        self.label_30.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_30.setObjectName("label_30")
        self.salesbycategoryGraphicsview = QtWidgets.QGraphicsView(parent=self.groupBox_5)
        self.salesbycategoryGraphicsview.setGeometry(QtCore.QRect(10, 50, 311, 341))
        self.salesbycategoryGraphicsview.setObjectName("salesbycategoryGraphicsview")
        self.salesbyProductnamegraphicsview = QtWidgets.QGraphicsView(parent=self.groupBox_5)
        self.salesbyProductnamegraphicsview.setGeometry(QtCore.QRect(330, 50, 351, 341))
        self.salesbyProductnamegraphicsview.setObjectName("salesbyProductnamegraphicsview")
        self.stackedWidget.addWidget(self.dashboardPagewidget)
        self.managefarmproducewidgetpage = QtWidgets.QWidget()
        self.managefarmproducewidgetpage.setObjectName("managefarmproducewidgetpage")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.managefarmproducewidgetpage)
        self.tabWidget.setGeometry(QtCore.QRect(0, 110, 681, 611))
        self.tabWidget.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.tabWidget.setObjectName("tabWidget")
        self.AddproduceTab = QtWidgets.QWidget()
        self.AddproduceTab.setObjectName("AddproduceTab")
        #self.AddproduceTab
        self.label = QtWidgets.QLabel(parent=self.AddproduceTab)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 21))
        self.label.setObjectName("label")
        self.productnamelineEdit = QtWidgets.QLineEdit(parent=self.AddproduceTab)
        self.productnamelineEdit.setGeometry(QtCore.QRect(160, 20, 261, 22))
        self.productnamelineEdit.setObjectName("productnamelineEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.AddproduceTab)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 131, 21))
        self.label_2.setObjectName("label_2")
        self.productcategorycomboBox = QtWidgets.QComboBox(parent=self.AddproduceTab)
        self.productcategorycomboBox.setGeometry(QtCore.QRect(160, 70, 261, 22))
        self.productcategorycomboBox.setObjectName("productcategorycomboBox")
        self.productcategorycomboBox.addItem("")
        self.productcategorycomboBox.addItem("")
        self.productcategorycomboBox.addItem("")
        self.productcategorycomboBox.addItem("")
        self.productcategorycomboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(parent=self.AddproduceTab)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 131, 21))
        self.label_3.setObjectName("label_3")
        self.quantitylinedit = QtWidgets.QLineEdit(parent=self.AddproduceTab)
        self.quantitylinedit.setGeometry(QtCore.QRect(160, 120, 261, 22))
        self.quantitylinedit.setObjectName("quantitylinedit")
        self.label_4 = QtWidgets.QLabel(parent=self.AddproduceTab)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 131, 21))
        self.label_4.setObjectName("label_4")
        self.pricelinedit = QtWidgets.QLineEdit(parent=self.AddproduceTab)
        self.pricelinedit.setGeometry(QtCore.QRect(160, 180, 261, 22))
        self.pricelinedit.setObjectName("pricelinedit")
        self.label_5 = QtWidgets.QLabel(parent=self.AddproduceTab)
        self.label_5.setGeometry(QtCore.QRect(20, 290, 151, 21))
        self.label_5.setObjectName("label_5")
        self.imageproducepath = QtWidgets.QLineEdit(parent=self.AddproduceTab)
        self.imageproducepath.setGeometry(QtCore.QRect(190, 290, 231, 22))
        self.imageproducepath.setReadOnly(True)
        self.imageproducepath.setObjectName("imageproducepath")
        self.label_6 = QtWidgets.QLabel(parent=self.AddproduceTab)
        self.label_6.setGeometry(QtCore.QRect(20, 240, 131, 21))
        self.label_6.setObjectName("label_6")
        self.locationlinedit = QtWidgets.QLineEdit(parent=self.AddproduceTab)
        self.locationlinedit.setGeometry(QtCore.QRect(160, 240, 261, 22))
        self.locationlinedit.setObjectName("locationlinedit")
        self.uploadProduceImagepushButton = QtWidgets.QPushButton(parent=self.AddproduceTab)
        self.uploadProduceImagepushButton.setGeometry(QtCore.QRect(440, 280, 171, 31))
        self.uploadProduceImagepushButton.setObjectName("uploadProduceImagepushButton")
        self.uploadProduceImagepushButton.clicked.connect(self.uploadProduceImagepushButtonClicked)
        self.imagesettinglabel = QtWidgets.QLabel(parent=self.AddproduceTab)
        self.imagesettinglabel.setGeometry(QtCore.QRect(190, 320, 200, 200))
        self.imagesettinglabel.setStyleSheet("border: 1px solid black")
        self.imagesettinglabel.setText("")
        self.imagesettinglabel.setObjectName("imagesettinglabel")
        self.addTheProducePushButton = QtWidgets.QPushButton(parent=self.AddproduceTab)
        self.addTheProducePushButton.clicked.connect( self.addTheProducePushButtonClicked)
        self.addTheProducePushButton.setGeometry(QtCore.QRect(190, 540, 171, 31))
        self.addTheProducePushButton.setObjectName("addTheProducePushButton")
        self.tabWidget.addTab(self.AddproduceTab, "")
        self.editAvailabilityTab = QtWidgets.QWidget()
        self.editAvailabilityTab.setObjectName("editAvailabilityTab")
        self.editproducetableWidget = QtWidgets.QTableWidget(parent=self.editAvailabilityTab)
        self.editproducetableWidget.setGeometry(QtCore.QRect(0, 0, 671, 331))
        self.editproducetableWidget.setObjectName("editproducetableWidget")
        self.editproducetableWidget.setColumnCount(6)
        self.editproducetableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.editproducetableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.editproducetableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.editproducetableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.editproducetableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.editproducetableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.editproducetableWidget.setHorizontalHeaderItem(5, item)
        self.saveChanges_editproducewidgetpushButton = QtWidgets.QPushButton(parent=self.editAvailabilityTab)
        self.saveChanges_editproducewidgetpushButton.setGeometry(QtCore.QRect(0, 360, 141, 28))
        self.saveChanges_editproducewidgetpushButton.setObjectName("saveChanges_editproducewidgetpushButton")
        self.tabWidget.addTab(self.editAvailabilityTab, "")
        self.setAvailabilityTab = QtWidgets.QWidget()
        self.setAvailabilityTab.setObjectName("setAvailabilityTab")
        self.label_8 = QtWidgets.QLabel(parent=self.setAvailabilityTab)
        self.label_8.setGeometry(QtCore.QRect(10, 30, 111, 21))
        self.label_8.setObjectName("label_8")
        self.productnameSetAvalabilityLineedit = QtWidgets.QLineEdit(parent=self.setAvailabilityTab)
        self.productnameSetAvalabilityLineedit.setGeometry(QtCore.QRect(140, 30, 261, 22))
        self.productnameSetAvalabilityLineedit.setReadOnly(True)
        self.productnameSetAvalabilityLineedit.setObjectName("productnameSetAvalabilityLineedit")
        self.label_9 = QtWidgets.QLabel(parent=self.setAvailabilityTab)
        self.label_9.setGeometry(QtCore.QRect(10, 80, 131, 21))
        self.label_9.setObjectName("label_9")
        self.quantitylinedit_setavailability = QtWidgets.QLineEdit(parent=self.setAvailabilityTab)
        self.quantitylinedit_setavailability.setGeometry(QtCore.QRect(140, 80, 261, 22))
        self.quantitylinedit_setavailability.setReadOnly(True)
        self.quantitylinedit_setavailability.setObjectName("quantitylinedit_setavailability")
        self.label_10 = QtWidgets.QLabel(parent=self.setAvailabilityTab)
        self.label_10.setGeometry(QtCore.QRect(20, 140, 131, 21))
        self.label_10.setObjectName("label_10")
        self.pricelinedit_setAvailability = QtWidgets.QLineEdit(parent=self.setAvailabilityTab)
        self.pricelinedit_setAvailability.setGeometry(QtCore.QRect(140, 140, 261, 22))
        self.pricelinedit_setAvailability.setReadOnly(True)
        self.pricelinedit_setAvailability.setObjectName("pricelinedit_setAvailability")
        self.label_11 = QtWidgets.QLabel(parent=self.setAvailabilityTab)
        self.label_11.setGeometry(QtCore.QRect(20, 200, 131, 21))
        self.label_11.setObjectName("label_11")
        self.availableradioButton = QtWidgets.QRadioButton(parent=self.setAvailabilityTab)
        self.availableradioButton.setGeometry(QtCore.QRect(200, 200, 95, 20))
        self.availableradioButton.setObjectName("availableradioButton")
        self.outOfStockradioButton = QtWidgets.QRadioButton(parent=self.setAvailabilityTab)
        self.outOfStockradioButton.setGeometry(QtCore.QRect(200, 240, 141, 20))
        self.outOfStockradioButton.setObjectName("outOfStockradioButton")
        self.savepushButton_setAvailability = QtWidgets.QPushButton(parent=self.setAvailabilityTab)
        self.savepushButton_setAvailability.setGeometry(QtCore.QRect(200, 320, 93, 28))
        self.savepushButton_setAvailability.setObjectName("savepushButton_setAvailability")
        self.tabWidget.addTab(self.setAvailabilityTab, "")
        self.viewproduceTab = QtWidgets.QWidget()
        self.viewproduceTab.setObjectName("viewproduceTab")
        self.viewProducetableWidget = QtWidgets.QTableWidget(parent=self.viewproduceTab)
        self.viewProducetableWidget.setGeometry(QtCore.QRect(0, 0, 681, 411))
        self.viewProducetableWidget.setObjectName("viewProducetableWidget")
        self.viewProducetableWidget.setColumnCount(5)
        self.viewProducetableWidget.setRowCount(0)
        self.updateviewProduceTableWidget()
        item = QtWidgets.QTableWidgetItem()
        self.viewProducetableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.viewProducetableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.viewProducetableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.viewProducetableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.viewProducetableWidget.setHorizontalHeaderItem(4, item)
        self.label_12 = QtWidgets.QLabel(parent=self.viewproduceTab)
        self.label_12.setGeometry(QtCore.QRect(0, 430, 201, 21))
        self.label_12.setObjectName("label_12")
        self.saveproduceascomboBox_viewproduce = QtWidgets.QComboBox(parent=self.viewproduceTab)
        self.saveproduceascomboBox_viewproduce.setGeometry(QtCore.QRect(220, 430, 261, 22))
        self.saveproduceascomboBox_viewproduce.setObjectName("saveproduceascomboBox_viewproduce")
        self.saveproduceascomboBox_viewproduce.addItem("")
        self.saveproduceascomboBox_viewproduce.addItem("")
        self.saveproduceascomboBox_viewproduce.addItem("")
        self.saveproduceascomboBox_viewproduce.addItem("")
        self.saveproduceascomboBox_viewproduce.addItem("")
        self.saveproduceaspushButton_viewproduce = QtWidgets.QPushButton(parent=self.viewproduceTab)
        self.saveproduceaspushButton_viewproduce.setGeometry(QtCore.QRect(220, 480, 93, 28))
        self.saveproduceaspushButton_viewproduce.setObjectName("saveproduceaspushButton_viewproduce")
        self.tabWidget.addTab(self.viewproduceTab, "")
        self.label_7 = QtWidgets.QLabel(parent=self.managefarmproducewidgetpage)
        self.label_7.setGeometry(QtCore.QRect(50, 40, 311, 21))
        self.label_7.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.managefarmproducewidgetpage)
        self.vieworderspagewidget = QtWidgets.QWidget()
        self.vieworderspagewidget.setObjectName("vieworderspagewidget")
        self.label_13 = QtWidgets.QLabel(parent=self.vieworderspagewidget)
        self.label_13.setGeometry(QtCore.QRect(60, 30, 261, 31))
        self.label_13.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.vieworderstableWidget = QtWidgets.QTableWidget(parent=self.vieworderspagewidget)
        self.vieworderstableWidget.setGeometry(QtCore.QRect(0, 100, 681, 351))
        self.vieworderstableWidget.setObjectName("vieworderstableWidget")
        self.vieworderstableWidget.setColumnCount(6)
        self.vieworderstableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.vieworderstableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.vieworderstableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.vieworderstableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.vieworderstableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.vieworderstableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.vieworderstableWidget.setHorizontalHeaderItem(5, item)
        self.label_14 = QtWidgets.QLabel(parent=self.vieworderspagewidget)
        self.label_14.setGeometry(QtCore.QRect(0, 480, 101, 31))
        self.label_14.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.filterorderscomboBox = QtWidgets.QComboBox(parent=self.vieworderspagewidget)
        self.filterorderscomboBox.setGeometry(QtCore.QRect(110, 480, 231, 22))
        self.filterorderscomboBox.setObjectName("filterorderscomboBox")
        self.filterorderscomboBox.addItem("")
        self.filterorderscomboBox.addItem("")
        self.filterorderscomboBox.currentTextChanged.connect(self.filterorderstable)
        self.stackedWidget.addWidget(self.vieworderspagewidget)
        self.profilepagewidget = QtWidgets.QWidget()
        self.profilepagewidget.setObjectName("profilepagewidget")
        self.label_15 = QtWidgets.QLabel(parent=self.profilepagewidget)
        self.label_15.setGeometry(QtCore.QRect(50, 20, 281, 16))
        self.label_15.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.profilepagewidget)
        self.label_16.setGeometry(QtCore.QRect(0, 90, 51, 20))
        self.label_16.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_16.setObjectName("label_16")
        self.namelineEdit_profile = QtWidgets.QLineEdit(parent=self.profilepagewidget)
        self.namelineEdit_profile.setGeometry(QtCore.QRect(110, 90, 311, 22))
        self.namelineEdit_profile.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.namelineEdit_profile.setObjectName("namelineEdit_profile")
        self.label_17 = QtWidgets.QLabel(parent=self.profilepagewidget)
        self.label_17.setGeometry(QtCore.QRect(0, 140, 91, 20))
        self.label_17.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_17.setObjectName("label_17")
        self.phoneNolinedit_profile = QtWidgets.QLineEdit(parent=self.profilepagewidget)
        self.phoneNolinedit_profile.setGeometry(QtCore.QRect(110, 140, 311, 22))
        self.phoneNolinedit_profile.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.phoneNolinedit_profile.setObjectName("phoneNolinedit_profile")
        self.label_18 = QtWidgets.QLabel(parent=self.profilepagewidget)
        self.label_18.setGeometry(QtCore.QRect(0, 200, 91, 20))
        self.label_18.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_18.setObjectName("label_18")
        self.locationlineedit_profile = QtWidgets.QLineEdit(parent=self.profilepagewidget)
        self.locationlineedit_profile.setGeometry(QtCore.QRect(110, 200, 311, 22))
        self.locationlineedit_profile.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.locationlineedit_profile.setObjectName("locationlineedit_profile")
        self.label_19 = QtWidgets.QLabel(parent=self.profilepagewidget)
        self.label_19.setGeometry(QtCore.QRect(0, 260, 121, 20))
        self.label_19.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_19.setObjectName("label_19")
        self.paymentaccouncomboBox_profile = QtWidgets.QComboBox(parent=self.profilepagewidget)
        self.paymentaccouncomboBox_profile.setGeometry(QtCore.QRect(140, 260, 281, 22))
        self.paymentaccouncomboBox_profile.setObjectName("paymentaccouncomboBox_profile")
        self.paymentaccouncomboBox_profile.addItem("")
        self.paymentaccouncomboBox_profile.addItem("")
        self.paymentaccouncomboBox_profile.addItem("")
        
        self.paymentaccouncomboBox_profile.currentIndexChanged.connect(self.paymentmethodtextchanged)
        
        self.paymentaccountChoicelinedit_profile = QtWidgets.QLineEdit(parent=self.profilepagewidget)
        self.paymentaccountChoicelinedit_profile.setGeometry(QtCore.QRect(140, 310, 281, 22))
        self.paymentaccountChoicelinedit_profile.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.paymentaccountChoicelinedit_profile.setObjectName("paymentaccountChoicelinedit_profile")
        self.saveprofileinfopushButton_profile = QtWidgets.QPushButton(parent=self.profilepagewidget)
        self.saveprofileinfopushButton_profile.setGeometry(QtCore.QRect(140, 360, 93, 28))
        self.saveprofileinfopushButton_profile.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.saveprofileinfopushButton_profile.setObjectName("saveprofileinfopushButton_profile")
        self.saveprofileinfopushButton_profile .clicked.connect(self.saveprofileinfopushButton_profileclicked)
        self.stackedWidget.addWidget(self.profilepagewidget)
        self.salespagewidget = QtWidgets.QWidget()
        self.salespagewidget.setObjectName("salespagewidget")
        self.label_20 = QtWidgets.QLabel(parent=self.salespagewidget)
        self.label_20.setGeometry(QtCore.QRect(40, 40, 271, 21))
        self.label_20.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_20.setObjectName("label_20")
        self.salestableWidget_sales = QtWidgets.QTableWidget(parent=self.salespagewidget)
        self.salestableWidget_sales.setGeometry(QtCore.QRect(5, 70, 671, 271))
        self.salestableWidget_sales.setObjectName("salestableWidget_sales")
        self.salestableWidget_sales.setColumnCount(4)
        self.salestableWidget_sales.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.salestableWidget_sales.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.salestableWidget_sales.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.salestableWidget_sales.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.salestableWidget_sales.setHorizontalHeaderItem(3, item)
        self.label_21 = QtWidgets.QLabel(parent=self.salespagewidget)
        self.label_21.setGeometry(QtCore.QRect(10, 380, 231, 21))
        self.label_21.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_21.setObjectName("label_21")
        self.salesreportcomboBox_sales = QtWidgets.QComboBox(parent=self.salespagewidget)
        self.salesreportcomboBox_sales.setGeometry(QtCore.QRect(240, 380, 261, 22))
        self.salesreportcomboBox_sales.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.salesreportcomboBox_sales.setObjectName("salesreportcomboBox_sales")
        self.salesreportcomboBox_sales.addItem("")
        self.salesreportcomboBox_sales.addItem("")
        self.salesreportcomboBox_sales.addItem("")
        self.saveandExportreportpushButton_sales = QtWidgets.QPushButton(parent=self.salespagewidget)
        self.saveandExportreportpushButton_sales.setGeometry(QtCore.QRect(240, 450, 191, 28))
        self.saveandExportreportpushButton_sales.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.saveandExportreportpushButton_sales.setObjectName("saveandExportreportpushButton_sales")
        self.stackedWidget.addWidget(self.salespagewidget)
        self.settingpage = QtWidgets.QWidget()
        self.settingpage.setObjectName("settingpage")
        self.accountsettingsgroupBox = QtWidgets.QGroupBox(parent=self.settingpage)
        self.accountsettingsgroupBox.setGeometry(QtCore.QRect(0, 80, 371, 221))
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
        self.changePasswordpushButton.setObjectName("changePasswordpushButton")
        
        self.changePasswordpushButton.clicked.connect(self.changePasswordpushButtonclicked)
        
        self.groupBox = QtWidgets.QGroupBox(parent=self.settingpage)
        self.groupBox.setGeometry(QtCore.QRect(0, 320, 371, 141))
        self.groupBox.setObjectName("groupBox")
        self.requestdeletionofAccountcommandLinkButton = QtWidgets.QCommandLinkButton(parent=self.groupBox)
        self.requestdeletionofAccountcommandLinkButton.setGeometry(QtCore.QRect(10, 20, 271, 48))
        self.requestdeletionofAccountcommandLinkButton.setObjectName("requestdeletionofAccountcommandLinkButton")
        
        self.requestdeletionofAccountcommandLinkButton.clicked.connect(self.requestdeletionofAccountcommandLinkButtonClicked)
        
        self.switchtodarkmodeCommandlinkbutton = QtWidgets.QCommandLinkButton(parent=self.groupBox)
        self.switchtodarkmodeCommandlinkbutton.setGeometry(QtCore.QRect(10, 70, 271, 48))
        self.switchtodarkmodeCommandlinkbutton.setObjectName("switchtodarkmodeCommandlinkbutton")
        self.switchtodarkmodeCommandlinkbutton.clicked.connect(self.switchtodarkmodeCommandlinkbuttonclicked)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.settingpage)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 480, 371, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.notificationstextEdit_settingspage = QtWidgets.QTextEdit(parent=self.groupBox_2)
        self.notificationstextEdit_settingspage.setGeometry(QtCore.QRect(0, 20, 371, 211))
        self.notificationstextEdit_settingspage.setObjectName("notificationstextEdit_settingspage")
        self.stackedWidget.addWidget(self.settingpage)
        self.logoutpage = QtWidgets.QWidget()
        self.logoutpage.setObjectName("logoutpage")
        self.stackedWidget.addWidget(self.logoutpage)
        self.lo = QtWidgets.QWidget()
        self.lo.setObjectName("lo")
        self.stackedWidget.addWidget(self.lo)
        MainWindow.setCentralWidget(self.centralwidget)
        
        #connectdb
        self.connectagrimeshDB()
        self.totalsales=0

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Farmer DashBoard- AgriMesh Company"))
        self.dashboardwidgetpushButton.setText(_translate("MainWindow", "Dashboard"))
        self.managefarmproducePushButton.setText(_translate("MainWindow", "Farmers' Market"))
        self.viewordersPushButton.setText(_translate("MainWindow", "View Orders"))
        self.profilepushButton.setText(_translate("MainWindow", "Profile"))
        self.salespushbutton.setText(_translate("MainWindow", "Sales"))
        self.settingspushbutton.setText(_translate("MainWindow", "Settings"))
        self.logoutpushbutton.setText(_translate("MainWindow", "Logout"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Key Metrics"))
        self.label_26.setText(_translate("MainWindow", "Total Sales"))
        self.label_27.setText(_translate("MainWindow", "Pending Orders"))
        self.label_28.setText(_translate("MainWindow", "Available Produce"))
        self.label_25.setText(_translate("MainWindow", "Your Farming Business At A Glance"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Quick Actions"))
        self.settingscommandLinkButton_dashboard.setText(_translate("MainWindow", "Settings"))
        self.profilecommandLinkButton.setText(_translate("MainWindow", "profile"))
        self.viewOrderscommandLinkButton.setText(_translate("MainWindow", "View Ordes"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Table and Charts"))
        self.label_29.setText(_translate("MainWindow", "sales,orders and available produce"))
        self.label_30.setText(_translate("MainWindow", "Sales By Category"))
        self.label.setText(_translate("MainWindow", "Product Name"))
        self.label_2.setText(_translate("MainWindow", "Product Category"))
        self.productcategorycomboBox.setItemText(0, _translate("MainWindow", "Fruits"))
        self.productcategorycomboBox.setItemText(1, _translate("MainWindow", "Vegetables"))
        self.productcategorycomboBox.setItemText(2, _translate("MainWindow", "Others"))
        self.productcategorycomboBox.setItemText(3, _translate("MainWindow", "Cereals"))
        self.productcategorycomboBox.setItemText(4, _translate("MainWindow", "Animals"))
        self.productcategorycomboBox.setItemText(5, _translate("MainWindow", "Others"))
        self.label_3.setText(_translate("MainWindow", "Quantity"))
        self.quantitylinedit.setPlaceholderText(_translate("MainWindow", "e.g 2kg,1L or 2"))
        self.label_4.setText(_translate("MainWindow", "Price"))
        self.label_5.setText(_translate("MainWindow", "Image Produce Path"))
        self.label_6.setText(_translate("MainWindow", "Location"))
        self.uploadProduceImagepushButton.setText(_translate("MainWindow", "Upload Produce photo"))
        self.addTheProducePushButton.setText(_translate("MainWindow", "Add The Produce"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AddproduceTab), _translate("MainWindow", "Add Produce"))
        item = self.editproducetableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.editproducetableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Category"))
        item = self.editproducetableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.editproducetableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        item = self.editproducetableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Location"))
        item = self.editproducetableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Action"))
        self.saveChanges_editproducewidgetpushButton.setText(_translate("MainWindow", "Save Changes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.editAvailabilityTab), _translate("MainWindow", "Edit Produce"))
        self.label_8.setText(_translate("MainWindow", "Product Name"))
        self.label_9.setText(_translate("MainWindow", "Quantity"))
        self.quantitylinedit_setavailability.setPlaceholderText(_translate("MainWindow", "in terms of Kilograms"))
        self.label_10.setText(_translate("MainWindow", "Price"))
        self.label_11.setText(_translate("MainWindow", "Set Availability"))
        self.availableradioButton.setText(_translate("MainWindow", "Available"))
        self.outOfStockradioButton.setText(_translate("MainWindow", "Out Of Stock"))
        self.savepushButton_setAvailability.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setAvailabilityTab), _translate("MainWindow", "Set Availability"))
        item = self.viewProducetableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.viewProducetableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Category"))
        item = self.viewProducetableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.viewProducetableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        item = self.viewProducetableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Location"))
        self.label_12.setText(_translate("MainWindow", "Save Produce Details As"))
        self.saveproduceascomboBox_viewproduce.setItemText(0, _translate("MainWindow", "PDF format"))
        self.saveproduceascomboBox_viewproduce.setItemText(1, _translate("MainWindow", "Docx Format"))
        self.saveproduceascomboBox_viewproduce.setItemText(2, _translate("MainWindow", "Json"))
        self.saveproduceascomboBox_viewproduce.setItemText(3, _translate("MainWindow", "CSV "))
        self.saveproduceascomboBox_viewproduce.setItemText(4, _translate("MainWindow", "ScreenShot"))
        self.saveproduceaspushButton_viewproduce.setText(_translate("MainWindow", "Save"))
        self.saveproduceaspushButton_viewproduce.clicked.connect(self.saveproduceaspushButton_viewproduceclicked)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.viewproduceTab), _translate("MainWindow", "View Produce"))
        self.label_7.setText(_translate("MainWindow", "Add, Update And Track Your Produce"))
        self.label_13.setText(_translate("MainWindow", "Track and Manage orders"))
        item = self.vieworderstableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Buyer Name"))
        item = self.vieworderstableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Phone No."))
        item = self.vieworderstableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Product"))
        item = self.vieworderstableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.vieworderstableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Price"))
        item = self.vieworderstableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Payment Method"))
        self.label_14.setText(_translate("MainWindow", "Filter By"))
        self.filterorderscomboBox.setItemText(0, _translate("MainWindow", "Quantity"))
        self.filterorderscomboBox.setItemText(1, _translate("MainWindow", "Price"))
        self.label_15.setText(_translate("MainWindow", "View and Edit Pesonal Details"))
        self.label_16.setText(_translate("MainWindow", "Name"))
        self.label_17.setText(_translate("MainWindow", "Phone No"))
        self.label_18.setText(_translate("MainWindow", "Location"))
        self.label_19.setText(_translate("MainWindow", "PaymentAccount"))
        self.paymentaccouncomboBox_profile.setItemText(0, _translate("MainWindow", "M-PESA"))
        self.paymentaccouncomboBox_profile.setItemText(1, _translate("MainWindow", "AirtelMoney"))
        self.paymentaccouncomboBox_profile.setItemText(2, _translate("MainWindow", "KCB"))
        self.saveprofileinfopushButton_profile.setText(_translate("MainWindow", "Save"))
        self.label_20.setText(_translate("MainWindow", "Sales Overview and Reports"))
        item = self.salestableWidget_sales.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.salestableWidget_sales.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Buyer Name"))
        item = self.salestableWidget_sales.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.salestableWidget_sales.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.label_21.setText(_translate("MainWindow", "Sales Sales Reports As?"))
        self.salesreportcomboBox_sales.setItemText(0, _translate("MainWindow", "PDF"))
        self.salesreportcomboBox_sales.setItemText(1, _translate("MainWindow", "Docx"))
        self.salesreportcomboBox_sales.setItemText(2, _translate("MainWindow", "CSV"))
        self.saveandExportreportpushButton_sales.setText(_translate("MainWindow", "Save and Export Report"))
        self.accountsettingsgroupBox.setTitle(_translate("MainWindow", "Account Settings"))
        self.label_22.setText(_translate("MainWindow", "Change Password"))
        self.label_23.setText(_translate("MainWindow", "Old Password"))
        self.label_24.setText(_translate("MainWindow", "New Password"))
        self.changePasswordpushButton.setText(_translate("MainWindow", "Change"))
        self.groupBox.setTitle(_translate("MainWindow", "Preferences"))
        self.requestdeletionofAccountcommandLinkButton.setText(_translate("MainWindow", "Request deletion of account?"))
        self.switchtodarkmodeCommandlinkbutton.setText(_translate("MainWindow", "Switch to darkmode"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Notifications"))
        
        self.saveandExportreportpushButton_sales.clicked.connect(self.saveandExportreportpushButton_salesClicked)
        self.tabWidget.currentChanged.connect(self.setavalabilitytabclicked)
        self.updateeditproduceTablewidget() 
        self.updateviewProducepageTableWidget()
        self.updatesalestableWidget_sales()
        self.salesbycategoryGraphicsviewepdate()
        self.salesbyProductnamegraphicsviewupdate()
        self.updatenotificationstextEdit_settingspage()
        self.checkordercancelledbyadmin()
        self.pendingorder=0
        
        self.availableproduce=0
        
        
        
        
    #checkordercancelledbyadmin
    def checkordercancelledbyadmin(self):
            try:
                    connnection=self.connectagrimeshDB()
                    cursor=connnection.cursor()
                    cursor.execute("SELECT * FROM produce WHERE status='Cancelled'")
                    results=cursor.fetchall()
                    if results:
                        count=len(results)
                        QMessageBox.information(None,"SO sad",f"{count} Product(s) Were Cancelled By admin!")
                        cursor.execute("DELETE FROM produce WHERE status='Cancelled'")
                        connnection.commit()
                            
                    
                    
                    cursor.close()
                    connnection.close() 
            except psycopg2.Error as e:
                    QMessageBox.information(None,"Error",f"An Error Occurred {e}")   
        
    #updatenotificationstextEdit_settingspage
    def updatenotificationstextEdit_settingspage(self):
            try:
                    connection=self.connectagrimeshDB()
                    cursor=connection.cursor()
                    
                    cursor.execute("SELECT notification FROM notifications")
                    notifications = cursor.fetchall()  

                    cursor.close()
                    connection.close()

        
                    if notifications:
                        self.notificationstextEdit_settingspage.clear()
                        self.notificationstextEdit_settingspage.setReadOnly(True)
                        formatted_notifications = "\n".join([row[0] for row in notifications])
                        self.notificationstextEdit_settingspage.setText(formatted_notifications)
                        
                    else:
                        self.notificationstextEdit_settingspage.setText("No notifications available.")
                
                    
            except psycopg2.Error as e:
                    QMessageBox.information(None,"Error",f"Error Occurred {e}")    
        
     #salesbyProductnamegraphicsview
    def salesbyProductnamegraphicsviewupdate(self):
            from produceBycategory import ProduceChartHelper
            chart_helper = ProduceChartHelper(self.salesbyProductnamegraphicsview)  
            chart_helper.load_chart()   
            
            
     #self.salesbycategoryGraphicsview
    def salesbycategoryGraphicsviewepdate(self):
        from sale_orders_andAvailableproduce import ProduceChartHelper
        chart = ProduceChartHelper(self.salesbycategoryGraphicsview)  
        chart.load_pie_chart(self.totalsales, self.pendingorder, self.availableproduce)
        
     #saveandExportreportpushButton_salesClicked
    def saveandExportreportpushButton_salesClicked(self):
        option=self.salesreportcomboBox_sales.currentText()
        
        if option=="PDF":
                from reportlab.lib.pagesizes import A4
                from reportlab.pdfgen import canvas
                
                connection=self.connectagrimeshDB()
                query = ("SELECT productname, buyername, price FROM vieworders")
                cursor=connection.cursor()
                cursor.execute(query)
                records = cursor.fetchall()
                file_name = "sale_Report.pdf"
                c = canvas.Canvas(file_name, pagesize=A4)
                width, height = A4
                c.setFont("Helvetica-Bold", 14)
                c.drawString(200, height - 50, "Sales Data Report")
                c.setFont("Helvetica-Bold", 12)
                headers = ["Product Name", "Buyer Name", "Price"]
                x_positions = [50, 150, 300, 400, 500]  
                y_position = height - 80
                for i, header in enumerate(headers):
                   c.drawString(x_positions[i], y_position, header)
                   
                c.line(50, y_position - 3, 550, y_position - 3) 
                c.setFont("Helvetica", 10)
                y_position -= 20
                for row_data in records:
                        if y_position < 50:  
                                c.showPage()
                                y_position = height - 50
                                c.setFont("Helvetica", 10)

                        for col_idx, cell_data in enumerate(row_data):
                                c.drawString(x_positions[col_idx], y_position, str(cell_data))

                        y_position -= 20  

                c.save()
                import os

                file_name = "sale_Report.pdf"
                file_path = os.path.abspath(file_name)
                QMessageBox.information(None,"Saved",f"PDF saved Successfully As {file_name} to \n\nLocation : {file_path}")
                
                connection.close()
                cursor.close()
        elif option=="Docx":
                file_name = "sale_Report.docx"
                from saveProduceasdocx import save_to_docx
                savedpath=save_to_docx(file_name)
                QMessageBox.information(None,"Saved",f"Saved File As {file_name} to \n\nLcation: {savedpath}")
        else:
                file_name = "sale_Report.csv"
                from saveProduceasCsv import save_to_csv
                savecsvpath=save_to_csv(file_name)
                QMessageBox.information(None,"Saved",f"Saved File As {file_name} to \n\nLcation: {savecsvpath}")
        
                   
     
     
    #updatesalestableWidget_sales
    def updatesalestableWidget_sales(self):
            try:
                    totalsales=0
                    connection=self.connectagrimeshDB()
                    cursor=connection.cursor()
                    
                    cursor.execute("""
                                   SELECT productname,buyername,price FROM vieworders
                                   """)
                    results=cursor.fetchall()
                    if results:
                        self.salestableWidget_sales.setRowCount(0)
                        
                        for rowId,rowData in enumerate(results):
                                self.salestableWidget_sales.insertRow(rowId)
                                totalsales+=1
                                for colId,ColData in enumerate(rowData):
                                        self.salestableWidget_sales.setItem(rowId,colId,QTableWidgetItem(str(ColData)))
                                        label=QLabel("Completed")
                                        self.salestableWidget_sales.setCellWidget(rowId, 3, label)
                                
                    self.salestableWidget_sales.resizeColumnsToContents()
                    self.totalsaleslcdNumber.display(totalsales)
                    
                    cursor.close()
                    connection.close()
                    
            except psycopg2.Error as e:
                    QMessageBox.information(None,"Error",f"Error  Occured {e}")
        
    #filterorderstable
    def filterorderstable(self):
        from PyQt6.QtCore import Qt
        selected_filter = self.filterorderscomboBox.currentText()

        if selected_filter == "Quantity":
              column_index = 3  
        elif selected_filter == "Price":
              column_index =4
        else:
              return  

    
        self.vieworderstableWidget.sortItems(column_index, Qt.SortOrder.AscendingOrder)

        
    #updateviewProducepageTableWidget
    def updateviewProducepageTableWidget(self):
            from functools import partial
            try:
                    availableOrders=0
                    connection=self.connectagrimeshDB()
                    cursor=connection.cursor()
                    cursor.execute("""
                                   SELECT * FROM vieworders  
                                   
                                   """)
                    
                    results=cursor.fetchall()
                    
                    self.vieworderstableWidget.setColumnCount(9)
                    headers = [self.vieworderstableWidget.horizontalHeaderItem(i).text() if self.vieworderstableWidget.horizontalHeaderItem(i) else f"Column {i+1}" for i in range(9)]
                    headers[6]="Status"
                    headers[7] = "Cancel Order"
                    headers[8] = "Dispatch Order"
                    

                    self.vieworderstableWidget.setHorizontalHeaderLabels(headers)

                    self.vieworderstableWidget.setRowCount(0)
                    for rowID,rowData in enumerate(results):
                            self.vieworderstableWidget.insertRow(rowID)
                            availableOrders+=1
                            for colID,colData in enumerate(rowData):
                                    self.vieworderstableWidget.setItem(rowID,colID,QTableWidgetItem(str(colData)))
                            btn_add = QPushButton("Cancel Order")
                            btn_add.clicked.connect(lambda _, r=rowData: self.cancelOrder(r))
                            self.vieworderstableWidget.setCellWidget(rowID, 7, btn_add)
                            
                            btn_adddispatch = QPushButton("Accept and Dispatch")
                            btn_adddispatch.clicked.connect(lambda _, r=rowData: self.acceptAndDispatchOrder(r))
                            self.vieworderstableWidget.setCellWidget(rowID, 8, btn_adddispatch)
                           


                            
                    self.pendingordersLCDnumber.display(availableOrders) 
                    self.pendingorder=availableOrders
                    self.vieworderstableWidget.resizeColumnsToContents()        
                    cursor.close()
                    connection.close()
            except psycopg2.Error as e:
                QMessageBox.information(None,"Database Error",f"Error Occurred {e}")
                
       #cancelOrder
    def cancelOrder(self,row):
        
         try:
                connection=self.connectagrimeshDB()
                cursor=connection.cursor()
                cursor.execute("UPDATE vieworders SET status = 'Cancelled' WHERE buyername = %s AND phoneno = %s;",(str(row[0]),str(row[1])))
               
                connection.commit()
                QMessageBox.information(None,"Cancel Order","Order Cancelled Successsfully!")
                cursor.close()
                connection.close()
         except psycopg2.Error as e:
                QMessageBox.information(None,"Database Error",f"Error Occurred {e}")
                
    
    
    #acceptAndDispatchOrder
    def acceptAndDispatchOrder(self,row):
            QMessageBox.information(None,"Order Confirmed","Order was Confirmed. And The buyer Notified!")
    #logoutpushbuttonClicked
    def logoutpushbuttonClicked(self):
        from loginandRegistrationDialog import Ui_loginOrregistrationDialog
        self.loginwindow = QtWidgets.QMainWindow()
        self.ui = Ui_loginOrregistrationDialog()
        self.ui.setupUi(self.loginwindow)
        self.loginwindow.setFixedSize(400, 340)
        self.loginwindow.show()
        QtWidgets.QApplication.instance().activeWindow().close()
        QMessageBox.information(None,"Loggout Successfully","LOGGED OUT SUCCESSFULLY!")
        
    #requestdeletionofAccountcommandLinkButtonClicked
    def requestdeletionofAccountcommandLinkButtonClicked(self):
        from deleteaccount import Ui_deleteaccountdialog
        self.deleteacc = QtWidgets.QMainWindow()
        self.ui = Ui_deleteaccountdialog()
        self.ui.setupUi(self.deleteacc)
        self.deleteacc.setFixedSize(375, 146)
        self.deleteacc.show()
        
    
    
    #connectagrimeshDB
    def connectagrimeshDB(self):
        connection=psycopg2.connect(
                host="localhost",
                user="postgres",
                password="3062",
                database="agrimesh"
        )
        return connection

    #setavalabilitytabclicked
    def  setavalabilitytabclicked(self,index):
            if index == 2 and self.tabWidget.tabText(2)=="Set Availability":
                    QMessageBox.information(None,"Unfortunately!","This Section Is Under Maintainance!\n Come Back Later")
          
     
     #changePasswordpushButtonclicked
    def changePasswordpushButtonclicked(self):
        oldpassword=self.oldpasswordlineEdit_settings.text()
        newpassword=self.newpasswordlinedit_settings.text()
        
        if not oldpassword or not newpassword or  len(oldpassword)>4 or  len(newpassword)>4:
                QMessageBox.warning(None,"Error","All Fields Are Required!\nPassword must also be less than 4 characters!")
                return
        else:
                connection=self.connectagrimeshDB()
                cursor=connection.cursor()
                cursor.execute("SELECT * FROM userinfo WHERE password=%s;",(oldpassword,))
                passwordexists=cursor.fetchone()
                
                if passwordexists:
                        cursor.execute("UPDATE userinfo SET password=%s WHERE password=%s;",(newpassword,oldpassword))
                        connection.commit()
                        QMessageBox.information(None,"Success","Password Changed Successfully!")
                        self.oldpasswordlineEdit_settings.clear()
                        self.newpasswordlinedit_settings.clear()
                else:
                        QMessageBox.warning(None,"Error","Wrong Password!")
                        self.oldpasswordlineEdit_settings.clear()
                        self.newpasswordlinedit_settings.clear()
                        return
                
                connection.commit()
                cursor.close()
                connection.close()
     #saveproduceaspushButton_viewproduceclicked
    def saveproduceaspushButton_viewproduceclicked(self):
        choice=self.saveproduceascomboBox_viewproduce.currentText()
        
        if choice=="PDF format":
                from reportlab.lib.pagesizes import A4
                from reportlab.pdfgen import canvas
                
                connection=self.connectagrimeshDB()
                query = ("SELECT productname, category, quantity, price, location FROM produce")
                cursor=connection.cursor()
                cursor.execute(query)
                records = cursor.fetchall()
                file_name = "produce_report.pdf"
                c = canvas.Canvas(file_name, pagesize=A4)
                width, height = A4
                c.setFont("Helvetica-Bold", 14)
                c.drawString(200, height - 50, "Produce Data Report")
                c.setFont("Helvetica-Bold", 12)
                headers = ["Product Name", "Category", "Quantity", "Price", "Location"]
                x_positions = [50, 150, 300, 400, 500]  
                y_position = height - 80
                for i, header in enumerate(headers):
                   c.drawString(x_positions[i], y_position, header)
                   
                c.line(50, y_position - 5, 550, y_position - 5) 
                c.setFont("Helvetica", 10)
                y_position -= 20
                for row_data in records:
                        if y_position < 50:  
                                c.showPage()
                                y_position = height - 50
                                c.setFont("Helvetica", 10)

                        for col_idx, cell_data in enumerate(row_data):
                                c.drawString(x_positions[col_idx], y_position, str(cell_data))

                        y_position -= 20  

                c.save()
                import os

                file_name = "produce_report.pdf"
                file_path = os.path.abspath(file_name)
                QMessageBox.information(None,"Saved",f"Image saved Successfully As {file_name} to \n\nLocation : {file_path}")
                
                connection.close()
                cursor.close()
        elif choice=="Docx Format":
                file_name = "produce_report.docx"
                from saveProduceasdocx import save_to_docx
                savedpath=save_to_docx(file_name)
                QMessageBox.information(None,"Saved",f"Saved File As {file_name} to \n\nLcation: {savedpath}")
                
        elif choice=="Json":
                file_name = "produce_report.json"
                from saveProduceasJson import save_to_json
                savedjsonpath=save_to_json(file_name)
                QMessageBox.information(None,"Saved",f"Saved File As {file_name} to \n\nLcation: {savedjsonpath}")
                
        elif choice=="CSV":
                file_name = "produce_report.csv"
                from saveProduceasCsv import save_to_csv
                savecsvpath=save_to_csv(file_name)
                QMessageBox.information(None,"Saved",f"Saved File As {file_name} to \n\nLcation: {savecsvpath}")
               
        else:
                file_name = "produce_report.png"
                from saveasScreenshot import save_as_screenshot
                screenshhot=save_as_screenshot(file_name)
                QMessageBox.information(None,"Saved",f"Saved File As {file_name} to \n\nLcation: {screenshhot}")
                
                

             
    #saveprofileinfopushButton_profileclicked
    def saveprofileinfopushButton_profileclicked(self):
            try:
                    name=self.namelineEdit_profile.text()
                    phoneNo=self.phoneNolinedit_profile.text()
                    location=self.locationlineedit_profile.text()
                    paymentmethod=self.paymentaccouncomboBox_profile.currentText()
                    paymentno=self.paymentaccountChoicelinedit_profile.text()
                    
                    if not name or not phoneNo or not location:
                            QMessageBox.warning(None,"Error","All Fields Are Required!")
                            return
                    else:
                            phoneNo=int(phoneNo)
                            paymentno=int(paymentno)
                            connection=self.connectToDB()
                            cursor=connection.cursor()
                            cursor.execute("""
                                           CREATE TABLE IF NOT EXISTS profileinfo(
                                                   name VARCHAR(20),
                                                   phoneno INTEGER PRIMARY KEY,
                                                   location VARCHAR(20),
                                                   paymentmethod VARCHAR(10),
                                                   paymentno INTEGER    
                                           )
                                           """)
                            print("table created successfuly!")
                            cursor.execute("""
                                           INSERT INTO  profileinfo(name,phoneno,location,paymentmethod,paymentno)
                                           VALUES(%s,%s,%s,%s,%s) ON CONFLICT
                                           (phoneNo) DO NOTHING;
                                           """,(name,phoneNo,location,paymentmethod,paymentno))
                            connection.commit()
                            QMessageBox.information(None,"Success","Profile Info Saved Successfully!")
                            cursor.close()
                            connection.close()
                            
            except psycopg2.Error as e:
                    QMessageBox.warning(None,"Error",f"Error: {e}")
             
    
    
    #create database 
    def createdatabaseConnection(self):
            
            connection=psycopg2.connect(
                    host="localhost",
                    user="postgres",
                    password="3062",
                    database="postgres"
                    
            )
            connection.autocommit = True
            cursor=connection.cursor()
            cursor.execute("SELECT 1 FROM pg_database WHERE datname='agrimesh'")
            exists=cursor.fetchone()
            if not  exists:
                cursor.execute("CREATE DATABASE agrimesh")
            cursor=connection.cursor()
            cursor.close()
    #connect to db
    def connectToDB(self):
        conection=psycopg2.connect(
                    host="localhost",
                    user="postgres",
                    password="3062",
                    database="agrimesh"
                    
            )
        return conection
     
     
     #paymentmethodcombotextchanged
    def paymentmethodtextchanged(self):
            method=self.paymentaccouncomboBox_profile.currentText()
            
            if method=="M-PESA":
                    self.paymentaccountChoicelinedit_profile.setPlaceholderText("Enter Your M-PESA number")
            elif method=="KCB":
                    self.paymentaccountChoicelinedit_profile.setPlaceholderText("Enter Bank Account Number")
            else:
                    self.paymentaccountChoicelinedit_profile.setPlaceholderText("Enter airtel money number")

    def switchtodarkmodeCommandlinkbuttonclicked(self, MainWindow):
        # Dark Mode Stylesheet
        dark_mode_stylesheet = """
        QWidget {
            background-color: #2E2E2E;
            color: white;
        }
        QPushButton {
            background-color: #444444;
            color: white;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #666666;
        }
        QLineEdit {
            background-color: #444444;
            color: white;
            border: 1px solid #666666;
        }
        QComboBox {
            background-color: #444444;
            color: white;
            border: 1px solid #666666;
        }
        """
        
        # Apply Dark Mode stylesheet to the whole MainWindow
        self.centralwidget.setStyleSheet(dark_mode_stylesheet)  
        self.widget1.setStyleSheet(dark_mode_stylesheet)             
        self.widget.setStyleSheet(dark_mode_stylesheet)  
        
        
   #addTheProducePushButtonClicked
    def addTheProducePushButtonClicked(self):
        productname=self.productnamelineEdit.text().lower()
        category=self.productcategorycomboBox.currentText()
        quantity=self.quantitylinedit.text()
        price=self.pricelinedit.text()
        location=self.locationlinedit.text()
        imagepath=self.imageproducepath.text()
        
        if not productname or not location or not quantity or not price or not imagepath:
                QMessageBox.information(None,"Error","All fields Are Required!")
                return
        else:
                try:
                        connection=self.connectagrimeshDB()
                        cursor=connection.cursor()
                        cursor.execute("""
                                       CREATE TABLE IF NOT EXISTS produce(
                                               
                                               productname VARCHAR(20),
                                               category TEXT,
                                               quantity VARCHAR(20),
                                               price INTEGER,
                                               location TEXT,
                                               imagepath VARCHAR(200)
                                       )
                                       
                                       """)
                        cursor.execute("""
                                       INSERT INTO produce(productname,category,quantity,price,location,imagepath)
                                       VALUES(%s,%s,%s,%s,%s,%s)
                                       
                                       """,(productname,category,quantity,price,location,imagepath))
                        connection.commit()
                        
                        from plyer import notification
                        notification.notify(
                                title="Success",
                                message=f"{productname} added successfully!",
                                app_name="JustoSoftwares"
                                
                        )
                        QMessageBox.information(None,"Error","Produce Added Successfully!")
                        cursor.close()
                        connection.close()
                except psycopg2.Error as e:
                        QMessageBox.information(None,"Error",f"An error Occurred {e}")
    
    #uploadProduceImagepushButtonClicked
    def uploadProduceImagepushButtonClicked(self):
        fileFilter="Images (*.png *.jpg *.BMP *.GIF *.TIFF *.webp)"
        filepath,_=QFileDialog.getOpenFileName(None,"SELCT IMAGE FILE","",fileFilter)
        if filepath:
                from PyQt6.QtGui import QPixmap
                QMessageBox.information(None,"Success","Image uploaded Successfully!")
                self.imageproducepath.setText(filepath)
                pixmap = QPixmap(filepath)
                self.imagesettinglabel.setPixmap(pixmap)
                self.imagesettinglabel.setScaledContents(True)
           
        else:
              QMessageBox.information(None,"Success","Image Not Uploaded Try Again!")  
              self.imageproducepath.setText("No Image selected")

    #updateviewProduceTableWidget
    def updateviewProduceTableWidget(self):
                availableproduce=0
                connection = self.connectagrimeshDB()
                cursor = connection.cursor()

                
                query = "SELECT productname, category, quantity, price, location FROM produce"
                cursor.execute(query)
                records = cursor.fetchall()

                
                cursor.close()
                connection.close()

                
                self.viewProducetableWidget.setRowCount(0)

                for row_idx, row_data in enumerate(records):
                        self.viewProducetableWidget.insertRow(row_idx)  
                        availableproduce+=1
                        for col_idx, cell_data in enumerate(row_data):
                                self.viewProducetableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(cell_data)))
                
                self.availableproduceLCDnumber.display(availableproduce)
                self.availableproduce=availableproduce
                                
                                
     #updateeditproduceTablewidget
    def updateeditproduceTablewidget(self):
        connection = self.connectagrimeshDB()
        cursor = connection.cursor()

        # Fetch data
        query = ("SELECT productname, category, quantity, price, location FROM produce")
        cursor.execute(query)
        records = cursor.fetchall()

        # Close connection
        cursor.close()
        connection.close()
        

        # Clear existing rows only 
        self.editproducetableWidget.setRowCount(0)
                
        for row_idx, row_data in enumerate(records):
                self.editproducetableWidget.insertRow(row_idx)  
                for col_idx, cell_data in enumerate(row_data):
                        self.editproducetableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(cell_data)))
        
                        btn_edit = QPushButton("Edit")
                        btn_edit.clicked.connect(lambda _, r=row_idx: self.edit_product(r))  
                        self.editproducetableWidget.setCellWidget(row_idx, 5, btn_edit)

               
      #edit_product
    def edit_product(self,row):
         details = [self.editproducetableWidget.item(row, col).text() for col in range(5)]
         from editproduceDialog import Ui_editproduceDialog
         self.editproducedialoG = QtWidgets.QMainWindow()
         self.ui = Ui_editproduceDialog()
         self.ui.setupUi(self.editproducedialoG)
         self.ui.fillInLineEdits(details)
         self.editproducedialoG.setFixedSize(384, 300)
         
         self.ui.editandsavepushButton_editproduce.clicked.connect(lambda: self.ui.editandsavepushButton_editproduceClicked(details))
         self.editproducedialoG.show()
         
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())