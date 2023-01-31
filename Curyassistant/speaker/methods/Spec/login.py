import os
import pickle
import random
from CHOICEassistance.Curie.Curyassistant.tools.Classes.Base.connectCl import *


class LogIn(object):
    def __init__(self, password, name):
        self.__idGen = 12
        self.password = password
        self.name = name

    def generateId__(self, id=None):
        self.__idGen = id if id else str(hash(self.name + self.password))
        print(pickle.dumps(self.__idGen))
        with open(f'{os.getcwd()}/hash/idGn.dictionary', 'wb') as file:
            pickle.dump(self.__idGen, file)
        return self.__idGen

    def SaveInBase(self, Login: bool = None, SignUp: bool = None):
        Connection.connector.connect()
        UserGet = User.select(User).where(User.password == self.password, User.UserName == self.name)[0]
        if SignUp:
            if not UserGet:
                User.create(userId=self.generateId__(), password=self.password, UserName=self.name).save()
                return True, "Congrats you account created successfully!"
            else: return False, "Your account is already exists"

        if Login:
            if not UserGet: return False, "You have wrong account"
            else:
                self.generateId__(id=UserGet[0].userId)
                return False, "Congrats you are in!"

    def LastExecute(self):
        performing = self.SaveInBase()
        return "Welcome here our new user" if performing else "Welcome here, Nice to see you again there"

    def Converter(self):
        """To get the id code inside pickle file and find user in Base"""

        print(self.__dict__)


        return True

    def __call__(self):
        return self.__str__

    def __str__(self):
        return "For Log in class"


if __name__ == "__main__":
    elem = LogIn("Rasul", '1212').generateId__()