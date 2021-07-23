from model.pawns.properties.alive.alive import Alive
from model.pawns.properties.color.blue import Blue
from model.pawns.properties.color.green import Green
from model.pawns.properties.color.red import Red
from model.pawns.properties.direction.direction import Direction
from model.pawns.properties.energy.energy import Energy
from model.pawns.properties.id.id import Id
from model.pawns.properties.max_energy.max_energy import MaxEnergy
from model.pawns.properties.lifecycle.lifecycle import Lifecycle
from model.pawns.properties.parent_pawn.parent_pawn import ParentPawn
from model.pawns.properties.position.position import Position
from model.pawns.properties.shape.insect import Insect
from model.pawns.properties.shape.simple import Simple as SimpleShape
from model.pawns.properties.shape.forkhead import Forkhead
from model.pawns.properties.size.size import Size as SimpleSize
from model.pawns.properties.max_size.max_size import MaxSize as SimpleMaxSize
from model.pawns.properties.tail.tail import Tail
from model.pawns.properties.taxonomy.microbe import Microbe
from model.pawns.properties.taxonomy.plant import Plant
from shared.registries.iproperties import IProperties


class PropertiesRegistry(IProperties):
    def __init__(self):
        self.__properties = {
            "id": {
                "id": Id
            },
            "taxonomy": {
                "plant": Plant,
                "microbe": Microbe
            },
            "color": {
                "green": Green,
                "red": Red,
                "blue": Blue
            },
            "position": {
                "position": Position
            },
            "shape": {
                "simple": SimpleShape,
                "forkhead": Forkhead,
                "insect": Insect
            },
            "direction": {
                "direction": Direction
            },
            "size": {
                "size": SimpleSize
            },
            "max_size": {
                "max_size": SimpleMaxSize
            },
            "energy": {
                "energy": Energy
            },
            "max_energy": {
                "max_energy": MaxEnergy
            },
            "alive": {
                "alive": Alive
            },
            "tail": {
                "tail": Tail
            },
            "parent_pawn": {
                "parent_pawn": ParentPawn
            },
            "lifecycle": {
                "lifecycle": Lifecycle
            }
        }

    def get_properties(self):
        return self.__properties
