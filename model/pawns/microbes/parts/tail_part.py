from model.pawns.microbes.parts.special_part_abstract import SpecialPartAbstract


class TailPart(SpecialPartAbstract):
    def __init__(self, properties=None, behaviors=None):
        super().__init__(properties, behaviors)
