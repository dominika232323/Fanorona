from random import choice

from source.hit import Hit
from source.move import Move
from source.pawns import Pawns
from source.configuration import (
    FIRST_COLOR,
    SECOND_COLOR,
    OPPONENT_PLAYER,
    OPPONENT_COMPUTER_RANDOM,
    OPPONENT_COMPUTER_BEST,
    CHOICE_APPROACH,
    CHOICE_WITHDRAWAL
)


class Game:
    @staticmethod
    def order_of_players(player_color, opponent_type):
        if player_color == FIRST_COLOR:
            return OPPONENT_PLAYER, opponent_type
        if player_color == SECOND_COLOR:
            return opponent_type, OPPONENT_PLAYER

    @staticmethod
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

    @staticmethod
    def get_random_move_choice(pawns, pawn_color, pawn_cords, empty_cords):
        hit = Hit(pawns, pawn_color)
        if (pawn_cords, empty_cords) in hit.which_hits_by_withdrawal().keys() and \
                (pawn_cords, empty_cords) in hit.which_hits_by_approach().keys():
            return choice([CHOICE_APPROACH, CHOICE_WITHDRAWAL])
        return None

    @staticmethod
    def get_best_pawns_and_empty_cords(pawns, pawn_color):
        hit = Hit(pawns, pawn_color)
        hitting_pawns = list(hit.which_can_hit())
        if hitting_pawns:
            pawn_by_w, empty_by_w, length_by_w = Game.find_longest_group_to_kill(hit.which_hits_by_withdrawal())
            pawn_by_a, empty_by_a, length_by_a = Game.find_longest_group_to_kill(hit.which_hits_by_approach())
            if length_by_w >= length_by_a:
                return pawn_by_w, empty_by_w
            else:
                return pawn_by_a, empty_by_a
        else:
            pawn_cords = choice(list(hit.which_can_move()))
            empty_cords = choice(hit.where_can_move()[pawn_cords])
            return pawn_cords, empty_cords

    @staticmethod
    def find_longest_group_to_kill(dict_of_hits):
        pawn_cords = None
        empty_cords = None
        len_group_to_kill = 0
        for pawn_and_empty in dict_of_hits:
            if len(dict_of_hits[pawn_and_empty]) > len_group_to_kill:
                pawn_cords = pawn_and_empty[0]
                empty_cords = pawn_and_empty[1]
                len_group_to_kill = len(dict_of_hits[pawn_and_empty])
        return pawn_cords, empty_cords, len_group_to_kill

    @staticmethod
    def find_best_choice(pawns, pawn_color, pawn_cords, empty_cords):
        hit = Hit(pawns, pawn_color)
        if (pawn_cords, empty_cords) in hit.which_hits_by_withdrawal().keys() and \
                (pawn_cords, empty_cords) in hit.which_hits_by_approach().keys():
            if len(hit.which_hits_by_approach()[(pawn_cords, empty_cords)]) > len(hit.which_hits_by_withdrawal()[(pawn_cords, empty_cords)]):
                return CHOICE_APPROACH
            else:
                return CHOICE_WITHDRAWAL
        return None

    @staticmethod
    def get_best_empty_for_combo(hit, combo, pawn_cords):
        empties = combo.find_empty_for_combo()
        combo_withdrawal, len_withdrawal = Game.find_best_empty_for_combo_by(pawn_cords, empties, hit.which_hits_by_withdrawal())
        combo_approach, len_approach = Game.find_best_empty_for_combo_by(pawn_cords, empties, hit.which_hits_by_approach())
        if len_withdrawal >= len_approach:
            combo_empty_cords = combo_withdrawal
        else:
            combo_empty_cords = combo_approach
        return combo_empty_cords

    @staticmethod
    def find_best_empty_for_combo_by(pawn_cords, list_of_empties, dict_of_hits):
        length = 0
        empty_cords = None
        for empty in list_of_empties:
            if (pawn_cords, empty) in dict_of_hits.keys():
                if len(dict_of_hits[(pawn_cords, empty)]) > length:
                    empty_cords = empty
                    length = len(dict_of_hits[(pawn_cords, empty)])
        return empty_cords, length
