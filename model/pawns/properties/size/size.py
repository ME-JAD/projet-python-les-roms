from model.pawns.properties.property_interface import PropertyInterface


class Size(PropertyInterface):
    __size: int = 1

    def __init__(self, size: int = None):
        self.__size = 1 if size is None or type(size) == dict else size

    def get(self) -> int:
        return self.__size

    def set(self, size: int):
        self.__size = size

    def to_string(self) -> str:
        return "size"
