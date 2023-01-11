import multiprocessing
import threading
import time
import random
from multiprocessing import Process
from typing import Optional, Union

import requests
import wikipedia

# from CHOICEassistance.Curyassistant.speaker.Curie import speak


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

from browser_history.browsers import Chrome

# from bot.search.googleser import Googlesearch

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

# global Dol
# Dol = {'source': [], 'iterator': []}
#
#
# def os():
#     elem = []
#     for i in range(5):
#         elem.append(i)
#     return elem
#
# source = os(); iterator = iter(source)
# Dol['source'] = source; Dol['iterator'] = iterator
#
# for _ in range(len(Dol['source'])):
#     print(next(Dol['iterator']))


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


# def Text(method):
#     def pox(*ags, **kwargs):
#         while True:
#             san = random.randint(1, 5)
#             ep = method(san)
#             if ep:
#                 print(ep)
#             else:
#                 break
#
#
#     return pox
#
# @Text
# def write(san):
#     print("Into", san)
#     time.sleep(0.5)
#     if san == 4:
#         return False
#     return san + 1
#
#
# s = write()
# class Dect(object):
#     def __init__(self, sor, soh):
#         self.sor = sor
#         self.soh = soh
#
#     def __repr__(self):
#         return '{sor=' + self.sor + ' soh=' + self.soh + '}'
#
#     def __str__(self):
#         return '{sor=' + self.sor + ' soh=' + self.soh + '}'
#
# def Arma(alma: Optional[Dect], sakura: Union[Dect | str]):
#     print(alma)
#     print(sakura)
#     pass
#
# des = Dect('kuks', 'suck')
# Arma(alma=des, sakura=(des, 'time'))

# def alma(xan, hope):
#     xan += 2 + hope / 2
#     return int(xan)
#
# numbers = [10, 15, 21, 33, 42, 55]
# numbers2 = [10, 15, 21, 33, 42, 55]
# mapped_numbers = list(map(sum, numbers, numbers2))
# print(mapped_numbers)

# elem = [
#     {
#         'title': 'Alma',
#         'url': 'http://',
#         'desc': 'sweet'
#     },
#     {
#         'title': 'Olma',
#         'url': 'http://',
#         'desc': 'sweetD'
#     },
#     {
#         'title': 'alma',
#         'url': 'http://',
#         'desc': 'sweetDD'
#     }
# ]
# def tool(iterator):
#     iterator['summary'] = f"{iterator['desc']} {iterator['url']}"; iterator.pop('desc', None)
#     return iterator
#
# DictFull = list(map(tool, elem)); print(DictFull)
# class Dect(object):
#     def __init__(self, sor, soh):
#         self.sor = sor
#         self.soh = soh
#
#     def __repr__(self):
#         return '{sor=' + self.sor + ' soh=' + self.soh + '}'
#
#     def __str__(self):
#         return '{sor=' + self.sor + ' soh=' + self.soh + '}'
#
# def Arma(alma: Optional[Dect], sakura: Union[Dect | str]):
#     print(alma)
#     print(sakura)
#     pass
#
# des = Dect('kuks', 'suck')
# Arma(alma=des, sakura=(des, 'time'))elem = [
#     {
#         'title': 'Alma',
#         'url': 'http://',
#         'desc': 'sweet'
#     },
#     {
#         'title': 'Olma',
#         'url': 'http://',
#         'desc': 'sweetD'
#     },
#     {
#         'title': 'alma',
#         'url': 'http://',
#         'desc': 'sweetDD'
#     }
# ]
# def tool(iterator):
#     iterator['summary'] = f"{iterator['desc']} {iterator['url']}"; iterator.pop('desc', None)
#     return iterator
#
# DictFull = list(map(tool, elem)); print(DictFull)
# class Dect(object):
#     def __init__(self, sor, soh):
#         self.sor = sor
#         self.soh = soh
#
#     def __repr__(self):
#         return '{sor=' + self.sor + ' soh=' + self.soh + '}'
#
#     def __str__(self):
#         return '{sor=' + self.sor + ' soh=' + self.soh + '}'
#
# def Arma(alma: Optional[Dect], sakura: Union[Dect | str]):
#     print(alma)
#     print(sakura)
#     pass
#
# des = Dect('kuks', 'suck')
# Arma(alma=des, sakura=(des, 'time'))

# import pickle
# from mainQT import main
#
#
#
# class Alma(object):
#     def __init__(self, sort1, sort2):
#         self.socks = sort1 + sort2 + random.randint(1, 1000)
#         self.cocks = None
#
#     def supposeer(self):
#         return self.socks
#
#     def also(self):
#         while True:
#             time.sleep(2)
#             print("TT", self.socks)
#
#     def __call__(self):
#         return self.socks
#
# elem = Alma(12, 12)
# print(elem.socks)
# with open('Class.dictionary', 'wb') as CDCT:
#     pickle.dump(elem, CDCT)
#
# with open('Class.dictionary', 'rb') as DCt:
#     Class = pickle.load(DCt)
#     Class.socks = 12
#     print(Class.supposeer())
#
# elem.also()


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # Base Case
#         if len(s) == 1: return 1
#
#         count, s_result = 0, ''
#
#         for i in s:
#             if i not in s_result:
#                 s_result += i
#             else:
#                 s_result = s_result[s_result.index(i) + 1:] + i
#
#             if len(s_result) >= count:
#                 count = len(s_result)
#
#         return count
#
# print(Solution().lengthOfLongestSubstring('almasalpd'))


# text = "aacabdkacaa"

# class Solution(object):
#     def longestPalindrome(self, s):
#         fragment = ''
#         if len(s) <= 1: return s
#
#         for elem in range(0, len(s)):
#             if s[elem] in s[elem + 1:]:
#                 san = s[elem + 1:].index(s[elem]) + 1; print('san', san)
#                 Catchstring = s[elem:][0: san + 1]; print(Catchstring)
#                 San = False
#
#                 for loo in range(1, len(Catchstring) - 1):
#                     if not Catchstring[loo] in Catchstring[loo + 1:]:
#                         San = True; print(San); break
#
#                 if not San:
#                     if len(s[elem:][0: san + 1]) > len(fragment):
#                         fragment = s[elem:][0: san + 1]
#
#         return fragment if fragment else s[0]
#
# print(Solution().longestPalindrome(text))

elems = Chrome().fetch_history(sort=True, desc=False).histories
for i in elems:
    print(i[1])