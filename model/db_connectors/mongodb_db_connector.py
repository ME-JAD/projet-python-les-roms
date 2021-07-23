import os

import json
from pymongo import MongoClient


class MongoDbDbConnector:
    def __init__(self):
        self.__db: MongoClient
        self.__db_conf = {}
        self.__load_conf()
        self.__db_connect()

    def __db_connect(self):
        __mongo_db_conf = self.__db_conf["mongodb"]
        self.__db = MongoClient(host=__mongo_db_conf["host"],
                                port=__mongo_db_conf["port"],
                                )[__mongo_db_conf["database"]]

    def __load_conf(self):
        with open(os.path.dirname(__file__) + '/../../conf/dbconfs/mongodbdbconf.json') as jsonfile:
            self.__db_conf = json.load(jsonfile)

    def get_collection(self, collection: str):
        return self.__db[collection]
