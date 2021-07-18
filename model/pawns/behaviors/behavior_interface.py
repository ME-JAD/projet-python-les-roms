from abc import abstractmethod

from model.pawns.pawn_interface import PawnInterface
from shared.ipetri_dish import IPetriDish


class BehaviorInterface:
    @abstractmethod
    def act(self, petri_dish: IPetriDish, microbe: PawnInterface):
        pass

    @abstractmethod
    def to_string(self):
        pass
