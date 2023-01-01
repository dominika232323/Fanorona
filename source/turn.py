from configuration import (
    FIRST_COLOR,
    SECOND_COLOR,
    EMPTY_COLOR
)
from source.pawns import Pawns


class Turn:
    def __init__(self, pawns, turn):
        self._validate(pawns, turn)
        self._pawns = pawns.actual_pawns
        self._turn = turn
        self._pawn_to_hit = FIRST_COLOR if turn == SECOND_COLOR else SECOND_COLOR
        self._length = pawns.board_length
        self._width = pawns.board_width

    @staticmethod
    def _validate(pawns, turn):
        if not isinstance(pawns, Pawns):
            raise TypeError
        if turn != FIRST_COLOR and turn != SECOND_COLOR:
            raise ValueError('This type of pawn does not exist.')

    @property
    def pawns(self):
        return self._pawns

    @property
    def turn(self):
        return self._turn

    @property
    def pawn_to_hit(self):
        return self._pawn_to_hit

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width
