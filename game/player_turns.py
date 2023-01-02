from source.board import Board
from source.hit import Hit
from source.pawns import Pawns
from source.move import Move
from random import choice


def player_turn(pawns, pawn_color):
    move = Move(pawns, pawn_color)


def computer_random(pawns, pawn_color):
    pawn_cords, empty_cords = get_random_pawn_and_empty_cords(pawns, pawn_color)


def computer_the_best(pawns, pawn_color):
    pass


def get_random_pawn_and_empty_cords(pawns, pawn_color):
    hit = Hit(pawns, pawn_color)
    hitting_pawns = list(hit.which_can_hit())
    if hitting_pawns:
        pawn_cords = choice(hitting_pawns)
        empty_for_hitting_pawns = hit.where_can_hit()[pawn_cords]
        empty_cords = choice(empty_for_hitting_pawns)
    else:
        pawn_cords = choice(list(hit.which_can_move()))
        empty_cords = choice(hit.where_can_move()[pawn_cords])
    return pawn_cords, empty_cords

