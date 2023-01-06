import ast
import os

import vosk
import sys
import sounddevice as sd
import queue

from CHOICEassistance.Curyassistant.speaker.modules.Speaker import Speaker


class Recognizer:
    def __init__(self):
        path = os.getcwd() + "\models\model\\vosk-model-en-us-0.22-lgraph\\vosk-model-en-us-0.22-lgraph"; print(path)
        self.model = vosk.Model(path)
        self.sample_rate = 16000
        self.device = 1
        self.q = queue.Queue()
        self.Explorer()

    def callback(self, intdata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(intdata))

    def Explorer(self):
        with sd.RawInputStream(samplerate=self.sample_rate, blocksize=8000, device=self.device, dtype='int16',
                               channels=1, callback=self.callback):
            rec = vosk.KaldiRecognizer(self.model, self.sample_rate)
            while True:
                data = self.q.get()
                if rec.AcceptWaveform(data):
                    obj = rec.Result(); elem = ast.literal_eval(obj); print(elem)
                    if elem['text']:
                        return elem['text'].replace('the', '', 1)

# Recognizer()