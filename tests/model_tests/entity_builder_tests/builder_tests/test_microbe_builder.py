from model.pawns.behaviors.eating_behaviors.herbivorous import Herbivorous
from model.pawns.behaviors.moving_behaviors.anarchic import Anarchic
from model.pawns.behaviors.reproducing_behaviors.mitosis import Mitosis
from model.pawns.builders.pawn_builder import PawnBuilder
from model.pawns.properties.shape.simple import Simple
from model.petri_dish import PetriDish


# Test fonctionnel de création de pawns avec le constructeur de pawns
def test_build_microbe():
    petri_dish = PetriDish([])

    pawn_builder = PawnBuilder()
    petri_dish.change_builder(pawn_builder)
    petri_dish.make_basic_microbe()

    pawn_builder.set_behavior('eating', Herbivorous())
    pawn_builder.set_behavior('reproducing', Mitosis())
    pawn_builder.set_behavior('moving', Anarchic())

    microbe = pawn_builder.get_pawn()

    assert microbe.get_property('color').get() == '#ff0000'
    assert microbe.get_property('shape').get() == []
    assert microbe.get_property('size').get() == 1
    assert microbe.get_property('energy').get() == 3



