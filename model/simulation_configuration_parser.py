import json
import os

from model.pawns.behaviors.behaviors_registry import BehaviorsRegistry
from model.pawns.pawn import Pawn
from model.pawns.pawns_registry import PawnsRegistry
from model.pawns.properties.properties_registry import PropertiesRegistry


class SimulationConfigurationParser:
    __pawns = []

    def __init__(self, file_path):
        self.__pawns = []
        # Opening JSON file

        f = open(os.path.dirname(__file__) + file_path, )

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        # Iterating through the json
        pawns_registry = PawnsRegistry()
        for pawn_type in pawns_registry.get_pawn_types():
            if pawn_type in data['pawns']:
                for pawn in data['pawns'][pawn_type]:
                    self.__pawns.append(self.__parse_pawn(data['pawns'][pawn_type][pawn]))

        # Closing file
        f.close()

    def __parse_pawn(self, pawn_data):
        new_pawn = Pawn()
        self.parse_properties(new_pawn, pawn_data)
        self.parse_behaviors(new_pawn, pawn_data)

        return new_pawn

    @staticmethod
    def parse_properties(pawn, pawn_data):
        properties_registry = PropertiesRegistry()
        properties = properties_registry.get_properties()

        for prop_type, prop in pawn_data['properties'].items():
            for prop_name, prop_value in prop.items():
                property_instance = properties[prop_type][prop_name](prop_value)
                pawn.set_property(prop_type, property_instance)

        return pawn

    @staticmethod
    def parse_behaviors(pawn, pawn_data):
        behaviors_registry = BehaviorsRegistry()
        behaviors = behaviors_registry.get_behaviors()

        for behavior_type, behavior_name in pawn_data['behaviors'].items():
            behavior_instance = behaviors[behavior_type][behavior_name]()
            pawn.set_behavior(behavior_type, behavior_instance)

        return pawn

    def get_pawns(self):
        return self.__pawns
