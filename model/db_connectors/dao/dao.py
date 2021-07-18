from model.db_connectors.mongodb_db_connector import MongoDbDbConnector


class DAO:
    def __init__(self, db_connector: MongoDbDbConnector, entity: str):
        self.__db_connector = db_connector
        self.__entity = entity

    def get_db_connector(self):
        return self.__db_connector

    def get_collection(self):
        return self.__db_connector.get_collection(self.__entity)
