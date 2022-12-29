from source.move import Move
from source.board import Board
from source.pawns import Pawns
from configuration import (
    FIRST_COLOR,
    SECOND_COLOR,
    EMPTY_COLOR,
    MOVEMENT_DIAGONAL_LEFT_UP,
    MOVEMENT_UP,
    MOVEMENT_DIAGONAL_RIGHT_UP,
    MOVEMENT_SIDEWAYS_RIGTH,
    MOVEMENT_DIAGONAL_RIGTH_DOWN,
    MOVEMENT_DOWN,
    MOVEMENT_DIAGONAL_LEFT_DOWN,
    MOVEMENT_SIDEWAYS_LEFT
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


# ---------------------------------------- recognize_move()


def test_recognize_move():
    move = Move(Pawns(Board()), FIRST_COLOR)
    assert move.recognize_move((1, 1), (0, 0)) == MOVEMENT_DIAGONAL_LEFT_UP
    assert move.recognize_move((1, 1), (0, 1)) == MOVEMENT_UP
    assert move.recognize_move((1, 1), (0, 2)) == MOVEMENT_DIAGONAL_RIGHT_UP
    assert move.recognize_move((1, 1), (1, 2)) == MOVEMENT_SIDEWAYS_RIGTH
    assert move.recognize_move((1, 1), (2, 2)) == MOVEMENT_DIAGONAL_RIGTH_DOWN
    assert move.recognize_move((1, 1), (2, 1)) == MOVEMENT_DOWN
    assert move.recognize_move((1, 1), (2, 0)) == MOVEMENT_DIAGONAL_LEFT_DOWN
    assert move.recognize_move((1, 1), (1, 0)) == MOVEMENT_SIDEWAYS_LEFT


# ---------------------------------------- which_can_move()


def test_which_can_move_start():
    move = Move(Pawns(Board()), FIRST_COLOR)
    expected = [(2, 3), (3, 3), (3, 4), (3, 5)]
    assert move.which_can_move() == expected


def test_which_can_move():
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


def test_which_can_move_without_hits():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, FIRST_COLOR)
    assert move.which_can_move() == [(4, 1), (4, 3), (4, 6), (4, 7)]


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


def test_where_can_move():
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


def test_where_can_move_without_hits():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, FIRST_COLOR)
    expected = {
        (4, 1): [(3, 1), (4, 2), (4, 0)],
        (4, 3): [(3, 3), (4, 4), (4, 2)],
        (4, 6): [(3, 5), (3, 6), (3, 7), (4, 5)],
        (4, 7): [(3, 7), (4, 8)]
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


def test_which_can_hit_by_withdrawl_without_hits():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, FIRST_COLOR)
    assert move.which_can_hit_by_withdrawl() == []


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


def test_which_can_hit_by_approach_without_hits():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, FIRST_COLOR)
    assert move.which_can_hit_by_approach() == []


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


def test_which_can_hit_without_hits():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, FIRST_COLOR)
    assert move.which_can_hit() == []


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


def test_where_can_hit_by_withdrawl_without_hits():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, FIRST_COLOR)
    assert move.where_can_hit_by_withdrawl() == {}


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


def test_where_can_hit_by_approach_without_hits():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, FIRST_COLOR)
    assert move.where_can_hit_by_approach() == {}


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


def test_where_can_hit_without_hits():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, FIRST_COLOR)
    assert move.where_can_hit() == {}


# ---------------------------------------- which_hits_by_withdrawl()


def test_which_hits_by_withdrawl():
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
        ((2, 7), (1, 7)): [(3, 7), (4, 7)],
        ((3, 3), (3, 4)): [(3, 2), (3, 1), (3, 0)]
        }
    assert move.which_hits_by_withdrawl() == expected


def test_which_hits_by_withdrawl_without_hits():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, FIRST_COLOR)
    assert move.which_hits_by_withdrawl() == {}


# ---------------------------------------- which_hits_by_approach()


def test_which_hits_by_approach():
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
        ((0, 5), (1, 5)): [(2, 5), (3, 5), (4, 5)],
        ((0, 6), (1, 7)): [(2, 8)],
        ((0, 6), (1, 6)): [(2, 6), (3, 6), (4, 6)],
        ((0, 8), (1, 8)): [(2, 8), (3, 8), (4, 8)],
        ((0, 8), (1, 7)): [(2, 6), (3, 5)],
        ((1, 0), (2, 0)): [(3, 0), (4, 0)],
        ((1, 1), (2, 1)): [(3, 1), (4, 1)],
        ((1, 2), (1, 3)): [(1, 4)],
        ((1, 2), (2, 2)): [(3, 2)],
        ((3, 3), (3, 4)): [(3, 5), (3, 6), (3, 7), (3, 8)]
        }
    assert move.which_hits_by_approach() == expected


def test_which_hits_by_approach_without_hits():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, FIRST_COLOR)
    assert move.which_hits_by_approach() == {}


# ---------------------------------------- copy_pawns()


def test_copy_pawns():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)

    move = Move(pawns, FIRST_COLOR)
    assert move.copy_pawns() == new_pawns
