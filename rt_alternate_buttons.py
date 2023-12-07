from PyQt6.QtWidgets import *


class AlternateButtonsFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.prev_button = QPushButton("<< Prev")
        self.layout.addWidget(self.prev_button)

        self.next_button = QPushButton("Next >>")
        self.layout.addWidget(self.next_button)
