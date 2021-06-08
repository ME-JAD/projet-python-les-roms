from model.model import Model
from view.view import View
from shared.icontroller import IController


class Controller(IController):
    def __init__(self):
        self.__model = Model()
        self.__view = View(self)

    def start(self):
        pass
