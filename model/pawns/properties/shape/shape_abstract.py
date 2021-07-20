from model.pawns.microbes.parts.head_part import HeadPart
from model.pawns.properties.parent_pawn.parent_pawn import ParentPawn
from model.pawns.properties.position.position import Position
from model.pawns.properties.property_interface import PropertyInterface


class ShapeAbstract(PropertyInterface):
    __head_parts_positions = []
    __rotated_head_parts_positions = []
    __head_parts = []

    def __init__(self, head_parts_positions: list = None):
        self.__head_parts_positions = head_parts_positions
        self.__head_parts = []

    def get(self):
        return self.__head_parts

    def set(self, head_parts: list):
        self.__head_parts = head_parts

    def get_relative_positions(self) -> list:
        return self.__head_parts_positions

    def set_relative_positions(self, relative_positions: list):
        self.__head_parts_positions = relative_positions

    def to_string(self):
        return "shape_abstract"

    def update_pawn_shape(self, petri_dish, pawn):
        head_pawn_direction = pawn.get_property('direction').get()
        self.__rotated_head_parts_positions = self.__head_parts_positions.copy()
        for head_part_index in range(head_pawn_direction):
            self.__rotate_right_relative_positions()

        if len(self.__head_parts_positions) > len(self.__head_parts):
            self.__initialize_head_parts(petri_dish, pawn)

        for head_part_index in range(len(self.__head_parts_positions)):
            self._update_head_part_position(head_part_index)

    def _update_head_part_position(self, head_part_index):
        head_part_position = self.__rotated_head_parts_positions[head_part_index]
        parent_pawn = self.__head_parts[head_part_index].get_property('parent_pawn').get()

        self.__head_parts[head_part_index].get_property('position').set((
            parent_pawn.get_property('position').get()['x'] + head_part_position[0],
            parent_pawn.get_property('position').get()['y'] + head_part_position[1]
        ))
        self.__update_head_part_color(head_part_index)

    def __update_head_part_color(self, head_part_index):
        head_part_parent_color = self.__head_parts[head_part_index].get_property('parent_pawn').get().get_property('color').clone()
        head_part_parent_color.darken(70)
        head_part_parent_color.swap()
        self.__head_parts[head_part_index].set_property('color', head_part_parent_color)

    def __initialize_head_parts(self, petri_dish, pawn):
        for head_part_position in self.__head_parts_positions:
            head_part_parent = ParentPawn(pawn)
            new_head_part = HeadPart(head_part_parent)

            new_head_part.set_property('position', Position({
                'x': pawn.get_property('position').get()['x'] + head_part_position[0],
                'y': pawn.get_property('position').get()['y'] + head_part_position[1]
            }))

            self.__head_parts.append(new_head_part)
            petri_dish.get_pawns().append(new_head_part)

    # y = - x
    # x = y
    def __rotate_right_relative_positions(self):
        head_parts_to_rotate = self.__rotated_head_parts_positions
        for i in range(len(head_parts_to_rotate)):
            y = - head_parts_to_rotate[i][0]
            x = head_parts_to_rotate[i][1]
            head_parts_to_rotate[i] = (x, y)
