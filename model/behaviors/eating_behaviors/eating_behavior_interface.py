from abc import abstractmethod


class EatingBehaviorInterface:
    @abstractmethod
    def eat(self):
        pass