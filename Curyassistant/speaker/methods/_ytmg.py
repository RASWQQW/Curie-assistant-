import json
import os
import random
import re
from datetime import date, datetime
from functools import cache
from typing import Optional, Tuple, Dict, Any

import bs4
import pytube
import requests
from browser_history.browsers import Chrome
from pytube import YouTube

from CHOICEassistance.Curie.Curyassistant.tools.methods import methods
from CHOICEassistance.Curie.Curyassistant.tools.Classes.Base.connectCl import *


class _Sources(object):
    def __init__(self):
        pass

    @staticmethod
    def DeskOpt(method: Optional[Any] = None, elems: tuple[str, bool] = None) -> Any:
        def _statMethod(result):
            _fType = result[1]; _url = result[0]
            _result = YouTube(_url).streams.filter(only_audio=_fType)
            _result[0].download(filename='audio.mp3')

        if not elems and method:
            def Pox(*args, **kwargs):
                result = method(*args, **kwargs)  # get the two values fType, url
                _statMethod(result)

            return Pox
        else:
            _statMethod(elems)

    @staticmethod
    def SaveIn(method):
        def invS(*args, **kwargs):
            result = method(*args, **kwargs)
            if result['savelist']:

                # TODO: save last opened link
                Connection.connector.connect()

                if result['userId'] is not None:

                    _saver = YouTubeManagement \
                        .update({YouTubeManagement.m_LastVideo: result['link'],
                                 YouTubeManagement.m_Array: result['len']}) \
                        .where(YouTubeManagement.User.UserName == result['_class']['userId']).execute()
                else:
                    LookFor(userId=result['userId'], saveLast=False).userHistSaver(result['link'])

                # return result['link']  Because essentially opens a link in browser

            return invS  # return inner method which executes decorator obtained method



# it is a still needs accurately object needs dunder methods
class link(object):
    def __init__(self, obj):
        if obj[:3] == 'htt' and isinstance(obj, str):
            self.obj = obj

    def __str__(self):
        return self.obj


class LookFor(object):
    def __init__(self, saveLast, userId=None):
        self.saveLast = saveLast
        self.userId = userId

    def userHistSaver(self, linkOf: str):
        with open('historyData.json', 'r') as history:
            dict = json.load(history)

        if self.userId in dict:
            if str(linkOf) not in dict[self.userId]:
                dict[self.userId].append(str(linkOf))
            else: return True
        else:
            dict[self.userId] = [str(linkOf)]

        with open('historyData.json', 'w') as history:
            json.dump(dict, history, indent=4, separators=(',', ': '))

        return False

    @_Sources.SaveIn
    def RandomSearchDropper(self):
        """For Calling a decorator """

        """ if it is required to install and send to back in telegram, 
        but in other circumstances in not vital """
        @_Sources.DeskOpt
        def _runner(url, fType): return url, fType
        # _runner()

        def CatchMusic():
            # partially parsing in spotify
            _response = requests.get("https://open.spotify.com/playlist/57EG9lWmdn7HHofXuQVsow")
            _parser = bs4.BeautifulSoup(_response.text, 'html.parser')
            _mainBlock = _parser.find('div', class_='ufy3rNNsNBx6IOixSXEG')
            _secondBlocks = _mainBlock.findAll('div', class_='ufy3rNNsNBx6IOixSXEG')

            _DictOF = [_namesA.find('a', '_4R6oAAgA1uWIjEr03kKg') for _namesA in _secondBlocks]
            _DictOFRes = random.choice(_DictOF)
            # end of parsing

            if self.userHistSaver(_DictOFRes):
                _searchLink = 'https://www.youtube.com/results?search_query=top+music+of+2023+&sp=EgIQAw%253D%253D'
                response = requests.get(_searchLink)
                _parsing = bs4.BeautifulSoup(response.text, 'html.parser')
                _parser = _parsing.findAll('div', class_='style-scope ytd-playlist-renderer', id='content')[:3]

                _dictOnYouTube = [_elemOn.find('a', class_=
                'yt-simple-endpoint style-scope ytd-playlist-renderer') for _elemOn in _parser]

                _PlaylistVideos = []
                for elems in _dictOnYouTube:
                    _PlaylistVideos += elems.videos
                # for sending random youtube music video link
                _link = random.choice([elem.watch_url for elem in _PlaylistVideos]); return _link
            else: return _DictOFRes

        _url = CatchMusic(); self.sorterFor_(link=_url)
        # TODO: write about how perform catching random famous videos randomly and search it in youtube therefore send
        return {'saveLast': self.saveLast, 'userId': self.userId, 'link': _url, 'len': 1}


    @_Sources.SaveIn
    @cache
    def Seeker(self) -> Optional[Any]:  # dict, str[link | int]
        listCode = []

        elems = Chrome().fetch_history(sort=False, desc=False).histories
        elems = [torchs if 'youtube.com' in torchs[1] else 'None' for torchs in elems]

        for elem in range(100 if len(elems) > 100 else len(elems)):
            if elems[elem][1] != 'None':
                _sourceForGet = elems[elem][1]
                try:
                    _sourceForGet = _sourceForGet[:_sourceForGet.rindex('&')]
                except: print(_sourceForGet)

                if str(_sourceForGet) not in listCode:
                    if self.sorterFor_(_sourceForGet):
                        listCode.append(_sourceForGet)
                continue

        _count = YouTubeManagement \
            .select(YouTubeManagement.m_Array).where(YouTubeManagement.User.userId == self.userId)[0]

        if len(listCode) + len(_count) <= 10:
            return self.RandomSearchDropper()

        print(listCode, end=' '); _random = random.choice(listCode)
        methods.OpenOf(_random)

        _backAttr = {'link': link(_random), 'len': len(listCode), 'saveLast': self.saveLast, 'userId': self.userId}

        self.userHistSaver(str(_backAttr['link']))
        return _backAttr

    def sorterFor_(self, link: Optional[str]):
        _sourceForGet = link
        try:
            title = YouTube(_sourceForGet).title
            _timeLength = round(YouTube(_sourceForGet).length / 60, 2)

            print(title, "||", _timeLength)

            angle = ['music', 'speed up', 'track', 'slow', 'remix', 'playlist', 'slowed', 'lyrics']
            _dict = [True if " ".join(  # join for finding and removing all no letter elements, such as ) in music)
                re.findall("[a-zA-Z]+", text.lower())) in angle else False for text in title.split()]

            if _timeLength <= 5.30 or any(_dict):
                return True
            return False
        except Exception as e: return False


class LogManager(object):
    def __init__(self):
        pass

    def step1ForSaving(self: object) -> None:
        print(self)
        try:
            with open('historyData.json', 'r') as f:
                _array = json.load(f)
            if (datetime.datetime.now()- datetime.date(_array['date'])).days > 1:
                os.remove('historyData.txt')
        except Exception:
            today = datetime.datetime.now()
            dict = {'date': (today.year, today.month, today.day)}
            with open('historyData.json', 'w') as f:
                json.dump(dict, f, indent=4, separators=(',', ':'))

if __name__ == "__main__":
    LogManager().step1ForSaving()  # regulation of data saving inside json delete or dump and write a current date
    LookFor(saveLast=True).Seeker()
    url = 'https://www.youtube.com/watch?v=m7Bc3pLyij0'
    # _Sources.DeskOpt(method=None, elems=(url, True))
