from model.pawns.microbes.parts.special_part_abstract import SpecialPartAbstract
from model.pawns.properties.parent_pawn.parent_pawn import ParentPawn


class TailPart(SpecialPartAbstract):
    def __init__(self, parent_pawn: ParentPawn):
        super().__init__(parent_pawn)
