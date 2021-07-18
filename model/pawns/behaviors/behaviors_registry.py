from model.pawns.behaviors.birth_behaviors.spontaneous import Spontaneous
from model.pawns.behaviors.death_behaviors.silent_death import SilentDeath
from model.pawns.behaviors.eating_behaviors.carnivorous import Carnivorous
from model.pawns.behaviors.eating_behaviors.herbivorous import Herbivorous
from model.pawns.behaviors.eating_behaviors.necrophagous import Necrophagous
from model.pawns.behaviors.eating_behaviors.photosynthesis import Photosynthesis
from model.pawns.behaviors.moving_behaviors.anarchic import Anarchic
from model.pawns.behaviors.moving_behaviors.explorer import Explorer
from model.pawns.behaviors.moving_behaviors.follow import Follow
from model.pawns.behaviors.moving_behaviors.static import Static
from model.pawns.behaviors.mutation_behaviors.high import High
from model.pawns.behaviors.mutation_behaviors.low import Low
from model.pawns.behaviors.mutation_behaviors.medium import Medium
from model.pawns.behaviors.reproducing_behaviors.assimilation import Assimilation
from model.pawns.behaviors.reproducing_behaviors.grow import Grow
from model.pawns.behaviors.reproducing_behaviors.mitosis import Mitosis
from shared.registries.ibehaviors import IBehaviors


class BehaviorsRegistry(IBehaviors):
    def __init__(self):
        self.__behaviors = {
            "birth": {
                "spontaneous": Spontaneous
            },
            "death": {
                "silent_death": SilentDeath
            },
            "eating": {
                "herbivorous": Herbivorous,
                "photosynthesis": Photosynthesis,
                "carnivorous": Carnivorous,
                "necrophagous": Necrophagous
            },
            "moving": {
                "anarchic": Anarchic,
                "explorer": Explorer,
                "static": Static,
                "follow": Follow
            },
            "reproducing": {
                "mitosis": Mitosis,
                "grow": Grow,
                "assimilation": Assimilation
            },
            "mutation": {
                "high": High,
                "medium": Medium,
                "low": Low
            }
        }

    def get_behaviors(self):
        return self.__behaviors
