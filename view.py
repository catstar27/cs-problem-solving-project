import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import waveform_model as wm
import spectrogram_model as sm
import reverbform_model as rm
import file_select_frame as fsf
import file_load_frame_view as flf
import rt_alternate_buttons_view as rtab


class View(QApplication):
    """
    Loads and contains the GUI of the program
    """
    def __init__(self):
        super().__init__(sys.argv)
        self.setApplicationName("Sound Visualizer")
        self.setStyleSheet("QWidget { background-color: rgb(54, 48, 98); color: rgb(245, 232, 199); } ")
        self.current_rt_graph_index = 0
        self.is_file_loaded = False

        # window and layout setup
        self.window = QWidget()
        self.window.setMinimumSize(1064, 520)
        self.layout = QHBoxLayout(self.window)
        self.settings_layout = QVBoxLayout()
        self.graph_layout = QVBoxLayout()

        # graphs setup
        self.spectrogram = sm.SpectrogramModel()
        self.spectrogram.setMinimumSize(640, 200)
        self.graph_layout.addWidget(self.spectrogram)
        self.waveform = wm.WaveformModel()
        self.graph_layout.addWidget(self.waveform)
        self.rt_graph = rm.ReverbFormModel()
        self.graph_layout.addWidget(self.rt_graph)

        # graph alternate buttons setup
        self.rt_buttons = rtab.AlternateButtonsFrame()
        self.graph_layout.addWidget(self.rt_buttons)

        # file select setup
        self.file_select_label = QLabel("Select a sound file to analyze:")
        self.file_select_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.file_select_label.setMaximumHeight(20)
        self.settings_layout.addWidget(self.file_select_label)
        self.file_select_frame = fsf.FileSelectFrame()
        self.file_select_frame.setMaximumWidth(500)
        self.settings_layout.addWidget(self.file_select_frame)

        # file length message
        self.length_message = QLabel("Audio Duration: ")
        self.settings_layout.addWidget(self.length_message)

        # graph rt display setup
        self.rt_display = QLabel("RT60 Value: ")
        self.settings_layout.addWidget(self.rt_display)

        # max freq display setup
        self.max_freq_display = QLabel("Maximum Frequency: ")
        self.settings_layout.addWidget(self.max_freq_display)

        # spectrogram show/hide button
        self.spectrogram_display_button = QCheckBox("Enable Spectrogram")
        self.spectrogram_display_button.setChecked(True)
        self.settings_layout.addWidget(self.spectrogram_display_button)

        # file load setup
        self.file_load_frame = flf.FileLoadFrame()
        self.file_load_frame.filepath = self.file_select_frame.file_path_label.toPlainText()
        self.settings_layout.addWidget(self.file_load_frame)

        # frames setup
        self.graph_frame = QFrame()
        self.graph_frame.setLayout(self.graph_layout)
        self.settings_frame = QFrame()
        self.settings_frame.setLayout(self.settings_layout)
        self.layout.addWidget(self.settings_frame)
        self.layout.addWidget(self.graph_frame)
