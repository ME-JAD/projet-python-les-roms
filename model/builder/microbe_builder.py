from model.behaviors.eating_behaviors.eating_behavior_interface import EatingBehaviorInterface
from model.builder.entity_builder_interface import EntityBuilderInterface
from model.builder.entity_color.color_interface import ColorInterface
from model.builder.entity_shape.shape_interface import ShapeInterface
from model.microbe.microbe_interface import MicrobeInterface


class MicrobeBuilder(EntityBuilderInterface):
    _microbe: MicrobeInterface

    def set_property(self, property_name, property):
        self._microbe.set_property(property_name, property)

    def set_behavior(self, behavior_name, behavior):
        self._eating_behavior = eating_behavior


    def reset(self):
        pass

