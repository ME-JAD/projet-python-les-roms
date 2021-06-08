from abc import abstractmethod


class MicrobeInterface:
    @abstractmethod
    def birth(self):
        pass

    @abstractmethod
    def death(self):
        pass

    @abstractmethod
    def max_energy(self):
        pass