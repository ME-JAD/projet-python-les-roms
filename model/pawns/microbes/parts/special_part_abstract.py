from model.pawns.behaviors.birth_behaviors.spontaneous import Spontaneous
from model.pawns.behaviors.death_behaviors.silent_death import SilentDeath
from model.pawns.behaviors.moving_behaviors.static import Static
from model.pawns.pawn_abstract import PawnAbstract
from model.pawns.properties.id.id import Id
from model.pawns.properties.lifecycle.lifecycle import Lifecycle
from model.pawns.properties.taxonomy.microbe import Microbe


class SpecialPartAbstract(PawnAbstract):
    def __init__(self, properties=None, behaviors=None):
        super().__init__(properties, behaviors)

        self.set_property('id', Id())
        self.set_property('taxonomy', Microbe())
        self.set_property('lifecycle', Lifecycle("birth;moving"))

        self.set_behavior('birth', Spontaneous())
        self.set_behavior('death', SilentDeath())
        self.set_behavior('moving', Static())
