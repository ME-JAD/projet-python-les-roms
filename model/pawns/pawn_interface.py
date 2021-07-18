from abc import abstractmethod

from shared.ipetri_dish import IPetriDish


class PawnInterface:
    @abstractmethod
    def has_property(self, property_name):
        pass

    @abstractmethod
    def get_properties(self) -> dict:
        pass

    @abstractmethod
    def get_behaviors(self) -> dict:
        pass

    @abstractmethod
    def get_property(self, property_name):
        pass

    @abstractmethod
    def set_property(self, property_name, prop):
        pass

    @abstractmethod
    def has_behavior(self, behavior_name):
        pass

    @abstractmethod
    def get_behavior(self, behavior_name):
        pass

    @abstractmethod
    def set_behavior(self, behavior_name, behavior):
        pass

    @abstractmethod
    def act(self, petri_dish: IPetriDish):
        pass

    @abstractmethod
    def to_string(self):
        pass

    @abstractmethod
    def find_adj_tiles_free(self, petri_dish, pawns_to_ignore):
        pass
