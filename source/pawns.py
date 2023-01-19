from source.board import Board
from source.constants import (
    FIRST_COLOR,
    SECOND_COLOR,
    EMPTY_COLOR,
    SECOND_COLOR_WINNER,
    FIRST_COLOR_WINNER
)


class Pawns:
    """
    Class Pawns. Contains attributes:
    :param board: board for a game of Fanorona
    :type board: instance of class Board
    """
    def __init__(self, board):
        """
        Creates an instance of Pawns.
        """
        self._validate(board)
        self._board_length = board.length
        self._board_width = board.width
        self._set_starting_pawns()

    @staticmethod
    def _validate(board):
        """
        :param board: board for a game of Fanorona
        :raise: TypeError if board is not an instance of class Board.
        """
        if not isinstance(board, Board):
            raise TypeError('Given board is not an instance of class Board')

    @property
    def board_length(self):
        """
        :return: board's length
        """
        return self._board_length

    @property
    def board_width(self):
        """
        :return: board's width
        """
        return self._board_width

    def _create_row_one_color(self, color):
        """
        :param color: color of pawns to set up in a row
        :return: list of pawns in a row in the given color
        """
        row = []
        for i in range(self._board_length):
            row.append(color)
        return row

    def _append_one_color_half(self, color, where):
        """
        Appends half of the board with pawns in the given color to given destination.
        :param color: color of pawns to set on the half of the board
        :param where: variable to which function appends the half of the board
        """
        for i in range(self._board_width // 2):
            empty_row = self._create_row_one_color(color)
            where.append(empty_row)

    def _create_starting_middle_row(self):
        """
        :return: list of pawns from the middle row of the board set to start the game
        """
        row = []
        for i in range(self._board_length // 4):
            row.append(SECOND_COLOR)
            row.append(FIRST_COLOR)

        if round(self._board_length / 4) < self._board_length / 4:
            row.append(EMPTY_COLOR)
        else:
            row.append(SECOND_COLOR)
            row.append(EMPTY_COLOR)
            row.append(FIRST_COLOR)

        for i in range(self._board_length // 4):
            row.append(SECOND_COLOR)
            row.append(FIRST_COLOR)
        return row

    def _set_starting_pawns(self):
        """
        Sets pawns for the start of the game of Fanorona.
        """
        self._actual_pawns = []
        self._append_one_color_half(SECOND_COLOR, self._actual_pawns)
        self._actual_pawns.append(self._create_starting_middle_row())
        self._append_one_color_half(FIRST_COLOR, self._actual_pawns)

    @property
    def actual_pawns(self):
        """
        :return: two-dimensional list of pawns' placement on the board
        """
        return self._actual_pawns

    def set_actual_pawns(self, new_pawns):
        """
        Sets new placement of the pawns on the board.
        :param new_pawns: pawns' placement on the board to set
        """
        self._validate_new_pawns(new_pawns)
        for index, (actual, new) in enumerate(zip(self._actual_pawns, new_pawns)):
            self._actual_pawns[index] = new

    def _validate_new_pawns(self, new_pawns):
        """
        :param new_pawns: pawns' placement on the board to set
        :raise: PawnsError if new pawns' placement will not fit the board
        :raise: PawnsError if type of one of the pawns doesn't exist in the game Fanorona
        """
        if len(new_pawns) != self._board_width:
            raise PawnsError('Given pawns will not fit on the board')

        for row in new_pawns:
            if len(row) != self._board_length:
                raise PawnsError('Given pawns will not fit on the board')
            for pawn in row:
                if pawn not in (FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR):
                    raise PawnsError('This type of pawn does not exist')

    def check_for_winner(self):
        """
        :return: True if one of the players has zero pawns on the board
        """
        first_color_count, second_color_count = self.count_pawns()

        return first_color_count == 0 or second_color_count == 0

    def count_pawns(self):
        """
        :return: numbers of players' pawns on the board
        """
        first_color_count = 0
        second_color_count = 0
        for row in self._actual_pawns:
            first_color_count += row.count(FIRST_COLOR)
            second_color_count += row.count(SECOND_COLOR)
        return first_color_count, second_color_count

    def winner_message(self):
        """
        :return: information who won if one of the players has zero pawns
        """
        if not self.check_for_winner():
            return None

        first_color_count, second_color_count = self.count_pawns()
        if first_color_count == 0:
            return SECOND_COLOR_WINNER
        else:
            return FIRST_COLOR_WINNER


class PawnsError(Exception):
    pass
