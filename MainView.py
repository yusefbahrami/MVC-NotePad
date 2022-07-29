from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QWidget, QGridLayout, QToolBar, QAction, QStatusBar
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Notepad")
        self.font = QFont("vazir", 8)
        self.setFont(self.font)
        self.setMinimumSize(300, 300)

        self.toolbar = QToolBar("main toolbar")
        self.addToolBar(self.toolbar)

        self.fileStripMenuItem = QAction("File", self)
        self.fileStripMenuItem.setToolTip("File Strip Menu Item")
        self.fileStripMenuItem.triggered.connect(self.onMyToolBarButtonClick)
        self.toolbar.addAction(self.fileStripMenuItem)

        self.editStripMenuItem = QAction("Edit", self)
        self.editStripMenuItem.setToolTip("Edit Strip Menu Item")
        self.editStripMenuItem.triggered.connect(self.onMyToolBarButtonClick)
        self.toolbar.addAction(self.editStripMenuItem)

        self.viewStripMenuItem = QAction("View", self)
        self.viewStripMenuItem.setToolTip("View Strip Menu Item")
        self.viewStripMenuItem.triggered.connect(self.onMyToolBarButtonClick)
        self.toolbar.addAction(self.viewStripMenuItem)

        self.helpStripMenuItem = QAction("Help", self)
        self.helpStripMenuItem.setToolTip("Help Strip Menu Item")
        self.helpStripMenuItem.triggered.connect(self.onMyToolBarButtonClick)
        self.toolbar.addAction(self.helpStripMenuItem)

        self.widget = CentralWidget()
        self.setCentralWidget(self.widget)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def onMyToolBarButtonClick(self):

        print(self.widget.txtDisplay.toPlainText())
        # .toPlainText() -> is a method to access the text of the QTextEdit


class CentralWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.font = QFont("vazir", 12)

        layout = QGridLayout()
        self.setLayout(layout)

        self.txtDisplay = QTextEdit()
        self.txtDisplay.setFont(self.font)
        layout.addWidget(self.txtDisplay, 0, 0)


# test
app = QApplication([])
win = MainWindow()
win.show()
app.exec()
