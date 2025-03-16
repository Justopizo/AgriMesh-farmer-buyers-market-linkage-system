
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from farmersDashboard import Ui_MainWindow
import psycopg2
from    PyQt6.QtCore import QTimer,QDateTime
from PyQt6.QtGui import QIcon

class Ui_admnidashboardDialog(object):
    def setupUi(self, admnidashboardDialog):
        admnidashboardDialog.setObjectName("admnidashboardDialog")
        admnidashboardDialog.resize(954, 713)
        self.widget = QtWidgets.QWidget(parent=admnidashboardDialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 281, 711))
        self.widget.setStyleSheet("background-color: rgb(31, 0, 93);")
        self.widget.setObjectName("widget")
        self.widget1 = QtWidgets.QWidget(parent=self.widget)
        self.widget1.setGeometry(QtCore.QRect(10, 20, 261, 621))
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
        self.managefarmerspushbutton = QtWidgets.QPushButton(parent=self.widget1)
        self.managefarmerspushbutton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.managefarmerspushbutton.setObjectName("managefarmerspushbutton")
        self.managefarmerspushbutton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.verticalLayout.addWidget(self.managefarmerspushbutton)
        self.managebuyerspushbutton = QtWidgets.QPushButton(parent=self.widget1)
        self.managebuyerspushbutton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.managebuyerspushbutton.setObjectName("managebuyerspushbutton")
        self.managebuyerspushbutton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.verticalLayout.addWidget(self.managebuyerspushbutton)
        self.manageproductslisting = QtWidgets.QPushButton(parent=self.widget1)
        self.manageproductslisting.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.manageproductslisting.setObjectName("manageproductslisting")
        self.manageproductslisting.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.verticalLayout.addWidget(self.manageproductslisting)
        self.reportsandanalyticspushbutton = QtWidgets.QPushButton(parent=self.widget1)
        self.reportsandanalyticspushbutton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.reportsandanalyticspushbutton.setObjectName("reportsandanalyticspushbutton")
        self.reportsandanalyticspushbutton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.verticalLayout.addWidget(self.reportsandanalyticspushbutton)
        self.logoutpushbutton = QtWidgets.QPushButton(parent=self.widget1)
        self.logoutpushbutton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.logoutpushbutton.setObjectName("logoutpushbutton")
        self.logoutpushbutton.clicked.connect(self.logoutpushbuttonclicked)
        self.verticalLayout.addWidget(self.logoutpushbutton)
        self.widget_2 = QtWidgets.QWidget(parent=admnidashboardDialog)
        self.widget_2.setGeometry(QtCore.QRect(280, 0, 671, 711))
        self.widget_2.setObjectName("widget_2")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget_2)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 671, 711))
        self.stackedWidget.setObjectName("stackedWidget")
        self.dashboardpage = QtWidgets.QWidget()
        self.dashboardpage.setObjectName("dashboardpage")
        self.groupBox = QtWidgets.QGroupBox(parent=self.dashboardpage)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 351, 241))
        self.groupBox.setObjectName("groupBox")
        self.managefarmers_commandLinkButton = QtWidgets.QCommandLinkButton(parent=self.groupBox)
        self.managefarmers_commandLinkButton.setGeometry(QtCore.QRect(10, 20, 222, 48))
        self.managefarmers_commandLinkButton.setObjectName("managefarmers_commandLinkButton")
        self.managebuyers_commandLinkButton = QtWidgets.QCommandLinkButton(parent=self.groupBox)
        self.managebuyers_commandLinkButton.setGeometry(QtCore.QRect(10, 100, 222, 48))
        self.managebuyers_commandLinkButton.setObjectName("managebuyers_commandLinkButton")
        self.managefarmers_commandLinkButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.reportsandAnalytics_commandlinkbutton = QtWidgets.QCommandLinkButton(parent=self.groupBox)
        self.reportsandAnalytics_commandlinkbutton.setGeometry(QtCore.QRect(10, 180, 251, 48))
        self.reportsandAnalytics_commandlinkbutton.setObjectName("reportsandAnalytics_commandlinkbutton")
        self.reportsandAnalytics_commandlinkbutton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.dashboardpage)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 0, 311, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 111, 16))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 101, 16))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 101, 16))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.totalbuyers_lcdNumber = QtWidgets.QLCDNumber(parent=self.groupBox_2)
        self.totalbuyers_lcdNumber.setGeometry(QtCore.QRect(160, 30, 64, 23))
        self.totalbuyers_lcdNumber.setObjectName("totalbuyers_lcdNumber")
        self.totalfarmers_lcdNumber = QtWidgets.QLCDNumber(parent=self.groupBox_2)
        self.totalfarmers_lcdNumber.setGeometry(QtCore.QRect(160, 70, 64, 23))
        self.totalfarmers_lcdNumber.setObjectName("totalfarmers_lcdNumber")
        self.totaluser_lcdNumber = QtWidgets.QLCDNumber(parent=self.groupBox_2)
        self.totaluser_lcdNumber.setGeometry(QtCore.QRect(160, 120, 64, 23))
        self.totaluser_lcdNumber.setObjectName("totaluser_lcdNumber")
        self.todaydatecount_label = QtWidgets.QLabel(parent=self.groupBox_2)
        self.todaydatecount_label.setGeometry(QtCore.QRect(160, 190, 101, 16))
        self.todaydatecount_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.todaydatecount_label.setObjectName("todaydatecount_label")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.dashboardpage)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 240, 671, 471))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(20, 15, 141, 31))
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.userdistribution_graphicsView = QtWidgets.QGraphicsView(parent=self.groupBox_3)
        self.userdistribution_graphicsView.setGeometry(QtCore.QRect(0, 50, 321, 411))
        self.userdistribution_graphicsView.setObjectName("userdistribution_graphicsView")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(390, 15, 231, 21))
        self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.salesbycategory_graphicsView = QtWidgets.QGraphicsView(parent=self.groupBox_3)
        self.salesbycategory_graphicsView.setGeometry(QtCore.QRect(320, 50, 351, 411))
        self.salesbycategory_graphicsView.setObjectName("salesbycategory_graphicsView")
        self.stackedWidget.addWidget(self.dashboardpage)
        self.managefarmespage = QtWidgets.QWidget()
        self.managefarmespage.setObjectName("managefarmespage")
        self.managefarmers_tableWidget = QtWidgets.QTableWidget(parent=self.managefarmespage)
        self.managefarmers_tableWidget.setGeometry(QtCore.QRect(0, 0, 671, 461))
        self.managefarmers_tableWidget.setObjectName("managefarmers_tableWidget")
        self.managefarmers_tableWidget.setColumnCount(4)
        self.managefarmers_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.managefarmers_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.managefarmers_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.managefarmers_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.managefarmers_tableWidget.setHorizontalHeaderItem(3, item)
        self.stackedWidget.addWidget(self.managefarmespage)
        self.managebuyerspage = QtWidgets.QWidget()
        self.managebuyerspage.setObjectName("managebuyerspage")
        self.manageBuyers_tableWidget = QtWidgets.QTableWidget(parent=self.managebuyerspage)
        self.manageBuyers_tableWidget.setGeometry(QtCore.QRect(0, 0, 671, 441))
        self.manageBuyers_tableWidget.setObjectName("manageBuyers_tableWidget")
        self.manageBuyers_tableWidget.setColumnCount(4)
        self.manageBuyers_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.manageBuyers_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.manageBuyers_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.manageBuyers_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.manageBuyers_tableWidget.setHorizontalHeaderItem(3, item)
        self.stackedWidget.addWidget(self.managebuyerspage)
        self.manageproductlistingspage = QtWidgets.QWidget()
        self.manageproductlistingspage.setObjectName("manageproductlistingspage")
        self.manageproductlistings_tableWidget = QtWidgets.QTableWidget(parent=self.manageproductlistingspage)
        self.manageproductlistings_tableWidget.setGeometry(QtCore.QRect(0, 0, 671, 501))
        self.manageproductlistings_tableWidget.setObjectName("manageproductlistings_tableWidget")
        self.manageproductlistings_tableWidget.setColumnCount(6)
        self.manageproductlistings_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.manageproductlistings_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.manageproductlistings_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.manageproductlistings_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.manageproductlistings_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.manageproductlistings_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.manageproductlistings_tableWidget.setHorizontalHeaderItem(5, item)
        self.stackedWidget.addWidget(self.manageproductlistingspage)
        self.reportsandAnalyticspage = QtWidgets.QWidget()
        self.reportsandAnalyticspage.setObjectName("reportsandAnalyticspage")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.reportsandAnalyticspage)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 10, 661, 241))
        self.groupBox_4.setObjectName("groupBox_4")
        self.downloadusersreport_commandLinkButton = QtWidgets.QCommandLinkButton(parent=self.groupBox_4)
        self.downloadusersreport_commandLinkButton.setGeometry(QtCore.QRect(20, 20, 271, 48))
        self.downloadusersreport_commandLinkButton.setObjectName("downloadusersreport_commandLinkButton")
        self.downloadsalesreport_commandLinkButton = QtWidgets.QCommandLinkButton(parent=self.groupBox_4)
        self.downloadsalesreport_commandLinkButton.setGeometry(QtCore.QRect(20, 90, 261, 48))
        self.downloadsalesreport_commandLinkButton.setObjectName("downloadsalesreport_commandLinkButton")
        self.allreportscommandLinkButton = QtWidgets.QCommandLinkButton(parent=self.groupBox_4)
        self.allreportscommandLinkButton.setGeometry(QtCore.QRect(370, 20, 222, 48))
        self.allreportscommandLinkButton.setObjectName("allreportscommandLinkButton")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.reportsandAnalyticspage)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 260, 671, 441))
        self.groupBox_5.setObjectName("groupBox_5")
        self.analysisAI_textEdit = QtWidgets.QTextEdit(parent=self.groupBox_5)
        self.analysisAI_textEdit.setGeometry(QtCore.QRect(10, 20, 661, 421))
        self.analysisAI_textEdit.setObjectName("analysisAI_textEdit")
        self.stackedWidget.addWidget(self.reportsandAnalyticspage)

        self.retranslateUi(admnidashboardDialog)
        QtCore.QMetaObject.connectSlotsByName(admnidashboardDialog)
        
        self.timer=QTimer()
        self.timer.timeout.connect(self.todayDateLableupdate)
        self.timer.timeout.connect(self.populateManageproductlisTablewidget)
        self.timer.timeout.connect(self.populatemanagebuyertablewidget)
        self.timer.timeout.connect(self.populatefarmerstableWidget)
        self.timer.timeout.connect(self.plotuserdistributiongraph)
        self.timer.timeout.connect(self.plotcategorysalesGraph)
        self.timer.timeout.connect(self.notify)
        self.timer.start(1000)
        self.farmer=0
        self.Buyers=0
        self.todayDateLableupdate()
        self.getFarmercount()
        self.getBuyersCount()
        self.getTotalusers()
        self.populateManageproductlisTablewidget()
        self.populatemanagebuyertablewidget()
        self.populatefarmerstableWidget()
        self.plotcategorysalesGraph()
        self.downloadusersreport_commandLinkButton.clicked.connect(self.downloadusersreport_commandLinkButtonclicked)
        self.downloadsalesreport_commandLinkButton.clicked.connect(self.downloadsalesreport_commandLinkButtonclicked)
        self.allreportscommandLinkButton.clicked.connect(self.allreportscommandLinkButtonclicked)
        
    #notifications
    def notify(self):
            from getanalysisNotificationReport import generate_report
            self.analysisAI_textEdit.setText(generate_report())
        
    #allreportscommandLinkButtonclicked
    def allreportscommandLinkButtonclicked(self):
            from allreports import save_combined_docx
            filename="allreports.docx"
            path=save_combined_docx(filename,self.analysisAI_textEdit)
            QMessageBox.information(None,"Docx",f"Report File '{filename}' saved to {path}")
        
    #downloadsalesreport_commandLinkButtonclicked
    def downloadsalesreport_commandLinkButtonclicked(self):
            from salesreport import save_to_docx
            filename="sale_report.docx"
            path=save_to_docx(filename)
            QMessageBox.information(None,"Docx",f"sales Report File '{filename}' saved to {path}")
            
        
    #downloadusersreport_commandLinkButtonclicked
    def downloadusersreport_commandLinkButtonclicked(self):
            from usersreport import save_to_docx
            filename="user_Report.pdf"
            path=save_to_docx(filename)
            QMessageBox.information(None,"PDF",f"Users Report File '{filename}' saved to {path}")
        
      
    #plotcategorysalesGraph
    def plotcategorysalesGraph(self):
        from produceBycategory import ProduceChartHelper
        chart = ProduceChartHelper(self.salesbycategory_graphicsView)  
        chart.load_chart()
        
            
    #plotuserdistributiongraph
    def plotuserdistributiongraph(self):
                import plotfarmerAgainbuyerstallygraph
                farmers = self.farmer
                buyers = self.Buyers
                plotfarmerAgainbuyerstallygraph.plot_user_distribution(self.userdistribution_graphicsView, farmers, buyers)
        
     #populatebuyerstableWidget
    def populatefarmerstableWidget(self):
            try:
                connection=Ui_MainWindow.connectagrimeshDB(self)
                cursor=connection.cursor()
                query = """
 SELECT 
    u.name, 
    COALESCE(p.location, 'N/A') AS location, 
    COALESCE(CAST(p.phoneno AS TEXT), 'N/A') AS phoneno
FROM userinfo u
LEFT JOIN profileinfo p ON u.name = p.name WHERE role='Farmer';


    """

                cursor.execute(query)
                records = cursor.fetchall()

                self.managefarmers_tableWidget.setRowCount(len(records))

                for row_index, row_data in enumerate(records):
                         for col_index, col_data in enumerate(row_data):
                                 self.managefarmers_tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
                                 btn=QPushButton("Unregister User")
                                 self.managefarmers_tableWidget.setCellWidget(row_index,len(row_data),btn)
                                 btn.clicked.connect(lambda _,r=row_data: self.unregisterfarmer(r))
                connection.commit()
                self.managefarmers_tableWidget.resizeColumnToContents(col_index)
                cursor.close()
                connection.close()
                
            except psycopg2.Error as e:
                QMessageBox.information(None,"Error",f"Error Occrred {e}")  
                
    #unregisterbuyer
    def unregisterfarmer(self,data):
            try:
                name,location,phoneno=data
                connection=Ui_MainWindow.connectagrimeshDB(self)
                cursor=connection.cursor()
                cursor.execute("DELETE FROM userinfo WHERE name=%s;",(name,))
                connection.commit()
                QMessageBox.information(None,"Success",f"User '{name}' Unregistered!!")
                cursor.close()
                connection.close()
            except psycopg2.Error as e:
                    QMessageBox.information(None,"Error",f"Error Occrred {e}")  
        
    #populatemanagebuyertablewidget
    def populatemanagebuyertablewidget(self):
            try:
                connection=Ui_MainWindow.connectagrimeshDB(self)
                cursor=connection.cursor()
                query = """
    SELECT 
        u.name, 
        COALESCE(b.location, 'N/A') AS location, 
        COALESCE(b.phoneno, 'N/A') AS phoneno
    FROM userinfo u
    LEFT JOIN buyerinfo b ON u.name = b.name WHERE role='Buyer';
    """

                cursor.execute(query)
                records = cursor.fetchall()

                self.manageBuyers_tableWidget.setRowCount(len(records))

                for row_index, row_data in enumerate(records):
                         for col_index, col_data in enumerate(row_data):
                                 self.manageBuyers_tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
                                 btn=QPushButton("Unregister User")
                                 self.manageBuyers_tableWidget.setCellWidget(row_index,len(row_data),btn)
                                 btn.clicked.connect(lambda _,r=row_data: self.unregisterbuyer(r))
                connection.commit()
                   
                cursor.close()
                connection.close()
                
            except psycopg2.Error as e:
                QMessageBox.information(None,"Error",f"Error Occrred {e}")
                
     #unregisterbuyer
    def unregisterbuyer(self,data):
            try:
                name,location,phoneno=data
                connection=Ui_MainWindow.connectagrimeshDB(self)
                cursor=connection.cursor()
                cursor.execute("DELETE FROM userinfo WHERE name=%s;",(name,))
                connection.commit()
                QMessageBox.information(None,"Success",f"User '{name}' Unregistered!!")
                cursor.close()
                connection.close()
            except psycopg2.Error as e:
                    QMessageBox.information(None,"Error",f"Error Occrred {e}")
                
        
        
    #populateManageproductlisTablewidget
    def populateManageproductlisTablewidget(self):
            try:
                    connection=Ui_MainWindow.connectagrimeshDB(self)
                    cursor=connection.cursor()
                    cursor.execute("SELECT productname, category, quantity, price,  imagepath  FROM produce")
                    results=cursor.fetchall()
                    self.manageproductlistings_tableWidget.setRowCount(0)
                    
                    for row,produce in enumerate(results):
                            self.manageproductlistings_tableWidget.insertRow(row)
                            for col in range(4):
                                self.manageproductlistings_tableWidget.setItem(row,col,QTableWidgetItem(str(produce[col])))
                                viewimage=QPushButton("View Image")
                                self.manageproductlistings_tableWidget.setCellWidget(row,4,viewimage)
                                viewimage.clicked.connect(lambda _,row=produce[4]: self.showImagedialog(row))
                                deleteproduct=QPushButton("Delete Product")
                                self.manageproductlistings_tableWidget.setCellWidget(row,5,deleteproduct)
                                deleteproduct.clicked.connect(lambda _,row=produce: self.deleteproduct(row))
                   
            except psycopg2.Error as e:
                    QMessageBox.information(None,"Error",f"Error Occrred {e}")

    #deleteproduct
    def deleteproduct(self,data):
            try:
                    productname, category, quantity, price,  imagepath =data
                    connection=Ui_MainWindow.connectagrimeshDB(self)
                    cursor=connection.cursor()
                    cursor.execute("UPDATE produce SET status='Cancelled' WHERE productname=%s;",(productname,))
                    connection.commit()
                    
                    QMessageBox.information(None,"Success",f"Product '{productname}' Deleted successfully!")
                    self.populateManageproductlisTablewidget()
                    cursor.close()
                    connection.close()    
                    
            except psycopg2.Error as e:
                    QMessageBox.information(None,"Error",f"An Error occurred {e}")
                              
                    
    def showImagedialog(self,imagepath):
        from PyQt6.QtGui import QPixmap
        from imagedialog import Ui_imageDialog_admin
        self.imagedialog = QtWidgets.QMainWindow()
        self.ui = Ui_imageDialog_admin()
        self.ui.setupUi(self.imagedialog)
        pixmap=QPixmap(imagepath)
        self.ui.imagelabel.setPixmap(pixmap)
        self.ui.imagelabel.setScaledContents(True)
        self.imagedialog.setFixedSize(264, 265)
        self.imagedialog.show()
            
            
    #logoutpushbuttonclicked
    def logoutpushbuttonclicked(self):
        QMessageBox.information(None,"Logout","Are You Sure You Want To logout?")
        QtWidgets.QApplication.instance().activeWindow().close()
        from loginandRegistrationDialog import Ui_loginOrregistrationDialog
        self.loginwindow = QtWidgets.QMainWindow()
        self.ui = Ui_loginOrregistrationDialog()
        self.ui.setupUi(self.loginwindow)
        self.loginwindow.setFixedSize(400, 340)
        self.loginwindow.show()
        QMessageBox.information(None,"Loggout Successfully","LOGGED OUT SUCCESSFULLY!")
        
    #get farmers count
    def getFarmercount(self):
            try:
                    connection=Ui_MainWindow.connectagrimeshDB(self)
                    cursor=connection.cursor()
                    cursor.execute("SELECT * FROM userinfo WHERE role='Farmer'")
                    results=cursor.fetchall()
                    count=len(results)
                    cursor.close()
                    self.totalfarmers_lcdNumber.display(count)
                    self.farmer=count
            except psycopg2.Error as e:
                    QMessageBox.information(None,"Error",f"Error Occrred {e}")
                    
    #getBuyersCount
    def getBuyersCount(self):
            try:
                    connection=Ui_MainWindow.connectagrimeshDB(self)
                    cursor=connection.cursor()
                    cursor.execute("SELECT * FROM userinfo WHERE role='Buyer'")
                    results=cursor.fetchall()
                    count=len(results)
                    cursor.close()
                    self.totalbuyers_lcdNumber.display(count)
                    self.Buyers=count
            except psycopg2.Error as e:
                    QMessageBox.information(None,"Error",f"Error Occrred {e}")
                    
     #getTotalusers
    def getTotalusers(self):
              try:
                    connection=Ui_MainWindow.connectagrimeshDB(self)
                    cursor=connection.cursor()
                    cursor.execute("SELECT * FROM userinfo ")
                    results=cursor.fetchall()
                    count=len(results)
                    cursor.close()
                    self.totaluser_lcdNumber.display(count)
              except psycopg2.Error as e:
                    QMessageBox.information(None,"Error",f"Error Occrred {e}")
                    
     #todayDateLableupdate
    def todayDateLableupdate(self):
            currentTime=QDateTime.currentDateTime()
            formatedTime=currentTime.toString("dddd,dd MMMM yyyy-hh:mm:ss AP")
            self.todaydatecount_label.setText(formatedTime)
            

    def retranslateUi(self, admnidashboardDialog):
        _translate = QtCore.QCoreApplication.translate
        admnidashboardDialog.setWindowTitle(_translate("admnidashboardDialog", "Admin-Agrimesh Company"))
        self.dashboardwidgetpushButton.setText(_translate("admnidashboardDialog", "Dashboard"))
        self.managefarmerspushbutton.setText(_translate("admnidashboardDialog", "Manage Farmers"))
        self.managebuyerspushbutton.setText(_translate("admnidashboardDialog", "Manage Buyers"))
        self.manageproductslisting.setText(_translate("admnidashboardDialog", "Manage Product Listings"))
        self.reportsandanalyticspushbutton.setText(_translate("admnidashboardDialog", "Reports and Analytics"))
        self.logoutpushbutton.setText(_translate("admnidashboardDialog", "Logout"))
        self.groupBox.setTitle(_translate("admnidashboardDialog", "Quick Actions"))
        self.managefarmers_commandLinkButton.setText(_translate("admnidashboardDialog", "Manage Farmers"))
        self.managebuyers_commandLinkButton.setText(_translate("admnidashboardDialog", "Manage Buyers"))
        self.managebuyers_commandLinkButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.reportsandAnalytics_commandlinkbutton.setText(_translate("admnidashboardDialog", "Reports and Analytics"))
        self.groupBox_2.setTitle(_translate("admnidashboardDialog", "Tallies"))
        self.label.setText(_translate("admnidashboardDialog", "Total Buyers"))
        self.label_2.setText(_translate("admnidashboardDialog", "Total Farmers"))
        self.label_3.setText(_translate("admnidashboardDialog", "Total Users"))
        self.label_4.setText(_translate("admnidashboardDialog", "Date"))
        self.todaydatecount_label.setText(_translate("admnidashboardDialog", "today is"))
        self.groupBox_3.setTitle(_translate("admnidashboardDialog", "Graphs Displays"))
        self.label_5.setText(_translate("admnidashboardDialog", "Users Distribution"))
        self.label_6.setText(_translate("admnidashboardDialog", "Sales Distribution By category"))
        item = self.managefarmers_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("admnidashboardDialog", "Name"))
        item = self.managefarmers_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("admnidashboardDialog", "Location"))
        item = self.managefarmers_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("admnidashboardDialog", "PhoneNo"))
        item = self.managefarmers_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("admnidashboardDialog", "Action"))
        item = self.manageBuyers_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("admnidashboardDialog", "Name"))
        item = self.manageBuyers_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("admnidashboardDialog", "Location"))
        item = self.manageBuyers_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("admnidashboardDialog", "PhoneNo"))
        item = self.manageBuyers_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("admnidashboardDialog", "Action"))
        item = self.manageproductlistings_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("admnidashboardDialog", "Product Name"))
        item = self.manageproductlistings_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("admnidashboardDialog", "Category"))
        item = self.manageproductlistings_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("admnidashboardDialog", "Quantity"))
        item = self.manageproductlistings_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("admnidashboardDialog", "Price"))
        item = self.manageproductlistings_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("admnidashboardDialog", "View Image"))
        item = self.manageproductlistings_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("admnidashboardDialog", "Action"))
        self.groupBox_4.setTitle(_translate("admnidashboardDialog", "Users Reports"))
        self.downloadusersreport_commandLinkButton.setText(_translate("admnidashboardDialog", "Download Users Reports"))
        self.downloadsalesreport_commandLinkButton.setText(_translate("admnidashboardDialog", "Download Sales Reports"))
        self.allreportscommandLinkButton.setText(_translate("admnidashboardDialog", "All reports"))
        self.groupBox_5.setTitle(_translate("admnidashboardDialog", "Analysis AI notifications"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admnidashboardDialog = QtWidgets.QDialog()
    ui = Ui_admnidashboardDialog()
    ui.setupUi(admnidashboardDialog)
    admnidashboardDialog.show()
    sys.exit(app.exec())
