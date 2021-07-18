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
        iterator = iter(self.get_property('lifecycle').get())
        acted = False
        while not acted:
            acted = self.get_behavior(next(iterator)).act(petri_dish, self)
        self.__death_check(petri_dish)

    def __death_check(self, petri_dish):
        if not self.get_property('alive').get():
            self.__delete_pawns_after_countdown(petri_dish)

        if self.get_property('energy').get() <= 0:
            return self.get_behavior('death').act(petri_dish, self)

    def __delete_pawns_after_countdown(self, petri_dish):
        self.get_property('energy').set(self.get_property('energy').get() - 1)
        if self.get_property('energy').get() < 1:
            petri_dish.get_pawns().remove(self)

    def find_adj_tiles_free(self, petri_dish, pawns_to_ignore):
        position = self.get_property('position').get()
        adj_tiles_pos = petri_dish.get_adj_tiles(petri_dish, position)

        for adj_pawn in petri_dish.get_pawns():
            adj_pawn_pos = adj_pawn.get_property('position').get()
            if adj_pawn_pos in adj_tiles_pos and adj_pawn not in pawns_to_ignore:
                adj_tiles_pos.remove(adj_pawn_pos)
            if len(adj_tiles_pos) == 0:
                break

        return adj_tiles_pos

    def to_string(self):
        pawn_to_string = ''
        for prop, value in self._properties.items():
            pawn_to_string += prop + ': ' + str(value.get()) + ' '

        pawn_to_string += '\n'

        for behavior, value in self._behaviors.items():
            pawn_to_string += behavior + ' '

        return pawn_to_string
