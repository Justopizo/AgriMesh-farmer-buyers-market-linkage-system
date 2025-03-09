import psycopg2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtCore import Qt

def plot_user_distribution(graphics_view, farmers, buyers):
    if farmers is None or buyers is None:
        return

    farmers = int(farmers)
    buyers = int(buyers)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(["Farmers", "Buyers"], [farmers, buyers], color="#301A66")
    ax.set_title("User Distribution")
    ax.set_ylabel("Number of Users")
    ax.set_xlabel("User Type")
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    canvas = FigureCanvas(fig)
    scene = QGraphicsScene()
    scene.addWidget(canvas)

    graphics_view.setScene(scene)
    graphics_view.fitInView(scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
    

    plt.close(fig)
