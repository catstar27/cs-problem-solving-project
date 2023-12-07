import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import waveform_model as wm
import file_select_frame as fsf
import file_load_frame_view as flf
import reverbform_model as rm
import graph_model as gm
import rt_alternate_buttons_view as rtab
import atexit
import os

pi = 3.14159
frequencies = ["Low", "Mid", "High", "All"]
# making use of color palette from here: https://colorhunt.co/palette/363062435585818fb4f5e8c7


def set_rt_graph(num):
    global current_graph_index, loaded
    if loaded:
        current_graph_index += num
        current_graph_index %= 4
        if frequencies[current_graph_index] != "All":
            rt_graph.plot_waveform(frequencies[current_graph_index])
        else:
            rt_graph.plot_all()
        rt_buttons.update_graph_label(frequencies[current_graph_index])


def update_rt_display():
    rt_display.setText(f"RT60 Value: {round(abs(rt_graph.rt60), 2)} seconds")


def update_max_freq_display():
    max_freq_display.setText(f"Max Frequency: {round(rt_graph.value_of_max, 2)} Hz")


def file_loaded():  # updates the label of audio duration after the file is loaded
    global current_graph_index, loaded, spectrogram
    length_message.setText(f"Audio Duration: {file_load_frame.file.duration} seconds")
    waveform.plot_waveform()
    rt_graph.plot_waveform(frequencies[current_graph_index])
    rt_buttons.update_graph_label(frequencies[current_graph_index])
    loaded = True


def filepath_changed():  # updates file load frame filepath to the filepath in file select frame
    file_load_frame.filepath = file_select_frame.file_path_label.toPlainText()


def exit_handler():  # runs on exit, deleting the temporary wav file
    if os.path.exists("file.wav"):
        os.remove("file.wav")


if __name__ == "__main__":
    # app preparation
    loaded = False
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
    rt_graph = rm.ReverbFormModel()
    rt_graph.rt60_changed.connect(update_rt_display)
    rt_graph.max_freq_changed.connect(update_max_freq_display)
    graph_layout.addWidget(rt_graph)
    spectrogram = gm.GraphWidget("Spectrogram")

    # graph alternate buttons setup
    rt_buttons = rtab.AlternateButtonsFrame()
    rt_buttons.next_button.clicked.connect(lambda: set_rt_graph(1))
    rt_buttons.prev_button.clicked.connect(lambda: set_rt_graph(-1))
    graph_layout.addWidget(rt_buttons)
    current_graph_index = 0

    # file select setup
    file_select_label = QLabel("Select a sound file to analyze:")
    file_select_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
    file_select_label.setMaximumHeight(20)
    settings_layout.addWidget(file_select_label)
    file_select_frame = fsf.FileSelectFrame()
    file_select_frame.setMaximumWidth(500)
    settings_layout.addWidget(file_select_frame)

    # file length message
    length_message = QLabel("Audio Duration: ")
    settings_layout.addWidget(length_message)

    # graph rt display setup
    rt_display = QLabel("RT60 Value: ")
    settings_layout.addWidget(rt_display)

    # max freq display setup
    max_freq_display = QLabel("Maximum Frequency: ")
    settings_layout.addWidget(max_freq_display)

    # file load setup
    file_load_frame = flf.FileLoadFrame()
    file_load_frame.filepath = file_select_frame.file_path_label.toPlainText()
    file_select_frame.file_path_label.textChanged.connect(filepath_changed)
    file_load_frame.load_signal.connect(file_loaded)
    settings_layout.addWidget(file_load_frame)

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
