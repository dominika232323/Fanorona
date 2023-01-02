from game.player_turns import *
from configuration import (
    FIRST_COLOR,
    SECOND_COLOR,
    EMPTY_COLOR
)


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
