from source.move import Move
from source.board import Board
from source.pawns import Pawns
from configuration import (
    FIRST_COLOR,
    SECOND_COLOR,
    EMPTY_COLOR
)
import pytest


# ---------------------------------------- __init__()


def test_create_move():
    move = Move(Pawns(Board()), FIRST_COLOR)
    expected = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR, EMPTY_COLOR, SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    assert move.pawns == expected
    assert move.turn == FIRST_COLOR
    assert move.pawn_to_hit == SECOND_COLOR
    assert move.length == 9
    assert move.width == 5


def test_create_move_invalid_pawns():
    expected = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR, EMPTY_COLOR, SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    with pytest.raises(TypeError):
        Move(expected, SECOND_COLOR)


def test_create_move_invalid_turn():
    with pytest.raises(ValueError):
        Move(Pawns(Board()), 'fgh')


# ---------------------------------------- which_can_move()


def test_which_can_move_start():
    move = Move(Pawns(Board()), FIRST_COLOR)
    expected = [(2, 3), (3, 3), (3, 4), (3, 5)]
    assert move.which_can_move() == expected


def test_which_can_move_():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, SECOND_COLOR)
    assert move.which_can_move() == [(0, 2), (0, 3), (0, 5), (0, 6), (0, 7), (0, 8), (1, 0), (1, 1), (1, 2), (2, 7), (3, 3)]


# ---------------------------------------- where_can_move()


def test_where_can_move_starting():
    move = Move(Pawns(Board()), FIRST_COLOR)
    expected = {
        (2, 3): [(2, 4)],
        (3, 3): [(2, 4)],
        (3, 4): [(2, 4)],
        (3, 5): [(2, 4)]
    }
    assert move.where_can_move() == expected


def test_where_can_move_():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, SECOND_COLOR)
    expected = {
        (0, 2): [(1, 3)],
        (0, 3): [(0, 4), (1, 3)],
        (0, 5): [(1, 5), (0, 4)],
        (0, 6): [(1, 7), (1, 6), (1, 5)],
        (0, 7): [(1, 7)],
        (0, 8): [(1, 8), (1, 7)],
        (1, 0): [(2, 0)],
        (1, 1): [(2, 2), (2, 1), (2, 0)],
        (1, 2): [(1, 3), (2, 2)],
        (2, 7): [(1, 7)],
        (3, 3): [(2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2)]
        }
    assert move.where_can_move() == expected


# ---------------------------------------- which_can_hit_by_withdrawl()


def test_which_can_hit_by_withdrawl():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, SECOND_COLOR)
    expected = {(2, 7), (3, 3)}
    assert move.which_can_hit_by_withdrawl() == expected


# ---------------------------------------- which_can_hit_by_approach()


def test_which_can_hit_by_approach():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, SECOND_COLOR)
    expected = {(0, 5), (0, 6), (0, 8), (1, 0), (1, 1), (1, 2), (3, 3)}
    assert move.which_can_hit_by_approach() == expected


# ---------------------------------------- which_can_hit()


def test_which_can_hit():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, SECOND_COLOR)
    expected = {(0, 5), (0, 6), (0, 8), (1, 0), (1, 1), (1, 2), (2, 7), (3, 3)}
    assert move.which_can_hit() == expected


# ---------------------------------------- where_can_hit_by_withdrawl()


def test_where_can_hit_by_withdrawl():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, SECOND_COLOR)
    expected = {
        (2, 7): [(1, 7)],
        (3, 3): [(3, 4)]
        }
    assert move.where_can_hit_by_withdrawl() == expected


# ---------------------------------------- where_can_hit_by_approach()


def test_where_can_hit_by_approach():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, SECOND_COLOR)
    expected = {
        (0, 5): [(1, 5)],
        (0, 6): [(1, 7), (1, 6)],
        (0, 8): [(1, 8), (1, 7)],
        (1, 0): [(2, 0)],
        (1, 1): [(2, 1)],
        (1, 2): [(1, 3), (2, 2)],
        (3, 3): [(3, 4)]
        }
    assert move.where_can_hit_by_approach() == expected


# ---------------------------------------- where_can_hit()


def test_where_can_hit():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, SECOND_COLOR)
    expected = {
        (2, 7): [(1, 7)],
        (0, 5): [(1, 5)],
        (0, 6): [(1, 7), (1, 6)],
        (0, 8): [(1, 8), (1, 7)],
        (1, 0): [(2, 0)],
        (1, 1): [(2, 1)],
        (1, 2): [(1, 3), (2, 2)],
        (3, 3): [(3, 4)]
        }
    assert move.where_can_hit() == expected
