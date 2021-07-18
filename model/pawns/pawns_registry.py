class PawnsRegistry:
    def __init__(self):
        self.__pawn_types = [
            "microbes",
            "plants"
        ]

    def get_pawn_types(self):
        return self.__pawn_types
