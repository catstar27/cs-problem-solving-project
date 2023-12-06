import sys
import numpy as np
from PyQt6.QtWidgets import *
import graph_widget as gw
import file_select_frame as fsf
import file_load_frame as flf
import atexit
import os

pi = 3.14159
# making use of color palette from here: https://colorhunt.co/palette/363062435585818fb4f5e8c7


def update_file_duration():  # updates the label of audio duration after the file is loaded
    length_message.setText(f"The audio duration is {file_load_frame.file.duration} seconds")


def filepath_changed():  # updates file load frame filepath to the filepath in file select frame
    file_load_frame.filepath = file_select_frame.file_path_label.toPlainText()


def exit_handler():  # runs on exit, deleting the temporary wav file
    if os.path.exists("file.wav"):
        os.remove("file.wav")


if __name__ == "__main__":
    # app preparation
    atexit.register(exit_handler)
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
    figure1 = gw.GraphWidget()
    figure1.new_plot(x, y)
    graph_layout.addWidget(figure1)

    # file select setup
    file_select_label = QLabel("Select a sound file to analyze:")
    settings_layout.addWidget(file_select_label)
    file_select_frame = fsf.FileSelectFrame()
    settings_layout.addWidget(file_select_frame)

    # file load setup
    file_load_frame = flf.FileLoadFrame()
    file_load_frame.filepath = file_select_frame.file_path_label.toPlainText()
    file_select_frame.file_path_label.textChanged.connect(filepath_changed)
    file_load_frame.load_signal.connect(update_file_duration)
    settings_layout.addWidget(file_load_frame)

    # file length message
    length_message = QLabel()
    settings_layout.addWidget(length_message)

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
