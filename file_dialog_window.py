from PyQt6.QtWidgets import *


class FileWindow:
    def __init__(self, file_filter):
        self.file_filter = file_filter
        self.file_dialog = QFileDialog()
        self.file_dialog.setNameFilter(self.file_filter)

