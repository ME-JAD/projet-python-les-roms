from model.pawns.microbes.parts.special_part_abstract import SpecialPartAbstract


class HeadPart(SpecialPartAbstract):
    def __init__(self, properties=None, behaviors=None):
        super().__init__(properties, behaviors)
