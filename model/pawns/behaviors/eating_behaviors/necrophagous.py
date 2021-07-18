from model.pawns.behaviors.behavior_interface import BehaviorInterface
from model.pawns.pawn_interface import PawnInterface
from shared.ipetri_dish import IPetriDish


class Necrophagous(BehaviorInterface):
    def act(self, petri_dish: IPetriDish, pawn: PawnInterface):
        if pawn.get_property('energy').get() < pawn.get_property('max_energy').get():
            pawn_pos = pawn.get_property('position').get()
            adj_tiles_pos = petri_dish.get_adj_tiles(petri_dish, pawn_pos)

            for adj_pawn in petri_dish.get_pawns():
                found_adj_pawn_dead = adj_pawn.get_property('position').get() in adj_tiles_pos \
                        and adj_pawn.get_property('taxonomy').get() == "plant"\
                        and adj_pawn.has_property('alive')\
                        and not adj_pawn.get_property('alive').get()

                if found_adj_pawn_dead:
                    adj_pawn.get_property('energy').set(adj_pawn.get_property('energy').get() - 1)
                    if adj_pawn.get_property('energy').get() <= 0:
                        adj_pawn.get_behavior('death').act(petri_dish, adj_pawn)
                    pawn.get_property('energy').set(pawn.get_property('energy').get() + 1)
                    return True

        return False

    def to_string(self):
        return "necrophagous"


