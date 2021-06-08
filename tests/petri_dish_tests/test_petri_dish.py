from model.petri_dish import PetriDish


def test_petri_dish_creation():
    petri_dish = PetriDish()

    assert petri_dish.get_size_x() == 200
    assert petri_dish.get_size_y() == 200
