import pytest

from source.board import Board
from source.combo import Combo
from source.hit import Hit
from source.move import Move
from source.pawns import Pawns
from source.constants import (
    FIRST_COLOR,
    SECOND_COLOR,
    EMPTY_COLOR,
    MOVEMENT_DOWN,
    MOVEMENT_UP
)


# ---------------------------------------- __init__()


def test_create_combo():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)
    combo = Combo(Move(Hit(pawns, SECOND_COLOR)), (0, 5), (1, 5))
    assert combo.pawns == new_pawns
    assert combo.turn == SECOND_COLOR
    assert combo.previous_pawn == (0, 5)
    assert combo.previous_empty == (1, 5)
    assert combo.previous_move_type == MOVEMENT_DOWN
    assert combo.other_side_of_previous == MOVEMENT_UP
    assert combo.new_pawn == (1, 5)


def test_create_combo_invalid_move():
    with pytest.raises(TypeError):
        Combo('move', (0, 5), (1, 5))


def test_create_combo_invalid_type_pawn_cords():
    pawns = Pawns(Board())
    with pytest.raises(TypeError):
        Combo(Move(Hit(pawns, SECOND_COLOR)), [0, 5], (1, 5))


def test_create_combo_invalid_type_empty_cords():
    pawns = Pawns(Board())
    with pytest.raises(TypeError):
        Combo(Move(Hit(pawns, SECOND_COLOR)), (1, 5), [0, 5])


def test_create_combo_pawn_cords_too_long():
    pawns = Pawns(Board())
    with pytest.raises(TypeError):
        Combo(Move(Hit(pawns, SECOND_COLOR)), (0, 5, 4), (1, 5))


def test_create_combo_empty_cords_too_long():
    pawns = Pawns(Board())
    with pytest.raises(TypeError):
        Combo(Move(Hit(pawns, SECOND_COLOR)), (0, 5), (1, 4, 5))


def test_create_combo_pawn_cords_out_of_range():
    pawns = Pawns(Board())
    with pytest.raises(ValueError):
        Combo(Move(Hit(pawns, SECOND_COLOR)), (0, 15), (1, 5))


def test_create_combo_empty_cords_out_of_range():
    pawns = Pawns(Board())
    with pytest.raises(ValueError):
        Combo(Move(Hit(pawns, SECOND_COLOR)), (0, 5), (-1, 5))


# ---------------------------------------- possible_combo()


def test_possible_combo_return_true():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)
    combo = Combo(Move(Hit(pawns, SECOND_COLOR)), (0, 5), (1, 5))
    assert combo.possible_combo() is True


def test_possible_combo_2():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)
    combo = Combo(Move(Hit(pawns, SECOND_COLOR)), (1, 6), (0, 6))
    assert combo.possible_combo() is True


def test_possible_combo_cannot_hit():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [EMPTY_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)
    combo = Combo(Move(Hit(pawns, SECOND_COLOR)), (1, 0), (2, 0))
    assert combo.possible_combo() is False


def test_possible_combo_repeated_move_type():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)
    combo = Combo(Move(Hit(pawns, SECOND_COLOR)), (3, 4), (2, 4))
    assert combo.possible_combo() is False


# ---------------------------------------- possible_combo()


def test_find_empty_for_combo():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)
    combo = Combo(Move(Hit(pawns, SECOND_COLOR)), (1, 6), (0, 6))
    assert combo.find_empty_for_combo() == [(1, 5)]


def test_find_empty_for_combo_2():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR],
        [EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)
    combo = Combo(Move(Hit(pawns, SECOND_COLOR)), (0, 5), (1, 5))
    assert combo.find_empty_for_combo() == [(1, 6)]


def test_find_empty_for_combo_repeated_move_type():
    pawns = Pawns(Board())
    new_pawns = [
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, EMPTY_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR, SECOND_COLOR],
        [SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR, SECOND_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, EMPTY_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR],
        [FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR, FIRST_COLOR]
    ]
    pawns.set_actual_pawns(new_pawns)
    combo = Combo(Move(Hit(pawns, SECOND_COLOR)), (3, 4), (2, 4))
    assert combo.find_empty_for_combo() == []
