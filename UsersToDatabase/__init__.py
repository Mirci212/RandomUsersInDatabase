from UsersToDatabase.DataAdapter import *
from UsersToDatabase.Users import *

class GenerateUsersInTable:
    adapter: MySqlDatAdapter

    def __init__(self, host: str, user: str, password: str,  database: str):
        self.adapter = MySqlDatAdapter(host,user,password,database)

    def writeUsersInTable(self,datatable: str,count: int):
        sql = f'INSERT IGNORE INTO {datatable} (firstName,lastName,email,country,plz,city,street,streetNum,birth) ' \
              f'VALUES (%s, %s, %s, (SELECT Land_Kurz FROM countries WHERE en=%s), %s, %s, %s, %s, %s)'
        users = UserList.createUsersRandom(count)
        data = [user.generateDataForSQL() for user in users]

        self.adapter.NonQuerySQLMany(sql,data)

        print("Wrote all users in sql finished!")


