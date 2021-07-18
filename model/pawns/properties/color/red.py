from model.pawns.properties.color.color_abstract import ColorAbstract


class Red(ColorAbstract):
    def __init__(self, prop=None):
        super().__init__((255, 0, 0))

    def to_string(self):
        return "red"
