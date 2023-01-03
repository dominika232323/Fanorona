from source.board import Board
from source.hit import Hit
from source.move import Move
from source.movement import Movement
from source.pawns import Pawns
from source.turn import Turn
from configuration import (
    FIRST_COLOR,
    SECOND_COLOR,
    EMPTY_COLOR
)


class Combo(Turn):
    def __init__(self, pawns, turn, previous_pawn, previous_empty):
        super().__init__(pawns, turn)
        self._previous_pawn = previous_pawn
        self._previous_empty = previous_empty
        self._previous_move_type = Movement.recognize_move(previous_pawn, previous_empty)
        self.hit = Hit(pawns, turn)
        self.move = Move(pawns, turn)
        self._new_pawn = previous_empty

    @property
    def previous_pawn(self):
        return self._previous_pawn

    @property
    def previous_empty(self):
        return self._previous_empty

    @property
    def previous_move_type(self):
        return self._previous_move_type

    @property
    def new_pawn(self):
        return self._new_pawn

    def possible_combo(self):
        if self._new_pawn not in self.hit.which_can_hit():
            return False
        for empty_space in self.hit.where_can_hit()[self._new_pawn]:
            if Movement.recognize_move(self._new_pawn, empty_space) != self._previous_move_type:
                return True
        return False

    def make_combo(self):
        pass
