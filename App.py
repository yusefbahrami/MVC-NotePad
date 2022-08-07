from PyQt5.QtWidgets import QApplication
# from MainModel import speak
from SpeakModel import Speak, SpeakCore, speakObject
from MainWindow import MainWindow

app = QApplication([])

window = MainWindow(speakObject)
window.show()
app.exec()
