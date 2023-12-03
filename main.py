import sys
import numpy as np
from PyQt6.QtWidgets import *
import graph_widget as gw
import file_select_frame as fsf

pi = 3.14159
# making use of color palette from here: https://colorhunt.co/palette/363062435585818fb4f5e8c7


if __name__ == "__main__":
    # app preparation
    app = QApplication(sys.argv)
    app.setApplicationName("Sound Visualizer")
    app.setStyleSheet("QWidget { background-color: rgb(54, 48, 98); color: rgb(245, 232, 199); } ")
    window = QWidget()
    layout = QHBoxLayout(window)
    settings_layout = QVBoxLayout()
    graph_layout = QVBoxLayout()

    # graph setup
    label1 = QLabel("Sin Wave")
    graph_layout.addWidget(label1)
    x = np.arange(0, 8*pi, .01)
    y = np.sin(1*x)
    figure1 = gw.GraphWidget(x, y)
    graph_layout.addWidget(figure1)

    # file select setup
    file_select_label = QLabel("Select a sound file to analyze:")
    settings_layout.addWidget(file_select_label)
    file_select_frame = fsf.FileSelectFrame()
    settings_layout.addWidget(file_select_frame)

    # frames setup
    graph_frame = QFrame()
    graph_frame.setLayout(graph_layout)
    settings_frame = QFrame()
    settings_frame.setLayout(settings_layout)
    layout.addWidget(settings_frame)
    layout.addWidget(graph_frame)

    # execution
    window.show()
    app.exec()
