from model.pawns.properties.shape.shape_abstract import ShapeAbstract


class Simple(ShapeAbstract):
    def __init__(self, prop=None):
        super().__init__([])

    def to_string(self):
        return "simple"

