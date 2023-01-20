from source.constants import (
    EMPTY_COLOR,
    CHOICE_WITHDRAWAL,
    CHOICE_APPROACH
)
from source.hit import Hit


class Move:
    """
    Class Move. Contains attributes:
    :param hit: an instance of class Hit
    :type hit: an instance of class Hit
    """
    def __init__(self, hit):
        """
        Creates an instance of Move.
        """
        self._validate(hit)
        self.hit = hit

    @staticmethod
    def _validate(hit):
        """
        :param hit: an instance of class Hit
        :raise: TypeError if given hit is not an instance of class Hit
        """
        if not isinstance(hit, Hit):
            raise TypeError('Given hit is not an instance of class Hit.')

    @property
    def pawns(self):
        """
        :return: placement of the pawns on the board
        """
        return self.hit.pawns()

    @property
    def turn(self):
        """
        :return: whose turn is it, first or second player
        """
        return self.hit.turn()

    @property
    def pawn_to_hit(self):
        """
        :return: type of pawns to capture
        """
        return self.hit.pawn_to_hit()

    @property
    def length(self):
        """
        :return: board's length
        """
        return self.hit.length()

    @property
    def width(self):
        """
        :return: board's width
        """
        return self.hit.width()

    def move_maker(self, pawn, empty, choice):
        """
        :param pawn: co-ordinates of a pawn that makes move
        :param empty: co-ordinates of an empty space where the pawn moves
        :param choice: player's choice to capture opponent's pawns by withdrawal or by approach
        :return: two-dimensional list of pawns placement after move
        """
        self._validate_move_maker(empty, pawn)

        if not self.hit.which_can_hit():
            return self.move_without_hits(pawn, empty)
        else:
            return self.move_with_hits(pawn, empty, choice)

    def _validate_move_maker(self, empty, pawn):
        """
        :param empty: co-ordinates of an empty space where the pawn moves
        :param pawn: co-ordinates of a pawn that makes move
        :raise: MoveError if the pawn cannot move
        :raise: MoveError if the pawn cannot move to the empty space
        :raise: MoveError if there are pawns that capture opponent's pawns but the pawn isn't one of them
        :raise: MoveError if the pawn can capture opponent's pawns but not by moving to the empty space
        """
        if pawn not in self.hit.which_can_move():
            raise MoveError('This pawn cannot move')
        if empty not in self.hit.where_can_move()[pawn]:
            raise MoveError('This pawn cannot move here')
        if self.hit.which_can_hit() and pawn not in self.hit.which_can_hit():
            raise MoveError('This pawn does not have any hits')
        if self.hit.which_can_hit() and empty not in self.hit.where_can_hit()[pawn]:
            raise MoveError('This pawn does not have any hits here')

    def move_without_hits(self, pawn, empty):
        """
        :param pawn: co-ordinates of a pawn that makes move
        :param empty: co-ordinates of an empty space where the pawn moves
        :return: two-dimensional list of pawns placement after move
        """
        pawns_after_move = self.copy_pawns()
        pawns_after_move[pawn[0]][pawn[1]] = EMPTY_COLOR
        pawns_after_move[empty[0]][empty[1]] = self.turn
        return pawns_after_move

    def move_with_hits(self, pawn, empty, choice):
        """
        :param pawn: co-ordinates of a pawn that makes move
        :param empty: co-ordinates of an empty space where the pawn moves
        :param choice: player's choice to capture opponent's pawns by withdrawal or by approach
        :return: two-dimensional list of pawns placement after move
        """
        withdrawal = self.hit.which_hits_by_withdrawal()
        approach = self.hit.which_hits_by_approach()

        if choice == CHOICE_WITHDRAWAL or (choice is None and (pawn, empty) in withdrawal):
            dead_pawns = withdrawal[(pawn, empty)]
        elif choice == CHOICE_APPROACH or (choice is None and (pawn, empty) in approach):
            dead_pawns = approach[(pawn, empty)]

        return self.move_with_hits_kill_pawns(pawn, empty, dead_pawns)

    def move_with_hits_kill_pawns(self, pawn, empty, dead_pawns):
        """
        :param pawn: co-ordinates of a pawn that makes move
        :param empty: co-ordinates of an empty space where the pawn moves
        :param dead_pawns: list of co-ordinates of opponent's pawns that are being captured
        :return: two-dimensional list of pawns placement after move
        """
        pawns_after_move = self.move_without_hits(pawn, empty)

        for dead in dead_pawns:
            pawns_after_move[dead[0]][dead[1]] = EMPTY_COLOR
        
        return pawns_after_move

    def copy_pawns(self):
        """
        :return: copy of two-dimensional list of pawns placement
        """
        copied_pawns = []

        for row in self.pawns:
            row_after_move = []
            for pawn in row:
                row_after_move.append(pawn)
            copied_pawns.append(row_after_move)
        
        return copied_pawns

    def was_move_capturing(self, pawn, empty):
        """
        :param pawn: co-ordinates of a pawn that makes move
        :param empty: co-ordinates of an empty space where the pawn moves
        :return: True if move made by moving the pawn to the empty space was capturing
        """
        if pawn in self.hit.which_can_hit():
            if empty in self.hit.where_can_hit()[pawn]:
                return True
            return False
        return False


class MoveError(Exception):
    pass
