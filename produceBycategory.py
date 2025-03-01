import psycopg2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtCore import Qt

class ProduceChartHelper:
    def __init__(self, category_view):
        self.category_view = category_view

    def load_chart(self):
        data = self.fetch_data()

        if not data:
            return  

        categories = [row[0] for row in data]
        prices = [row[1] for row in data]

        
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(categories, prices, color='#1F005D')
        ax.set_title("Produce Prices per Category")
        ax.set_ylabel("Price (KES)")
        ax.set_xlabel("Category")
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        
        canvas = FigureCanvas(fig)
        scene = QGraphicsScene()
        scene.addWidget(canvas)

        self.category_view.setScene(scene)

        
        self.category_view.fitInView(scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
        plt.close(fig)

    def fetch_data(self):
        try:
            from farmersDashboard import Ui_MainWindow
            conn = Ui_MainWindow.connectagrimeshDB(self)
           
            cursor = conn.cursor()
            cursor.execute("SELECT category, price FROM produce")
            data = cursor.fetchall()
            conn.close()
            return data
        except Exception as e:
            print(f"Database error: {e}")
            return []
