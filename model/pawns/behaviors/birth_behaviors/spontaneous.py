from model.pawns.behaviors.behavior_interface import BehaviorInterface
from model.pawns.pawn_interface import PawnInterface
from model.pawns.properties.alive.alive import Alive
from shared.ipetri_dish import IPetriDish


class Spontaneous(BehaviorInterface):
    def act(self, petri_dish: IPetriDish, pawn: PawnInterface):
        if pawn.has_property('alive'):
            return False
        pawn.set_property('alive', Alive())
        return True

    def to_string(self):
        return "spontaneous"
