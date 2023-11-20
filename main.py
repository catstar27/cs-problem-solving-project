import sys
import numpy as np
from PyQt6.QtWidgets import *
import graph_widget as gw

pi = 3.14159

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout(window)
    label1 = QLabel("Sin Wave")
    layout.addWidget(label1)
    x = np.arange(0, 8*pi, .1)
    y = np.sin(4*x)
    z = 3*x
    figure1 = gw.GraphWidget(x, y)
    layout.addWidget(figure1)
    label2 = QLabel("Line")
    layout.addWidget(label2)
    figure2 = gw.GraphWidget(x, z)
    layout.addWidget(figure2)
    window.show()
    app.exec()
