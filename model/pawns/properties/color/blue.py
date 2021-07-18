from model.pawns.properties.color.color_abstract import ColorAbstract


class Blue(ColorAbstract):
    def __init__(self, prop=None):
        super().__init__((0, 0, 255))

    def to_string(self):
        return "blue"

