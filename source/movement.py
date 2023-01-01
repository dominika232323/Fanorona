from configuration import (
    MOVEMENT_UP,
    MOVEMENT_DIAGONAL_RIGHT_UP,
    MOVEMENT_SIDEWAYS_RIGHT,
    MOVEMENT_DIAGONAL_RIGHT_DOWN,
    MOVEMENT_DOWN,
    MOVEMENT_DIAGONAL_LEFT_DOWN,
    MOVEMENT_SIDEWAYS_LEFT,
    MOVEMENT_DIAGONAL_LEFT_UP,
    FIRST_COLOR,
    SECOND_COLOR,
    EMPTY_COLOR
)
from source.pawns import PawnsError


class Movement:
    @staticmethod
    def check_for_max_to_left_or_up(index):
        if index == 0:
            return True
        return False

    @staticmethod
    def check_for_max_to_right_or_down(index, length):
        if index == length-1:
            return True
        return False

    @staticmethod
    def check_for_diagonal_connections(row_index, index):
        if row_index % 2 == 0 and index % 2 == 1:
            return False
        if row_index % 2 == 1 and index % 2 == 0:
            return False
        return True

    @staticmethod
    def validate_wanted_pawn(pawn):
        if pawn not in (FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR):
            raise PawnsError('This type of pawn does not exist')

    def diagonal_movement_to_left_up(self, pawns, row_index, index, wanted_pawn):
        self.validate_wanted_pawn(wanted_pawn)
        if self.check_for_max_to_left_or_up(row_index):
            return False
        if self.check_for_max_to_left_or_up(index):
            return False
        if not self.check_for_diagonal_connections(row_index, index):
            return False
        if pawns[row_index-1][index-1] == wanted_pawn:
            return True
        return False

    def up_movement(self, pawns, row_index, index, wanted_pawn):
        self.validate_wanted_pawn(wanted_pawn)
        if self.check_for_max_to_left_or_up(row_index):
            return False
        if pawns[row_index-1][index] == wanted_pawn:
            return True
        return False

    def diagonal_movement_to_right_up(self, pawns, row_index, index, wanted_pawn):
        self.validate_wanted_pawn(wanted_pawn)
        if self.check_for_max_to_left_or_up(row_index):
            return False
        if self.check_for_max_to_right_or_down(index, len(pawns[0])):
            return False
        if not self.check_for_diagonal_connections(row_index, index):
            return False
        if pawns[row_index-1][index+1] == wanted_pawn:
            return True
        return False

    def sideways_movement_to_right(self, pawns, row_index, index, wanted_pawn):
        self.validate_wanted_pawn(wanted_pawn)
        if self.check_for_max_to_right_or_down(index, len(pawns[0])):
            return False
        if pawns[row_index][index+1] == wanted_pawn:
            return True
        return False

    def diagonal_movement_to_right_down(self, pawns, row_index, index, wanted_pawn):
        self.validate_wanted_pawn(wanted_pawn)
        if self.check_for_max_to_right_or_down(row_index, len(pawns)):
            return False
        if self.check_for_max_to_right_or_down(index, len(pawns[0])):
            return False
        if not self.check_for_diagonal_connections(row_index, index):
            return False
        if pawns[row_index+1][index+1] == wanted_pawn:
            return True
        return False

    def down_movement(self, pawns, row_index, index, wanted_pawn):
        self.validate_wanted_pawn(wanted_pawn)
        if self.check_for_max_to_right_or_down(row_index, len(pawns)):
            return False
        if pawns[row_index+1][index] == wanted_pawn:
            return True
        return False

    def diagonal_movement_to_left_down(self, pawns, row_index, index, wanted_pawn):
        self.validate_wanted_pawn(wanted_pawn)
        if self.check_for_max_to_right_or_down(row_index, len(pawns)):
            return False
        if self.check_for_max_to_left_or_up(index):
            return False
        if not self.check_for_diagonal_connections(row_index, index):
            return False
        if pawns[row_index+1][index-1] == wanted_pawn:
            return True
        return False

    def sideways_movement_to_left(self, pawns, row_index, index, wanted_pawn):
        self.validate_wanted_pawn(wanted_pawn)
        if self.check_for_max_to_left_or_up(index):
            return False
        if pawns[row_index][index-1] == wanted_pawn:
            return True
        return False

    @staticmethod
    def recognize_move(pawn, where_moves):
        if where_moves[0] < pawn[0]:
            if where_moves[1] < pawn[1]:
                return MOVEMENT_DIAGONAL_LEFT_UP
            if where_moves[1] == pawn[1]:
                return MOVEMENT_UP
            if where_moves[1] > pawn[1]:
                return MOVEMENT_DIAGONAL_RIGHT_UP
        if where_moves[0] == pawn[0]:
            if where_moves[1] < pawn[1]:
                return MOVEMENT_SIDEWAYS_LEFT
            if where_moves[1] > pawn[1]:
                return MOVEMENT_SIDEWAYS_RIGHT
        if where_moves[0] > pawn[0]:
            if where_moves[1] < pawn[1]:
                return MOVEMENT_DIAGONAL_LEFT_DOWN
            if where_moves[1] == pawn[1]:
                return MOVEMENT_DOWN
            if where_moves[1] > pawn[1]:
                return MOVEMENT_DIAGONAL_RIGHT_DOWN
