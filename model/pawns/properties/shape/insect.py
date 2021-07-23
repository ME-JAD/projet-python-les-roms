from model.pawns.properties.shape.shape_abstract import ShapeAbstract


class Insect(ShapeAbstract):
    def __init__(self, prop=None):
        super().__init__([
            (-2, 0),
            (2, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
            (-2, -2),
            (-1, -2),
            (0, -2),
            (1, -2),
            (2, -2),
            (-1, -3),
            (0, -3),
            (1, -3),
            (-2, -4),
            (2, -4)
        ])

    def to_string(self):
        return "forkhead"
