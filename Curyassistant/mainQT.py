import os
import random
import threading
import time

from PIL import Image
from PySide6 import QtCore, QtWidgets, QtGui, QtWebEngineWidgets
import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel
from CHOICEassistance.Curie.Curyassistant.speaker import Curie
import multiprocessing as mc

from CHOICEassistance.Curie.Curyassistant.speaker.Curie import speak

global PRList
PRList = [None, None, None, None]

class MyWidget(QtWidgets.QWidget):
    def Values(self):
        return os.getcwd() + '/speaker/files/'

    def Runner(self):
        while True:
            try:
                time.sleep(1)
                with open(f'{self.Values()}2Key.txt', 'r') as f:
                    olm = f.read()
                if olm == '011': self.textForListen.setText('Listening...')
                if olm == '001': self.textForListen.setText("")

            except Exception as e:
                print(e)

    def __init__(self):
        super().__init__()

        self.path = os.getcwd() + '/speaker/files/'
        img = Image.open(f'{self.path}icon.ico'); img.resize((45, 45))

        self.label = QLabel('Image', self)

        pixmap = QPixmap(f'{self.path}Curie0.1.png')
        pixmap4 = pixmap.scaledToHeight(260); pixmap.scaledToWidth(100)
        self.label.setPixmap(pixmap4); self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.button = QtWidgets.QPushButton("Stop assistant")
        self.button.clicked.connect(self.magic)

        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)
        self.text.setStyleSheet(""" font-size: 20px; """)

        self.textForListen = QtWidgets.QLabel("")
        self.setStyleSheet(""" font-size: 10px; margin:10, 45, 10, 10; """)

        # for add layout elements properly
        self.layout = QtWidgets.QVBoxLayout(self)
        for elem in [self.label, self.text, self.button, self.textForListen]:
            self.layout.addWidget(elem)

        self.pr = threading.Thread(target=self.Runner); self.pr.start()

    @QtCore.Slot()
    def magic(self):
        if self.button.text() == "Run Assistant":
            SpeakerRunner();
            self.button.setText("Stop Assistant"); self.text.setText("Assitant is on")
        else:
            self.text.setText("Please Wait!")
            # for checking what will attend second flow
            if PRList[1].is_alive():
                PRList[1].kill(); mc.Process(target=speak, args=("Bye Bye Boss", )).start()  # to stop in loop
                self.text.setText("Assitant is off"); self.button.setText("Run Assistant")

    def __call__(self):
        return "Alma"

def SpeakerRunner():
    killer = mc.Event()
    conn1, conn2 = mc.Pipe()
    thread = mc.Process(target=Curie.main, args=(conn1, killer)); thread.start()
    PRList[0] = killer; PRList[1] = thread; PRList[3] = conn2

def MainWidgetStyle(main):
    # for set the relative style
    main.setStyleSheet(
        """
            background-color: #262626;
            color: #FFFFFF;
            font-family: Montserrat;
            font-size: 12px;
        """
    )

def main(*args, **kwargs):
    print(os.getcwd())
    app = QtWidgets.QApplication([])
    widget = MyWidget(); MainWidgetStyle(widget)

    widget.resize(350, 500)
    widget.setWindowTitle("Choice")
    widget.move(600, 150)

    widget.setWindowIcon(QtGui.QIcon(f'{MyWidget().path}icon.ico'))
    widget.show()

    SpeakerRunner()   # speaker thread function
    sys.exit((app.exec(), PRList[1].kill(), print("yes")))

if __name__ == "__main__":
    main()


