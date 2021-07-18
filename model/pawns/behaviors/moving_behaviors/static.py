from model.pawns.behaviors.behavior_interface import BehaviorInterface
from model.pawns.pawn_interface import PawnInterface
from shared.ipetri_dish import IPetriDish


class Static(BehaviorInterface):
    def act(self, petri_dish: IPetriDish, pawn: PawnInterface):
        return True

    def to_string(self):
        return "static"
