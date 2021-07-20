from model.pawns.pawn_interface import PawnInterface
from shared.ipetri_dish import IPetriDish


class PawnAbstract(PawnInterface):
    _properties: {}
    _behaviors: {}

    def __init__(self, properties=None, behaviors=None):
        self._behaviors = {} if behaviors is None else behaviors
        self._properties = {} if properties is None else properties

    def get_properties(self):
        return self._properties

    def get_behaviors(self):
        return self._behaviors

    def has_property(self, property_name):
        return property_name in self._properties

    def get_property(self, property_name):
        if self.has_property(property_name):
            return self._properties[property_name]
        return None

    def set_property(self, property_name, prop):
        self._properties[property_name] = prop

    def has_behavior(self, behavior_name):
        return behavior_name in self._behaviors

    def get_behavior(self, behavior_name):
        if self.has_behavior(behavior_name):
            return self._behaviors[behavior_name]
        return None

    def set_behavior(self, behavior_name, behavior):
        self._behaviors[behavior_name] = behavior

    def act(self, petri_dish: IPetriDish):
        if self.has_property('lifecycle'):
            iterator = iter(self.get_property('lifecycle').get())
            acted = False
            while not acted:
                acted = self.get_behavior(next(iterator)).act(petri_dish, self)
        self.get_behavior('death').check(petri_dish, self)

    def to_string(self):
        pawn_to_string = ''
        for prop, value in self._properties.items():
            pawn_to_string += prop + ': ' + str(value.get()) + ' '

        pawn_to_string += '\n'

        for behavior, value in self._behaviors.items():
            pawn_to_string += behavior + ' '

        return pawn_to_string
