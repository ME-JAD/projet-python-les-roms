from abc import ABC, abstractmethod

from model.pawns.builders.pawn_builder_interface import PawnBuilderInterface


class IPetriDish:
    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def get_size_x(self):
        pass

    @abstractmethod
    def get_size_y(self):
        pass

    @abstractmethod
    def get_pawns(self):
        pass

    @abstractmethod
    def get_simulation_steps(self):
        pass

    @abstractmethod
    def change_builder(self, builder: PawnBuilderInterface):
        pass

    @abstractmethod
    def get_adj_tiles(self, position: dict):
        pass

    @abstractmethod
    def get_inbound_pos(self, position: dict):
        pass

    @abstractmethod
    def find_adj_tiles_free(self, position: dict, pawns_to_ignore: list):
        pass
