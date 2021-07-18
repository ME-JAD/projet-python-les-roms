from model.pawns.properties.property_interface import PropertyInterface


class Energy(PropertyInterface):
    __energy: float = 1

    def __init__(self, energy: float = None):
        self.__energy = True if energy is None or type(energy) == dict else energy

    def get(self) -> float:
        return self.__energy

    def set(self, amount: float):
        self.__energy = amount

    def to_string(self) -> str:
        return "energy"
