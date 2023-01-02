from source.pawns import Pawns
from configuration import (
    FIRST_COLOR,
    SECOND_COLOR,
    EMPTY_COLOR,
    MOVEMENT_DIAGONAL_LEFT_UP,
    MOVEMENT_UP,
    MOVEMENT_DIAGONAL_RIGHT_UP,
    MOVEMENT_SIDEWAYS_RIGHT,
    MOVEMENT_DIAGONAL_RIGHT_DOWN,
    MOVEMENT_DOWN,
    MOVEMENT_DIAGONAL_LEFT_DOWN,
    MOVEMENT_SIDEWAYS_LEFT,
    CHOICE_WITHDRAWAL,
    CHOICE_APPROACH
)
from source.movement import Movement
from source.hit import Hit
from source.turn import Turn


class Move(Turn):
    def move_maker(self, pawn, empty):
        self._validate_move_maker(empty, pawn)

        if not Hit.which_can_hit():
            return self.move_without_hits(pawn, empty)
        else:
            return self.move_with_hits(pawn, empty)

    @staticmethod
    def _validate_move_maker(empty, pawn):
        if pawn not in Hit.which_can_move():
            raise MoveError('This pawn cannot move')
        if empty not in Hit.where_can_move()[pawn]:
            raise MoveError('This pawn cannot move here')
        if Hit.which_can_hit() and pawn not in Hit.which_can_hit():
            raise MoveError('This pawn does not have any hits')
        if Hit.which_can_hit() and empty not in Hit.where_can_hit()[pawn]:
            raise MoveError('This pawn does not have any hits here')

    def possible_combo(self, previous_move_type):
        # sprawdza czy mozna zrobic kombo
        pass

    def move_without_hits(self, pawn, empty):
        pawns_after_move = self.copy_pawns()
        pawns_after_move[pawn[0]][pawn[1]] = EMPTY_COLOR
        pawns_after_move[empty[0]][empty[1]] = self.turn
        return pawns_after_move

    def move_with_hits(self, pawn, empty):
        withdrawal = Hit.which_hits_by_withdrawal()
        approach = Hit.which_hits_by_approach()

        if (pawn, empty) in withdrawal and (pawn, empty) in approach:
            chosen_group = self.choose_group_to_kill(pawn, empty)
            choice = self.choose_move_with_hits(pawn, empty, chosen_group)
            if choice == CHOICE_WITHDRAWAL:
                dead_pawns = withdrawal[(pawn, empty)]
            if choice == CHOICE_APPROACH:
                dead_pawns = approach[(pawn, empty)]
        elif (pawn, empty) in withdrawal:
            dead_pawns = withdrawal[(pawn, empty)]
        elif (pawn, empty) in approach:
            dead_pawns = approach[(pawn, empty)]

        return self.move_with_hits_kill_pawns(pawn, empty, dead_pawns)

    def choose_group_to_kill(self, pawn, empty):
        # NOT READY FUNCTION
        group = []
        return group

    @staticmethod
    def choose_move_with_hits(pawn, empty, chosen_group):
        withdrawal = Hit.which_hits_by_withdrawal
        group_withdrawal = withdrawal[(pawn, empty)]
        approach = Hit.which_hits_by_approach
        group_approach = approach[(pawn, empty)]
        if chosen_group == group_withdrawal:
            return CHOICE_WITHDRAWAL
        elif chosen_group == group_approach:
            return CHOICE_APPROACH
        else:
            raise MoveError('You cannot choose this group of pawns')

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


class MoveError(Exception):
    pass
