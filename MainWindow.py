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
        self.fileName = None
        self.isSaved = False

        # self.fileToolStripMenu.triggered.connect(self.onMyToolBarButtonClick)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.widget = CentralWidget()
        self.setCentralWidget(self.widget)

        self.widget.txtDisplay.textChanged.connect(self.textChanged)

    def toolStripMenu(self):
        self.menu = self.menuBar()

        # File menu
        self.newToolStripMenuItem = QAction("New", self)
        self.newToolStripMenuItem.setShortcut(QKeySequence("ctrl+n"))
        self.newToolStripMenuItem.triggered.connect(self.newDocument)

        self.saveToolStripMenuItem = QAction("Save", self)
        self.saveToolStripMenuItem.setShortcut(QKeySequence("ctrl+s"))
        self.saveToolStripMenuItem.triggered.connect(
            self.isFirstSave)

        self.openToolStripMenuItem = QAction("Open", self)
        self.openToolStripMenuItem.setShortcut(QKeySequence("ctrl+o"))
        self.openToolStripMenuItem.triggered.connect(
            self.openMenu)

        self.fileToolStripMenu = self.menu.addMenu("&File")
        self.fileToolStripMenu.addAction(self.newToolStripMenuItem)
        self.fileToolStripMenu.addAction(self.saveToolStripMenuItem)
        self.fileToolStripMenu.addAction(self.openToolStripMenuItem)

        # Run menu
        self.speakToolStripMenuItem = QAction("Speak", self)
        self.speakToolStripMenuItem.setShortcut(QKeySequence("ctrl+alt+s"))
        self.speakToolStripMenuItem.triggered.connect(self.speakMethod)

        self.runToolStripMenu = self.menu.addMenu("&Run")
        self.runToolStripMenu.addAction(self.speakToolStripMenuItem)

    def textChanged(self):
        self.isSaved = False

    def newDocument(self):
        print("in new")

    # save region
    def handleSaveFile(self):
        try:
            with open(self.fileName[0], 'w') as file:
                file.write(self.widget.txtDisplay.toPlainText())
            self.isSaved = True
        except FileNotFoundError:
            pass

    def isFirstSave(self):
        if self.fileName and self.fileName[0] != '':
            self.handleSaveFile()
        else:
            self.saveMenu()

    def saveMenu(self):
        # self.fileName will be a tuple
        self.fileName = QFileDialog.getSaveFileName(
            self, "Save File", filter=self.fileTypes)
        self.handleSaveFile()
    # end save region

    def openMenu(self):
        self.fileName = QFileDialog.getOpenFileName(
            self, "Open File", filter=self.fileTypes)
        try:
            with open(self.fileName[0], 'r') as file:
                text = tuple(file.readlines())
                for line in text:
                    self.widget.txtDisplay.setText(
                        f"{self.widget.txtDisplay.toPlainText()}{line.strip()}\n")
            self.isSaved = True
        except FileNotFoundError:
            pass

    def speakMethod(self):
        self.speakObject.setText(self.widget.txtDisplay.toPlainText())
        self.speakObject.start()
