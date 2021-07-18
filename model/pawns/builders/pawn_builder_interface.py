from abc import abstractmethod


class PawnBuilderInterface:
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_property(self, property_name, prop):
        pass

    @abstractmethod
    def set_behavior(self, property_name, behavior):
        pass

    @abstractmethod
    def get_pawn(self):
        pass
