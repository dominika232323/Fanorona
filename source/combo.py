from source.board import Board
from source.hit import Hit
from source.move import Move
from source.movement import Movement
from source.pawns import Pawns
from source.turn import Turn


class Combo(Turn):
    def __init__(self, pawns, turn):
        super().__init__(pawns, turn)
        self.move = Move(self.pawns, turn)
        self.hit = Hit(self.pawns(), self.turn())

    def possible_combo(self, pawn, empty):
        if not self._if_can_hit(pawn, empty):
            return False
        pawns_after_move = self.move.move_with_hits(pawn, empty)
        self.pawns.set_actual_pawns(pawns_after_move)
        previous_move_type = Movement.recognize_move(pawn, empty)
        new_pawn_cords = empty
        if new_pawn_cords in self.hit.which_can_hit():
            for empty_space in self.hit.where_can_hit()[new_pawn_cords]:
                if Movement.recognize_move(new_pawn_cords, empty_space) != previous_move_type:
                    return True
        return False

    def _if_can_hit(self, pawn, empty):
        if pawn not in self.hit.which_can_hit():
            return False
        if empty not in self.hit.where_can_hit()[pawn]:
            return False
        return True

    def make_combo(self):
        pass