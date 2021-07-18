import random

from model.pawns.behaviors.behavior_interface import BehaviorInterface
from model.pawns.pawn_interface import PawnInterface
from model.pawns.properties.tail.tail import Tail
from shared.ipetri_dish import IPetriDish


class Anarchic(BehaviorInterface):
    def act(self, petri_dish: IPetriDish, pawn: PawnInterface):
        adj_tiles_free = pawn.find_adj_tiles_free(petri_dish, pawn.get_property('shape').get())

        if len(adj_tiles_free) == 0:
            return pawn.get_behavior('death').act(petri_dish, pawn)

        pawn.get_property('energy').set(pawn.get_property('energy').get() - 0.1)
        random_direction = random.randint(0, len(adj_tiles_free) - 1)
        pawn.get_property('position').set(
            (adj_tiles_free[random_direction]['x'], adj_tiles_free[random_direction]['y']))

        if pawn.has_property('tail'):
            Tail.update_pawn_tail(petri_dish, pawn)

        return True

    def to_string(self):
        return "anarchic"
