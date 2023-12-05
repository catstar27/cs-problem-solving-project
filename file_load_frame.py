from PyQt6.QtWidgets import *
import wave_model as wav


class FileLoadFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.filepath = ""
        self.file = ""

        # file load button
        self.file_load_button = QPushButton("Load File")
        self.file_load_button.clicked.connect(self.load_file)
        self.layout.addWidget(self.file_load_button)

        # status message
        self.status_message = QLabel()
        self.layout.addWidget(self.status_message)

        # file length message
        self.length_message = QLabel("No file is loaded.")
        self.layout.addWidget(self.length_message)

    def update_filepath(self, filepath):
        self.filepath = filepath

    def load_file(self):
        self.file = wav.WaveModel(self.filepath)
        load_file_data = self.file.load_file()
        if load_file_data[1]:
            color = 'green'
            self.length_message.setText(f"The audio duration is {self.file.duration} seconds")
        else:
            color = 'red'
        self.status_message.setText(f"<font color={color}>"+load_file_data[0]+f"<font color={color}>")
