from PyQt6.QtWidgets import *


class FileSelectFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()

        self.file_path_label = QTextEdit("Path to File")
        self.file_path_label.setMaximumHeight(50)
        self.layout.addWidget(self.file_path_label)

        self.file_select_button = QPushButton()
        self.file_select_button.setText("Browse...")
        self.file_select_button.clicked.connect(self.on_file_select_button_pressed)
        self.layout.addWidget(self.file_select_button)

        self.file_dialog = QFileDialog()
        self.file_dialog.setNameFilter("Sound files (*.mp3 *.wav)")

        self.setLayout(self.layout)

    def on_file_select_button_pressed(self):
        self.file_path_label.setText(self.file_dialog.getOpenFileName()[0])
