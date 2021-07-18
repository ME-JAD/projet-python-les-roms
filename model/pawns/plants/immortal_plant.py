import random

from model.pawns.behaviors.birth_behaviors.spontaneous import Spontaneous
from model.pawns.behaviors.death_behaviors.silent_death import SilentDeath
from model.pawns.behaviors.eating_behaviors.photosynthesis import Photosynthesis
from model.pawns.behaviors.moving_behaviors.static import Static
from model.pawns.behaviors.reproducing_behaviors.grow import Grow
from model.pawns.pawn_abstract import PawnAbstract
from model.pawns.properties.color.green import Green
from model.pawns.properties.energy.energy import Energy
from model.pawns.properties.id.id import Id
from model.pawns.properties.lifecycle.lifecycle import Lifecycle
from model.pawns.properties.max_energy.max_energy import MaxEnergy
from model.pawns.properties.position.position import Position
from model.pawns.properties.shape.simple import Simple as SimpleShape
from model.pawns.properties.size.size import Size as SimpleSize
from model.pawns.properties.max_size.max_size import MaxSize as SimpleMaxSize
from model.pawns.properties.taxonomy.plant import Plant


class ImmortalPlant(PawnAbstract):
    def __init__(self, properties=None, behaviors=None):
        if behaviors is None:
            behaviors = {}
        if properties is None:
            properties = {}
        self._properties = properties
        self._behaviors = behaviors

        self.set_property('id', Id())
        self.set_property('taxonomy', Plant())
        self.set_property('position', Position({
            'x': random.randint(0, 200),
            'y': random.randint(0, 200),
        }))
        self.set_property('size', SimpleSize())
        self.set_property('max_size', SimpleMaxSize())
        self.set_property('energy', Energy(1000))
        self.set_property('max_energy', MaxEnergy())

        self.set_property('color', Green())
        self.set_property('shape', SimpleShape())
        self.set_property('lifecycle', Lifecycle("birth;reproducing;eating;moving"))

        self.set_behavior('birth', Spontaneous())
        self.set_behavior('death', SilentDeath())
        self.set_behavior('eating', Photosynthesis())
        self.set_behavior('moving', Static())
        self.set_behavior('reproducing', Grow())
