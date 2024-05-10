import time

import requests
import math

randomUserApi: str = "https://randomuser.me/api/?results={}"
apiLimitPerRequest: int = 5_000
RequestsPerMinute: int = 4




class User:
    firstname: str
    lastname: str
    email: str
    gender: str
    plz: str
    street: str
    country: str
    birthday: str
    streetNum: int
    city: str

    def __init__(self, firstname: str, lastname: str, email: str, gender: str, plz: str, street: str, streetNum: int,
                 country: str, city: str, birthday: str):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.gender = gender[0].upper()
        self.plz = plz
        self.streetNum = streetNum
        self.street = street
        self.country = country
        self.birthday = birthday
        self.city = city

    @property
    def FullName(self) -> str:
        return f'{self.firstname} {self.lastname}'

    @staticmethod
    def CreateUserFromDictAPI(userDict: dict) -> 'User':
        return User(userDict["name"]["first"], userDict["name"]["last"], userDict["email"], userDict["gender"],
                    userDict["location"]["postcode"], userDict["location"]["street"]["name"],
                    userDict["location"]["street"]["number"], userDict["location"]["country"],
                    userDict["location"]["city"], userDict["dob"]["date"])

    def generateDataForSQL(self):
        country_sql = f"(SELECT LEFT(Land_Kurz, 2) FROM countries WHERE en='{self.country}')"
        return (self.firstname,self.lastname,self.email,self.country,self.plz,self.city,self.street,self.streetNum,self.birthday.split("T")[0])


class UserList:
    userlist: list[User]

    def __init__(self, userlist: list[User] = None):
        if userlist != None:
            self.userlist = userlist
        else:
            self.userlist = []


    def addUser(self, user: User) -> bool:
        self.userlist.append(user)
        return True

    def removeUserPos(self, pos: int) -> User:
        return self.userlist.pop(pos)

    def removeUser(self, user: User):
        self.userlist.remove(user)

    def createUsersAPI(self,count: int = 1) -> bool:
        apiResult: list = requests.get(randomUserApi.format(count)).json()["results"]
        for res in apiResult:
            self.addUser(User.CreateUserFromDictAPI(res))
        return True

    @staticmethod
    def createUsersRandom(count: int) -> 'UserList':
        result: UserList = UserList()
        requestmax = math.ceil(count / apiLimitPerRequest)
        for i in range(requestmax):
            print(f'RequestCountAPI: {(i+1)} / {requestmax}')
            if (i+1) % RequestsPerMinute == 0:
                time.sleep(300)

            if i == requestmax - 1:
                requestCount = count % apiLimitPerRequest
                if requestCount == 0: continue
                apiResult: list = requests.get(randomUserApi.format(requestCount)).json()["results"]
            else:
                apiResult: list = requests.get(randomUserApi.format(apiLimitPerRequest)).json()["results"]

            for res in apiResult:
                result.addUser(User.CreateUserFromDictAPI(res))

        return result

    def removeUserWithUserName(self, FullName: str) -> User or None:
        for user in self.userlist:
            if user.FullName == FullName:
                self.userlist.remove(user)
                return user
        return None

    def __getitem__(self, item):
        return self.userlist[item]

    def __iter__(self):
        return iter(self.userlist)