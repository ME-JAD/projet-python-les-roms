from model.pawns.properties.property_interface import PropertyInterface


class MaxEnergy(PropertyInterface):
    __max_energy: float = 3

    def __init__(self, max_energy: float = None):
        self.__max_energy = 3 if max_energy is None or type(max_energy) == dict else max_energy

    def get(self) -> float:
        return self.__max_energy

    def set(self, amount: float):
        self.__max_energy = amount

    def to_string(self) -> str:
        return "max_energy"
