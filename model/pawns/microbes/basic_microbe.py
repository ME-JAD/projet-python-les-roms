import random

from model.pawns.behaviors.birth_behaviors.spontaneous import Spontaneous
from model.pawns.behaviors.death_behaviors.silent_death import SilentDeath
from model.pawns.behaviors.eating_behaviors.herbivorous import Herbivorous
from model.pawns.behaviors.moving_behaviors.anarchic import Anarchic
from model.pawns.behaviors.reproducing_behaviors.mitosis import Mitosis
from model.pawns.pawn_abstract import PawnAbstract
from model.pawns.properties.color.red import Red
from model.pawns.properties.energy.energy import Energy
from model.pawns.properties.id.id import Id
from model.pawns.properties.lifecycle.lifecycle import Lifecycle
from model.pawns.properties.max_energy.max_energy import MaxEnergy
from model.pawns.properties.position.position import Position
from model.pawns.properties.shape.simple import Simple as SimpleShape
from model.pawns.properties.size.size import Size as SimpleSize
from model.pawns.properties.max_size.max_size import MaxSize as SimpleMaxSize
from model.pawns.properties.taxonomy.microbe import Microbe


class BasicMicrobe(PawnAbstract):
    def __init__(self, properties=None, behaviors=None):
        super().__init__(properties, behaviors)

        self.set_property('id', Id())
        self.set_property('taxonomy', Microbe())
        self.set_property('position', Position({
            'x': random.randint(0, 200),
            'y': random.randint(0, 200),
        }))
        self.set_property('size', SimpleSize())
        self.set_property('max_size', SimpleMaxSize())
        self.set_property('energy', Energy(1))
        self.set_property('max_energy', MaxEnergy())

        self.set_property('color', Red())
        self.set_property('shape', SimpleShape())
        self.set_property('lifecycle', Lifecycle("birth;reproducing;eating;moving"))

        self.set_behavior('birth', Spontaneous())
        self.set_behavior('death', SilentDeath())
        self.set_behavior('eating', Herbivorous())
        self.set_behavior('moving', Anarchic())
        self.set_behavior('reproducing', Mitosis())
