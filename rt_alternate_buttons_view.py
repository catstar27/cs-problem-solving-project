from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class AlternateButtonsFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.prev_button = QPushButton("<< Prev")
        self.layout.addWidget(self.prev_button)

        self.graph_label = QLabel("Current Graph: N/A")
        self.graph_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.graph_label)

        self.next_button = QPushButton("Next >>")
        self.layout.addWidget(self.next_button)

    def update_graph_label(self, f):
        self.graph_label.setText(f"Current Graph: {f}")
