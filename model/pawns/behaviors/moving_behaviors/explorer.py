from model.pawns.behaviors.moving_behaviors.anarchic_abstract import AnarchicAbstract


class Explorer(AnarchicAbstract):
    def __init__(self):
        super().__init__(0.01)

    def to_string(self) -> str:
        return "explorer"
