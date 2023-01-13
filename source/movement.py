from source.configuration import (
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
    """
    Class Movement.
    """
    @staticmethod
    def check_for_max_to_left_or_up(index):
        """
        :param index: one of the co-ordinates of a pawn
        :return: True if pawn isn't most left or most up on the board
        """
        if index == 0:
            return True
        return False

    @staticmethod
    def check_for_max_to_right_or_down(index, length):
        """
        :param index: one of the co-ordinates of a pawn
        :param length: board's length
        :return: True if pawn isn't most right or most down on the board
        """
        if index == length-1:
            return True
        return False

    @staticmethod
    def check_for_diagonal_connections(row_index, index):
        """
        :param row_index: index of a row in which a pawn is seated
        :param index: index of a column in which a pawn is seated
        :return: True if a pawn can move diagonally
        """
        if row_index % 2 == 0 and index % 2 == 1:
            return False
        if row_index % 2 == 1 and index % 2 == 0:
            return False
        return True

    @staticmethod
    def validate_wanted_pawn(pawn):
        """
        :param pawn: pawn seated on the board
        :raise: PawnsError if type of given pawn doesn't exist in the game Fanorona
        """
        if pawn not in (FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR):
            raise PawnsError('This type of pawn does not exist')

    @staticmethod
    def diagonal_movement_to_left_up(pawns, row_index, index, wanted_pawn):
        """
        :param pawns: pawns' placement on the board
        :param row_index: index of a row in which a pawn is seated
        :param index: index of a column in which a pawn is seated
        :param wanted_pawn: pawn type wanted diagonally to the left and up of the pawn
        :return: True if wanted pawn is diagonally to the left and up of the pawn
        """
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
        """
        :param pawns: pawns' placement on the board
        :param row_index: index of a row in which a pawn is seated
        :param index: index of a column in which a pawn is seated
        :param wanted_pawn: pawn type wanted on top of the pawn
        :return: True if wanted pawn is on top of the pawn
        """
        Movement.validate_wanted_pawn(wanted_pawn)
        if Movement.check_for_max_to_left_or_up(row_index):
            return False
        if pawns[row_index-1][index] == wanted_pawn:
            return True
        return False

    @staticmethod
    def diagonal_movement_to_right_up(pawns, row_index, index, wanted_pawn):
        """
        :param pawns: pawns' placement on the board
        :param row_index: index of a row in which a pawn is seated
        :param index: index of a column in which a pawn is seated
        :param wanted_pawn: pawn type wanted diagonally to the right and up of the pawn
        :return: True if wanted pawn is diagonally to the right and up of the pawn
        """
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
        """
        :param pawns: pawns' placement on the board
        :param row_index: index of a row in which a pawn is seated
        :param index: index of a column in which a pawn is seated
        :param wanted_pawn: pawn type wanted on the right of the pawn
        :return: True if wanted pawn is on the right of the pawn
        """
        Movement.validate_wanted_pawn(wanted_pawn)
        if Movement.check_for_max_to_right_or_down(index, len(pawns[0])):
            return False
        if pawns[row_index][index+1] == wanted_pawn:
            return True
        return False

    @staticmethod
    def diagonal_movement_to_right_down(pawns, row_index, index, wanted_pawn):
        """
        :param pawns: pawns' placement on the board
        :param row_index: index of a row in which a pawn is seated
        :param index: index of a column in which a pawn is seated
        :param wanted_pawn: pawn type wanted diagonally to the right and down of the pawn
        :return: True if wanted pawn is diagonally to the right and down of the pawn
        """
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
        """
        :param pawns: pawns' placement on the board
        :param row_index: index of a row in which a pawn is seated
        :param index: index of a column in which a pawn is seated
        :param wanted_pawn: pawn type wanted at the bottom of the pawn
        :return: True if wanted pawn is at the bottom of the pawn
        """
        Movement.validate_wanted_pawn(wanted_pawn)
        if Movement.check_for_max_to_right_or_down(row_index, len(pawns)):
            return False
        if pawns[row_index+1][index] == wanted_pawn:
            return True
        return False

    @staticmethod
    def diagonal_movement_to_left_down(pawns, row_index, index, wanted_pawn):
        """
        :param pawns: pawns' placement on the board
        :param row_index: index of a row in which a pawn is seated
        :param index: index of a column in which a pawn is seated
        :param wanted_pawn: pawn type wanted diagonally to the left and down of the pawn
        :return: True if wanted pawn is diagonally to the left and down of the pawn
        """
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
        """
        :param pawns: pawns' placement on the board
        :param row_index: index of a row in which a pawn is seated
        :param index: index of a column in which a pawn is seated
        :param wanted_pawn: pawn type wanted on the left of the pawn
        :return: True if wanted pawn is on the left of the pawn
        """
        Movement.validate_wanted_pawn(wanted_pawn)
        if Movement.check_for_max_to_left_or_up(index):
            return False
        if pawns[row_index][index-1] == wanted_pawn:
            return True
        return False

    @staticmethod
    def recognize_move(pawn, where_moves):
        """
        :param pawn: co-ordinates of a pawn
        :param where_moves: co-ordinates of an empty space where the pawn moves
        :return: type of movement that the pawn moves
        """
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
