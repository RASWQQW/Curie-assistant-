import multiprocessing
import pickle
import re
import threading
import time
import random
from multiprocessing import Process
from typing import Optional, Union, List

import bs4
import pytube
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

# elems = Chrome().fetch_history(sort=True, desc=False).histories
# for i in elems:
#     print(i[1])


# class Solution(object):
#     def threeSum(self, nums):
#         _list = []
#         sos = range(len(nums))
#         for i in sos:
#             for j in sos:
#                 for s in sos:
#                     if nums[i] + nums[j] + nums[s] == 0:
#                         if i != j and i != s and j != s:
#                             if nums[i] == 0 and nums[j] == 0 and nums[s] == 0:
#                                 if [nums[i], nums[j], nums[s]] not in _list:
#                                     _list.append([nums[i], nums[j], nums[s]])
#                             else:
#                                 for elem2 in _list:
#                                     ifit = 0
#                                     for elem in [nums[i], nums[j], nums[s]]:
#                                         count = False
#                                         for elem3 in elem2:
#                                             if elem == elem3:
#                                                 count = True
#                                         if count:
#                                             ifit += 1
#                                     if ifit > 2:
#                                         break
#                                 else:
#                                     _list.append([nums[i], nums[j], nums[s]])
#
#         return _list
#
#
# print(Solution().threeSum(
#     [-9,-14,-3,2,0,-11,-5,11,5,-5,4,-4,5,-15,14,-8,-11,10,-6,1,-14,-12,-13,-11,9,-7,-2,-13,2,2,-15,1,3,-3,-12,-12,1,-2,6,14
#     ,0,-4,-13,-10,-12,8,-2,-8,3,-1,8,4,-6,2,1,10,2,14,4,12,1,4,-2,11,9,-7,6,-13,7,-3,8,14,8,10,12,11,-4,-13,10,14,1,-4,
#      -4,2,5,4,-11,-7,3,8,-10,11,-11,-5,7,13,3,-2,8,-13,2,1,9,-12,-11,6]))
#
# elem = [0,8,2,-9,-14,5,2,-5,-5,-9,-1,3,1,-8,0,-3,-12,2,11,9,13,-14,2,-15,4,10,9,7,14,-8,-2,-1,-15,-15,
#         -2,8,-3,7,-12,8,6,2,-12,-8,1,-4,-3,5,13,-7,-1,11,-13,8,4,6,3,-2,-2,3,-2,3,9,-10,-4,-8,14,8,7,9,1,
#         -2,-3,5,5,5,8,9,-5,6,-12,1,-5,12,-6,14,3,5,-11,8,-7,2,-12,9,8,-1,9,-1,-7,1,-7,1,14,-3,13,-4,-12,
#         6,-9,-10,-10,-14,7,0,13,8,-9,1,-2,-5,-14]
#
#
# print(elem.count(0))


# class Solution(object):
#     def counter(self, _str):
#         _dict = {}
#         for char in range(len(_str)):
#             if not _str[char] in _dict:
#                 _dict[_str[char]] = 1
#                 for san in range(char+1, len(_str)):
#                     if _str[san] == _str[char]: _dict[_str[char]] = _dict[_str[char]] + 1
#         return _dict
#
#     def isAnagram(self, s, t):
#         _s = {}; _t = {}
#
#         if len(s) == len(t):
#             _s_dict = self.counter(s); _t_dict = self.counter(t)
#             print(_s_dict, "||", _t_dict)
#
#             for _char, _aut in _s_dict.items():
#                 try:
#                     if not _t_dict[_char] == _aut: return False
#                 except Exception as e:
#                     return False
#             return True
#         return False
#
# Solution().isAnagram('nagaram', 'anagram')
# word = 'alma'
# _dictOff = [['mala', 'sor'], ['pep', 'cucu']]
#
# if sorted(word) in [sorted(elem[0]) for elem in _dictOff]:
#     print("Yes")


# _video = pytube.Channel('https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ')
# print(_video)
#
# response = requests.get('https://open.spotify.com/playlist/57EG9lWmdn7HHofXuQVsow', timeout=100)
#
# _bsel = bs4.BeautifulSoup(response.text, 'lxml')
# elem = _bsel.find('div', class_="ufy3rNNsNBx6IOixSXEG")
# elem2 = _bsel.findAll('div', class_="wbGUuBgShYJ7AJN775Uy")
#
#
# for elemse in elem2:
#     sos = elemse.find('a', '_4R6oAAgA1uWIjEr03kKg')
#     print(sos)


# searchRes = pytube.Search('top music of 2023 playlist')
#
# for elem in searchRes.results:
#     print(elem.watch_url, elem.views)

#
# ds = {'1': 10, '2': 3, '4': 54}
#
# print(sorted(ds, key=ds.get, reverse=True)[:2])
#
#
#
# def topKFrequent(self, nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: List[int]
#     """
#
# print(topKFrequent.__doc__)

# class Solution(object):
#     def findSubsequences(self, nums):
#         _dict = []
#         for num in range(len(nums)-1):
#             _dicts = [nums[num]]
#             for nn in range(num+1, len(nums)):
#                 if all([True if nums[nn] >= eles else False for eles in _dicts]):
#                     _dicts.append(nums[nn])
#                     _dict.append(_dicts.copy())
#                     for tt in range(nums[nn], len(nums)):
#                         if nums[tt] >= nums[nn]:
#                             _dict.append(nums[tt])
#
#         _dict2 = []
#         for elem in _dict:
#             if elem not in _dict2:
#                 _dict2.append(elem)
#
#         print('1dict:', _dict)
#         print('2dict:', _dict2)
#         return _dict2
#
# print(Solution().findSubsequences([4, 6, 7, 7]))


# class Solution(object):
#     def intToRoman(self, num):
#
#         _dict = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
#         # print(dict(reversed(list(_dict.items()))))
#
#         _digitLen = len(str(num))
#         num = str(num)[::-1]
#         dar = 1
#         text = ''
#         for elem in str(num):
#             elem = int(elem) * dar
#             for key, value in _dict.items():
#
#                 if int(elem) == key:
#                     text+= value; break
#
#                 elif int(elem) % key == 0:
#                     for _ in range(int(elem / dar)):
#                         text+=value
#                     break
#
#                 elif 3 * dar >= int(elem) % key > 0 and int(elem) % key != elem:
#                     for ss in range(int(int(elem) % key / dar)):
#                         text+=_dict[dar]
#                     text += value
#                     break
#
#                 elif int(elem) + dar == key:
#                     text+=value+_dict[dar]; break
#             dar *= 10
#
#         return text[::-1]
#
#
# print(Solution().intToRoman(3435))
#
# "MCMXCIV"


# from itertools import permutations, product, combinations
#
# _dict = [4,6,7,7]
# _dictSS = []
# for amount in range(2, len(_dict)):
#     sos = list(combinations(_dict, amount))
#     _dictSS += sos
#
# print(_dictSS)
# _dict = _dictSS
#
# _dictIS = []
#
# for i in range(len(_dict)):
#     if list(_dict[i]) == sorted(_dict[i]):
#         _dictIS.append(list(_dict[i]))
# print(_dictIS)


from itertools import combinations

from pytube import YouTube

# class Solution:
#     def partition(self, s: str):
#         _dictOf = list(s)
#         _dictOn = [_dictOf]
#
#         for _esess in range(len(_dictOf)):
#             # print(_dictOf[_esess])
#             sickd = []
#             for es in range(_esess+1, len(_dictOf)):
#                 print('s', _dictOf[_esess: es+1], _esess, es); sos=''
#                 for sor in _dictOf[_esess: es+1]:
#                     sos+=sor
#                 if sos == sos[::-1]:
#                     if sos:
#                         sickd.append(sos)
#                 else:
#                     print('ss', _dictOf[es])
#                     if _dictOf[es-1] != _dictOf[es-1] and _dictOf[es] != _dictOf[es+1]:
#                         sickd.append(_dictOf[es-1])
#
#             if sickd:
#                 _dictOn += [sickd]
#
#         print(_dictOn)
#
# Solution().partition("aab")


# class Foo:
#     def SaveIn(self, func):
#         def wrapper(*args, **kwargs):
#             print("ss")
#             elem = func(*args, **kwargs); print(elem)
#         return wrapper
#
# class Bar(object):
#     foo = Foo()
#
#     @foo.SaveIn
#     def func(self):
#         return 'alma'
#
# Bar().func()

# print(list)

# _dictOnYouTube = [_elemOn.find_element(by='class',
#                                        value='yt-simple-endpoint style-scope ytd-playlist-renderer')
#                   .get_attribute('href') for _elemOn in videos]

#
# elem = requests.get('https://open.spotify.com/track/4iJyoBOLtHqaGxP12qzhQI')
#
# elem = bs4.BeautifulSoup(elem.text, 'lxml')
# finder = elem.find('title')
# elem = finder.text[:finder.text.rindex('-')]
# print(elem)
# _DictOFRes = pytube.Search(elem).results[0].watch_url
# print(_DictOFRes)


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         _dictOff = []
#         for elem in nums:
#             _dict = nums.copy(); _dict.remove(elem); adds = 1
#             _dictOff.append(sum(_dict, key=lambda x:x))
#
#         print(_dictOff)
#
# Solution().productExceptSelf([-1,1,0,-3,3])


# class Solution:
#     def findJudge(self, n: int, trust: List[List[int]]) -> int:
#         _dict = {}
#         _dictofTr = [iis[0] for iis in trust]
#
#         for elent in trust:
#             if elent[1] not in _dictofTr:
#                 if elent[1] in _dict:
#                     _dict[elent[1]] += 1
#                 else:
#                     _dict[elent[1]] = 1
#
#         if len(_dict) == 0: return -1
#         elif len(_dict) == 1: return list(_dict.keys())[0]
#         else: return max(_dict, key=_dict.get)


# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         _dict = sorted(nums1 + nums2)
#
#         if len(_dict) % 2 == 1:
#             return float(_dict[int(len(_dict) // 2)])
#         else:
#             return (_dict[len(_dict) // 2] + _dict[(len(_dict) // 2) -1]) / 2
#
#
# print(Solution().findMedianSortedArrays([1, 2], [3, 4]))


# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#
#         def runner(ss: str):
#             _box = {}
#             for elem in enumerate(ss):
#                 if elem[1] not in _box:
#                     _box[elem[1]] = [elem[0]]
#                 else:
#                     _box[elem[1]] += [elem[0]]
#             return list(_box.values())
#
#         return runner(s) == runner(t)


# s = "title"
# t = "paper"
#
# ss = {1: 2, 3: 4}
#
# # print(ss.values())
#
# print(Solution().isIsomorphic(s, t))

# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#
#         def Definding(isFrom, price, path, tos):
#             _lost = []
#             for elem in flights:
#                 if elem[0] == isFrom[1]:
#                     if elem[1] not in path:
#                         path += [elem[0]]; price += elem[2]
#                         if elem[1] == dst:
#                             return [price, path]
#                         else:
#                             tos += "-"
#                             _lost +=[Definding(isFrom=elem, price=price, path=path, tos=tos)]
#                             tos = tos[:-1]
#                         path = [isFrom[0]]; price = isFrom[2]
#
#             def resof(typeIS):
#                 if type(typeIS): return typeIS
#                 else: return resof(typeIS[0])
#             return resof(_lost)
#
#         sumPrice = []
#         for once in flights:
#             if once[0] == src:
#                 if once[1] == dst: elem = [once[2], [src]]
#                 else: elem = Definding(once, once[2], path=[once[0]], tos=".")
#                 if elem is not False: sumPrice += [elem]
#
#         if len(sumPrice) < 1: return -1
#
#         _min = []
#         for _elentIs in sumPrice:
#             if len(_elentIs[1]) <= k+1: _min +=[_elentIs[0]]
#         return _min[0] if len(_min) > 1 else min(_min)



# class Solution:
#   def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#
#     def Fork(elem, path, price):
#         for eles in flights:
#             if eles[0] == elem[0] and eles[0] not in path:
#                 path += eles[0]; price +=eles[2]
#                 return eles, price, path
#
#     for elem in flights:
#         if elem[0] == src:
#             elem = Fork(elem, [elem[0]], elem[2])
#             while elem:
#                 elem = Fork(elem[0], elem[1], elem[2])
#
#
#
# print(Solution().findCheapestPrice(10, [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10]
#     ,[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6]
#     ,[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]], 6, 0, 7))


# ["aria-label"]
# import multiprocessing as mp
# import numpy as np
#
#
#
#
#
#
# def divider():
#     def oppa():
#         return random.randint(1, 10)
#
#     fork, list_ = [], [oppa() for _ in range(12)]
#     print(list_)
#
#     divide = 3; tot = (len(list_) // divide)
#     countSos = tot if tot == len(list_) / divide else tot + 1
#     sumIs = countSos
#
#     for _ in range(divide):
#         _gettingElement = list_[sumIs - countSos:sumIs]
#         if _gettingElement:
#             fork += [list_[sumIs - countSos:sumIs]]
#             sumIs += countSos
#         else:
#             break
#     print(fork, "\n\n"); return fork
#
#
#
# def alma(elem: int, dicOfList: list, queue: mp.Queue):
#     for el in dicOfList:
#         print(el)
#         time.sleep(elem)
#
#     setter = queue.get()
#     setter["elem"] = f"{elem}{sum(dicOfList)}"
#     queue.put(setter)
#     print("isisOF", queue)
#
#
# if __name__ == "__main__":
#
#     fork = divider()
#     listOfGetting = {"elem": None}
#
#
#     processes: list[dict] = []
#     for pr in range(3):
#         manager = mp.Queue()
#         manager.put(listOfGetting)
#
#         pr_is = mp.Process(target=alma, args=(pr, fork[pr], manager))
#         processes.append({"pr": pr_is, "mn": manager})
#         pr_is.start()
#
#     print(processes)
#     for isis in processes:
#         isis["pr"].join()
#         print("All", isis["mn"].get())
#         isis["pr"].kill()

# from typing import NewType
#
# listOF: List[int | str] = [1, 12]
#
# Linker = NewType("Linker", int)
# to = Linker(12)
#
# print(listOF, to, to.__class__)
#
# def okko(link: ):
#     print("is", type(link))
#
# okko(12)

# class Occo:
#     def __init__(self):
#         pass
#
# print(Occo.__name__)
#
#
# class Link:
#     def __init__(self, val, next):
#         self.val = val
#         self.next = next
#
#
# alm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# oc = Link(val=alm[0], next=[1])
#
# for elem in range(len(alm)-1):
#     oc = Link(val=alm[elem], next=oc)
#
# for elem in range(len(alm)):
#     print(oc.val)
#     oc = oc.next


# def Cocco():
#     elem = list("abcdefghijklmnopqrstuvwxyz")
#     words = ["apple","app"]
#     _list = []
#
#     for word in enumerate(words):
#         for nexts in enumerate(words[word[0]+1:]):
#             for char in word[1]:
#                 _sum = 0
#                 for chars in enumerate(nexts[1]):
#                     print(chars[1], char)
#                     if elem.index(char) > elem.index(chars[1]) or char == chars[1]:
#                         _sum += 1
#                 print(_sum, len(nexts[1]))
#                 if _sum >= len(nexts[1]):
#                     return False
#     else:
#         return True
#
# print(Cocco())

