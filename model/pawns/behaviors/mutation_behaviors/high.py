from model.pawns.behaviors.behavior_interface import BehaviorInterface
from model.pawns.behaviors.mutation_behaviors.possible_mutations import PossibleMutations
from model.pawns.pawn_interface import PawnInterface
from shared.ipetri_dish import IPetriDish


class High(BehaviorInterface):
    def act(self, petri_dish: IPetriDish, pawn: PawnInterface):
        possible_mutations = PossibleMutations()
        possible_mutations.try_mutation(pawn, 10)

    def to_string(self):
        return "high"
