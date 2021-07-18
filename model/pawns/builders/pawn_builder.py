import copy

from model.pawns.builders.pawn_builder_interface import PawnBuilderInterface
from model.pawns.microbes.basic_microbe import BasicMicrobe
from model.pawns.pawn import Pawn
from model.pawns.pawn_interface import PawnInterface


class PawnBuilder(PawnBuilderInterface):
    _pawn: PawnInterface

    def __init__(self):
        self._pawn = BasicMicrobe()

    def set_property(self, property_name, prop):
        self._pawn.set_property(property_name, prop)

    def set_behavior(self, behavior_name, behavior):
        self._pawn.set_behavior(behavior_name, behavior)

    def get_pawn(self):
        return copy.deepcopy(self._pawn)

    def reset(self):
        self._pawn = Pawn()
