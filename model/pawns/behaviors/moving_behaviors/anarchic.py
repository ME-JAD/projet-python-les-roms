from model.pawns.behaviors.moving_behaviors.anarchic_abstract import AnarchicAbstract


class Anarchic(AnarchicAbstract):
    def __init__(self):
        super().__init__(0.1)

    def to_string(self):
        return "anarchic"
