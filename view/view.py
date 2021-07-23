import tkinter.messagebox

from model.model import Model
from shared.icontroller import IController


class View:
    def __init__(self, controller: IController, window, general_conf):
        self.__controller = controller
        self.__window = window
        self.__header = "A petri dish simulator"
        self.__footer = "made by Romain Duraysseix and Romain Roubaix"
        self.__pawn_size = general_conf['simulation_pawn_size']
        self.__open_window(general_conf['simulation_size_x'], general_conf['simulation_size_y'])

    def __open_window(self, size_x: int = 100, size_y: int = 100):
        self.__window.title(self.__header)
        self.__window.geometry(str(size_x * self.__pawn_size) + 'x' + str(size_y * self.__pawn_size) + '+25+25')
        self.__window.resizable(False, False)
        self.__window.protocol("WM_DELETE_WINDOW", self.__on_closing)
        self.__canvas = tkinter.Canvas(self.__window)
        self.__canvas.pack(fill='both', expand='True')
        self.__canvas.configure(bg='black')

    def update(self, model: Model):
        self.__canvas.delete("all")

        for pawn in model.get_petri_dish().get_pawns():
            pawn_pos = pawn.get_property('position').get()
            pawn_color = pawn.get_property('color').pawn_true_color(pawn) \
                if pawn.has_property('alive') and pawn.get_property('alive').get() else '#a6a6a6'

            self.__canvas.create_rectangle(pawn_pos['x'] * self.__pawn_size,
                                           pawn_pos['y'] * self.__pawn_size,
                                           pawn_pos['x'] * self.__pawn_size + self.__pawn_size,
                                           pawn_pos['y'] * self.__pawn_size + self.__pawn_size,
                                           fill=pawn_color)
        self.__window.update()

    def __on_closing(self):
        self.__controller.stop()
        self.__window.destroy()
