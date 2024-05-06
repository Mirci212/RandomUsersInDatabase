import requests

randomUserApi: str = "https://randomuser.me/api/?results={}"


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

    def generateSQLInsertWithoutCountry(self):
        return f'(\'{self.firstname}\',\'{self.lastname}\',\'{self.email}\',\'{"{}"}\',\'{self.plz}\',\'{self.city}\',\'{self.street}\',{self.streetNum},\'{self.birthday.split("T")[0]}\')'


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

    def removeUser(self, pos: int) -> User:
        return self.userlist.pop(pos)

    @staticmethod
    def createUsersRandom(count: int) -> 'UserList':
        apiResult: list = requests.get(randomUserApi.format(count)).json()["results"]
        result: UserList = UserList()
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
