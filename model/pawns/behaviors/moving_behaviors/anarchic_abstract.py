import random

from model.pawns.behaviors.behavior_interface import BehaviorInterface
from model.pawns.pawn_interface import PawnInterface
from shared.ipetri_dish import IPetriDish


class AnarchicAbstract(BehaviorInterface):
    def __init__(self, decay_rate: float):
        self.__decay_rate = decay_rate

    def act(self, petri_dish: IPetriDish, pawn: PawnInterface):
        adj_tiles_free = petri_dish.find_adj_tiles_free(pawn.get_property('position').get(),
                                                        pawn.get_property('shape').get())

        pawn.get_property('energy').set(pawn.get_property('energy').get() - self.__decay_rate)
        if len(adj_tiles_free) > 0:
            if pawn.has_property('tail'):
                pawn.get_property('tail').update_pawn_tail(petri_dish, pawn)

            self.__update_pawn_position(petri_dish, pawn, adj_tiles_free)

            if pawn.has_property('shape'):
                pawn.get_property('shape').update_pawn_shape(petri_dish, pawn)

        return True

    def __update_pawn_position(self, petri_dish, pawn, adj_tiles_free):
        random_direction = random.randint(0, len(adj_tiles_free) - 1)
        new_random_inbound_position = petri_dish.get_inbound_pos(adj_tiles_free[random_direction])
        pawn.get_property('direction').set(pawn.get_property('direction').get_direction_from_two_positions(
            pawn.get_property('position').get(),
            {'x': new_random_inbound_position['x'], 'y': new_random_inbound_position['y']}))
        pawn.get_property('position').set((new_random_inbound_position['x'], new_random_inbound_position['y']))

    def to_string(self) -> str:
        return "explorer"
