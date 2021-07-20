import random

from model.db_connectors.dao.dao_petri import DaoPetri
from model.pawns.builders.pawn_builder_interface import PawnBuilderInterface
from model.pawns.microbes.basic_microbe import BasicMicrobe
from model.pawns.microbes.complex_microbe import ComplexMicrobe
from model.pawns.plants.immortal_plant import ImmortalPlant
from model.pawns.properties.id.id import Id
from model.pawns.properties.position.position import Position
from shared.ipetri_dish import IPetriDish


class PetriDish(IPetriDish):
    _pawn_builder: PawnBuilderInterface
    __pawns: list
    __size_x: int
    __size_y: int
    __simulation_steps: dict

    def __init__(self, initial_pawns=None, size_x: int = 200, size_y: int = 200):
        if initial_pawns is None:
            initial_pawns = []
        self.__size_x = size_x
        self.__size_y = size_y
        self.__id = Id().get()
        self.__simulation_step = 0
        self.__simulation_steps = dict()
        self.__pawns = initial_pawns

    def get_id(self):
        return self.__id

    def get_size_x(self):
        return self.__size_x

    def get_size_y(self):
        return self.__size_y

    def get_pawns(self):
        return self.__pawns

    def change_builder(self, builder: PawnBuilderInterface):
        self._pawn_builder = builder

    def make_basic_microbe(self):
        self.get_pawns().append(BasicMicrobe({'position': Position(self.get_random_position())}))

    def make_complex_microbe(self):
        self.get_pawns().append(ComplexMicrobe({'position': Position(self.get_random_position())}))

    def make_immortal_plant(self):
        self.get_pawns().append(ImmortalPlant({'position': Position(self.get_random_position())}))

    def marshall_simulation_step(self, step):
        self.__simulation_steps[str(step)] = DaoPetri.marshall_step(self)
        self.__simulation_step = step

    def get_simulation_step_count(self):
        return self.__simulation_step

    def get_simulation_steps(self):
        return self.__simulation_steps

    def get_random_position(self):
        return {
            'x': random.randint(0, self.__size_x),
            'y': random.randint(0, self.__size_y),
        }

    def get_adj_tiles(self, position):
        return [
            self.get_inbound_pos({'x': position['x'] + 1, 'y': position['y']}),
            self.get_inbound_pos({'x': position['x'], 'y': position['y'] + 1}),
            self.get_inbound_pos({'x': position['x'] - 1, 'y': position['y']}),
            self.get_inbound_pos({'x': position['x'], 'y': position['y'] - 1}),
        ]

    def get_inbound_pos(self, position: dict):
        if position['x'] < 0:
            position['x'] += self.__size_x
        elif position['x'] >= self.__size_x:
            position['x'] -= self.__size_x

        if position['y'] < 0:
            position['y'] += self.__size_y
        elif position['y'] >= self.__size_y:
            position['y'] -= self.__size_y

        return position

    def find_adj_tiles_free(self, position: dict, pawns_to_ignore=None):
        if pawns_to_ignore is None:
            pawns_to_ignore = []
        adj_tiles_pos = self.get_adj_tiles(position)

        for adj_pawn in self.__pawns:
            adj_pawn_pos = adj_pawn.get_property('position').get()
            if adj_pawn_pos in adj_tiles_pos and adj_pawn not in pawns_to_ignore:
                adj_tiles_pos.remove(adj_pawn_pos)
            if len(adj_tiles_pos) == 0:
                break

        return adj_tiles_pos

    def to_string(self):
        for pawn in self.get_pawns():
            print(pawn.to_string())

    def to_visual_representation(self):
        visual_representation = ''
        for x in range(self.__size_x):
            for y in range(self.__size_y):
                no_pawn = True
                for pawn in self.__pawns:
                    if pawn.get_property('position').get() == {'x': x, 'y': y} and pawn.get_property('alive').get():
                        no_pawn = False
                        visual_representation += pawn.get_property('taxonomy').get()[0]
                if no_pawn:
                    visual_representation += '-'
            visual_representation += '\n'

            print(visual_representation)
