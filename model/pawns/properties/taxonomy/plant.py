import string

from model.pawns.properties.property_interface import PropertyInterface


class Plant(PropertyInterface):
    __taxonomy: string = "plant"

    def __init__(self, taxonomy: str = None):
        self.__taxonomy = "plant" if taxonomy is None or type(taxonomy) == dict else taxonomy

    def get(self) -> str:
        return self.__taxonomy

    def set(self, taxonomy: str):
        self.__taxonomy = taxonomy

    def to_string(self):
        return "plant"
