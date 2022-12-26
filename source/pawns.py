from source.board import Board
from configuration import (
    FIRST_COLOR,
    SECOND_COLOR,
    EMPTY_COLOR
)


class Pawns():
    def __init__(self, board):
        self._validate(board)
        self._board_length = board.length
        self._board_width = board.width
        self.set_starting_pawns()

    def _validate(self, board):
        if not isinstance(board, Board):
            raise TypeError('Given board is not an instance of class Board')

    @property
    def board_length(self):
        return self._board_length

    @property
    def board_width(self):
        return self._board_width

    def _create_row_one_color(self, color):
        row = []
        for i in range(self._board_length):
            row.append(color)
        return row

    def _append_one_color_half(self, color, where):
        for i in range(self._board_width // 2):
            empty_row = self._create_row_one_color(color)
            where.append(empty_row)

    def _create_starting_middle_row(self):
        row = []
        for i in range(self._board_length // 4):
            row.append(SECOND_COLOR)
            row.append(FIRST_COLOR)
        row.append(EMPTY_COLOR)
        for i in range(self._board_length // 4):
            row.append(SECOND_COLOR)
            row.append(FIRST_COLOR)
        return row

    def set_starting_pawns(self):
        self._actual_pawns = []
        self._append_one_color_half(SECOND_COLOR, self._actual_pawns)
        self._actual_pawns.append(self._create_starting_middle_row())
        self._append_one_color_half(FIRST_COLOR, self._actual_pawns)

    @property
    def actual_pawns(self):
        return self._actual_pawns

    def set_actual_pawns(self, new_pawns):
        for index, (actual, new) in enumerate(zip(self._actual_pawns, new_pawns)):
            self._actual_pawns[index] = new

    def pawns_after_move(self):
        # aktualizuje tablice pionkow po ruchu gracza
        pass

    def check_for_winner(self):
        # sprawdza czy wszystkie pionki jednego z graczy zostaly juz zbite
        pass
