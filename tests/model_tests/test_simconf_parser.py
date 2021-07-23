from model.pawns.behaviors.birth_behaviors.spontaneous import Spontaneous
from model.pawns.behaviors.death_behaviors.silent_death import SilentDeath
from model.pawns.behaviors.eating_behaviors.herbivorous import Herbivorous
from model.pawns.behaviors.eating_behaviors.photosynthesis import Photosynthesis
from model.pawns.behaviors.moving_behaviors.anarchic import Anarchic
from model.pawns.behaviors.moving_behaviors.static import Static
from model.pawns.behaviors.mutation_behaviors.low import Low
from model.pawns.behaviors.reproducing_behaviors.grow import Grow
from model.pawns.behaviors.reproducing_behaviors.mitosis import Mitosis
from model.petri_dish import PetriDish
from model.simulation_configuration_parser import SimulationConfigurationParser


# functional test to assert that loading a sim from a file loads the correct microbes
def test_simconf_parser():
    parser = SimulationConfigurationParser('/../conf/simconfs/tests.json')
    assert len(parser.get_pawns()) == 2
    parsed_microbe = parser.get_pawns()[0]

    assert parsed_microbe.get_property('taxonomy').get() == 'microbe'
    assert parsed_microbe.get_property('position').get() == {'x': 20, 'y': 21}
    assert parsed_microbe.get_property('size').get() == 1
    assert parsed_microbe.get_property('max_size').get() == 3
    assert parsed_microbe.get_property('energy').get() == 1
    assert parsed_microbe.get_property('max_energy').get() == 3
    assert parsed_microbe.get_property('shape').get() == []
    assert parsed_microbe.get_property('color').get() == '#ff0000'
    assert parsed_microbe.get_property('lifecycle').get() == ['birth', 'reproducing', 'eating', 'moving']

    assert type(parsed_microbe.get_behavior('birth')) == Spontaneous
    assert type(parsed_microbe.get_behavior('death')) == SilentDeath
    assert type(parsed_microbe.get_behavior('eating')) == Herbivorous
    assert type(parsed_microbe.get_behavior('moving')) == Anarchic
    assert type(parsed_microbe.get_behavior('reproducing')) == Mitosis
    assert type(parsed_microbe.get_behavior('mutation')) == Low

    parsed_plant = parser.get_pawns()[1]

    assert parsed_plant.get_property('taxonomy').get() == 'plant'
    assert parsed_plant.get_property('position').get() == {'x': 20, 'y': 20}
    assert parsed_plant.get_property('size').get() == 1
    assert parsed_plant.get_property('max_size').get() == 3
    assert parsed_plant.get_property('energy').get() == 10000
    assert parsed_plant.get_property('max_energy').get() == 3
    assert parsed_plant.get_property('shape').get() == []
    assert parsed_plant.get_property('color').get() == '#00ff00'
    assert parsed_plant.get_property('lifecycle').get() == ['birth', 'reproducing', 'eating', 'moving']

    assert type(parsed_plant.get_behavior('birth')) == Spontaneous
    assert type(parsed_plant.get_behavior('death')) == SilentDeath
    assert type(parsed_plant.get_behavior('eating')) == Photosynthesis
    assert type(parsed_plant.get_behavior('moving')) == Static
    assert type(parsed_plant.get_behavior('reproducing')) == Grow
    assert type(parsed_plant.get_behavior('mutation')) == Low

    petri_dish = PetriDish([])
    petri_dish.get_pawns().append(parsed_plant)
    petri_dish.get_pawns().append(parsed_microbe)
    for i in range(100):
        parsed_plant.act(petri_dish)
    assert parsed_plant.get_property('energy').get() == 9998
    assert parsed_plant.get_property('alive').get()

    for i in range(2):
        parsed_microbe.act(petri_dish)
    assert parsed_plant.get_property('alive').get()
