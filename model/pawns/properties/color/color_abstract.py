import copy

from model.pawns.properties.property_interface import PropertyInterface


class ColorAbstract(PropertyInterface):
    __red: int = 0
    __green: int = 0
    __blue: int = 0

    def __init__(self, rgb: tuple = None):
        self.__red = 0 if rgb is None or type(rgb) == dict else rgb[0]
        self.__green = 0 if rgb is None or type(rgb) == dict else rgb[1]
        self.__blue = 0 if rgb is None or type(rgb) == dict else rgb[2]

    def get(self) -> str:
        return f'#{self.__red:02x}{self.__green:02x}{self.__blue:02x}'

    def get_red(self) -> int:
        return self.__red

    def get_green(self) -> int:
        return self.__green

    def get_blue(self) -> int:
        return self.__blue

    def set(self, rgb: tuple):
        self.__red = rgb[0]
        self.__green = rgb[1]
        self.__blue = rgb[2]

    def darken(self, dark_coefficient: int):
        self.__red = max(0, self.__red - dark_coefficient)
        self.__green = max(0, self.__green - dark_coefficient)
        self.__blue = max(0, self.__blue - dark_coefficient)

    def pawn_true_color(self, pawn):
        if pawn.has_property('max_energy'):
            pawn_energy = pawn.get_property('energy').get()
            pawn_max_energy = pawn.get_property('max_energy').get()
            energy_level = pawn_energy / pawn_max_energy
            if energy_level < 1:
                pawn_energy_level = energy_level * 255
                darkened_color = self.clone()
                darkened_color.darken(int(round(pawn_energy_level)))
                return darkened_color
        return pawn.get_property('color')

    def swap(self):
        red = self.__red
        self.__red = self.__green
        self.__green = self.__blue
        self.__blue = red

    def clone(self):
        return copy.deepcopy(self)

    def to_string(self) -> str:
        return "color"

