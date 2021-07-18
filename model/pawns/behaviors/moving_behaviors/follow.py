import random

from model.pawns.behaviors.behavior_interface import BehaviorInterface
from model.pawns.pawn_interface import PawnInterface
from shared.ipetri_dish import IPetriDish


class Follow(BehaviorInterface):
    def act(self, petri_dish: IPetriDish, pawn: PawnInterface):
        if pawn.has_property("parent_pawn"):
            pawn.get_property("position").set(pawn.get_property('parent_pawn').get().get_property("position").get())
        else:
            pawn.get_behavior("death").act(petri_dish, pawn)

        return True

    def to_string(self):
        return "follow"
