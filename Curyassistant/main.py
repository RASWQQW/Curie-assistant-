import os
import random
import threading
import time

from PIL import Image
from PySide6 import QtCore, QtWidgets, QtGui, QtWebEngineWidgets
import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel
from CHOICEassistance.Curyassistant.speaker import Curie

global PRList
PRList = [None, None]


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel('Image', self)
        img = Image.open('photo_2022-07-22_13-49-00.jpg')
        img.resize((45, 45))


        pixmap = QPixmap('photo_2022-07-22_13-49-00.jpg')
        pixmap4 = pixmap.scaledToHeight(260); pixmap.scaledToWidth(100)
        self.label.setPixmap(pixmap4)
        self.label.setAlignment(QtCore.Qt.AlignCenter)


        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Stop assistant")

        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)
        self.text.setStyleSheet("""
        font-size: 20px;
        """)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)
        self.bundle = [0, ]

    @QtCore.Slot()
    def magic(self):
        if self.button.text() == "Run Assistant":
            SpeakerRunner(); self.button.setText("Stop Assistant"); self.text.setText("Assitant is on")

        else:
            self.text.setText("Please Wait!")
            # for checking what will attend second flow
            try:
                PRList[0].set()  # to stop in loop
            except Exception: pass
            finally:
                threading.Thread(target=self.TextEnv).start()

    def TextEnv(self):
        while True:
            time.sleep(1)
            if not PRList[1].is_alive():
                self.text.setText("Assitant is off"); self.button.setText("Run Assistant")
                break

def SpeakerRunner():
    killer = threading.Event()
    thread = threading.Thread(target=Curie.main, args=(killer, )); thread.start()
    PRList[0] = killer; PRList[1] = thread

if __name__ == "__main__":
    print(os.getcwd())
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.setStyleSheet("""
        background-color: #262626;
        color: #FFFFFF;
        font-family: Montserrat;
        font-size: 12px;
        """)
    widget.resize(370, 500)
    widget.setWindowTitle("Choice")
    widget.move(600, 150)

    widget.setWindowIcon(QtGui.QIcon('photo_2022-07-22_13-49-00.jpg'))
    widget.show()

    SpeakerRunner()  # speaker thread function
    sys.exit(app.exec())
