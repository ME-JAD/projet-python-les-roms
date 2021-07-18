from model.pawns.properties.property_interface import PropertyInterface


class Microbe(PropertyInterface):
    __taxonomy: str = "microbe"

    def __init__(self, taxonomy: str = None):
        self.__taxonomy = "microbe" if taxonomy is None or type(taxonomy) == dict else taxonomy

    def get(self) -> str:
        return self.__taxonomy

    def set(self, taxonomy: str):
        self.__taxonomy = taxonomy

    def to_string(self):
        return "microbe"
