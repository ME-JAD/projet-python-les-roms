import array
import re

from model.pawns.properties.property_interface import PropertyInterface


class Lifecycle(PropertyInterface):
    __lifecycle: list = ['birth', 'reproducing', 'eating', 'moving']

    def __init__(self, lifecycle=None):
        if isinstance(lifecycle, str):
            self.__lifecycle = re.split(";|,|\n", lifecycle)
        elif isinstance(lifecycle, list):
            self.__lifecycle = lifecycle
        else:
            raise ValueError('Need array or string for lifecycle')

    def get(self) -> list:
        return self.__lifecycle

    def set(self, lifecycle: list):
        self.__lifecycle = lifecycle

    def to_string(self) -> str:
        return "lifecycle"
