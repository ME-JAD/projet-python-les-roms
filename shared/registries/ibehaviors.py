from abc import abstractmethod


class IBehaviors:
    @abstractmethod
    def get_behaviors(self):
        pass
