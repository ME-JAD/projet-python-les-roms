from model.pawns.behaviors.death_behaviors.silent_death import SilentDeath
from model.pawns.pawn_abstract import PawnAbstract
from model.pawns.properties.alive.alive import Alive
from model.pawns.properties.id.id import Id
from model.pawns.properties.parent_pawn.parent_pawn import ParentPawn
from model.pawns.properties.position.position import Position
from model.pawns.properties.taxonomy.microbe import Microbe


class SpecialPartAbstract(PawnAbstract):
    def __init__(self, parent_pawn: ParentPawn):
        super().__init__()

        self.set_property('id', Id())
        self.set_property('taxonomy', Microbe())
        self.set_property('alive', Alive())

        self.set_property('parent_pawn', parent_pawn)
        self.set_property('energy', parent_pawn.get().get_property('energy'))
        self.set_property('max_energy', parent_pawn.get().get_property('max_energy'))
        self.set_property('size', parent_pawn.get().get_property('size'))
        self.set_property('max_size', parent_pawn.get().get_property('max_size'))
        self.set_property('position', Position(parent_pawn.get().get_property('position').get()))

        self.set_behavior('death', SilentDeath())
