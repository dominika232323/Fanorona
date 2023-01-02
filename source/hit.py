from configuration import (
    MOVEMENT_UP,
    MOVEMENT_DIAGONAL_RIGHT_UP,
    MOVEMENT_SIDEWAYS_RIGHT,
    MOVEMENT_DIAGONAL_RIGHT_DOWN,
    MOVEMENT_DOWN,
    MOVEMENT_DIAGONAL_LEFT_DOWN,
    MOVEMENT_SIDEWAYS_LEFT,
    MOVEMENT_DIAGONAL_LEFT_UP,
    FIRST_COLOR,
    SECOND_COLOR,
    EMPTY_COLOR
)
from source.pawns import Pawns
from source.movement import Movement
from source.turn import Turn


class Hit:
    @staticmethod
    def __init__(pawns, turn):
        Hit._validate(pawns, turn)
        Hit._pawns = pawns.actual_pawns
        Hit._turn = turn
        Hit._pawn_to_hit = FIRST_COLOR if turn == SECOND_COLOR else SECOND_COLOR
        Hit._length = pawns.board_length
        Hit._width = pawns.board_width

    @staticmethod
    def _validate(pawns, turn):
        if not isinstance(pawns, Pawns):
            raise TypeError
        if turn != FIRST_COLOR and turn != SECOND_COLOR:
            raise ValueError('This type of pawn does not exist.')

    @staticmethod
    def pawns():
        return Hit._pawns

    @staticmethod
    def turn():
        return Hit._turn

    @staticmethod
    def pawn_to_hit():
        return Hit._pawn_to_hit

    @staticmethod
    def length():
        return Hit._length

    @staticmethod
    def width():
        return Hit._width

    @staticmethod
    def which_can_move():
        """
        Returns a list of co-ordinates of pawns that can move, because they have an empty space near them.
        """
        result_pawns = []
        for index_row, row in enumerate(Hit.pawns()):
            for index, pawn in enumerate(row):
                if pawn == Hit.turn():
                    if Hit._can_move(index, index_row):
                        result_pawns.append((index_row, index))
        return result_pawns

    @staticmethod
    def _can_move(index, index_row):
        return (
                Movement.diagonal_movement_to_left_up(Hit.pawns(), index_row, index, EMPTY_COLOR) or
                Movement.up_movement(Hit.pawns(), index_row, index, EMPTY_COLOR) or
                Movement.diagonal_movement_to_right_up(Hit.pawns(), index_row, index, EMPTY_COLOR) or
                Movement.down_movement(Hit.pawns(), index_row, index, EMPTY_COLOR) or
                Movement.diagonal_movement_to_left_down(Hit.pawns(), index_row, index, EMPTY_COLOR) or
                Movement.diagonal_movement_to_right_down(Hit.pawns(), index_row, index, EMPTY_COLOR) or
                Movement.sideways_movement_to_left(Hit.pawns(), index_row, index, EMPTY_COLOR) or
                Movement.sideways_movement_to_right(Hit.pawns(), index_row, index, EMPTY_COLOR)
        )

    @staticmethod
    def where_can_move():
        which = Hit.which_can_move()
        where = {}

        for indexs in which:
            where_for_pawn = []
            tab = [
                (Movement.diagonal_movement_to_left_up(Hit.pawns(), indexs[0], indexs[1], EMPTY_COLOR), -1, -1),
                (Movement.up_movement(Hit.pawns(), indexs[0], indexs[1], EMPTY_COLOR), -1, 0),
                (Movement.diagonal_movement_to_right_up(Hit.pawns(), indexs[0], indexs[1], EMPTY_COLOR), -1, 1),
                (Movement.sideways_movement_to_right(Hit.pawns(), indexs[0], indexs[1], EMPTY_COLOR), 0, 1),
                (Movement.diagonal_movement_to_right_down(Hit.pawns(), indexs[0], indexs[1], EMPTY_COLOR), 1, 1),
                (Movement.down_movement(Hit.pawns(), indexs[0], indexs[1], EMPTY_COLOR), 1, 0),
                (Movement.diagonal_movement_to_left_down(Hit.pawns(), indexs[0], indexs[1], EMPTY_COLOR), 1, -1),
                (Movement.sideways_movement_to_left(Hit.pawns(), indexs[0], indexs[1], EMPTY_COLOR), 0, -1),
            ]
            for t in tab:
                if t[0]:
                    where_for_pawn.append((indexs[0] + t[1], indexs[1] + t[2]))
            where[indexs] = where_for_pawn

        return where

    @staticmethod
    def which_can_hit():
        which = []
        which_withdrawal = Hit.which_can_hit_by_withdrawal()
        for element in which_withdrawal:
            which.append(element)

        which_approach = Hit.which_can_hit_by_approach()
        for element in which_approach:
            which.append(element)

        return [] if not which else set(which)

    @staticmethod
    def which_can_hit_by_approach():
        moving_pawns = Hit.where_can_move()
        which = []

        for pawn in moving_pawns:
            for empty in moving_pawns[pawn]:
                if Hit._check_by_approach(pawn, empty, pawn) is not None:
                    which.append(Hit._check_by_approach(pawn, empty, pawn))

        return [] if not which else set(which)

    @staticmethod
    def _check_by_approach(pawn, empty, what_append):
        move_type = Movement.recognize_move(pawn, empty)
        if move_type == MOVEMENT_DIAGONAL_LEFT_UP and Movement.diagonal_movement_to_left_up(Hit.pawns(), empty[0], empty[1], Hit.pawn_to_hit()):
            return what_append
        if move_type == MOVEMENT_UP and Movement.up_movement(Hit.pawns(), empty[0], empty[1], Hit.pawn_to_hit()):
            return what_append
        if move_type == MOVEMENT_DIAGONAL_RIGHT_UP and Movement.diagonal_movement_to_right_up(Hit.pawns(), empty[0], empty[1], Hit.pawn_to_hit()):
            return what_append
        if move_type == MOVEMENT_SIDEWAYS_RIGHT and Movement.sideways_movement_to_right(Hit.pawns(), empty[0], empty[1], Hit.pawn_to_hit()):
            return what_append
        if move_type == MOVEMENT_DIAGONAL_RIGHT_DOWN and Movement.diagonal_movement_to_right_down(Hit.pawns(), empty[0], empty[1], Hit.pawn_to_hit()):
            return what_append
        if move_type == MOVEMENT_DOWN and Movement.down_movement(Hit.pawns(), empty[0], empty[1], Hit.pawn_to_hit()):
            return what_append
        if move_type == MOVEMENT_DIAGONAL_LEFT_DOWN and Movement.diagonal_movement_to_left_down(Hit.pawns(), empty[0], empty[1], Hit.pawn_to_hit()):
            return what_append
        if move_type == MOVEMENT_SIDEWAYS_LEFT and Movement.sideways_movement_to_left(Hit.pawns(), empty[0], empty[1], Hit.pawn_to_hit()):
            return what_append
        return None

    @staticmethod
    def which_can_hit_by_withdrawal():
        moving_pawns = Hit.where_can_move()
        which = []

        for pawn in moving_pawns:
            for empty in moving_pawns[pawn]:
                if Hit._check_by_withdrawal(pawn, empty, pawn) is not None:
                    which.append(Hit._check_by_withdrawal(pawn, empty, pawn))
        return [] if not which else set(which)

    @staticmethod
    def _check_by_withdrawal(pawn, empty, what_append):
        move_type = Movement.recognize_move(pawn, empty)
        if move_type == MOVEMENT_DIAGONAL_LEFT_UP and Movement.diagonal_movement_to_right_down(Hit.pawns(), pawn[0], pawn[1], Hit.pawn_to_hit()):
            return what_append
        if move_type == MOVEMENT_UP and Movement.down_movement(Hit.pawns(), pawn[0], pawn[1], Hit.pawn_to_hit()):
            return what_append
        if move_type == MOVEMENT_DIAGONAL_RIGHT_UP and Movement.diagonal_movement_to_left_down(Hit.pawns(), pawn[0], pawn[1], Hit.pawn_to_hit()):
            return what_append
        if move_type == MOVEMENT_SIDEWAYS_RIGHT and Movement.sideways_movement_to_left(Hit.pawns(), pawn[0], pawn[1], Hit.pawn_to_hit()):
            return what_append
        if move_type == MOVEMENT_DIAGONAL_RIGHT_DOWN and Movement.diagonal_movement_to_left_up(Hit.pawns(), pawn[0], pawn[1], Hit.pawn_to_hit()):
            return what_append
        if move_type == MOVEMENT_DOWN and Movement.up_movement(Hit.pawns(), pawn[0], pawn[1], Hit.pawn_to_hit()):
            return what_append
        if move_type == MOVEMENT_DIAGONAL_LEFT_DOWN and Movement.diagonal_movement_to_right_up(Hit.pawns(), pawn[0], pawn[1], Hit.pawn_to_hit()):
            return what_append
        if move_type == MOVEMENT_SIDEWAYS_LEFT and Movement.sideways_movement_to_right(Hit.pawns(), pawn[0], pawn[1], Hit.pawn_to_hit()):
            return what_append
        return None

    @staticmethod
    def where_can_hit():
        by_withdrawal = Hit.where_can_hit_by_withdrawal()
        by_approach = Hit.where_can_hit_by_approach()
        where = {}

        for pawn in by_withdrawal:
            where[pawn] = by_withdrawal[pawn]

        for pawn in by_approach:
            if pawn in where:
                for element in by_approach[pawn]:
                    if element not in where[pawn]:
                        where[pawn].append(element)
            else:
                where[pawn] = by_approach[pawn]

        return where

    @staticmethod
    def where_can_hit_by_approach():
        hitting_pawns = Hit.which_can_hit_by_approach()
        possible_move = Hit.where_can_move()
        where = {}

        for pawn in possible_move:
            if pawn not in hitting_pawns:
                continue
            where_for_pawn = []
            for empty in possible_move[pawn]:
                if Hit._check_by_approach(pawn, empty, empty) is not None:
                    where_for_pawn.append(Hit._check_by_approach(pawn, empty, empty))
            where[pawn] = where_for_pawn
        return where

    @staticmethod
    def where_can_hit_by_withdrawal():
        hitting_pawns = Hit.which_can_hit_by_withdrawal()
        possible_move = Hit.where_can_move()
        where = {}

        for pawn in possible_move:
            if pawn not in hitting_pawns:
                continue
            for empty in possible_move[pawn]:
                where_for_pawn = []
                if Hit._check_by_withdrawal(pawn, empty, empty) is not None:
                    where_for_pawn.append(Hit._check_by_withdrawal(pawn, empty, empty))
                    where[pawn] = where_for_pawn
        return where

    @staticmethod
    def which_hits():
        # dic = {[(pawns cords), (empty cords)]: [cords of each pawn that hits]}
        pass

    @staticmethod
    def which_hits_by_withdrawal():
        hitting_pawns = Hit.where_can_hit_by_withdrawal()
        which_hits = {}

        for pawn in hitting_pawns:
            for empty in hitting_pawns[pawn]:
                hits = []
                move_type = Movement.recognize_move(pawn, empty)
                if move_type == MOVEMENT_DIAGONAL_LEFT_UP:
                    for i in range(0, Hit.width() + 1):
                        if Movement.diagonal_movement_to_right_down(Hit.pawns(), pawn[0] + i, pawn[1] + i, Hit.pawn_to_hit()):
                            hits.append((pawn[0] + i + 1, pawn[1] + i + 1))
                        else:
                            break
                elif move_type == MOVEMENT_UP:
                    for i in range(0, Hit.width() + 1):
                        if Movement.down_movement(Hit.pawns(), pawn[0] + i, pawn[1], Hit.pawn_to_hit()):
                            hits.append((pawn[0] + i + 1, pawn[1]))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_RIGHT_UP:
                    for i in range(0, Hit.width() + 1):
                        if Movement.diagonal_movement_to_left_down(Hit.pawns(), pawn[0] + i, pawn[1] - i, Hit.pawn_to_hit()):
                            hits.append((pawn[0] + i + 1, pawn[1] - i - 1))
                        else:
                            break
                elif move_type == MOVEMENT_SIDEWAYS_RIGHT:
                    for i in range(0, Hit.width() + 1):
                        if Movement.sideways_movement_to_left(Hit.pawns(), pawn[0], pawn[1] - i, Hit.pawn_to_hit()):
                            hits.append((pawn[0], pawn[1] - i - 1))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_RIGHT_DOWN:
                    for i in range(0, Hit.width() + 1):
                        if Movement.diagonal_movement_to_left_up(Hit.pawns(), pawn[0] - i, pawn[1] - i, Hit.pawn_to_hit()):
                            hits.append((pawn[0] - i - 1, pawn[1] - i - 1))
                        else:
                            break
                elif move_type == MOVEMENT_DOWN:
                    for i in range(0, Hit.width() + 1):
                        if Movement.up_movement(Hit.pawns(), pawn[0] - i, pawn[1], Hit.pawn_to_hit()):
                            hits.append((pawn[0] - i - 1, pawn[1]))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_LEFT_DOWN:
                    for i in range(0, Hit.width() + 1):
                        if Movement.diagonal_movement_to_right_up(Hit.pawns(), pawn[0] - i, pawn[1] + i, Hit.pawn_to_hit()):
                            hits.append((pawn[0] - i - 1, pawn[1] + i + 1))
                        else:
                            break
                elif move_type == MOVEMENT_SIDEWAYS_LEFT:
                    for i in range(0, Hit.width() + 1):
                        if Movement.sideways_movement_to_right(Hit.pawns(), pawn[0], pawn[1] + i, Hit.pawn_to_hit()):
                            hits.append((pawn[0], pawn[1] + i + 1))
                        else:
                            break
                which_hits[(pawn, empty)] = hits
        return which_hits

    @staticmethod
    def which_hits_by_approach():
        hitting_pawns = Hit.where_can_hit_by_approach()
        which_hits = {}

        for pawn in hitting_pawns:
            for empty in hitting_pawns[pawn]:
                hits = []
                move_type = Movement.recognize_move(pawn, empty)
                if move_type == MOVEMENT_DIAGONAL_LEFT_UP:
                    for i in range(0, Hit.width() + 1):
                        if Movement.diagonal_movement_to_left_up(Hit.pawns(), empty[0] - i, empty[1] - i, Hit.pawn_to_hit()):
                            hits.append((empty[0] - i - 1, empty[1] - i - 1))
                        else:
                            break
                elif move_type == MOVEMENT_UP:
                    for i in range(0, Hit.width() + 1):
                        if Movement.up_movement(Hit.pawns(), empty[0] - i, empty[1], Hit.pawn_to_hit()):
                            hits.append((empty[0] - i - 1, empty[1]))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_RIGHT_UP:
                    for i in range(0, Hit.width() + 1):
                        if Movement.diagonal_movement_to_right_up(Hit.pawns(), empty[0] - i, empty[1] + i, Hit.pawn_to_hit()):
                            hits.append((empty[0] - i - 1, empty[1] + i + 1))
                        else:
                            break
                elif move_type == MOVEMENT_SIDEWAYS_RIGHT:
                    for i in range(0, Hit.width() + 1):
                        if Movement.sideways_movement_to_right(Hit.pawns(), empty[0], empty[1] + i, Hit.pawn_to_hit()):
                            hits.append((empty[0], empty[1] + i + 1))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_RIGHT_DOWN:
                    for i in range(0, Hit.width() + 1):
                        if Movement.diagonal_movement_to_right_down(Hit.pawns(), empty[0] + i, empty[1] + i, Hit.pawn_to_hit()):
                            hits.append((empty[0] + i + 1, empty[1] + i + 1))
                        else:
                            break
                elif move_type == MOVEMENT_DOWN:
                    for i in range(0, Hit.width() + 1):
                        if Movement.down_movement(Hit.pawns(), empty[0] + i, empty[1], Hit.pawn_to_hit()):
                            hits.append((empty[0] + i + 1, empty[1]))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_LEFT_DOWN:
                    for i in range(0, Hit.width() + 1):
                        if Movement.diagonal_movement_to_left_down(Hit.pawns(), empty[0] + i, empty[1] - i, Hit.pawn_to_hit()):
                            hits.append((empty[0] + i + 1, empty[1] - i - 1))
                        else:
                            break
                elif move_type == MOVEMENT_SIDEWAYS_LEFT:
                    for i in range(0, Hit.width() + 1):
                        if Movement.sideways_movement_to_left(Hit.pawns(), empty[0], empty[1] - i, Hit.pawn_to_hit()):
                            hits.append((empty[0], empty[1] - i - 1))
                        else:
                            break
                which_hits[(pawn, empty)] = hits
        return which_hits
