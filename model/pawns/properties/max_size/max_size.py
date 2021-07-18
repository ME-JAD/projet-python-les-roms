from model.pawns.properties.property_interface import PropertyInterface


class MaxSize(PropertyInterface):
    __max_size = 3

    def __init__(self, max_size: int = None):
        self.__max_size = 3 if max_size is None or type(max_size) == dict else max_size

    def get(self) -> int:
        return self.__max_size

    def set(self, max_size: int):
        self.__max_size = max_size

    def to_string(self) -> str:
        return "max_size"
