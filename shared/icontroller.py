from abc import abstractmethod


class IController:
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
