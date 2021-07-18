import uuid

from model.pawns.properties.property_interface import PropertyInterface


class Id(PropertyInterface):
    __id: str = "missing id"

    def __init__(self, identifier: str = None):
        self.__id = str(uuid.uuid4()) if identifier is None or type(identifier) == dict else identifier

    def get(self) -> str:
        return self.__id

    def set(self, identifier: str):
        self.__id = identifier

    def to_string(self) -> str:
        return "id"
