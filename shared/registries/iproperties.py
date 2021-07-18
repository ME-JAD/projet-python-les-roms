from abc import abstractmethod


class IProperties:
    @abstractmethod
    def get_properties(self):
        pass
