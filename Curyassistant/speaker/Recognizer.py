import multiprocessing as mp
import os

import speech_recognition as sr

class _RecManaging(object):
    """
    realizing a listening options
    """

    def __init__(self):
        pass

    def Saver(self, one=False):
        with open(f'{os.getcwd()}/files/2Key.txt', 'w') as e:
            e.write('011' if one else '001')

    def Recognizer(self):
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print('Listening....'); mp.Process(target=self.Saver, args=(True, )).start()
                # r.pause_threshold = 1
                audio = r.listen(source, timeout=7)
                print('Recognizing...'); mp.Process(target=self.Saver, args=(False,)).start()
                query = r.recognize_google(audio); print(query)

                return query
        except Exception as e:
            mp.Process(target=self.Saver, args=(False,)).start()
            print(e)
            return self.Recognizer()


if __name__ == '__main__':
    # TODO: for checking the mic settings to be cautiously
    print(_RecManaging().__doc__)
    _RecManaging().Recognizer()