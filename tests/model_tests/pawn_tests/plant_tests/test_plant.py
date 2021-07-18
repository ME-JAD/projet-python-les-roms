import pytest

from model.pawns.plants.immortal_plant import ImmortalPlant
from model.petri_dish import PetriDish


@pytest.fixture
def petri_dish():
    petri_dish = PetriDish([])
    petri_dish.make_immortal_plant()

    return petri_dish


def test_plant_creation(petri_dish):
    plant = petri_dish.get_pawns()[0]
    assert type(plant) == ImmortalPlant


def test_plant_lifecycle(petri_dish):
    plant = petri_dish.get_pawns()[0]

    plant.act(petri_dish)
    assert plant.get_property('alive').get()
    assert plant.get_property('energy').get() == 1000

    for i in range(100):
        plant.act(petri_dish)

    assert plant.get_property('alive').get()
    assert plant.get_property('energy').get() == 998
    # grow twice

