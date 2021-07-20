import json
import os
import tkinter

from model.db_connectors.dao.dao_petri import DaoPetri
from model.db_connectors.mongodb_db_connector import MongoDbDbConnector
from model.petri_dish import PetriDish
from model.simulation_configuration_parser import SimulationConfigurationParser


class Model:
    def __init__(self):
        self.__load_general_conf()
        self.__simulation_mode = self.__general_conf["simulation_mode"]
        self.__db_connector = MongoDbDbConnector()
        self.__dao_petri = DaoPetri(self.__db_connector)
        self.__tkinter = tkinter.Tk()
        self.__load_petri_dish()

    def __load_petri_dish(self):
        if self.__simulation_mode == 'file':
            self.__load_from_file()
        elif self.__simulation_mode == 'dao':
            self.__load_from_dao()
        else:
            self.__load_from_default_conditions()

    def __load_from_file(self):
        simulation_initial_conf = SimulationConfigurationParser(self.__general_conf["simulation_file"])
        self.__petri_dish = PetriDish(simulation_initial_conf.get_pawns(),
                                      self.__general_conf['simulation_size_x'],
                                      self.__general_conf['simulation_size_y'])

    def __load_from_dao(self):
        self.__simulation_id = self.__general_conf['simulation_id']
        self.__simulation_data = self.__dao_petri.load(self.__simulation_id)
        self.__petri_dish = PetriDish([], self.__simulation_data['size_x'], self.__simulation_data['size_y'])

    def __load_from_default_conditions(self):
        self.__petri_dish = PetriDish([],
                                      self.__general_conf['simulation_size_x'],
                                      self.__general_conf['simulation_size_y'])
        for i in range(self.__general_conf['default_plants_amount']):
            self.__petri_dish.make_immortal_plant()

        for i in range(self.__general_conf['default_microbes_amount']):
            self.__petri_dish.make_basic_microbe()
        for i in range(self.__general_conf['complex_microbes_amount']):
            self.__petri_dish.make_complex_microbe()

    def get_general_conf(self):
        return self.__general_conf

    def get_simulation_mode(self):
        return self.__simulation_mode

    def get_petri_dish(self):
        return self.__petri_dish

    def get_petri_dish_dao(self):
        return self.__dao_petri

    def get_simulation_id(self):
        return self.__simulation_id

    def get_simulation_data(self):
        return self.__simulation_data

    def get_tkinter(self):
        return self.__tkinter

    def __load_general_conf(self):
        with open(os.path.dirname(__file__) + '\\..\\conf\\general_conf.json') as jsonfile:
            self.__general_conf = json.load(jsonfile)
