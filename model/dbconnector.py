import mysql
import json
import mysql.connector


class DBConnector:
    def __init__(self):
        self.__db: mysql.connector = None
        self.__dbConf = {}
        self.__load_conf()
        self.__db_connect()
        self.__cursor = self.__db.cursor()

    def __db_connect(self):
        __mysqlConf = self.__dbConf["mysql"]
        self.__db = mysql.connector.connect(host=__mysqlConf["host"],
                                            user=__mysqlConf["user"],
                                            password=__mysqlConf["password"],
                                            database=__mysqlConf["database"])

    def __load_conf(self):
        with open('conf/dbconf.json') as jsonfile:
            self.__dbConf = json.load(jsonfile)

    def get_cursor(self):
        return self.__cursor
