from UsersToDatabase.DataAdapter import *
from UsersToDatabase.Users import *

class GenerateUsersInTable:
    adapter: MySqlDatAdapter

    def __init__(self, host: str, user: str, password: str,  database: str):
        self.adapter = MySqlDatAdapter(host,user,password,database)

    def writeUsersInTable(self,datatable: str):
        sql = f'INSERT INTO {datatable} (firstName,lastName,email,country,plz,city,street,streetNum,birth) VALUES '
        users = UserList.createUsersRandom(2000)
        for user in users:
            country = self.adapter.SelectSQL(f'SELECT Land_kurz FROM countries WHERE Name=\'{user.country}\'')[0][0]
            currsql = sql + user.generateSQLInsertWithoutCountry().format(country) + ';'
            try:
                self.adapter.NonQuerySQL(currsql)
            except:
                users.removeUser(user)
        print("Wrote all users in sql finished!")


