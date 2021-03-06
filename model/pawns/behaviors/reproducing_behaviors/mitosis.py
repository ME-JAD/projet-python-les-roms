import copy
import math
import random

from model.pawns.behaviors.behavior_interface import BehaviorInterface
from model.pawns.pawn_interface import PawnInterface
from model.pawns.properties.id.id import Id
from shared.ipetri_dish import IPetriDish


class Mitosis(BehaviorInterface):
    def act(self, petri_dish: IPetriDish, pawn: PawnInterface):
        if pawn.get_property('energy').get() >= 3:
            self.give_birth_to_new_pawn(petri_dish, pawn)
        else:
            return False
        return True

    def give_birth_to_new_pawn(self, petri_dish, parent_pawn):
        petri_dish.find_adj_tiles_free(parent_pawn.get_property('position').get())
        adj_tiles_free = self.__find_adj_tiles_free(petri_dish, parent_pawn.get_property('position').get())
        if len(adj_tiles_free) > 0:
            parent_pawn.get_property('energy').set(math.floor(parent_pawn.get_property('energy').get() / 2))

            new_pawn = copy.deepcopy(parent_pawn)
            new_pawn.set_property('id', Id())
            new_pawn_random_spawn_pos = random.randint(0, len(adj_tiles_free) - 1)
            new_random_inbound_position = petri_dish.get_inbound_pos(adj_tiles_free[new_pawn_random_spawn_pos])
            new_pawn.get_property('position').set((new_random_inbound_position['x'], new_random_inbound_position['y']))
            new_pawn.get_behavior('mutation').act(petri_dish, new_pawn)
            petri_dish.get_pawns().append(new_pawn)

    def __find_adj_tiles_free(self, petri_dish, position):
        adj_tiles_pos = petri_dish.get_adj_tiles(position)

        for tile_position in adj_tiles_pos:
            if not self.__is_tile_free(petri_dish, tile_position):
                adj_tiles_pos.remove(tile_position)

        return adj_tiles_pos

    def __is_tile_free(self, petri_dish, position):
        for adj_pawn in petri_dish.get_pawns():
            if adj_pawn.get_property('position').get() == position:
                return False
        return True

    def to_string(self):
        return "mitosis"
