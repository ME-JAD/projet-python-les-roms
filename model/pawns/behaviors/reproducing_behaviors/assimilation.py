

from model.pawns.behaviors.behavior_interface import BehaviorInterface
from model.pawns.pawn_interface import PawnInterface
from shared.ipetri_dish import IPetriDish


class Assimilation(BehaviorInterface):
    def act(self, petri_dish: IPetriDish, pawn: PawnInterface):
        adj_pawns = self.__find_adj_tiles_occupied(petri_dish, pawn.get_property('position').get())
        for adj_pawn in adj_pawns:
            pawn.get_property('energy').set(pawn.get_property('energy').get() + adj_pawn.get_property('energy').get())
            pawn.get_property('max_energy').set(pawn.get_property('max_energy').get() + adj_pawn.get_property('max_energy').get())
            pawn.get_property('size').set(pawn.get_property('size').get() + adj_pawn.get_property('size').get())
            pawn.get_property('max_size').set(pawn.get_property('max_size').get() + adj_pawn.get_property('max_size').get())
            petri_dish.get_pawns().remove(adj_pawn)

        return False

    def __find_adj_tiles_occupied(self, petri_dish, position):
        adj_tiles_pos = petri_dish.get_adj_tiles(petri_dish, position)
        adj_pawns = []

        for tile_position in adj_tiles_pos:
            adj_pawn = self.__get_pawn_if_tile_occupied(petri_dish, tile_position)
            if adj_pawn is not None:
                adj_pawns.append(adj_pawn)

        return adj_pawns

    def __get_pawn_if_tile_occupied(self, petri_dish, position):
        for adj_pawn in petri_dish.get_pawns():
            if adj_pawn.get_property('position').get() == position\
                    and adj_pawn.get_property('taxonomy').get() == 'microbe'\
                    and adj_pawn.has_property('alive')\
                    and adj_pawn.get_property('alive').get():
                return adj_pawn
        return None

    def to_string(self):
        return "assimilation"

