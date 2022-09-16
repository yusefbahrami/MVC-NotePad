from PyQt5.QtWidgets import QMainWindow, QAction, QStatusBar, QFileDialog
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QFont, QKeySequence
from CentralWidget import CentralWidget


class MainWindow(QMainWindow):
    def __init__(self, speakObject: QThread) -> None:
        super().__init__()
        self.setWindowTitle("Notepad")
        self.font = QFont("vazir", 8)
        self.setFont(self.font)
        self.setMinimumSize(300, 300)
        self.resize(600, 400)
        self.speakObject = speakObject
        self.toolStripMenu()

        # self.fileToolStripMenu.triggered.connect(self.onMyToolBarButtonClick)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.widget = CentralWidget()
        self.setCentralWidget(self.widget)

    def toolStripMenu(self):
        self.menu = self.menuBar()

        # File menu
        self.saveToolStripMenuItem = QAction("Save", self)
        self.saveToolStripMenuItem.setShortcut(QKeySequence("ctrl+s"))
        self.saveToolStripMenuItem.triggered.connect(
            self.saveMenu)

        self.fileToolStripMenu = self.menu.addMenu("&File")
        self.fileToolStripMenu.addAction(self.saveToolStripMenuItem)

        # Run menu
        self.speakToolStripMenuItem = QAction("Speak", self)
        self.speakToolStripMenuItem.setShortcut(QKeySequence("ctrl+alt+s"))
        self.speakToolStripMenuItem.triggered.connect(self.speakMethod)

        self.runToolStripMenu = self.menu.addMenu("&Run")
        self.runToolStripMenu.addAction(self.speakToolStripMenuItem)

    # test
    def saveMenu(self):
        fileTypes = "Text File (*.txt);; All File (*.*)"
        # name will be a tuple
        name = QFileDialog.getSaveFileName(self, "Save File", filter=fileTypes)
        text = self.widget.txtDisplay.toPlainText()
        try:
            with open(name[0], 'w') as file:
                file.write(text)
        except FileNotFoundError:
            pass

    def speakMethod(self):
        self.speakObject.setText(self.widget.txtDisplay.toPlainText())
        self.speakObject.start()
