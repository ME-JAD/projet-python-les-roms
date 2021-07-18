from model.pawns.pawn_interface import PawnInterface
from model.pawns.properties.property_interface import PropertyInterface


class ParentPawn(PropertyInterface):
    def __init__(self, parent_pawn: PawnInterface = None):
        if parent_pawn is None:
            raise Exception("Tried to create a tail part without parent")
        self.__parent_pawn = parent_pawn

    __parent_pawn: PawnInterface

    def get(self):
        return self.__parent_pawn

    def set(self, parent_pawn):
        self.__parent_pawn = parent_pawn

    def to_string(self):
        return "parent_pawn"
