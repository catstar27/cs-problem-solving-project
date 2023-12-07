from PyQt6.QtWidgets import *


class AlternateButtonsFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        low_button = QPushButton("Low")
        self.layout.addWidget(low_button)

        mid_button = QPushButton("Mid")
        self.layout.addWidget(mid_button)

        high_button = QPushButton("High")
        self.layout.addWidget(high_button)

        all_button = QPushButton("All")
        self.layout.addWidget(all_button)
