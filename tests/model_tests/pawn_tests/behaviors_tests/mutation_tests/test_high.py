import pytest

from model.pawns.behaviors.mutation_behaviors.high import High
from model.pawns.pawn_interface import PawnInterface
from model.petri_dish import PetriDish


@pytest.fixture
def petri_dish():
    petri_dish = PetriDish([])
    for i in range(1):
        petri_dish.make_basic_microbe()

    return petri_dish


# functional test to assert mutations are going well
def test_mutation(petri_dish):
    microbe: PawnInterface = petri_dish.get_pawns()[0]
    microbe.set_behavior('mutation', High())
    microbe_string_pre_mutation = microbe.to_string()

    for i in range(1000):
        microbe.get_behavior('mutation').act(petri_dish, microbe)

    microbe_string_post_mutation = microbe.to_string()

    assert microbe_string_pre_mutation != microbe_string_post_mutation
