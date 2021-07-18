from model.pawns.behaviors.behavior_interface import BehaviorInterface
from model.pawns.pawn_interface import PawnInterface
from shared.ipetri_dish import IPetriDish


class Grow(BehaviorInterface):
    def act(self, petri_dish: IPetriDish, pawn: PawnInterface):
        if pawn.get_property("size").get() < pawn.get_property("max_size").get():
            pawn.get_property("energy").set(pawn.get_property("energy").get() - 1)
            pawn.get_property("size").set(pawn.get_property("size").get() + 1)
            return True
        return False

    def to_string(self):
        return "grow"
