from classes.pawns import Pawns
from configuration import (
    FIRST_COLOR,
    SECOND_COLOR,
    EMPTY_COLOR
)


class Move():
    def __init__(self, pawns):
        self._validate(pawns)
        self._pawns = pawns.actual_pawns

    def _validate(self, pawns):
        if not isinstance(pawns, Pawns):
            raise TypeError

    @property
    def pawns(self):
        return self._pawns

    def _if_can_move_to_right_down(self, index_row, index):
        if self._pawns[index_row+1][index] == EMPTY_COLOR or self._pawns[index_row+1][index+1] == EMPTY_COLOR or self._pawns[index_row][index+1] == EMPTY_COLOR:
            return True
        return False

    def _if_can_move_to_left_down(self, index_row, index):
        if self._pawns[index_row+1][index] == EMPTY_COLOR or self._pawns[index_row+1][index-1] == EMPTY_COLOR or self._pawns[index_row][index-1] == EMPTY_COLOR:
            return True
        return False

    def _if_can_move_to_right_up(self, index_row, index):
        if self._pawns[index_row-1][index] == EMPTY_COLOR or self._pawns[index_row-1][index+1] == EMPTY_COLOR or self._pawns[index_row][index+1] == EMPTY_COLOR:
            return True
        return False

    def _if_can_move_to_left_up(self, index_row, index):
        if self._pawns[index_row-1][index] == EMPTY_COLOR or self._pawns[index_row-1][index-1] == EMPTY_COLOR or self._pawns[index_row][index-1] == EMPTY_COLOR:
            return True
        return False

    def which_can_move(self, turn):
        self._validate_turn(turn)
        result_pawns = []
        for index_row, row in enumerate(self._pawns):
            for index, pawn in enumerate(row):
                if pawn == turn:
                    if index_row == 0:
                        if index == 0:
                            if self._if_can_move_to_right_down(index_row, index):
                                result_pawns.append((index_row, index))
                        elif index == len(row)-1:
                            if self._if_can_move_to_left_down(index_row, index):
                                result_pawns.append((index_row, index))
                        elif self._if_can_move_to_left_down(index_row, index) or self._if_can_move_to_right_down(index_row, index):
                            result_pawns.append((index_row, index))
                    elif index_row == len(self._pawns)-1:
                        if index == 0:
                            if self._if_can_move_to_right_up(index_row, index):
                                result_pawns.append((index_row, index))
                        elif index == len(row)-1:
                            if self._if_can_move_to_left_up(index_row, index):
                                result_pawns.append((index_row, index))
                        elif self._if_can_move_to_left_up(index_row, index) or self._if_can_move_to_right_up(index_row, index):
                            result_pawns.append((index_row, index))
                    else:
                        if index == 0:
                            if self._if_can_move_to_right_up(index_row, index) or self._if_can_move_to_right_down(index_row, index):
                                result_pawns.append((index_row, index))
                        elif index == len(row)-1:
                            if self._if_can_move_to_left_up(index_row, index) or self._if_can_move_to_left_down(index_row, index):
                                result_pawns.append((index_row, index))
                        elif (self._if_can_move_to_right_down(index_row, index) or self._if_can_move_to_left_down(index_row, index)
                              or self._if_can_move_to_right_up(index_row, index) or self._if_can_move_to_left_up(index_row, index)):
                            result_pawns.append((index_row, index))
        return result_pawns

    def _validate_turn(self, turn):
        if turn != FIRST_COLOR and turn != SECOND_COLOR:
            raise ValueError('This type of pawn does not exist.')

    def which_can_hit(self, turn):
        # sprawdza, ktore pionki z tych co mogą się ruszyć mają bicie
        pass

    def possible_combo(self, previous_move_type):
        # sprawdza czy mozna zrobic kombo
        pass

    def move_without_hits(self):
        # jeśli nie ma żadnych bić, to to zachodzi
        pass
