from cgitb import text
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

        # using in file dialogs
        self.fileTypes = "Text File (*.txt);; All File (*.*)"

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

        self.openToolStripMenuItem = QAction("Open", self)
        self.openToolStripMenuItem.setShortcut(QKeySequence("ctrl+o"))
        self.openToolStripMenuItem.triggered.connect(
            self.openMenu)

        self.fileToolStripMenu = self.menu.addMenu("&File")
        self.fileToolStripMenu.addAction(self.saveToolStripMenuItem)
        self.fileToolStripMenu.addAction(self.openToolStripMenuItem)

        # Run menu
        self.speakToolStripMenuItem = QAction("Speak", self)
        self.speakToolStripMenuItem.setShortcut(QKeySequence("ctrl+alt+s"))
        self.speakToolStripMenuItem.triggered.connect(self.speakMethod)

        self.runToolStripMenu = self.menu.addMenu("&Run")
        self.runToolStripMenu.addAction(self.speakToolStripMenuItem)

    # test
    def saveMenu(self):
        # name will be a tuple
        fileName = QFileDialog.getSaveFileName(
            self, "Save File", filter=self.fileTypes)
        text = self.widget.txtDisplay.toPlainText()
        try:
            with open(fileName[0], 'w') as file:
                file.write(text)
        except FileNotFoundError:
            pass

    def openMenu(self):
        # print('in open menu')
        fileName = QFileDialog.getOpenFileName(
            self, "Open File", filter=self.fileTypes)

        try:
            with open(fileName[0], 'r') as file:
                text = tuple(file.readlines())
                for line in text:
                    self.widget.txtDisplay.setText(
                        f"{self.widget.txtDisplay.toPlainText()}{line.strip()}\n")
        except FileNotFoundError:
            pass

    def speakMethod(self):
        self.speakObject.setText(self.widget.txtDisplay.toPlainText())
        self.speakObject.start()
