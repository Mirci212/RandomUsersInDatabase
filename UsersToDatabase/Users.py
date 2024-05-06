
class User:
    def __init__(self):
        # TODO: Impliment init for User
        NotImplementedError()

    def CreateUserFromApi(self, user: dict) -> 'User':
        # TODO: Impliment to get the User from the API
        NotImplementedError()


class UserList:
     def __init__(self):
         # TODO: Impliment init for UserList
         NotImplementedError()

     def addUser(self, user: User):
         # TODO: Impliment addUser
         NotImplementedError()
     def removeUser(self, pos: int):
         # TODO: impliment removeUser for the pos
        NotImplementedError()

     def removeUserWithUserName(self, username: str):
         # TODO: impliment removeUser for the pos
         NotImplementedError()

     def __getitem__(self, item):
         # TODO: Impliment getItem[]
         NotImplementedError()

