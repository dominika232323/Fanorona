from source.board import Board
from source.hit import Hit
from source.pawns import Pawns
from source.move import Move
from random import choice


def player_turn(pawns, pawn_color):
    move = Move(pawns, pawn_color)
    # move.move_maker()
    # pawns.set_actual_pawns()
    # combo = Combo()
    # while combo.possible_combo():
    #     if combo.possible_combo():
    #         move_combo = Move()
    #         move_combo.move_maker()


def computer_random(pawns, pawn_color):
    pawn_cords, empty_cords = get_random_pawn_and_empty_cords(pawns, pawn_color)


def computer_best(pawns, pawn_color):
    pawn_cords, empty_cords = get_best_pawns_and_empty_cords(pawns, pawn_color)


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


def get_best_pawns_and_empty_cords(pawns, pawn_color):
    hit = Hit(pawns, pawn_color)
    hitting_pawns = list(hit.which_can_hit())
    if hitting_pawns:
        pawn_by_w, empty_by_w, length_by_w = find_longest_group_to_kill(hit.which_hits_by_withdrawal())
        pawn_by_a, empty_by_a, length_by_a = find_longest_group_to_kill(hit.which_hits_by_approach())
        if length_by_w >= length_by_a:
            return pawn_by_w, empty_by_w
        else:
            return pawn_by_a, empty_by_a
    else:
        pawn_cords = choice(list(hit.which_can_move()))
        empty_cords = choice(hit.where_can_move()[pawn_cords])
        return pawn_cords, empty_cords


def find_longest_group_to_kill(dict_of_hits):
    pawn_cords = (0, 0)
    empty_cords = (0, 0)
    len_group_to_kill = 0
    for pawn_and_empty in dict_of_hits:
        if len(dict_of_hits[pawn_and_empty]) > len_group_to_kill:
            pawn_cords = pawn_and_empty[0]
            empty_cords = pawn_and_empty[1]
            len_group_to_kill = len(dict_of_hits[pawn_and_empty])
    return pawn_cords, empty_cords, len_group_to_kill

