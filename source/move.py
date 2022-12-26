from source.pawns import Pawns
from configuration import (
    FIRST_COLOR,
    SECOND_COLOR,
    EMPTY_COLOR
)
from source.move_types import (
    diagonal_movement_to_left_up,
    up_movement,
    diagonal_movement_to_right_up,
    sideways_movement_to_right,
    diagonal_movement_to_right_down,
    down_movement,
    diagonal_movement_to_left_down,
    sideways_movement_to_left
)


class Move():
    def __init__(self, pawns, turn):
        self._validate(pawns, turn)
        self._pawns = pawns.actual_pawns
        self._turn = turn
        self._length = pawns.board_length
        self._width = pawns.board_width

    def _validate(self, pawns, turn):
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
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    def which_can_move(self):
        """
        Returns a list of co-ordinates of pawns that can move, because they have an empty space near them.
        """
        result_pawns = []
        for index_row, row in enumerate(self._pawns):
            for index, pawn in enumerate(row):
                if pawn == self._turn:
                    if diagonal_movement_to_left_up(self._pawns, index_row, index, EMPTY_COLOR):
                        result_pawns.append((index_row, index))
                    elif up_movement(self._pawns, index_row, index, EMPTY_COLOR):
                        result_pawns.append((index_row, index))
                    elif diagonal_movement_to_right_up(self._pawns, index_row, index, EMPTY_COLOR):
                        result_pawns.append((index_row, index))
                    elif sideways_movement_to_right(self._pawns, index_row, index, EMPTY_COLOR):
                        result_pawns.append((index_row, index))
                    elif diagonal_movement_to_right_down(self._pawns, index_row, index, EMPTY_COLOR):
                        result_pawns.append((index_row, index))
                    elif down_movement(self._pawns, index_row, index, EMPTY_COLOR):
                        result_pawns.append((index_row, index))
                    elif diagonal_movement_to_left_down(self._pawns, index_row, index, EMPTY_COLOR):
                        result_pawns.append((index_row, index))
                    elif sideways_movement_to_left(self._pawns, index_row, index, EMPTY_COLOR):
                        result_pawns.append((index_row, index))
        return result_pawns

    def where_can_move(self):
        """
        Returns a list of lists where the first element is co-ordinates of pawn that can move and
        other elements are co-ordinates of empty spaces around it.
        """
        which = self.which_can_move()
        where = []

        for indexs in which:
            where_for_pawn = []
            where_for_pawn.append(indexs)
            if diagonal_movement_to_left_up(self._pawns, indexs[0], indexs[1], EMPTY_COLOR):
                where_for_pawn.append((indexs[0]-1, indexs[1]-1))
            if up_movement(self._pawns, indexs[0], indexs[1], EMPTY_COLOR):
                where_for_pawn.append((indexs[0]-1, indexs[1]))
            if diagonal_movement_to_right_up(self._pawns, indexs[0], indexs[1], EMPTY_COLOR):
                where_for_pawn.append((indexs[0]-1, indexs[1]+1))
            if sideways_movement_to_right(self._pawns, indexs[0], indexs[1], EMPTY_COLOR):
                where_for_pawn.append((indexs[0], indexs[1]+1))
            if diagonal_movement_to_right_down(self._pawns, indexs[0], indexs[1], EMPTY_COLOR):
                where_for_pawn.append((indexs[0]+1, indexs[1]+1))
            if down_movement(self._pawns, indexs[0], indexs[1], EMPTY_COLOR):
                where_for_pawn.append((indexs[0]+1, indexs[1]))
            if diagonal_movement_to_left_down(self._pawns, indexs[0], indexs[1], EMPTY_COLOR):
                where_for_pawn.append((indexs[0]+1, indexs[1]-1))
            if sideways_movement_to_left(self._pawns, indexs[0], indexs[1], EMPTY_COLOR):
                where_for_pawn.append((indexs[0], indexs[1]-1))
            where.append(where_for_pawn)
        return where

    def which_can_hit(self):
        # sprawdza, ktore pionki z tych co mogą się ruszyć mają bicie
        pass

    def possible_combo(self, previous_move_type):
        # sprawdza czy mozna zrobic kombo
        pass

    def move_without_hits(self):
        # jeśli nie ma żadnych bić, to to zachodzi
        pass
