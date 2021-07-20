from model.pawns.behaviors.behavior_interface import BehaviorInterface
from model.pawns.pawn_interface import PawnInterface
from model.pawns.properties.alive.alive import Alive
from shared.ipetri_dish import IPetriDish


class SilentDeath(BehaviorInterface):
    def act(self, petri_dish: IPetriDish, pawn: PawnInterface):
        pawn.set_property('alive', Alive(False))
        return True

    def check(self, petri_dish: IPetriDish, pawn: PawnInterface):
        if not pawn.get_property('alive').get():
            return self.__delete_pawns_after_countdown(petri_dish, pawn)

        self.__kill_microbe_if_suffocated(pawn, petri_dish)

        if pawn.get_property('energy').get() <= 0:
            self.act(petri_dish, pawn)

    def __kill_microbe_if_suffocated(self, pawn, petri_dish):
        if pawn.has_property('shape') \
                and pawn.get_property('taxonomy').get() == 'microbe':
            adj_tiles_free = petri_dish.find_adj_tiles_free(pawn.get_property('position').get(),
                                                            pawn.get_property('shape').get())
            if len(adj_tiles_free) == 0:
                self.act(petri_dish, pawn)

    def __delete_pawns_after_countdown(self, petri_dish: IPetriDish, pawn: PawnInterface):
        pawn.get_property('energy').set(pawn.get_property('energy').get() - 1)
        if pawn.get_property('energy').get() <= 5:
            petri_dish.get_pawns().remove(pawn)

    def to_string(self) -> str:
        return "silent_death"
