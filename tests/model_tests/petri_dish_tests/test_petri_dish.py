import pytest

from model.petri_dish import PetriDish


def test_petri_dish_creation():
    petri_dish = PetriDish([])

    assert petri_dish.get_size_x() == 200
    assert petri_dish.get_size_y() == 200


@pytest.fixture
def petri_dish():
    petri_dish = PetriDish([])
    for i in range(3):
        petri_dish.make_basic_microbe()

    return petri_dish


def test_get_inbound_pos(petri_dish):
    microbe1 = petri_dish.get_pawns()[0]
    microbe1.get_property('position').set((0, 0))
    m1_adj_tiles = PetriDish.get_adj_tiles(petri_dish, microbe1.get_property('position').get())
    assert m1_adj_tiles == [
        {'x': 1, 'y': 0}, {'x': 0, 'y': 1},
        {'x': petri_dish.get_size_x() - 1, 'y': 0}, {'x': 0, 'y': petri_dish.get_size_y() - 1},
    ]

    microbe2 = petri_dish.get_pawns()[1]
    microbe2.get_property('position').set((petri_dish.get_size_x() - 1, petri_dish.get_size_y() - 1))
    m2_adj_tiles = PetriDish.get_adj_tiles(petri_dish, microbe2.get_property('position').get())
    assert m2_adj_tiles == [
        {'x': 0, 'y': petri_dish.get_size_y() - 1}, {'x': petri_dish.get_size_x() - 1, 'y': 0},
        {'x': petri_dish.get_size_x() - 2, 'y': petri_dish.get_size_y() - 1}, {'x': petri_dish.get_size_x() - 1, 'y': petri_dish.get_size_y() - 2},
    ]

    microbe3 = petri_dish.get_pawns()[2]
    microbe3.get_property('position').set((1, 1))
    m3_adj_tiles = PetriDish.get_adj_tiles(petri_dish, microbe3.get_property('position').get())
    assert m3_adj_tiles == [
        {'x': 2, 'y': 1}, {'x': 1, 'y': 2},
        {'x': 0, 'y': 1}, {'x': 1, 'y': 0},
    ]

