import sys
import matplotlib.pyplot as plt
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QGraphicsScene
from io import BytesIO

class ProduceChartHelper:
    def __init__(self, graphics_view):
        self.graphics_view = graphics_view

    def load_pie_chart(self, sales, orders, available):
        labels = ["Sales", "Orders", "Available Produce"]
        values = [sales, orders, available]
        colors = ["#00008B", "#0000CD", "#191970"]  

        fig, ax = plt.subplots(figsize=(6, 6), dpi=150)  
        ax.pie(
            values, labels=labels, autopct='%1.1f%%', startangle=140,
            colors=colors, wedgeprops={"edgecolor": "black", "linewidth": 1.5}
        )

        buf = BytesIO()
        plt.savefig(buf, format="png", bbox_inches='tight', transparent=True)
        plt.close(fig)

    
        buf.seek(0)
        img = QImage.fromData(buf.getvalue())
        pixmap = QPixmap.fromImage(img)

        scaled_pixmap = pixmap.scaled(
            self.graphics_view.width(), self.graphics_view.height()
        )


        scene = QGraphicsScene()
        scene.addPixmap(scaled_pixmap)
        self.graphics_view.setScene(scene)
