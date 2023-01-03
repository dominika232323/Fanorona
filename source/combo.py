from source.board import Board
from source.hit import Hit
from source.move import Move
from source.movement import Movement
from source.pawns import Pawns
from source.turn import Turn


class Combo(Turn):
    def possible_combo(self, pawn, empty):
        pawns_after_move = Move.move_with_hits(pawn, empty)
        pawns_for_combo = Pawns(Board(self.length, self.width))
        pawns_for_combo.set_actual_pawns(pawns_after_move)
        previous_move_type = Movement.recognize_move(pawn, empty)
        new_pawn_cords = empty
        hit_for_combo = Hit(pawns_for_combo, self.turn)
        if new_pawn_cords in hit_for_combo.which_can_hit():
            for empty_space in hit_for_combo.where_can_hit()[new_pawn_cords]:
                if Movement.recognize_move(new_pawn_cords, empty_space) != previous_move_type:
                    return True
        return False
