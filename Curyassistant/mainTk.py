import threading
import time
import speech_recognition as sr

from CHOICEassistance.Curie.Curyassistant.tools.methods.methods import OpenOf
from speaker import Curie
import multiprocessing as mc
import customtkinter
import os
from PIL import Image
import tkinter as tk

global PRList; global List


PRList = [None, None]
List = {'appObj': None}

def SpeakerRunner():
    killer = mc.Event()
    thread = mc.Process(target=Curie.main, args=(killer, )); thread.start()
    PRList[0] = killer; PRList[1] = thread

class App(customtkinter.CTk):

    def OpenLink(self, tg=False, wh=False):
        if tg: OpenOf("https://t.me/DaieVbot")
        if wh: OpenOf("https://wa.me/+77477427022")

    def Killer(self):
        if PRList[1].is_alive():
            # speak("By By I will see you later")
            PRList[0].set()
            self.sidebar_button_1.configure(text='Run Assistant')
        else:
            self.sidebar_button_1.configure(text='Stop Assistant')
            SpeakerRunner()

    def PutOff(self):
        self.ListeningText.configure(text='Analizing >>>')

    def PutOn(self):
        self.ListeningText.configure(text='Listening <<<')

    def __init__(self):
        super().__init__()

        self.mainImgPath = f"{os.getcwd()}/speaker/files/"

        self.title("Choice")
        self.geometry("300x500")
        self.eval('tk::PlaceWindow . center')
        self.iconbitmap(f'{self.mainImgPath}/icon.ico')
        self.Main()

    def Frames(self):
        # TODO: Main Frame Ok
        self.home_frame = customtkinter\
            .CTkFrame(self, height=1000, width=1000, border_color='white', corner_radius=45, fg_color="transparent")

    def Texts(self):  # Just mere texts
        self.ListeningText = customtkinter\
            .CTkLabel(self.home_frame, text='Listening <<<', text_color='white',
                      font=customtkinter.CTkFont(size=15, weight="bold"))
        self.ListeningText.grid(row=0, column=0, padx=0, pady=(300, 0))

    def Images(self):  # All images releasing
        self.LogoType = customtkinter.CTkImage(Image.open(self.mainImgPath + "/Curie0.1.png"), size=(200, 200))
        self.LogoTypeWh = customtkinter.CTkImage(Image.open(self.mainImgPath + "/iconWh.png"), size=(10, 10))
        self.LogoTypeTg = customtkinter.CTkImage(Image.open(self.mainImgPath + "/image.ss.png"), size=(10, 10))

    def ImageLables(self):  # Main Image Label to set
        self.LogoTypeLabel = customtkinter.CTkLabel(self.home_frame, text="", image=self.LogoType)
        self.LogoTypeLabel.grid(row=0, column=0, padx=0, pady=100)

    def ImgButtons(self):  # Main Icon buttons
        self.WhButton = customtkinter.CTkButton(self.home_frame, width=25, height=25, image=self.LogoTypeWh, text='',
                                                command=lambda: self.OpenLink(tg=False, wh=True))
        self.TgButton = customtkinter.CTkButton(self.home_frame, width=25, height=25, image=self.LogoTypeTg, text='',
                                                command=lambda: self.OpenLink(tg=True, wh=False))

        # and putting them
        self.WhButton.grid(row=3, column=0, padx=(10, 120), pady=0)
        self.TgButton.grid(row=3, column=0, padx=(0, 45), pady=0)

    def TextButtons(self):  # Mian text button
        self.sidebar_button_1 = customtkinter.CTkButton(self.home_frame, text='Stop Assistant', command=self.Killer)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

    def Main(self):
        self.Frames(); self.Texts(); self.Images(); self.ImageLables(); self.ImgButtons(); self.TextButtons()
        # The last establishing a Frame
        self.home_frame.grid(row=0, column=0, sticky="nsew")
        self.home_frame.pack()

if __name__ == "__main__":
    app = App()
    SpeakerRunner()
    app.mainloop()
