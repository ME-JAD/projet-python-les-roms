import time

from model.model import Model
from view.view import View
from shared.icontroller import IController


class Controller(IController):
    def __init__(self):
        self.__model = Model()
        self.__view = View(self,
                           self.__model.get_tkinter(),
                           self.__model.get_general_conf())
        self.__stop = False

    def start(self):
        simulation_mode = self.__model.get_simulation_mode()
        if simulation_mode == 'file' or simulation_mode == 'default':
            self.play_simulation_from_initial_conditions()
        elif simulation_mode == 'dao':
            self.replay_simulation()

    def play_simulation_from_initial_conditions(self):
        simulation_playing = True
        self.__model.get_petri_dish().marshall_simulation_step(0)
        while simulation_playing and not self.__stop:
            self.play_each_pawns_next_action()
            self.update_view()

            time.sleep(self.__model.get_general_conf()["simulation_speed"])
            # simulation_playing = self.get_simulation_state()

            self.__model.get_petri_dish().marshall_simulation_step(
                self.__model.get_petri_dish().get_simulation_step_count() + 1)

            print('pawn count: ' + str(len(self.__model.get_petri_dish().get_pawns())))
        self.save_state_in_bdd()

    def replay_simulation(self):
        petri_dish_dao = self.__model.get_petri_dish_dao()
        simulation_data = self.__model.get_simulation_data()
        simulation_steps = simulation_data["steps"].items()
        for step in simulation_steps:
            self.__model.get_petri_dish().get_pawns().clear()
            unmarshalled_step = petri_dish_dao.unmarshall_step(step[1])
            self.__model.get_petri_dish().get_pawns().extend(unmarshalled_step)
            self.update_view()

            time.sleep(self.__model.get_general_conf()["simulation_speed"])

            if self.__stop:
                break

    def stop(self):
        self.__stop = True

    def play_each_pawns_next_action(self):
        for pawn in self.__model.get_petri_dish().get_pawns():
            pawn.act(self.__model.get_petri_dish())

    def update_view(self):
        self.__view.update(self.__model)

    def save_state_in_bdd(self):
        self.__model.get_petri_dish_dao().save(self.__model.get_petri_dish())

    def get_simulation_state(self):
        for pawn in self.__model.get_petri_dish().get_pawns():
            if pawn.has_property('alive'):
                if pawn.get_property('alive').get() and pawn.get_property('taxonomy').get() == 'microbe':
                    return True
        return False
