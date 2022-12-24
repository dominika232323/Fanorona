from classes.board import Board


class Pawns():
    def __init__(self, board):
        self._validate(board)
        self._empty_pawns = []
        self._board_length = board.length
        self._board_width = board.width

        for i in range(self._board_width):
            empty_row = self._create_row_one_color('E')
            self._empty_pawns.append(empty_row)

    def _validate(self, board):
        if not isinstance(board, Board):
            raise TypeError('Given board is not an instance of class Board')

    @property
    def empty_pawns(self):
        return self._empty_pawns

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

    def starting_pawns(self):
        # ustawia pionki na początek gry
        pass

    def pawns_after_move(self):
        # aktualizuje tablice pionkow po ruchu gracza
        pass

    def check_for_winner(self):
        # sprawdza czy wszystkie pionki jednego z graczy zostaly juz zbite
        pass
