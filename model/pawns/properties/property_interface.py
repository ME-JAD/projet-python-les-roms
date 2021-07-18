from abc import ABC, abstractmethod


class PropertyInterface:
    @abstractmethod
    def __init__(self, prop=None):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def set(self, value):
        pass

    @abstractmethod
    def to_string(self):
        pass
