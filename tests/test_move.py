from classes.move import Move
from classes.board import Board
from classes.pawns import Pawns
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
