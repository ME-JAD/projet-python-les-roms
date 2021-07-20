
from model.pawns.behaviors.behavior_interface import BehaviorInterface
from model.pawns.pawn_interface import PawnInterface
from shared.ipetri_dish import IPetriDish


class Carnivorous(BehaviorInterface):
    def act(self, petri_dish: IPetriDish, pawn: PawnInterface):
        if pawn.get_property('energy').get() < pawn.get_property('max_energy').get():
            adj_tiles_pos = petri_dish.get_adj_tiles(pawn.get_property('position').get())

            pawn_parts_to_ignore = pawn.get_property('shape').get()
            if pawn.has_property('tail'):
                pawn_parts_to_ignore += pawn.get_property('tail').get()
            for adj_pawn in petri_dish.get_pawns():
                found_adj_microbe_alive = adj_pawn not in pawn_parts_to_ignore\
                        and adj_pawn.get_property('position').get() in adj_tiles_pos\
                        and adj_pawn.get_property('taxonomy').get() == "microbe"\
                        and adj_pawn.has_property('alive')\
                        and adj_pawn.get_property('alive').get()

                if found_adj_microbe_alive:
                    adj_pawn.get_property('energy').set(0)
                    if adj_pawn.get_property('energy').get() <= 0:
                        adj_pawn.get_behavior('death').act(petri_dish, adj_pawn)
                    pawn.get_property('energy').set(pawn.get_property('energy').get() + 10)
                    return True

        return False

    def to_string(self):
        return "carnivorous"


