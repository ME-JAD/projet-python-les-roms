import pytest

from model.pawns.pawn_interface import PawnInterface
from model.petri_dish import PetriDish


@pytest.fixture
def petri_dish():
    petri_dish = PetriDish([])
    for i in range(5):
        petri_dish.make_basic_microbe()

    return petri_dish


# functional test to assert that a surrounded microbe is suffocated and die
def test_microbe_suffocation(petri_dish):
    microbe1: PawnInterface = petri_dish.get_pawns()[0]
    microbe1.get_property('position').set((1, 0))
    microbe1.act(petri_dish)

    microbe2: PawnInterface = petri_dish.get_pawns()[1]
    microbe2.get_property('position').set((2, 1))
    microbe2.act(petri_dish)

    microbe3: PawnInterface = petri_dish.get_pawns()[2]
    microbe3.get_property('position').set((1, 2))
    microbe3.act(petri_dish)

    microbe4: PawnInterface = petri_dish.get_pawns()[3]
    microbe4.get_property('position').set((0, 1))
    microbe4.act(petri_dish)

    microbe_suffocated: PawnInterface = petri_dish.get_pawns()[4]
    microbe_suffocated.get_property('position').set((1, 1))
    microbe_suffocated.act(petri_dish)

    assert microbe_suffocated.get_property('alive').get()

    assert [
        microbe2.get_property('position').get(),
        microbe3.get_property('position').get(),
        microbe4.get_property('position').get(),
        microbe1.get_property('position').get(),
    ] == petri_dish.get_adj_tiles(petri_dish, microbe_suffocated.get_property('position').get())

    microbe_suffocated.get_behavior('moving').act(petri_dish, microbe_suffocated)

    assert not microbe_suffocated.get_property('alive').get()
