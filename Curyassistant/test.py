import multiprocessing
import threading
import time
import random
from multiprocessing import Process

import wikipedia

from CHOICEassistance.Curyassistant.speaker.Curie import speak


# def alma():
#     while True:
#         elem = random.randint(1, 5)
#         time.sleep(elem)
#         global atro
#         if atro:
#             print('over')
#             break
#         print("alma")
#
#
# def banana():
#     while True:
#         time.sleep(random.randint(1, 5))
#         print("banana")
#
#
# bananaTh = threading.Thread(target=banana)
# almaTh = threading.Thread(target=alma)
#
# atro = False
# almaTh.start(); bananaTh.start()
# time.sleep(2)
# atro = True

# query = "alma zhaman sol about"
# if any([True if i in ['about', 'tell'] else False for i in query.lower().split()]):
#     print('yes')

# def doit(stop_event, arg):
#     while not stop_event.wait(1):
#         print ("working on %s" % arg)
#     print("Stopping as you wish.")
#
#
# def main():
#     pill2kill = threading.Event()
#     t = threading.Thread(target=doit, args=(pill2kill, "task"))
#     t.start()
#     time.sleep(5)
#     pill2kill.set()
#     t.join()
#
# main()

# def IterForWiki(text: str = None):
#     # results = wikipedia.search(text, results=5)
#     for i in range(5):
#         print(i)
#
# IterForWiki()

# wikipedia.set_lang('en')
# info = wikipedia.search("Osaka", results=5)
# print(info)
# for i in info:
#     try: print(info.index(i), f"  {wikipedia.page(i).summary} \n")
#     except: continue


# def Spsourse():
#     while True:
#         speak("Holl")
#
#
# def main():
#     runner = multiprocessing.Process(target=Spsourse)
#     runner.start()
#     time.sleep(3.5)
#
#
#
# if __name__ == "__main__":
#     main()



# def sups():
#     for i in range(5):
#         yield i
#
# print(len(list(sups())))

# listFORC = ['alma', 'about', 'banana']
# source = [(True, i) if listFORC[i] in ['wiki', 'about', 'tell'] else (False, -1)
#           for i in range(len(listFORC))]

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()


import webbrowser

from bot.search.googleser import Googlesearch

# contents = Googlesearch('Solo').googlesearch2()
#
# for elems in contents:
#     print(elems['title'])
#     print(elems['url'])
#
# url = contents[0]['url']
# path = "C:\\Program Files\Google\Chrome\Application\chrome.exe"
# webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(path))
# webbrowser.get('chrome').open(url)

global Dol
Dol = {'source': [], 'iterator': []}


def os():
    elem = []
    for i in range(5):
        elem.append(i)
    return elem

source = os(); iterator = iter(source)
Dol['source'] = source; Dol['iterator'] = iterator

for _ in range(len(Dol['source'])):
    print(next(Dol['iterator']))


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#             l1.reverse(); l2.reverse()
#
#             l1n = ''; l2n = ''
#             for i in l1:
#                 l1n = l1n + str(i)
#
#             for i in l2:
#                 l2n = l2n + str(i)
#
#             l3 = int(l1n) + int(l2n)
#             l3 = list(str(l3)); l3.reverse(); return l3
#
#
# print(Solution().addTwoNumbers([4, 5], [2, 5]))

# elem = {'s': 1, 'n': {'s': 2, 'n': {'s': 4, 'n': None}}}
#
# def openner(elem):
#     if elem['n'] is None:
#         return elem['s']
#     else:
#         return str(elem['s']) + str(openner(elem['n']))
#
# print(openner(elem))
#

# class ListNode:
#     def __init__(self, val, next):
#         self.val = val
#         self.next = next
#
#     def __repr__(self):
#         return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"
#
# def creater(elem, i, range):
#     if i + 1 > range:
#         return None
#     else:
#         i += 1
#         return ListNode(val=elem[i], next=creater(elem, i, range))
#
# print(creater(str(108), -1, len(str(108)) - 1))


# print(dict(enumerate(list('12'))))


def Text(method):
    def pox(*ags, **kwargs):
        while True:
            san = random.randint(1, 5)
            ep = method(san)
            if ep:
                print(ep)
            else:
                break


    return pox

@Text
def write(san):
    print("Into", san)
    time.sleep(0.5)
    if san == 4:
        return False
    return san + 1


s = write()