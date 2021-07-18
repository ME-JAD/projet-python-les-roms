from model.pawns.properties.property_interface import PropertyInterface


class Alive(PropertyInterface):
    __alive: bool = True

    def __init__(self, alive: bool = None):
        self.__alive = True if alive is None or type(alive) == dict else alive

    def get(self) -> bool:
        return self.__alive

    def set(self, alive: bool):
        self.__alive = alive

    def to_string(self) -> str:
        return "alive"
