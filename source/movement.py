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

    @staticmethod
    def diagonal_movement_to_left_up(pawns, row_index, index, wanted_pawn):
        Movement.validate_wanted_pawn(wanted_pawn)
        if Movement.check_for_max_to_left_or_up(row_index):
            return False
        if Movement.check_for_max_to_left_or_up(index):
            return False
        if not Movement.check_for_diagonal_connections(row_index, index):
            return False
        if pawns[row_index-1][index-1] == wanted_pawn:
            return True
        return False

    @staticmethod
    def up_movement(pawns, row_index, index, wanted_pawn):
        Movement.validate_wanted_pawn(wanted_pawn)
        if Movement.check_for_max_to_left_or_up(row_index):
            return False
        if pawns[row_index-1][index] == wanted_pawn:
            return True
        return False

    @staticmethod
    def diagonal_movement_to_right_up(pawns, row_index, index, wanted_pawn):
        Movement.validate_wanted_pawn(wanted_pawn)
        if Movement.check_for_max_to_left_or_up(row_index):
            return False
        if Movement.check_for_max_to_right_or_down(index, len(pawns[0])):
            return False
        if not Movement.check_for_diagonal_connections(row_index, index):
            return False
        if pawns[row_index-1][index+1] == wanted_pawn:
            return True
        return False

    @staticmethod
    def sideways_movement_to_right(pawns, row_index, index, wanted_pawn):
        Movement.validate_wanted_pawn(wanted_pawn)
        if Movement.check_for_max_to_right_or_down(index, len(pawns[0])):
            return False
        if pawns[row_index][index+1] == wanted_pawn:
            return True
        return False

    @staticmethod
    def diagonal_movement_to_right_down(pawns, row_index, index, wanted_pawn):
        Movement.validate_wanted_pawn(wanted_pawn)
        if Movement.check_for_max_to_right_or_down(row_index, len(pawns)):
            return False
        if Movement.check_for_max_to_right_or_down(index, len(pawns[0])):
            return False
        if not Movement.check_for_diagonal_connections(row_index, index):
            return False
        if pawns[row_index+1][index+1] == wanted_pawn:
            return True
        return False

    @staticmethod
    def down_movement(pawns, row_index, index, wanted_pawn):
        Movement.validate_wanted_pawn(wanted_pawn)
        if Movement.check_for_max_to_right_or_down(row_index, len(pawns)):
            return False
        if pawns[row_index+1][index] == wanted_pawn:
            return True
        return False

    @staticmethod
    def diagonal_movement_to_left_down(pawns, row_index, index, wanted_pawn):
        Movement.validate_wanted_pawn(wanted_pawn)
        if Movement.check_for_max_to_right_or_down(row_index, len(pawns)):
            return False
        if Movement.check_for_max_to_left_or_up(index):
            return False
        if not Movement.check_for_diagonal_connections(row_index, index):
            return False
        if pawns[row_index+1][index-1] == wanted_pawn:
            return True
        return False

    @staticmethod
    def sideways_movement_to_left(pawns, row_index, index, wanted_pawn):
        Movement.validate_wanted_pawn(wanted_pawn)
        if Movement.check_for_max_to_left_or_up(index):
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
