from model.builder.entity_color.color_interface import ColorInterface
from model.builder.entity_shape.shape_interface import ShapeInterface
from model.microbe.microbe_interface import MicrobeInterface


class Microbe(MicrobeInterface):
    _properties: {}

    def __init__(self, color: ColorInterface, shape: ShapeInterface, size: int):
        self._properties['color'] = color
        self._properties['shape'] = shape
        self._properties['size'] = size

    def birth(self):
        pass

    def death(self):
        pass

    def max_energy(self):
        pass