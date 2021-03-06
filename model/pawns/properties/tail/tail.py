from model.pawns.microbes.parts.tail_part import TailPart
from model.pawns.properties.parent_pawn.parent_pawn import ParentPawn
from model.pawns.properties.property_interface import PropertyInterface


class Tail(PropertyInterface):
    __tail_parts: list = []

    def __init__(self, tail_parts: list = None):
        self.__tail_parts = [] if tail_parts is None or type(tail_parts) == dict else tail_parts

    def get(self) -> list:
        return self.__tail_parts

    def set(self, tail_parts: list):
        self.__tail_parts = tail_parts

    def to_string(self) -> str:
        return "tail"

    def update_pawn_tail(self, petri_dish, pawn):
        pawn_tail = pawn.get_property('tail').get()

        if len(pawn_tail) < pawn.get_property('size').get():
            tail_part_parent = ParentPawn(pawn) if len(pawn_tail) == 0 else ParentPawn(pawn_tail[len(pawn_tail) - 1])
            new_tail_part = TailPart(tail_part_parent)

            pawn_tail.append(new_tail_part)
            petri_dish.get_pawns().append(new_tail_part)
            self.__update_tail_part_color(new_tail_part)
        elif len(pawn_tail) > pawn.get_property('size').get():
            tail_part_to_delete = pawn_tail.pop(len(pawn_tail) - 1)
            petri_dish.get_pawns().remove(tail_part_to_delete)

        for tail_part in reversed(pawn_tail):
            self.__update_tail_part_position(tail_part)

    def __update_tail_part_position(self, tail_part):
        new_tail_part_pos = tail_part.get_property('parent_pawn').get().get_property('position').get()
        tail_part.get_property('position').set((new_tail_part_pos['x'], new_tail_part_pos['y']))

    def __update_tail_part_color(self, tail_part):
        pawn_root_color = self.get_pawn_root().get_property('color').clone()
        pawn_root_color.darken(70)
        pawn_root_color.swap()
        pawn_root_color.swap()
        tail_part.set_property('color', pawn_root_color)

    def get_pawn_root(self):
        return self.__tail_parts[0].get_property('parent_pawn').get()
