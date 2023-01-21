import os
import pickle
import random
from CHOICEassistance.Curie.Curyassistant.tools.Classes.Base.connectCl import *


class LogIn(object):
    def __init__(self, password, name):
        self.password = password
        self.name = name

    def _generateId(self, id=None):
        self.idGen = id if id else str(hash(self.name + self.password))
        print(pickle.dumps(self.idGen))
        with open(f'{os.getcwd()}/hash/idGn.dictionary', 'wb') as file:
            pickle.dump(self.idGen, file)

    def SaveInBase(self):
        Connection.connector.connect()
        UserGet = User.select(User).where(User.password == self.password, User.UserName == self.name)[0]
        if not UserGet:
            User.create(userId=self.idGen, password=self.password, UserName=self.name).save()
            self._generateId(); return True
        else:
            self._generateId(id=User.userId)
            return False

    def LastExecute(self):
        performing = self.SaveInBase()
        return "Welcome here our new user" if performing else "Welcome here, Nice to see you again there"

    def __call__(self):
        return self.__str__

    def __str__(self):
        return "For Log in class"


if __name__ == "__main__":
    LogIn("Rasul", '1212')._generateId()