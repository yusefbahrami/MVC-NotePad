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

        self.menu = self.menuBar()

        self.saveToolStripMenuItem = QAction("Save", self)
        self.saveToolStripMenuItem.setShortcut(QKeySequence("ctrl+s"))
        self.saveToolStripMenuItem.triggered.connect(
            self.onMyToolBarButtonClick)

        self.fileToolStripMenu = self.menu.addMenu("&File")
        self.fileToolStripMenu.addAction(self.saveToolStripMenuItem)
        # self.fileToolStripMenu.triggered.connect(self.onMyToolBarButtonClick)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.widget = CentralWidget()
        self.setCentralWidget(self.widget)

    # test
    def saveMenu(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Image files (*.jpg *.gif)")
        print(fname)

    # test function
    def onMyToolBarButtonClick(self):
        print(self.widget.txtDisplay.toPlainText())
        self.speakObject.setText(self.widget.txtDisplay.toPlainText())
        self.speakObject.start()
        # self.speakObject.start()
        # self.speakObject.speaker.speak()
        # .toPlainText() -> is a method to access the text of the QTextEdit


# test
# app = QApplication([])
# win = MainWindow()
# win.show()
# app.exec()
