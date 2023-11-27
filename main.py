import sys
import numpy as np
from PyQt6.QtWidgets import *
import graph_widget as gw
import file_dialog_window as fdw

pi = 3.14159


def on_file_select_button_pressed():
    global file_window
    file_window = fdw.FileWindow("Sound files (*.wav, *.mp3)")
    file_window.file_dialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Sound Visualizer")
    app.setStyleSheet("QWidget { background-color: black; color: white; } ")
    window = QWidget()
    layout = QHBoxLayout(window)
    settings_layout = QVBoxLayout()
    graph_layout = QVBoxLayout()
    label1 = QLabel("Sin Wave")
    graph_layout.addWidget(label1)
    x = np.arange(0, 8*pi, .01)
    y = np.sin(1*x)
    z = 3*x
    figure1 = gw.GraphWidget(x, y)
    graph_layout.addWidget(figure1)
    label2 = QLabel("Line")
    graph_layout.addWidget(label2)
    figure2 = gw.GraphWidget(x, z)
    graph_layout.addWidget(figure2)
    file_select_button = QPushButton()
    file_select_button.setText("Browse...")
    file_select_button.clicked.connect(on_file_select_button_pressed)
    settings_layout.addWidget(file_select_button)
    graph_frame = QFrame()
    graph_frame.setLayout(graph_layout)
    settings_frame = QFrame()
    settings_frame.setLayout(settings_layout)
    layout.addWidget(settings_frame)
    layout.addWidget(graph_frame)
    window.show()
    app.exec()
