
from model.pawns.behaviors.behavior_interface import BehaviorInterface
from model.pawns.pawn_interface import PawnInterface
from shared.ipetri_dish import IPetriDish


class Photosynthesis(BehaviorInterface):
    def act(self, petri_dish: IPetriDish, pawn: PawnInterface):
        if pawn.get_property('energy').get() <= pawn.get_property('max_energy').get():
            pawn.get_property('energy').set(pawn.get_property('energy').get() + 1)
            return True
        return False

    def to_string(self):
        return "photosynthesis"



