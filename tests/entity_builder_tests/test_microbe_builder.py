from model.behaviors.eating_behaviors.herbivorous import Herbivorous
from model.builder.microbe_builder import MicrobeBuilder
from model.petri_dish import PetriDish

def test_build_microbe():
    petri_dish = PetriDish()

    microbe_builder = MicrobeBuilder()
    petri_dish.change_builder(microbe_builder)
    petri_dish.make_basic_microbe()

    microbe_builder.set_behavior('eating', Herbivorous())
    microbe_builder.set_behavior('reproducing', Mitose())
    microbe_builder.set_behavior('moving', FoodSeeking())

    microbe = microbe_builder.get_result()

    assert microbe.getColor() == '#00FF00'
    assert microbe.getShape() == Square.class
    assert microbe.getProperty('size') == 1
    assert microbe.getProperty('') == 1

    # assert microbe.getMaxEnergy() == 1



