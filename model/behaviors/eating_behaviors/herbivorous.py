from model.behaviors.eating_behaviors.eating_behavior_interface import EatingBehaviorInterface


class Herbivorous(EatingBehaviorInterface):
    def eat(self):
        return 'eat only passive food'
