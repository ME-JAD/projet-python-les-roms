from model.db_connectors.dao.dao import DAO
from model.db_connectors.mongodb_db_connector import MongoDbDbConnector
from model.pawns.pawn import Pawn
from model.simulation_configuration_parser import SimulationConfigurationParser
from shared.ipetri_dish import IPetriDish


class DaoPetri(DAO):
    def __init__(self, db_connector: MongoDbDbConnector):
        DAO.__init__(self, db_connector, "petri_dish")

    def save(self, petri_dish: IPetriDish):
        petri_dict = {
            "_id": petri_dish.get_id(),
            "size_x": petri_dish.get_size_x(),
            "size_y": petri_dish.get_size_y(),
            "steps": petri_dish.get_simulation_steps(),
        }

        self.get_collection().insert(petri_dict)

    @staticmethod
    def marshall_step(step: IPetriDish) -> list:
        step_pawns = []
        for pawn in step.get_pawns():
            step_pawns.append(DaoPetri.marshall_pawn(pawn))
        # TODO si la simulation depase 16793598 on cree une autre simu
        return step_pawns

    @staticmethod
    def marshall_pawn(pawn) -> dict:
        pawn_dict = {
            "_id": pawn.get_property('id').get(),
            "properties": dict(),
            "behaviors": dict()
        }

        ignored_props = ['tail', 'parent_pawn', 'shape']
        for prop in pawn.get_properties().items():
            if prop[0] not in ignored_props:
                pawn_dict["properties"][prop[0]] = {prop[1].to_string(): prop[1].get()}
        for behavior in pawn.get_behaviors().items():
            pawn_dict["behaviors"][behavior[0]] = behavior[1].to_string()

        return pawn_dict

    def load(self, simulation_id: int):
        return self.get_collection().find({"_id": simulation_id})[0]

    @staticmethod
    def unmarshall_step(step: dict) -> list:
        step_pawns = []
        for pawn_data in step:
            new_pawn = Pawn()
            SimulationConfigurationParser.parse_properties(new_pawn, pawn_data)
            SimulationConfigurationParser.parse_behaviors(new_pawn, pawn_data)
            step_pawns.append(new_pawn)

        return step_pawns

