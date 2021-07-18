import pytest

from model.pawns.microbes.basic_microbe import BasicMicrobe
from model.petri_dish import PetriDish


@pytest.fixture
def petri_dish():
    petri_dish = PetriDish([])
    petri_dish.make_basic_microbe()

    return petri_dish


def test_microbe_creation(petri_dish):
    microbe = petri_dish.get_pawns()[0]
    assert type(microbe) == BasicMicrobe


def test_microbe_lifecycle(petri_dish):
    microbe = petri_dish.get_pawns()[0]

    microbe.act(petri_dish)
    assert microbe.get_property('alive').get()

    for i in range(100):
        if microbe.get_property('alive').get():
            microbe.act(petri_dish)

    assert not microbe.get_property('alive').get()

