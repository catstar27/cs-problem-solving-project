from PyQt6.QtWidgets import *


class FileSelectFrame(QFrame):
    """
    Contains a text edit for a path to the sound file, a browse button to open the file dialog,
    and the file dialog itself. Intended to make it easy to integrate to the main GUI
    """
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()

        # Filepath label setup
        self.file_path_label = QTextEdit("Path to File")
        self.file_path_label.setMaximumHeight(50)
        self.layout.addWidget(self.file_path_label)

        # Browse button setup
        self.file_select_button = QPushButton()
        self.file_select_button.setText("Browse...")
        self.file_select_button.clicked.connect(self.on_file_select_button_pressed)
        self.layout.addWidget(self.file_select_button)

        # File dialog setup
        self.file_dialog = QFileDialog()
        self.filter = "Sound files (*.mp3 *.wav)"

        self.setLayout(self.layout)

    def on_file_select_button_pressed(self):
        # Opens the dialog window and sets the text edit label to the filepath
        self.file_path_label.setText(self.file_dialog.getOpenFileName(self, "Open File", "", self.filter)[0])
