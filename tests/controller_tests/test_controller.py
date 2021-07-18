from controller.controller import Controller


# Test fonctionnel de declanchement de la fin du jeu lorsque tous les microbes sont morts
def test_simulation_state():
    controller = Controller()
    assert not controller.get_simulation_state()

    controller.play_each_pawns_next_action()
    assert controller.get_simulation_state()

    for i in range(15):
        controller.play_each_pawns_next_action()

    assert controller.get_simulation_state()


# Test fonctionnel de création de jeu
def test_controller_instantiation():
    Controller()
