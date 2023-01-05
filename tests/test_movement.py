from source.movement import Movement
from source.configuration import (
    FIRST_COLOR,
    SECOND_COLOR,
    EMPTY_COLOR,
    MOVEMENT_DIAGONAL_LEFT_UP,
    MOVEMENT_UP,
    MOVEMENT_DOWN,
    MOVEMENT_SIDEWAYS_LEFT,
    MOVEMENT_SIDEWAYS_RIGHT,
    MOVEMENT_DIAGONAL_LEFT_DOWN,
    MOVEMENT_DIAGONAL_RIGHT_DOWN,
    MOVEMENT_DIAGONAL_RIGHT_UP,
)
from source.pawns import PawnsError
import pytest


# --------------------------------------- check_for_max_to_left_or_up()


def test_check_for_max_to_left_or_up():
    assert Movement.check_for_max_to_left_or_up(0) is True
    assert Movement.check_for_max_to_left_or_up(8) is False


# --------------------------------------- check_for_max_to_right_or_down()


def test_check_for_max_to_right_or_down():
    assert Movement.check_for_max_to_right_or_down(6, 7) is True
    assert Movement.check_for_max_to_right_or_down(3, 5) is False


# --------------------------------------- check_for_diagonal_connections()


def test_check_for_diagonal_connections():
    assert Movement.check_for_diagonal_connections(0, 1) is False
    assert Movement.check_for_diagonal_connections(1, 0) is False
    assert Movement.check_for_diagonal_connections(3, 3) is True
    assert Movement.check_for_diagonal_connections(4, 4) is True


# --------------------------------------- validate_wanted_pawn()


def test_validate_wanted_pawn():
    with pytest.raises(PawnsError):
        Movement.validate_wanted_pawn('fvghjk')


# --------------------------------------- diagonal_movement_to_left_up()


def test_diagonal_movement_to_left_up():
    pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR, EMPTY_COLOR, SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    assert Movement.diagonal_movement_to_left_up(pawns, 2, 3, EMPTY_COLOR) is False
    assert Movement.diagonal_movement_to_left_up(pawns, 3, 5, EMPTY_COLOR) is True


# --------------------------------------- up_movement()


def test_up_movement():
    pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR, EMPTY_COLOR, SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    assert Movement.up_movement(pawns, 2, 3, EMPTY_COLOR) is False
    assert Movement.up_movement(pawns, 3, 4, EMPTY_COLOR) is True


# --------------------------------------- diagonal_movement_to_right_up()


def test_diagonal_movement_to_right_up():
    pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR, EMPTY_COLOR, SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    assert Movement.diagonal_movement_to_right_up(pawns, 2, 3, EMPTY_COLOR) is False
    assert Movement.diagonal_movement_to_right_up(pawns, 3, 3, EMPTY_COLOR) is True


# --------------------------------------- sideways_movement_to_right()


def test_sideways_movement_to_right():
    pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR, EMPTY_COLOR, SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    assert Movement.sideways_movement_to_right(pawns, 3, 3, EMPTY_COLOR) is False
    assert Movement.sideways_movement_to_right(pawns, 2, 3, EMPTY_COLOR) is True


# --------------------------------------- diagonal_movement_to_right_down()


def test_diagonal_movement_to_right_down():
    pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR, EMPTY_COLOR, SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    assert Movement.diagonal_movement_to_right_down(pawns, 3, 3, EMPTY_COLOR) is False
    assert Movement.diagonal_movement_to_right_down(pawns, 1, 3, EMPTY_COLOR) is True


# --------------------------------------- down_movement()


def test_down_movement():
    pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR, EMPTY_COLOR, SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    assert Movement.down_movement(pawns, 3, 3, EMPTY_COLOR) is False
    assert Movement.down_movement(pawns, 1, 4, EMPTY_COLOR) is True


# --------------------------------------- diagonal_movement_to_left_down()


def test_diagonal_movement_to_left_down():
    pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR, EMPTY_COLOR, SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    assert Movement.diagonal_movement_to_left_down(pawns, 3, 3, EMPTY_COLOR) is False
    assert Movement.diagonal_movement_to_left_down(pawns, 1, 5, EMPTY_COLOR) is True


# --------------------------------------- sideways_movement_to_left()


def test_sideways_movement_to_left():
    pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR, EMPTY_COLOR, SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    assert Movement.sideways_movement_to_left(pawns, 3, 3, EMPTY_COLOR) is False
    assert Movement.sideways_movement_to_left(pawns, 2, 5, EMPTY_COLOR) is True


# ---------------------------------------- recognize_move()


def test_recognize_move():
    assert Movement.recognize_move((1, 1), (0, 0)) == MOVEMENT_DIAGONAL_LEFT_UP
    assert Movement.recognize_move((1, 1), (0, 1)) == MOVEMENT_UP
    assert Movement.recognize_move((1, 1), (0, 2)) == MOVEMENT_DIAGONAL_RIGHT_UP
    assert Movement.recognize_move((1, 1), (1, 2)) == MOVEMENT_SIDEWAYS_RIGHT
    assert Movement.recognize_move((1, 1), (2, 2)) == MOVEMENT_DIAGONAL_RIGHT_DOWN
    assert Movement.recognize_move((1, 1), (2, 1)) == MOVEMENT_DOWN
    assert Movement.recognize_move((1, 1), (2, 0)) == MOVEMENT_DIAGONAL_LEFT_DOWN
    assert Movement.recognize_move((1, 1), (1, 0)) == MOVEMENT_SIDEWAYS_LEFT
