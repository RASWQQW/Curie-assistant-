import json
import os
import random
import re
from functools import cache
from typing import Optional, Tuple, Dict, Any

import bs4
import pytube
import requests
from browser_history.browsers import Chrome
from pytube import YouTube
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from CHOICEassistance.Curie.Curyassistant.speaker.methods.Spec.CurieMusic.items.serivce_definder import DefinerOF
from CHOICEassistance.Curie.Curyassistant.speaker.methods.Spec.CurieMusic.items.service_items import LogManager

from CHOICEassistance.Curie.Curyassistant.speaker.methods.Spec.objects.objects import link
from CHOICEassistance.Curie.Curyassistant.tools.methods import methods
from CHOICEassistance.Curie.Curyassistant.tools.Classes.Base.connectCl import *


class Sources_(object):
    def DeskOpt(self, method: Optional[Any] = None, elems: tuple[str, bool] = None) -> Any:
        def _statMethod(result):
            _fType = result[1]; _url = result[0]
            _result = YouTube(_url).streams.filter(only_audio=_fType)
            _result[0].download(filename='../../audio.mp3')

        if not elems and method:
            def Pox(*args, **kwargs):
                result = method(*args, **kwargs)  # get the two values fType, url
                _statMethod(result)
            return Pox
        else:
            _statMethod(elems)

    # its actually saves in base
    def rooser(self, fun):
        def wrapper(*args, **kwargs):
            result = fun(*args, **kwargs)
            if result['saveLast']:

                if result['userId'][0] is not None:
                    result['userid'] = result['userId'][1]

                    # TODO: save last opened link
                    # Connection.connector.connect()

                    _saver = YouTubeManagement \
                        .update({YouTubeManagement.m_LastVideo: result['link'],
                                 YouTubeManagement.m_Array: result['len']}) \
                        .where(YouTubeManagement.User.UserName == result['userId']).execute()
                else:
                    LookFor(userId=result['userId'], saveLast=False).userHistSaver(result['link'])

                # return result['link']  Because essentially opens a link in browser
        return wrapper  # return inner method which executes decorator obtained method


class LookFor(object):
    Fon = Sources_()  # establishing example of object till calling

    def __init__(
                self,
                saveLast: bool,
                userId: tuple = (None, False),
                mixing: Optional[bool] = False,
                genre: Optional[list] = None,
                vibe: Optional[str] = None
                 ):

        self.saveLast = saveLast
        self.userId = self.validId_(userId)
        self.Fon = Sources_()
        print(self.userId)

        #options values which is all as optional
        self.mixing = mixing
        self.mainJanres = genre
        self.vibe = vibe
        self.current_path = self.definePath()

    def definePath(self):

        """New definer of local path for with open() elements """
        local_path = ["speaker", "methods", "Spec", "CurieMusic"]
        if os.path.basename(os.getcwd()) == "Curyassistant":
            return os.getcwd() + "\\" + "\\".join(local_path) + "\\"
        else:
            path = os.getcwd()
            for el in range(len(local_path)-1):
                if os.path.basename(path) == local_path[el]:
                    path +=f"\\{local_path[el+1]}"
            return path + "\\"

    def editor(self, mix: bool):
        if mix: self.mixing = True
        # all on that jazz

    def PlaylistsOfVibe(self, vibeName: str) -> tuple[bool, bool]:
        """ TODO

        For assembling whole similar music by separating his specific species such as
        slowed, phonk, anime, sad, romantic, canon, etc.
        They all would be introduced to user as unique unrepeated playlists


        No No is actually gone ad definer taste of user and set say him about full video

        """

        if self.userId:
            vibes = MusicVibes.select().join(UserVibe)\
                .where(MusicVibes.id == UserVibe.vibe_id and UserVibe.user_id == self.userId
                       and MusicVibes.name == vibeName)
            if vibes:
                if len(vibes) and vibes[0].status >= 3:
                    return True, True  # it returns tuple each is True if vibe is quite popular
                else:
                    return True, False
            else:
                return False, False

    def PerferedJangres(self):
        """TODO

        About what janres user noted in list in wishful

        for examples user choose some kind of janres in and set arg he/she will get
        And relatively we will get this arg if True get random elem and sort in music and send back it

        """

        if self.userId:
            user = MusicJanres.select().where(MusicJanres.User_id == self.userId)
            if len(user) > 0:
                self.mainJanres = random.choices(user, k=2)

                # Saying in @Speaker what amount of genres you will seek among music
        pass

    def validId_(self, userId: tuple) -> tuple:
        import uuid; print(self.__dict__)
        if userId[0] is None:
            return None, str(uuid.UUID(int=uuid.getnode()))
        else: return True, userId

    def userHistSaver(self, linkOf: str):

        userId = str(self.userId[1])
        with open(f'{self.current_path}historyData.json', 'r') as history:
            dict = json.load(history)
        print(dict, userId)
        if userId in dict:
            if str(linkOf) not in dict[userId]:
                dict[userId].append(str(linkOf))
            else: return True
        else: dict[userId] = [str(linkOf)]

        with open(f'{self.current_path}historyData.json', 'w') as history:
            json.dump(dict, history, indent=4, separators=(',', ': '))

        return False

    def RandomSearchDropper(self):
        """For Calling a decorator """

        """ if {music} is required to install and send to back in telegram, 
        but in other circumstances is not vital  """

        @self.Fon.DeskOpt
        def _runner(url, fType): return url, fType
        # _runner()

        def CatchMusic():
            def MixingOF(songName: str):
                listOf = ['speed', 'slow', 'remix', 'slowed', 'edit', 'mix']
                MixedSongName = songName + " " + random.choice(listOf)
                return MixedSongName

            # partially parsing in Spotify
            _response = requests.get("https://open.spotify.com/playlist/57EG9lWmdn7HHofXuQVsow", timeout=100)
            _parser = bs4.BeautifulSoup(_response.text, 'lxml')
            _mainBlock = _parser.find('div', class_='ufy3rNNsNBx6IOixSXEG')
            _secondBlocks = _mainBlock.findAll('div', class_='wbGUuBgShYJ7AJN775Uy')


            _DictOF = [_namesA.find('a', '_4R6oAAgA1uWIjEr03kKg').get('href') for _namesA in _secondBlocks]
            # print(_DictOF)
            _DictOFRes = random.choice(_DictOF)
            text = requests.get(_DictOFRes)
            element = bs4.BeautifulSoup(text.text, 'lxml'); songName = element.find('title').text
            _songName = songName[:songName.rindex("| Spotify")]
            if self.mixing: _songName = MixingOF(_songName)
            _DictOFRes = pytube.Search(_songName).results[0].watch_url
            # end of parsing

            if self.userHistSaver(_DictOFRes):
                # parsing forward on YouTube
                ListOf = [f'top music of{0}', f'top music of{0}', f'top music of tiktok {0}', f'top music youtube {0}']
                searchText = random.choice(ListOf).format(datetime.datetime.now().year).strip().replace(" ", "+") + "+"
                _searchLink = f'https://www.youtube.com/results?search_query={searchText}&sp=EgIQAw%253D%253D'

                driver = webdriver.Chrome(ChromeDriverManager().install())
                driver.get(_searchLink)
                #just parsing of YouTube search settings
                videos = driver.find_elements(by="id", value='thumbnail')[2:5]

                _PlaylistVideos = []
                for elems in videos: _PlaylistVideos += pytube.Playlist(elems.get_attribute('href')).videos

                # for sending random youtube music video link
                _link = random.choice([elem.watch_url for elem in _PlaylistVideos])
                return _link
            else: return _DictOFRes

        _url = CatchMusic(); DefinerOF(userGenre=self.mainJanres).SorterIs(_url); methods.OpenOf(_url)
        # TODO: write about how perform catching random famous videos randomly and search it in youtube therefore send
        return {'saveLast': self.saveLast, 'userId': self.userId, 'link': _url, 'len': 1}

    @Fon.rooser
    @cache
    def Seeker(self) -> Optional[Any]:  # dict, str[link | int]

        """ TODO These function not available use in web but it worth get api from site just add these function
        Seeker. It is such good solution on my own """

        elems = Chrome().fetch_history(sort=False, desc=False).histories

        # sort hist objects by links consist
        elemsOn = []

        for torchs in elems:
            if 'youtube.com/watch?v=' in torchs[1]: elemsOn.append(torchs[1])

        print("elem", elemsOn)

        elemsOn = elemsOn if len(elemsOn) < 60 else elemsOn[0: 60]
        listCode = DefinerOF(LinkList=elemsOn, userGenre=self.mainJanres).CollectionMethod()

        print(listCode, end=' '); _random = random.choice(listCode); print(_random)

        if self.userHistSaver(str(_random)):
            if self.userId[0] is not None:
                # save all found music links in base
                _count = YouTubeManagement \
                    .select(YouTubeManagement.m_Array).where(YouTubeManagement.User.userId == self.userId[0])[0]

                if len(listCode) + len(_count) <= 10:
                    return self.RandomSearchDropper()
            else:
                return self.RandomSearchDropper()

        # the last execution in class to end full process
        methods.OpenOf(_random)

        # this rest of strings are beyond in main process which only have back save or edit settings
        _backAttr = {'link': link(_random), 'len': len(listCode), 'saveLast': self.saveLast, 'userId': self.userId}

        return _backAttr


if __name__ == "__main__":
    LogManager().step1ForSaving()  # regulation of data saving inside json delete or dump and write a current date
    elem = LookFor(saveLast=True).Seeker()

    url = 'https://www.youtube.com/watch?v=m7Bc3pLyij0'
    # Sources_.DeskOpt(method=None, elems=(url, True))
