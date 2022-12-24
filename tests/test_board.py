from classes.board import Board, BoardSizeError
import pytest


# -------------------------------- __init__()


def test_create_board():
    board = Board(7, 7)
    assert board.length == 7
    assert board.width == 7


def test_create_board_defaults():
    board = Board()
    assert board.length == 9
    assert board.width == 5


def test_create_board_convertable_string():
    board = Board('7', '7')
    assert board.length == 7
    assert board.width == 7


def test_create_board_float():
    with pytest.raises(BoardSizeError):
        Board(5.5, 3.4)


def test_create_board_less_than_min():
    with pytest.raises(BoardSizeError):
        Board(1, 1)


def test_create_board_more_than_max():
    with pytest.raises(BoardSizeError):
        Board(17, 19)


def test_create_board_even_numbers():
    with pytest.raises(BoardSizeError):
        Board(6, 6)


def test_create_board_invalid_string():
    with pytest.raises(BoardSizeError):
        Board('fvgbhnj', 'dfgh')
