from model.builder.entity_shape.shape_interface import ShapeInterface


class Square(ShapeInterface):
    def get_shape(self):
        return 'square'
