from model.pawns.properties.property_interface import PropertyInterface


class Position(PropertyInterface):
    __x: int = 0
    __y: int = 0

    def __init__(self, position: dict):
        self.__x = position['x']
        self.__y = position['y']

    def get(self) -> dict:
        return {'x': self.__x, 'y': self.__y}

    def set(self, position: tuple):
        self.__x, self.__y = position

    def to_string(self) -> str:
        return "position"
