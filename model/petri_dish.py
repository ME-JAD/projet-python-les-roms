from model.builder.entity_builder_interface import EntityBuilderInterface
from model.builder.entity_color.green import Green
from model.builder.entity_shape.square import Square


class PetriDish:
    _entity_builder: EntityBuilderInterface

    def __init__(self):
        self.size_x = 200
        self.size_y = 200

    def get_size_x(self):
        return self.size_x

    def get_size_y(self):
        return self.size_y

    def change_builder(self, builder: EntityBuilderInterface):
        self._entity_builder = builder

    def make_basic_microbe(self):
        self._entity_builder.set_property('size', 1)
        self._entity_builder.set_property('color', Green())
        self._entity_builder.set_property('shape', Square())






