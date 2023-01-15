from source.configuration import (
    EMPTY_COLOR,
    CHOICE_WITHDRAWAL,
    CHOICE_APPROACH
)
from source.hit import Hit


class Move:
    def __init__(self, pawns, turn):
        self.hit = Hit(pawns, turn)

    @property
    def pawns(self):
        return self.hit.pawns()

    @property
    def turn(self):
        return self.hit.turn()

    @property
    def pawn_to_hit(self):
        return self.hit.pawn_to_hit()

    @property
    def length(self):
        return self.hit.length()

    @property
    def width(self):
        return self.hit.width()

    def move_maker(self, pawn, empty, choice):
        self._validate_move_maker(empty, pawn)

        if not self.hit.which_can_hit():
            return self.move_without_hits(pawn, empty)
        else:
            return self.move_with_hits(pawn, empty, choice)

    def _validate_move_maker(self, empty, pawn):
        if pawn not in self.hit.which_can_move():
            raise MoveError('This pawn cannot move')
        if empty not in self.hit.where_can_move()[pawn]:
            raise MoveError('This pawn cannot move here')
        if self.hit.which_can_hit() and pawn not in self.hit.which_can_hit():
            raise MoveError('This pawn does not have any hits')
        if self.hit.which_can_hit() and empty not in self.hit.where_can_hit()[pawn]:
            raise MoveError('This pawn does not have any hits here')

    def move_without_hits(self, pawn, empty):
        pawns_after_move = self.copy_pawns()
        pawns_after_move[pawn[0]][pawn[1]] = EMPTY_COLOR
        pawns_after_move[empty[0]][empty[1]] = self.turn
        return pawns_after_move

    def move_with_hits(self, pawn, empty, choice):
        withdrawal = self.hit.which_hits_by_withdrawal()
        approach = self.hit.which_hits_by_approach()

        if choice == CHOICE_WITHDRAWAL or (choice is None and (pawn, empty) in withdrawal):
            dead_pawns = withdrawal[(pawn, empty)]
        elif choice == CHOICE_APPROACH or (choice is None and (pawn, empty) in approach):
            dead_pawns = approach[(pawn, empty)]

        return self.move_with_hits_kill_pawns(pawn, empty, dead_pawns)

    def move_with_hits_kill_pawns(self, pawn, empty, dead_pawns):
        pawns_after_move = self.move_without_hits(pawn, empty)

        for dead in dead_pawns:
            pawns_after_move[dead[0]][dead[1]] = EMPTY_COLOR
        
        return pawns_after_move

    def copy_pawns(self):
        copied_pawns = []

        for row in self.pawns:
            row_after_move = []
            for pawn in row:
                row_after_move.append(pawn)
            copied_pawns.append(row_after_move)
        
        return copied_pawns

    def was_move_capturing(self, pawn, empty):
        if pawn in self.hit.which_can_hit():
            if empty in self.hit.where_can_hit()[pawn]:
                return True
            return False
        return False


class MoveError(Exception):
    pass
