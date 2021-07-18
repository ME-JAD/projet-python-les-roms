from model.pawns.properties.shape.shape_abstract import ShapeAbstract


class Forkhead(ShapeAbstract):
    def __init__(self, prop=None):
        super().__init__([
            (-1, 1),
            (-1, 2),
            (1, 1),
            (1, 2)
        ])

    def to_string(self):
        return "forkhead"
