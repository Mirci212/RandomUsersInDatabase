from DataAdapter import *
from Users import *

class GenerateUsersInTable:
    adapter: MySqlDatAdapter

    def __init__(self, host: str, user: str, password: str,  database: str):
        self.adapter = MySqlDatAdapter(host,user,password,database)

    def writeUsersInTable(self,datatable: str):
        sql = f'INSERT INTO {datatable} (firstName,lastName,email,country,plz,city,street,streetNum,birth) VALUES '
        users = UserList.createUsersRandom(50)
        for user in users:
            country = self.adapter.SelectSQL(f'SELECT Land_kurz FROM countries WHERE Name=\'{user.country}\'')[0][0]
            sql += user.generateSQLInsertWithoutCountry().format(country) + ','
        sql = sql[:-1] + ";"
        self.adapter.NonQuerySQL(sql)
        print()

load_dotenv("../environment.env")
GenerateUsersInTable(os.getenv("HOST"),os.getenv("USER"),os.getenv("PASSWORD"), os.getenv("DATABASE")).writeUsersInTable("test_user")
