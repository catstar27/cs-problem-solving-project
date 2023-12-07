import sys
from PyQt6.QtWidgets import *
import waveform_model as wm
import file_select_frame as fsf
import file_load_frame as flf
import graph_widget as gw
import rt_alternate_buttons as rtab
import atexit
import os

pi = 3.14159
# making use of color palette from here: https://colorhunt.co/palette/363062435585818fb4f5e8c7


def file_loaded():  # updates the label of audio duration after the file is loaded
    length_message.setText(f"The audio duration is {file_load_frame.file.duration} seconds")
    waveform.plot_waveform()


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
    window.setMinimumSize(1064, 520)
    layout = QHBoxLayout(window)
    settings_layout = QVBoxLayout()
    graph_layout = QVBoxLayout()

    # graphs setup
    waveform = wm.WaveformModel()
    graph_layout.addWidget(waveform)
    rt_graph = gw.GraphWidget("Reverb")
    graph_layout.addWidget(rt_graph)

    # graph alternate buttons setup
    rt_buttons = rtab.AlternateButtonsFrame()
    graph_layout.addWidget(rt_buttons)

    # file select setup
    file_select_label = QLabel("Select a sound file to analyze:")
    file_select_label.setMaximumHeight(20)
    settings_layout.addWidget(file_select_label)
    file_select_frame = fsf.FileSelectFrame()
    settings_layout.addWidget(file_select_frame)

    # file load setup
    file_load_frame = flf.FileLoadFrame()
    file_load_frame.filepath = file_select_frame.file_path_label.toPlainText()
    file_select_frame.file_path_label.textChanged.connect(filepath_changed)
    file_load_frame.load_signal.connect(file_loaded)
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
    print(window.size())
    app.exec()
