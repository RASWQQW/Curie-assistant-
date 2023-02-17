from CHOICEassistance.Curie.Curyassistant.tools.Classes.Base.connectCl import *

class FullController(object):
    def __init__(self, userId):
        self.userId = userId
        pass

    def GenreSaver(self, genre_list: list) -> None:
        for genre in genre_list:
            genres = MusicJanres.select().where(MusicJanres.User_Id == self.userId and MusicJanres.name == genre)
            if len(genres) == 0:
                user = User.select().where(MusicJanres.User_Id == self.userId).first()
                if user is not None:
                    MusicJanres.create(User=user, name=genre)

    def Recognizer(self, text: str) -> None:
        text = text.split()
        whole_reg_genres = []

        # main genre container list
        genres = [
            'rap', 'pop', 'rock', 'classic', 'soundtrack', 'r&b', 'trap', 'k-pop', 'electronic', 'phonk',
            'anime-rock', 'j-pop', 'philosophy', 'traditional', 'lo-fi', 'sci-phy', 'hip-hop', 'jazz', 'opera']

        for on in text:
            for value in genres:
                if on[:len(value)] == value:
                    whole_reg_genres += [str(value)]; break

        self.GenreSaver(whole_reg_genres)


