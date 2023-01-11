import random
import re
from functools import cache

import requests
from browser_history.browsers import Chrome
from pytube import YouTube
from CHOICEassistance.Curie.Curyassistant.tools.methods import methods

@cache
def Seeker():
    listCode = []

    elems = Chrome().fetch_history(sort=False, desc=False).histories
    elems = [torchs if 'youtube.com' in torchs[1] else 'None' for torchs in elems]

    for elem in range(100 if len(elems) > 100 else len(elems)):
        if elems[elem][1] != 'None':
            _sourceForGet = elems[elem][1]
            try: _sourceForGet = _sourceForGet[:_sourceForGet.rindex('&')]
            except: print(_sourceForGet)

            try:
                title = YouTube(_sourceForGet).title
                _timeLength = round(YouTube(_sourceForGet).length / 60, 2)
                print(title, "||", _timeLength)

                angle = ['music', 'speed up', 'track', 'slow', 'remix', 'playlist', 'slowed', 'lyrics']
                if _timeLength <= 5.30 or any([True if " ".join(re.findall("[a-zA-Z]+", text.lower())) in angle
                                               else False for text in title.split()]):

                    if str(_sourceForGet) not in listCode:
                        listCode.append(_sourceForGet)

            except: continue
    print(listCode, end=' '); _random = random.choice(listCode); methods.OpenOf(_random)
    return _random

print(Seeker())

