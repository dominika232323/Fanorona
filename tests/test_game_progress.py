from game.game_progress import (
    order_of_players, get_random_pawn_and_empty_cords, find_longest_group_to_kill, get_best_pawns_and_empty_cords
)
from source.board import Board
from source.configuration import (
    FIRST_COLOR,
    SECOND_COLOR,
    OPPONENT_PLAYER,
    OPPONENT_COMPUTER_RANDOM,
    OPPONENT_COMPUTER_BEST, EMPTY_COLOR
)
from source.hit import Hit
from source.pawns import Pawns


# ----------------------------------------- order_of_players()


def test_order_of_players():
    assert order_of_players(FIRST_COLOR, OPPONENT_COMPUTER_RANDOM) == (OPPONENT_PLAYER, OPPONENT_COMPUTER_RANDOM)
    assert order_of_players(SECOND_COLOR, OPPONENT_COMPUTER_BEST) == (OPPONENT_COMPUTER_BEST, OPPONENT_PLAYER)
    assert order_of_players(SECOND_COLOR, OPPONENT_PLAYER) == (OPPONENT_PLAYER, OPPONENT_PLAYER)


# ---------------------------------- get_random_pawn_and_empty_cords()


def test_get_random_pawn_and_empty_cords_with_hits():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    pawn_cords, empty_cords = get_random_pawn_and_empty_cords(pawns, SECOND_COLOR)
    assert pawn_cords in {(0, 5), (0, 6), (0, 8), (1, 0), (1, 1), (1, 2), (2, 7), (3, 3)}
    assert empty_cords in [(1, 7), (1, 5), (1, 6), (1, 8), (2, 0), (2, 1), (1, 3), (2, 2), (3, 4)]


def test_get_random_pawn_and_empty_cords_without_hits():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    pawn_cords, empty_cords = get_random_pawn_and_empty_cords(pawns, FIRST_COLOR)
    assert pawn_cords in [(4, 1), (4, 3), (4, 6), (4, 7)]
    assert empty_cords in [(3, 1), (4, 2), (4, 0), (3, 3), (4, 4), (4, 2), (3, 5), (3, 6), (3, 7), (4, 5), (3, 7), (4, 8)]


# ---------------------------------- find_longest_group_to_kill()


def test_find_longest_group_to_kill():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR,
         SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR,
         EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR,
         FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR,
         FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR,
         FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Hit(pawns, SECOND_COLOR)
    assert find_longest_group_to_kill(move.which_hits_by_approach()) == ((3, 3), (3, 4), 4)


# ---------------------------------- get_best_pawn_and_empty_cords()


def test_get_best_pawn_and_empty_cords_with_hits():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    assert get_best_pawns_and_empty_cords(pawns, SECOND_COLOR) == ((3, 3), (3, 4))


def test_get_best_pawn_and_empty_cords_without_hits():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    pawn_cords, empty_cords = get_best_pawns_and_empty_cords(pawns, FIRST_COLOR)
    assert pawn_cords in [(4, 1), (4, 3), (4, 6), (4, 7)]
    assert empty_cords in [(3, 1), (4, 2), (4, 0), (3, 3), (4, 4), (4, 2), (3, 5), (3, 6), (3, 7), (4, 5), (3, 7), (4, 8)]
