import time
import tkinter as tk
import speech_recognition as sr
import multiprocessing as mc

class UpdateLabel(tk.Label):
  def __init__(self, *args, **kwargs):
    tk.Label.__init__(self, *args, **kwargs)
    self._count = ""

  def update_text(self):
    self.config(text=self._count)
    self._count = "" if self._count == "Listening" else "Listening"
    self.after(1000, self.update_text)

root = tk.Tk()
label = UpdateLabel(root)
label.pack()

def Runner():
  mc.Process(target=root.mainloop).start()
  while True:
    r = sr.Recognizer()
    label.update_text()
    with sr.Microphone() as sm:
      source = r.listen(sm, 7)
      print(f"elem: {source.sample_rate}")



Runner()





