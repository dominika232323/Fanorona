from classes.board import Board
from classes.pawns import Pawns
import pytest


# -------------------------------- __init__()


def test_create_empty_pawns():
    pawns = Pawns(Board())
    expected = [
        ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
    ]
    assert pawns.empty_pawns == expected
    assert pawns.board_length == 9
    assert pawns.board_width == 5


def test_create_empty_pawns_board_typeerror():
    with pytest.raises(TypeError):
        Pawns((9, 5))


# -------------------------------- set_starting_pawns()


def test_starting_pawns():
    pawns = Pawns(Board())
    pawns.set_starting_pawns()
    expected = [
        ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
        ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
        ['B', 'W', 'B', 'W', 'E', 'B', 'W', 'B', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
    ]
    assert pawns.actual_pawns == expected
