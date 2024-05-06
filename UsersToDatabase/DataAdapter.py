import os

from mysql.connector import *
from dotenv import load_dotenv

class MySqlDatAdapter:

    def __init__(self, host: str, user: str, password: str,  database: str):
        self._config = {
            'user': user,
            'password': password,
            'host': host,
            'database': database,
            'raise_on_warnings': True
        }
        self.TryConnect()
        self.conn.close()
    def SelectSQL(self, sql: str):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print("Error executing SQL query:", e)
            raise

    def NonQuerySQL(self, sql: str):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            print("SQL statement executed successfully")
        except Exception as e:
            print("Error executing SQL statement:", e)
            self.conn.rollback()
            raise

    def TryConnect(self):
        try:
            self.conn = connect(**self._config)
            print("Connection success")
        except:
            print("Connection failed")
            raise ConnectionError("Connection failed!")


load_dotenv("../environment.env")
MySqlDatAdapter(os.getenv("HOST"), os.getenv("USER"), os.getenv("PASSWORD"), os.getenv("DATABASE"))