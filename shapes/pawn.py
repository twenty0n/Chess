from .shape import Shape


class Pawn(Shape):
    @property
    def can_jump(self) -> bool:
        return False

    def moves(self):
        return [(0, 1), (0, 2)]
