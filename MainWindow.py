from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QWidget, QGridLayout, QToolBar, QAction, QStatusBar
from PyQt5.QtGui import QFont, QIcon
from CentralWidget import CentralWidget


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

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.widget = CentralWidget()
        self.setCentralWidget(self.widget)

    # test function
    def onMyToolBarButtonClick(self):

        print(self.widget.txtDisplay.toPlainText())
        # .toPlainText() -> is a method to access the text of the QTextEdit


# test
app = QApplication([])
win = MainWindow()
win.show()
app.exec()
