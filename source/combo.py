from source.hit import Hit
from source.move import Move
from source.movement import Movement
from source.turn import Turn
from source.constants import (
    MOVEMENT_UP,
    MOVEMENT_DOWN,
    MOVEMENT_SIDEWAYS_LEFT,
    MOVEMENT_SIDEWAYS_RIGHT,
    MOVEMENT_DIAGONAL_LEFT_DOWN,
    MOVEMENT_DIAGONAL_RIGHT_DOWN,
    MOVEMENT_DIAGONAL_RIGHT_UP,
    MOVEMENT_DIAGONAL_LEFT_UP
)


class Combo:
    """
    Class Combo. Contains attributes:
    :param move: an instance of class Move
    :type move: an instance of class Move

    :param previous_pawn: pawn's co-ordinates from previous move (before move)
    :type previous_pawn: tuple

    :param previous_empty: empty space's co-ordinates from previous move (before move)
    :type previous_empty: tuple
    """
    def __init__(self, move, previous_pawn, previous_empty):
        """
        Creates an instance of Combo.
        """
        self._validate(move, previous_pawn, previous_empty)
        self._previous_pawn = previous_pawn
        self._previous_empty = previous_empty
        self._previous_move_type = Movement.recognize_move(previous_pawn, previous_empty)
        self._other_side_of_previous = self._other_side_of_previous_move_type()
        self.move = move
        self._new_pawn = previous_empty

    @staticmethod
    def _validate(move, previous_pawn, previous_empty):
        """
        :param move: an instance of class Move
        :param previous_pawn: co-ordinates of a pawn in previous move
        :param previous_empty: co-ordinates of an empty space in previous move
        :raise: TypeError if given move is not an instance of class Move
        :raise: TypeError if pawn co-ordinates are not a tuple, or it's length isn't equal 2
        :raise: TypeError if empty space co-ordinates are not a tuple, or it's length isn't equal 2
        :raise: ValueError if given pawn cords are out of range
        :raise: ValueError if given empty space cords are out of range
        """
        if not isinstance(move, Move):
            raise TypeError('Given move is not an instance of class Move')
        if type(previous_pawn) != tuple or len(previous_pawn) != 2:
            raise TypeError('Invalid pawn cords')
        if type(previous_empty) != tuple or len(previous_empty) != 2:
            raise TypeError('Invalid empty space cords')
        if previous_pawn[0] < 0 or previous_pawn[0] >= move.width:
            raise ValueError('First pawn cord out of range')
        if previous_pawn[1] < 0 or previous_pawn[1] >= move.length:
            raise ValueError('Second pawn cord out of range')
        if previous_empty[0] < 0 or previous_empty[0] >= move.width:
            raise ValueError('First empty space cord out of range')
        if previous_empty[1] < 0 or previous_empty[1] >= move.length:
            raise ValueError('Second empty space cord out of range')

    @property
    def pawns(self):
        """
        :return: placement of the pawns on the board
        """
        return self.move.pawns

    @property
    def turn(self):
        """
        :return: whose turn is it, first or second player
        """
        return self.move.turn

    @property
    def previous_pawn(self):
        """
        :return: pawn's co-ordinates from previous move (before move)
        """
        return self._previous_pawn

    @property
    def previous_empty(self):
        """
        :return: empty space's co-ordinates from previous move (before move)
        """
        return self._previous_empty

    @property
    def previous_move_type(self):
        """
        :return: type of movement made in previous move
        """
        return self._previous_move_type

    @property
    def other_side_of_previous(self):
        """
        :return: type of movement made in previous move but in opposite direction
        """
        return self._other_side_of_previous

    @property
    def new_pawn(self):
        """
        :return: pawn's co-ordinates from previous move (after move)
        """
        return self._new_pawn

    def possible_combo(self):
        """
        Checks if the pawn can make combo.
        :return: False if the pawn doesn't have any hits
        :return: True if there is an empty space around the pawn to make combo
        """
        if self._new_pawn not in self.move.hit.which_can_hit():
            return False
        if self.find_empty_for_combo():
            return True
        return False

    def find_empty_for_combo(self):
        """
        :return: list of empty spaces where the pawn can move to make combo
        """
        empties = []
        if self._new_pawn not in self.move.hit.which_can_hit():
            return []
        for empty_space in self.move.hit.where_can_hit()[self._new_pawn]:
            if Movement.recognize_move(self._new_pawn, empty_space) != self._previous_move_type and \
                    Movement.recognize_move(self._new_pawn, empty_space) != self._other_side_of_previous:
                empties.append(empty_space)
        return empties

    def _other_side_of_previous_move_type(self):
        """
        :return: move type with opposite direction to self._previous_move_type
        """
        both_sides_of_move_types = [
            (MOVEMENT_UP, MOVEMENT_DOWN),
            (MOVEMENT_DIAGONAL_LEFT_UP, MOVEMENT_DIAGONAL_RIGHT_DOWN),
            (MOVEMENT_DIAGONAL_RIGHT_UP, MOVEMENT_DIAGONAL_LEFT_DOWN),
            (MOVEMENT_SIDEWAYS_LEFT, MOVEMENT_SIDEWAYS_RIGHT)
        ]
        for move_types in both_sides_of_move_types:
            if self._previous_move_type == move_types[0]:
                return move_types[1]
            elif self._previous_move_type == move_types[1]:
                return move_types[0]
