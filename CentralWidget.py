from PyQt5.QtWidgets import QGridLayout, QTextEdit, QWidget, QGridLayout
from PyQt5.QtGui import QFont


class CentralWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.font = QFont("vazir", 12)

        layout = QGridLayout()
        self.setLayout(layout)

        self.txtDisplay = QTextEdit()
        self.txtDisplay.setFont(self.font)
        layout.addWidget(self.txtDisplay, 0, 0)
