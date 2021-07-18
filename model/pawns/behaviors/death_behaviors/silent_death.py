from model.pawns.behaviors.behavior_interface import BehaviorInterface
from model.pawns.pawn_interface import PawnInterface
from model.pawns.properties.alive.alive import Alive
from shared.ipetri_dish import IPetriDish


class SilentDeath(BehaviorInterface):
    def act(self, petri_dish: IPetriDish, pawn: PawnInterface):
        pawn.set_property('alive', Alive(False))
        return True

    def to_string(self):
        return "silent_death"
