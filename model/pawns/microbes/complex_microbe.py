import random

from model.pawns.behaviors.birth_behaviors.spontaneous import Spontaneous
from model.pawns.behaviors.death_behaviors.silent_death import SilentDeath
from model.pawns.behaviors.eating_behaviors.herbivorous import Herbivorous
from model.pawns.behaviors.moving_behaviors.explorer import Explorer
from model.pawns.behaviors.mutation_behaviors.high import High
from model.pawns.behaviors.reproducing_behaviors.assimilation import Assimilation
from model.pawns.pawn_abstract import PawnAbstract
from model.pawns.properties.color.blue import Blue
from model.pawns.properties.direction.direction import Direction
from model.pawns.properties.energy.energy import Energy
from model.pawns.properties.id.id import Id
from model.pawns.properties.lifecycle.lifecycle import Lifecycle
from model.pawns.properties.max_energy.max_energy import MaxEnergy
from model.pawns.properties.shape.forkhead import Forkhead
from model.pawns.properties.size.size import Size as SimpleSize
from model.pawns.properties.max_size.max_size import MaxSize as SimpleMaxSize
from model.pawns.properties.tail.tail import Tail
from model.pawns.properties.taxonomy.microbe import Microbe


class ComplexMicrobe(PawnAbstract):
    def __init__(self, properties=None, behaviors=None):
        super().__init__(properties, behaviors)

        self.set_property('id', Id())
        self.set_property('taxonomy', Microbe())
        self.set_property('size', SimpleSize(5))
        self.set_property('max_size', SimpleMaxSize(5))
        self.set_property('energy', Energy(8))
        self.set_property('max_energy', MaxEnergy(10))
        self.set_property('direction', Direction())
        self.set_property('tail', Tail())

        self.set_property('color', Blue())
        self.set_property('shape', Forkhead())
        self.set_property('lifecycle', Lifecycle("birth;reproducing;eating;moving"))

        self.set_behavior('birth', Spontaneous())
        self.set_behavior('death', SilentDeath())
        self.set_behavior('eating', Herbivorous())
        self.set_behavior('moving', Explorer())
        self.set_behavior('reproducing', Assimilation())
        self.set_behavior('mutation', High())
