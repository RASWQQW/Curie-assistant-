import os
import webbrowser
from typing import Optional

import pyttsx3
import wikipedia
from pyqiwip2p.AioQiwip2p import requests

from CHOICEassistance.Curie.Curyassistant.speaker.config import paths
from choice.bot.search.googleser import Googlesearch

import speech_recognition as sr
import threading
import subprocess
from CHOICEassistance.Curie.Curyassistant.managment.Book import Finder
import CHOICEassistance.Curie.Curyassistant.main as moss
import multiprocessing as mp
from googletrans import Translator
from choice.bot.nlp.words import vectorize_func
from functools import cache

global DictRes; global DictBook; global Dict; Dict = {'next': ''}

@cache
def DictSet(Res: bool = False, Book: bool = False) -> bool:
    if Res:
        global DictRes; Dict['next'] = 'Wiki'
        DictRes = {'list': [], 'count': 1, 'flow': None, 'DictList': [
            {'title': None, 'sum': None}, ]}
        print(DictRes, Dict); return True

    if Book:
        global DictBook; Dict['next'] = 'Books'
        DictBook = {'source': [], 'iterator': []}
        print(DictBook, Dict); return True

    return False


# def speak(text):
#     from CHOICEassistance.Curyassistant.speaker.modules.Speaker import Speaker
#     Speaker(text)

# def Recognizer():
#     from CHOICEassistance.Curyassistant.speaker.modules.Recognizer import Recognizer
#     # print("Recognizing___")
#     # print("Recognizing___")
#     return Recognizer()

wikipedia.set_lang('en')

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 190)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()

@cache
def Recognizer():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening....')
            # r.pause_threshold = 1
            audio = r.listen(source, timeout=7); print('Recognizing...')
            query = r.recognize_google(audio); print(query)
            return query
    except Exception:
        # speak("Sorry I can get it")
        return ''

def FullManagement():
    query = Recognizer()

    if 'shut down laptop' in query.lower() or ('restart' in query.lower() and 'laptop' in query.lower() and
                                abs(query.lower().index("laptop") - query.lower().index("restart"))):

        speak('Are you sure that')
        while True:
            guessed = Recognizer()
            if guessed.lower() == 'yes':
                if 'shut down' in query.lower(): (speak("Ok I am going to shut down the PC"),
                    os.system("shutdown /s /t 1"))
                elif 'restart' in query.lower(): (speak("Ok I am going to shut down the PC"),
                    os.system("shutdown -t 0 -r -f"))
                break

    if 'exit' in query or 'stop' in query:
        speak("Ok ok we will restart")
        os.startfile(paths['google'])

    else:
        if 'pope' in query.lower():
            subprocess.run(paths['pycharm'], check=True, shell=True)

        elif 'telegram' in query.lower():
            os.startfile(paths['telegram'])
            speak("Ok the work is gone so Telegram is starts")

        elif 'book' in query.lower():
            source = query.split(); global BookName, Author
            for i in range(len(source)):
                try:
                    if source[i] in ['name', 'named', 'as', 'book']:
                        BookName = source[i + 1] + " " + source[i + 2] if source[i + 2] else ''

                    if source[i] in ['by', 'writer', 'author']:
                        Author = source[i + 1] + " " + source[i + 2] if source[i + 2] else ''
                except Exception as e: speak('You miss some words, please try to next time')

            def BookManager(BookName, Author):
                try:
                    print("List:", BookName, Author)
                    slim = Finder(authorName=str(Author), BookName=str(BookName))
                    speak(f"I ve found {len(slim)} books if you wanna catch call me there I always ready")
                    speak(f"They are {[text['title'] for text in slim]}")

                    DictSet(Book=True)
                    DictBook['iterator'] = iter(slim); DictBook['source'] = next(DictBook['iterator'])
                    speak("First one is " + DictBook['source']['title'])
                    Looper()
                except Exception:
                    speak("Something went wrong Do you wanna repeat request")
                    @LooperGain
                    def Waiter(recognisedText: Optional[str]):
                        if 'yeas' in recognisedText or 'yeah' in recognisedText:
                            BookManager(BookName, Author)
                        elif 'no' in recognisedText or 'stop' in recognisedText:
                            return False

            speak("ok I start to find it")
            BookManager(BookName, Author)

        elif 'switch' in query.lower():
            print("OK")
            FlowBroker()

        elif 'next' in query.lower() and Dict['next']:
            if Dict['next'] == 'Wiki':
                print("Ok"); print(DictRes); print(DictRes['list'] != '')

                FlowBroker()

                if DictRes['list'] and len(DictRes['DictList']) > DictRes['count']:
                    speak("Next is..." + str(DictRes['DictList'][DictRes['count']]['title']))
                    # text = str(next(DictRes['list'])); Process(text)
                    text = str(DictRes['DictList'][DictRes['count']]['sum']); Process(Spsourse, text)
                    DictRes['count'] += 1; print("Is came", DictRes['count'])
                else:
                    speak("The List is emtpy. Please you shall begin with new question there")
                    DictSet(Res=True)
        else:

            if Dict['next'] not in ['Book']:
                DictSet(Res=True)
                if query and DictRes['flow'] is None:
                    # query = 'Wiki Osaka'
                    listFORC = query.lower().split(); print(listFORC)
                    source = [(True, i) if listFORC[i] in ['search', 'wiki', 'about', 'tell'] else (False, -1)
                              for i in range(len(listFORC))]
                    print(source)

                    for tupleElement in source:
                        if tupleElement[0]:
                            number = tupleElement[1]  # element index
                            try:
                                if listFORC[number + 1]:
                                    oss = IterForWiki(str(listFORC[number + 1])); DictRes['list'] = oss
                                    text = str(DictRes['DictList'][0]['sum']); Process(Spsourse, text)
                                    print('Res', DictRes, "Len", len(list(DictRes['list'])))
                                break
                            except Exception as e: print(repr(e)); continue
                    else:
                        topic = vectorize_func(str(query))
                        if topic != 0:
                            respond = str(Translator().translate(topic['send_message'], dest='en').text)
                            print("replaying:", respond); speak(respond)
                        else:
                            speak("I can't get it")

def LooperGain(method):
    def pox(*args, **kwargs):
        while True:
            rec = Recognizer()
            elem = method(rec, *args, **kwargs)
            if elem == False:
                speak("Ok I brake")
                break
    return pox


def OpenOf():
    url = DictBook['source']['url']
    path = "C:\\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(path))
    webbrowser.get('chrome').open(url)

def DownLoad():
    response = requests.get(DictBook['source']['url'])
    with open(f"CHOICEassistance/Curyassistance/management/"
              f"{DictBook['source']['title']}", "w") as file:
        file.write(response.content)

@LooperGain
def Looper(elem):
    if 'open' in elem.lower():
        OpenOf()
    elif 'stop' in elem.lower():
        Dict['next'] = ''
        return False

    elif 'install' in elem.lower():
        Process(DownLoad)

    elif 'install' in elem.lower() and 'stop' in elem.lower():
        Process(DownLoad); OpenOf()

    elif 'next' in elem.lower():
        Book = next(DictBook['iterator']); DictBook['source'] = Book
        speak(Book['title'])
    else: return True

def Process(method, *args):
    runner = mp.Process(target=method, args=args); runner.start()
    if method == Spsourse:
        DictRes['flow'] = runner

def FlowBroker():
    try:
        DictRes['flow'].terminate(); print("good")
    except Exception as e: pass; print(e)

def Spsourse(text):
    speak(text)

@cache
def IterForWiki(text: str = None):
    print(text); results = wikipedia.search(text, results=5); print(results)
    global DicFull; DictFull = []
    if not results:
        for elems in results:
            try:
                DictFull.append({
                    'title': elems,
                    'sum': wikipedia.page(elems).summary}, )

                yield wikipedia.page(elems).summary
            except Exception as e: print(repr(e)); yield "Error"
    else:
        speak(f"Wikipedia can not hold any info about {text} Do you want to search in google? "+
              f"if yes say ok if not say no")

        @LooperGain
        def Looper(recognizing):
            if 'ok' in recognizing.lower():
                elem = Googlesearch(text).googlesearch2()
                def tool(iterator):
                    iterator['summary'] = f"{iterator['desc']} {iterator['url']}"; iterator.pop('desc', None)
                    return iterator
                global DictFull; DictFull = list(map(tool, elem))
            elif 'no' in recognizing.lower():
                return False

    DictRes['DictList'] = DictFull  # for ownership

def main(killer: threading.Event = None):
    speak("Hello user, I am a virtual assistant")
    while True:
        FullManagement()
        print(threading.active_count())
        if killer:
            if killer.is_set():
                speak("Bye Bye see you later Boss"); moss.MyWidget().TextEnv()
                break

if __name__ == "__main__":
    main()


