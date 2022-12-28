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
    sideways_movement_to_left,
)


class Move():
    def __init__(self, pawns, turn):
        self._validate(pawns, turn)
        self._pawns = pawns.actual_pawns
        self._turn = turn
        self._pawn_to_hit = FIRST_COLOR if turn == SECOND_COLOR else SECOND_COLOR
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
    def pawn_to_hit(self):
        return self._pawn_to_hit

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
        which = self.which_can_move()
        where = {}

        for indexs in which:
            where_for_pawn = []
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
            where[indexs] = where_for_pawn
        return where

    def which_can_hit(self):
        which = []
        which_withdrawl = self.which_can_hit_by_withdrawl()
        for element in which_withdrawl:
            which.append(element)

        which_approach = self.which_can_hit_by_approach()
        for element in which_approach:
            which.append(element)

        return set(which)

    def which_can_hit_by_approach(self):
        moving_pawns = self.where_can_move()
        which = []

        for pawn in moving_pawns:
            for empty in moving_pawns[pawn]:
                if empty[0] < pawn[0]:
                    if empty[1] < pawn[1] and diagonal_movement_to_left_up(self._pawns, empty[0], empty[1], self._pawn_to_hit):
                        which.append(pawn)
                    if empty[1] == pawn[1] and up_movement(self._pawns, empty[0], empty[1], self._pawn_to_hit):
                        which.append(pawn)
                    if empty[1] > pawn[1] and diagonal_movement_to_right_up(self._pawns, empty[0], empty[1], self._pawn_to_hit):
                        which.append(pawn)
                if empty[0] == pawn[0]:
                    if empty[1] < pawn[1] and sideways_movement_to_left(self._pawns, empty[0], empty[1], self._pawn_to_hit):
                        which.append(pawn)
                    if empty[1] > pawn[1] and sideways_movement_to_right(self._pawns, empty[0], empty[1], self._pawn_to_hit):
                        which.append(pawn)
                if empty[0] > pawn[0]:
                    if empty[1] < pawn[1] and diagonal_movement_to_left_down(self._pawns, empty[0], empty[1], self._pawn_to_hit):
                        which.append(pawn)
                    if empty[1] == pawn[1] and down_movement(self._pawns, empty[0], empty[1], self._pawn_to_hit):
                        which.append(pawn)
                    if empty[1] > pawn[1] and diagonal_movement_to_right_up(self._pawns, empty[0], empty[1], self._pawn_to_hit):
                        which.append(pawn)
        return set(which)

    def which_can_hit_by_withdrawl(self):
        moving_pawns = self.where_can_move()
        which = []

        for pawn in moving_pawns:
            for empty in moving_pawns[pawn]:
                if empty[0] < pawn[0]:
                    if empty[1] < pawn[1] and diagonal_movement_to_right_down(self._pawns, pawn[0], pawn[1], self._pawn_to_hit):
                        which.append(pawn)
                    if empty[1] == pawn[1] and down_movement(self._pawns, pawn[0], pawn[1], self._pawn_to_hit):
                        which.append(pawn)
                    if empty[1] > pawn[1] and diagonal_movement_to_left_down(self._pawns, pawn[0], pawn[1], self._pawn_to_hit):
                        which.append(pawn)
                if empty[0] == pawn[0]:
                    if empty[1] < pawn[1] and sideways_movement_to_right(self._pawns, pawn[0], pawn[1], self._pawn_to_hit):
                        which.append(pawn)
                    if empty[1] > pawn[1] and sideways_movement_to_left(self._pawns, pawn[0], pawn[1], self._pawn_to_hit):
                        which.append(pawn)
                if empty[0] > pawn[0]:
                    if empty[1] < pawn[1] and diagonal_movement_to_right_up(self._pawns, pawn[0], pawn[1], self._pawn_to_hit):
                        which.append(pawn)
                    if empty[1] == pawn[1] and up_movement(self._pawns, pawn[0], pawn[1], self._pawn_to_hit):
                        which.append(pawn)
                    if empty[1] > pawn[1] and diagonal_movement_to_left_up(self._pawns, pawn[0], pawn[1], self._pawn_to_hit):
                        which.append(pawn)
        return set(which)
    
    def where_can_hit(self):
        pass

    def where_can_hit_by_approach(self):
        pass

    def where_can_hit_by_withdrawl(self):
        pass

    def which_hits(self):
        # dic = {[(pawns cords), (empty cords)]: [cords of each pawn that hits]}
        pass

    def possible_combo(self, previous_move_type):
        # sprawdza czy mozna zrobic kombo
        pass

    def move_without_hits(self):
        # jeśli nie ma żadnych bić, to to zachodzi
        pass
