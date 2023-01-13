from source.configuration import (
    FIRST_COLOR,
    SECOND_COLOR
)
from source.pawns import Pawns


class Turn:
    """
    Class Turn. Contains attributes:
    :param pawns: two-dimensional list of pawns set on the board
    :type pawns: list

    :param turn: holds whose turn it is, first or second player
    :type turn: string
    """
    def __init__(self, pawns, turn):
        """
        Creates an instance of Turn.
        """
        self._validate(pawns, turn)
        self._pawns = pawns.actual_pawns
        self._turn = turn
        self._pawn_to_hit = FIRST_COLOR if turn == SECOND_COLOR else SECOND_COLOR
        self._length = pawns.board_length
        self._width = pawns.board_width

    @staticmethod
    def _validate(pawns, turn):
        """
        :param pawns: two-dimensional list of pawns set on the board
        :param turn: holds whose turn it is, first or second player
        :raise: TypeError if given pawns is not an instance of Pawns
        :raise: ValueError if given turn doesn't belong to the first or second player
        """
        if not isinstance(pawns, Pawns):
            raise TypeError('Invalid type of pawns')
        if turn != FIRST_COLOR and turn != SECOND_COLOR:
            raise ValueError('This type of pawn does not exist.')

    def pawns(self):
        """
        :return: placement of the pawns on the board
        """
        return self._pawns

    def turn(self):
        """
        :return: whose turn is it, first or second player
        """
        return self._turn

    def pawn_to_hit(self):
        """
        :return: type of pawns to capture
        """
        return self._pawn_to_hit

    def length(self):
        """
        :return: board's length
        """
        return self._length

    def width(self):
        """
        :return: board's width
        """
        return self._width
