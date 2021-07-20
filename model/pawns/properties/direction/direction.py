from model.pawns.properties.property_interface import PropertyInterface


class Direction(PropertyInterface):
    __direction: int = 0

    def __init__(self, direction: int = None):
        self.__direction = 0 if direction is None or type(direction) == dict else direction

    def get(self) -> int:
        return self.__direction

    def set(self, direction: int):
        self.__direction = direction

    def to_string(self) -> str:
        return "direction"

    def get_direction_from_two_positions(self, old_position: dict, new_position: dict):
        if old_position['x'] > new_position['x']:
            return 3
        elif old_position['x'] < new_position['x']:
            return 1
        elif old_position['y'] < new_position['y']:
            return 0
        else:
            return 2
