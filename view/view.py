import tkinter.messagebox

from model.model import Model
from shared.icontroller import IController


class View:
    def __init__(self, controller: IController, size_x: int = 100, size_y: int = 100, pawn_size: int = 5):
        self.__header = "A petri dish simulator"
        self.__footer = "made by Romain Duraysseix and Romain Roubaix"
        self.__create_window(size_x, size_y)
        self.__controller = controller
        self.__pawn_size = pawn_size

    def __create_window(self, size_x: int = 100, size_y: int = 100):
        self.__window = tkinter.Tk()
        self.__window.title(self.__header)
        self.__window.geometry(str(size_x) + 'x' + str(size_y) + '+50+50')
        self.__window.resizable(False, False)
        self.__window.protocol("WM_DELETE_WINDOW", self.__on_closing)
        self.__canvas = tkinter.Canvas(self.__window)
        self.__canvas.pack(fill='both', expand='True')
        self.__canvas.configure(bg='black')

    def update(self, model: Model):
        self.__canvas.delete("all")

        for pawn in model.get_petri_dish().get_pawns():
            pawn_pos = pawn.get_property('position').get()
            pawn_color = pawn.get_property('color').pawn_true_color(pawn).get() \
                if pawn.has_property('alive') and pawn.get_property('alive').get() else '#a6a6a6'

            self.__canvas.create_rectangle(pawn_pos['x'] * self.__pawn_size,
                                           pawn_pos['y'] * self.__pawn_size,
                                           pawn_pos['x'] * self.__pawn_size + self.__pawn_size,
                                           pawn_pos['y'] * self.__pawn_size + self.__pawn_size,
                                           fill=pawn_color)
        self.__window.update()

    def __clear_canvas(self):
        for old_pawn in self.__canvas.find_all():
            self.__canvas.delete(old_pawn)

    def __on_closing(self):
        self.__controller.stop()
        self.__window.destroy()
