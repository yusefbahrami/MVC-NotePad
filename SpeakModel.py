from PyQt5.QtCore import QThread, pyqtSignal
from pyttsx3 import init


class Speak:
    def __init__(self, text) -> None:
        self.text = str(text)

    def speak(self):
        engine = init()
        engine.setProperty('rate', 150)
        engine.say(self.text)
        engine.runAndWait()


class SpeakCore(QThread):
    sound = pyqtSignal("PyQt_PyObject")

    def run(self) -> None:
        self.speaker = Speak(self.text)
        self.sound.emit(self.speaker.speak())

    def setText(self, text=""):
        self.text = text


speakObject = SpeakCore()
