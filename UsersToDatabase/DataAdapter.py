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

    def SelectSQL(self, sql: str):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print("Error executing SQL query:", e)
            raise

    def NonQuerySQLMany(self, sql: str, data: list):
        try:
            cursor = self.conn.cursor()
            cursor.executemany(sql,data)
            print(f'SQL statement executed successfully: {sql}')
        except Exception as e:
            print("Error executing SQL statement:", e)
        self.conn.commit()

    def TryConnect(self):
        try:
            self.conn = connect(**self._config)
            print("Connection success")
        except:
            print("Connection failed")
            raise ConnectionError("Connection failed!")