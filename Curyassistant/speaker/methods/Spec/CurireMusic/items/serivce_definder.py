import multiprocessing as mp
import re
from typing import Optional
from pytube import YouTube
from CHOICEassistance.Curie.Curyassistant.speaker.methods.Spec.CurireMusic.items.serivce_genreProp import GenreProp


class DefinerOF(object):
    """ The profitably and faster version of determination of video category by mp"""

    def __init__(self,
                 userGenre: Optional[list | None] = None,
                 LinkList: Optional[list | None] = None
                 ):


        self.UserGenre = userGenre
        self.LinkList = LinkList
        self.fork = None



    def ForDividing(self, list_: list, flow_amount: int = 5):  # STEP 1
        self.fork = []

        divide = flow_amount

        tot = (len(list_) // divide)
        countSos = tot if tot == len(list_) / divide else tot + 1
        sumIs = countSos

        for _ in range(divide):
            _gettingElement = list_[sumIs - countSos:sumIs]
            if _gettingElement:
                self.fork += [list_[sumIs - countSos:sumIs]]; sumIs += countSos
            else: break

        print(self.fork, "\n\n"); return self.fork


    def BasicMethod(self, listOF: list, queue: mp.Queue):  # STEP 3
        listCodeOF: list = []
        queue_dict_setter = queue.get()

        for elem in range(len(listOF)):
            _sourceForGet = listOF[elem]  # [1] is additionally
            try:
                _sourceForGet = _sourceForGet[:_sourceForGet.rindex('&list')]
                print('link2:', _sourceForGet)
            except: pass

            if str(_sourceForGet) not in listCodeOF:
                if self.SorterIs(_sourceForGet):  # check links is contains music link properties
                    listCodeOF += [_sourceForGet]
            continue

        queue_dict_setter["ResultLists"] = listCodeOF
        queue.put(queue_dict_setter)
        print(queue_dict_setter, listCodeOF, queue)
        return True

    def SorterIs(self, link: Optional[str]):  # STEP 3/1 child method of 3
        _sourceForGet = link
        try:
            ytSource = YouTube(_sourceForGet)
            title = ytSource.title
            if GenreProp(UserGenres=self.UserGenre).ProperGenre(title):
                # songName = ytSource.description
                _timeLength = round(ytSource.length / 60, 2)
                print(title, "||", _timeLength)

                angle = ['music', 'speed up', 'track', 'slow', 'remix', 'playlist', 'slowed', 'lyrics', 'soundtrack']
                _dict = [True if " ".join(  # join for finding and removing all no letter elements, such as ) in music)
                    re.findall("[a-zA-Z]+", text.lower())) in angle else False for text in title.split()]

                if _timeLength <= 5.30 and any(_dict):
                    return True
            return False
        except Exception as e: print(repr(e)); return False


    def CollectionMethod(self):  # STEP 2, last to sum up all outcome for respective return
        ListOfRes = []
        self.ForDividing(self.LinkList)

        for list in range(len(self.fork)):
            _point = {'flow': list, 'ResultLists': None}
            manager = mp.Queue(); manager.put(_point)
            pr = mp.Process(target=self.BasicMethod, args=(self.fork[list], manager))
            ListOfRes.append({"process": pr, "mr": manager})
            pr.start()
        print("B2B1A11", mp.active_children())
        final_link_catalog = []

        for elIn in ListOfRes:
            elIn["process"].join()
            info = elIn["mr"].get()
            final_link_catalog += info["ResultLists"]

        print("IsIs:", final_link_catalog)
        return final_link_catalog

