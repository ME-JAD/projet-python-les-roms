from abc import ABC, abstractmethod


class ColorInterface:
    @abstractmethod
    def get_color(self):
        pass
