import random

from model.pawns.behaviors.eating_behaviors.carnivorous import Carnivorous
from model.pawns.behaviors.eating_behaviors.herbivorous import Herbivorous
from model.pawns.behaviors.eating_behaviors.necrophagous import Necrophagous
from model.pawns.behaviors.moving_behaviors.anarchic import Anarchic
from model.pawns.behaviors.moving_behaviors.explorer import Explorer
from model.pawns.behaviors.moving_behaviors.static import Static
from model.pawns.behaviors.reproducing_behaviors.assimilation import Assimilation
from model.pawns.behaviors.reproducing_behaviors.mitosis import Mitosis
from model.pawns.pawn_interface import PawnInterface
from model.pawns.properties.color.blue import Blue
from model.pawns.properties.color.green import Green
from model.pawns.properties.color.red import Red
from model.pawns.properties.shape.forkhead import Forkhead
from model.pawns.properties.tail.tail import Tail


class PossibleMutations:
    __properties_mutations: dict
    __behaviors_mutations: dict

    def __init__(self):
        self.__property_mutations = {
            "color": {
                "red": Red,
                "green": Green,
                "blue": Blue
            },
            "tail": {
                "tail": Tail
            },
            "shape": {
                "forkhead": Forkhead
            }
        }

        self.__behavior_mutations = {
            "eating": {
                "carnivorous": Carnivorous,
                "herbivorous": Herbivorous,
                "necrophagous": Necrophagous
            },
            "moving": {
                "anarchic": Anarchic,
                "explorer": Explorer,
                "static": Static
            },
            "reproducing": {
                "mitosis": Mitosis,
                "assimilation": Assimilation
            }
        }

    def get_possible_behavior_mutations(self):
        return self.__behavior_mutations

    def get_possible_property_mutations(self):
        return self.__property_mutations

    def try_mutation(self, pawn: PawnInterface, chances: int):
        if random.randint(0, chances) == 0:
            if random.randint(1, 2) == 1:
                random_property_type = random.choice(list(self.__property_mutations.keys()))
                random_property = random.choice(list(self.__property_mutations[random_property_type].values()))
                pawn.set_property(random_property_type, random_property())
            else:
                random_behavior_type = random.choice(list(self.__behavior_mutations.keys()))
                random_behavior = random.choice(list(self.__behavior_mutations[random_behavior_type].values()))
                pawn.set_behavior(random_behavior_type, random_behavior())

