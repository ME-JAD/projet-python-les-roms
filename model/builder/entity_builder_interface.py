from abc import abstractmethod

from model.builder.entity_color.color_interface import ColorInterface
from model.builder.entity_shape.shape_interface import ShapeInterface


class EntityBuilderInterface:
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_property(self, property_name, property):
        pass
