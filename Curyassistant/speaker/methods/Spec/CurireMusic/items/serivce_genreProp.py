from typing import Optional

import bs4
import requests


class GenreProp(object):
    def __init__(self, UserGenres: list):
        self.genres: list = UserGenres
        self.header: Optional[None | str] = None
        self.link: Optional[None | str] = None
        pass

    def SetterInParse(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
                   }

    def Linker(self, title):
        self.link = f"https://www.google.com/search?q={title}+genre"

        pass

    def ProperGenre(self, title: str) -> bool:
        title = title[:title.index("(")]
        title = title.replace(" ", "+").replace(",", "%2C")  # to edit text relatively to search
        self.Linker(title)

        # to start parsing of link
        response = requests.get(self.link, headers=self.header)
        sourceOfParse = bs4.BeautifulSoup(response.text, "html.parser")

        # check app to be confident about presence of genres
        appbar = sourceOfParse.find("div", class_="appbar")
        if appbar:
            genres = appbar.find("div", class_="yTYGId")
            genresNames = genres.find("div", class_="KKHQ8c")
            _all = genresNames.find_all("a")
            _dict = [elem["aria-label"] for elem in _all]

            for current_genre in _dict:
                if current_genre in self.genres: return True
            else: return False

        else:
            # Write code if appbar is None case, so let just start search through the found
            # pages and search all words related to genre

            pass

        return True