from source.constants import (
    MOVEMENT_UP,
    MOVEMENT_DIAGONAL_RIGHT_UP,
    MOVEMENT_SIDEWAYS_RIGHT,
    MOVEMENT_DIAGONAL_RIGHT_DOWN,
    MOVEMENT_DOWN,
    MOVEMENT_DIAGONAL_LEFT_DOWN,
    MOVEMENT_SIDEWAYS_LEFT,
    MOVEMENT_DIAGONAL_LEFT_UP,
    EMPTY_COLOR
)
from source.movement import Movement
from source.turn import Turn


class Hit(Turn):
    """
    Class Hit. Inherits from the class Turn. Contains attributes:
    :param pawns: two-dimensional list of pawns set on the board
    :type pawns: list

    :param turn: holds whose turn it is, first or second player
    :type turn: string
    """
    def __init__(self, pawns, turn):
        """
        Creates an instance of Hit.
        """
        super().__init__(pawns, turn)
        self._movement_types = [
            MOVEMENT_DIAGONAL_LEFT_UP,
            MOVEMENT_UP,
            MOVEMENT_DIAGONAL_RIGHT_UP,
            MOVEMENT_SIDEWAYS_RIGHT,
            MOVEMENT_DIAGONAL_RIGHT_DOWN,
            MOVEMENT_DOWN,
            MOVEMENT_DIAGONAL_LEFT_DOWN,
            MOVEMENT_SIDEWAYS_LEFT
        ]

    def which_can_move(self):
        """
        :return: a list of co-ordinates of pawns that can move, because they have an empty space around them.
        """
        result_pawns = []
        for index_row, row in enumerate(self.pawns()):
            for index, pawn in enumerate(row):
                if pawn == self.turn():
                    if self._can_move(index, index_row):
                        result_pawns.append((index_row, index))
        return result_pawns

    def _can_move(self, index, index_row):
        """
        :param index: number of column in which a pawn is seated
        :param index_row: number of row in which a pawn is seated
        :return: True if pawn have an empty space around
        """
        return (
                Movement.diagonal_movement_to_left_up(self.pawns(), index_row, index, EMPTY_COLOR) or
                Movement.up_movement(self.pawns(), index_row, index, EMPTY_COLOR) or
                Movement.diagonal_movement_to_right_up(self.pawns(), index_row, index, EMPTY_COLOR) or
                Movement.down_movement(self.pawns(), index_row, index, EMPTY_COLOR) or
                Movement.diagonal_movement_to_left_down(self.pawns(), index_row, index, EMPTY_COLOR) or
                Movement.diagonal_movement_to_right_down(self.pawns(), index_row, index, EMPTY_COLOR) or
                Movement.sideways_movement_to_left(self.pawns(), index_row, index, EMPTY_COLOR) or
                Movement.sideways_movement_to_right(self.pawns(), index_row, index, EMPTY_COLOR)
        )

    def where_can_move(self):
        """
        :return: dictionary where keys are pawns which can move and values are lists of empty spaces around them
        """
        moving_pawns = self.which_can_move()
        where = {}

        for pawn in moving_pawns:
            where_for_pawn = []
            """
            ((Movement.{move_type} returns True or False), the difference in the first coordinate of the pawn and the
            empty space, the difference in the second coordinate of the pawn and the empty space)
            """
            tab_of_movements = [
                (Movement.diagonal_movement_to_left_up(self.pawns(), pawn[0], pawn[1], EMPTY_COLOR), -1, -1),
                (Movement.up_movement(self.pawns(), pawn[0], pawn[1], EMPTY_COLOR), -1, 0),
                (Movement.diagonal_movement_to_right_up(self.pawns(), pawn[0], pawn[1], EMPTY_COLOR), -1, 1),
                (Movement.sideways_movement_to_right(self.pawns(), pawn[0], pawn[1], EMPTY_COLOR), 0, 1),
                (Movement.diagonal_movement_to_right_down(self.pawns(), pawn[0], pawn[1], EMPTY_COLOR), 1, 1),
                (Movement.down_movement(self.pawns(), pawn[0], pawn[1], EMPTY_COLOR), 1, 0),
                (Movement.diagonal_movement_to_left_down(self.pawns(), pawn[0], pawn[1], EMPTY_COLOR), 1, -1),
                (Movement.sideways_movement_to_left(self.pawns(), pawn[0], pawn[1], EMPTY_COLOR), 0, -1),
            ]
            for movement in tab_of_movements:
                if movement[0]:
                    where_for_pawn.append((pawn[0] + movement[1], pawn[1] + movement[2]))
            where[pawn] = where_for_pawn

        return where

    def which_can_hit(self):
        """
        :return: set of co-ordinates of pawns that can hit another pawn
        """
        which = []
        which_withdrawal = self.which_can_hit_by_withdrawal()
        for element in which_withdrawal:
            which.append(element)

        which_approach = self.which_can_hit_by_approach()
        for element in which_approach:
            which.append(element)

        return [] if not which else list(set(which))

    def which_can_hit_by_approach(self):
        """
        :return: set of co-ordinates of pawns that can hit another pawn by approach
        """
        moving_pawns = self.where_can_move()
        which = []

        for pawn in moving_pawns:
            for empty in moving_pawns[pawn]:
                if self._check_by_approach(pawn, empty, pawn) is not None:
                    which.append(self._check_by_approach(pawn, empty, pawn))

        return [] if not which else list(set(which))

    def _check_by_approach(self, pawn, empty, what_append):
        """
        :param pawn: co-ordinates of a pawn from self.which_can_move()
        :param empty: co-ordinates of an empty space for the pawn from self.where_can_move()
        :param what_append: variable to return, so it can be appended somewhere
        :return: what_append if the pawn can move to the empty space and hit by approach
        """
        move_type = Movement.recognize_move(pawn, empty)
        movement_by_approach = [
            Movement.diagonal_movement_to_left_up(self.pawns(), empty[0], empty[1], self.pawn_to_hit()),
            Movement.up_movement(self.pawns(), empty[0], empty[1], self.pawn_to_hit()),
            Movement.diagonal_movement_to_right_up(self.pawns(), empty[0], empty[1], self.pawn_to_hit()),
            Movement.sideways_movement_to_right(self.pawns(), empty[0], empty[1], self.pawn_to_hit()),
            Movement.diagonal_movement_to_right_down(self.pawns(), empty[0], empty[1], self.pawn_to_hit()),
            Movement.down_movement(self.pawns(), empty[0], empty[1], self.pawn_to_hit()),
            Movement.diagonal_movement_to_left_down(self.pawns(), empty[0], empty[1], self.pawn_to_hit()),
            Movement.sideways_movement_to_left(self.pawns(), empty[0], empty[1], self.pawn_to_hit())
        ]

        for movement_type, approach in zip(self._movement_types, movement_by_approach):
            if movement_type == move_type and approach:
                return what_append
        return None

    def which_can_hit_by_withdrawal(self):
        """
        :return: set of co-ordinates of pawns that can hit another pawn by withdrawal
        """
        moving_pawns = self.where_can_move()
        which = []

        for pawn in moving_pawns:
            for empty in moving_pawns[pawn]:
                if self._check_by_withdrawal(pawn, empty, pawn) is not None:
                    which.append(self._check_by_withdrawal(pawn, empty, pawn))
        return [] if not which else set(which)

    def _check_by_withdrawal(self, pawn, empty, what_append):
        """
        :param pawn: co-ordinates of a pawn from self.which_can_move()
        :param empty: co-ordinates of an empty space for the pawn from self.where_can_move()
        :param what_append: variable to return, so it can be appended somewhere
        :return: what_append if the pawn can move to the empty space and hit by withdrawal
        """
        move_type = Movement.recognize_move(pawn, empty)
        movement_by_withdrawal = [
            Movement.diagonal_movement_to_right_down(self.pawns(), pawn[0], pawn[1], self.pawn_to_hit()),
            Movement.down_movement(self.pawns(), pawn[0], pawn[1], self.pawn_to_hit()),
            Movement.diagonal_movement_to_left_down(self.pawns(), pawn[0], pawn[1], self.pawn_to_hit()),
            Movement.sideways_movement_to_left(self.pawns(), pawn[0], pawn[1], self.pawn_to_hit()),
            Movement.diagonal_movement_to_left_up(self.pawns(), pawn[0], pawn[1], self.pawn_to_hit()),
            Movement.up_movement(self.pawns(), pawn[0], pawn[1], self.pawn_to_hit()),
            Movement.diagonal_movement_to_right_up(self.pawns(), pawn[0], pawn[1], self.pawn_to_hit()),
            Movement.sideways_movement_to_right(self.pawns(), pawn[0], pawn[1], self.pawn_to_hit())
        ]

        for movement_type, withdrawal in zip(self._movement_types, movement_by_withdrawal):
            if movement_type == move_type and withdrawal:
                return what_append
        return None

    def where_can_hit(self):
        """
        :return: dictionary where keys are co-ordinates of pawns from self.which_can_hit() and values are co-ordinates
        of empty spaces where they can move to capture opponent's pawns
        """
        by_withdrawal = self.where_can_hit_by_withdrawal()
        by_approach = self.where_can_hit_by_approach()
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

    def where_can_hit_by_approach(self):
        """
        :return: dictionary where keys are co-ordinates of pawns from self.which_can_hit() and values are co-ordinates
        of empty spaces where they can move to capture by approach opponent's pawns
        """
        hitting_pawns = self.which_can_hit_by_approach()
        possible_move = self.where_can_move()
        where = {}

        for pawn in possible_move:
            if pawn not in hitting_pawns:
                continue
            where_for_pawn = []
            for empty in possible_move[pawn]:
                if self._check_by_approach(pawn, empty, empty) is not None:
                    where_for_pawn.append(self._check_by_approach(pawn, empty, empty))
            where[pawn] = where_for_pawn
        return where

    def where_can_hit_by_withdrawal(self):
        """
        :return: dictionary where keys are co-ordinates of pawns from self.which_can_hit() and values are co-ordinates
        of empty spaces where they can move to capture by withdrawal opponent's pawns
        """
        hitting_pawns = self.which_can_hit_by_withdrawal()
        possible_move = self.where_can_move()
        where = {}

        for pawn in possible_move:
            if pawn not in hitting_pawns:
                continue
            for empty in possible_move[pawn]:
                where_for_pawn = []
                if self._check_by_withdrawal(pawn, empty, empty) is not None:
                    where_for_pawn.append(self._check_by_withdrawal(pawn, empty, empty))
                    where[pawn] = where_for_pawn
        return where

    def which_hits_by_withdrawal(self):
        """
        :return: dictionary where keys are tuples of pawn's and empty space's co-ordinates and values are co-ordinates
        of opponent's pawns which the pawn can capture by withdrawal by moving to the empty space
        """
        hitting_pawns = self.where_can_hit_by_withdrawal()
        which_hits = {}

        for pawn in hitting_pawns:
            for empty in hitting_pawns[pawn]:
                hits = []
                move_type = Movement.recognize_move(pawn, empty)
                for i in range(0, self.width() + 1):
                    movement_types = {
                        MOVEMENT_DIAGONAL_LEFT_UP: Movement.diagonal_movement_to_right_down(self.pawns(), pawn[0] + i, pawn[1] + i, self.pawn_to_hit()),
                        MOVEMENT_UP: Movement.down_movement(self.pawns(), pawn[0] + i, pawn[1], self.pawn_to_hit()),
                        MOVEMENT_DIAGONAL_RIGHT_UP: Movement.diagonal_movement_to_left_down(self.pawns(), pawn[0] + i, pawn[1] - i, self.pawn_to_hit()),
                        MOVEMENT_SIDEWAYS_RIGHT: Movement.sideways_movement_to_left(self.pawns(), pawn[0], pawn[1] - i, self.pawn_to_hit()),
                        MOVEMENT_DIAGONAL_RIGHT_DOWN: Movement.diagonal_movement_to_left_up(self.pawns(), pawn[0] - i, pawn[1] - i, self.pawn_to_hit()),
                        MOVEMENT_DOWN: Movement.up_movement(self.pawns(), pawn[0] - i, pawn[1], self.pawn_to_hit()),
                        MOVEMENT_DIAGONAL_LEFT_DOWN: Movement.diagonal_movement_to_right_up(self.pawns(), pawn[0] - i, pawn[1] + i, self.pawn_to_hit()),
                        MOVEMENT_SIDEWAYS_LEFT: Movement.sideways_movement_to_right(self.pawns(), pawn[0], pawn[1] + i, self.pawn_to_hit())
                    }
                    delta_to_append = {
                        MOVEMENT_DIAGONAL_LEFT_UP: (i+1, 1+1),
                        MOVEMENT_UP: (i+1, 0),
                        MOVEMENT_DIAGONAL_RIGHT_UP: (i+1, -i-1),
                        MOVEMENT_SIDEWAYS_RIGHT: (0, -i-1),
                        MOVEMENT_DIAGONAL_RIGHT_DOWN: (-i-1, -i-1),
                        MOVEMENT_DOWN: (-i-1, 0),
                        MOVEMENT_DIAGONAL_LEFT_DOWN: (-i-1, i+1),
                        MOVEMENT_SIDEWAYS_LEFT: (0, i+1)
                    }
                    if movement_types.get(move_type):
                        delta_first_cords = delta_to_append.get(move_type)[0]
                        delta_second_cords = delta_to_append.get(move_type)[1]
                        hits.append((pawn[0]+delta_first_cords, pawn[1]+delta_second_cords))
                    else:
                        break
                which_hits[(pawn, empty)] = hits
                # if move_type == MOVEMENT_DIAGONAL_LEFT_UP:
                #     for i in range(0, self.width() + 1):
                #         if Movement.diagonal_movement_to_right_down(self.pawns(), pawn[0] + i, pawn[1] + i, self.pawn_to_hit()):
                #             hits.append((pawn[0] + i + 1, pawn[1] + i + 1))
                #         else:
                #             break
                # elif move_type == MOVEMENT_UP:
                #     for i in range(0, self.width() + 1):
                #         if Movement.down_movement(self.pawns(), pawn[0] + i, pawn[1], self.pawn_to_hit()):
                #             hits.append((pawn[0] + i + 1, pawn[1]))
                #         else:
                #             break
                # elif move_type == MOVEMENT_DIAGONAL_RIGHT_UP:
                #     for i in range(0, self.width() + 1):
                #         if Movement.diagonal_movement_to_left_down(self.pawns(), pawn[0] + i, pawn[1] - i, self.pawn_to_hit()):
                #             hits.append((pawn[0] + i + 1, pawn[1] - i - 1))
                #         else:
                #             break
                # elif move_type == MOVEMENT_SIDEWAYS_RIGHT:
                #     for i in range(0, self.width() + 1):
                #         if Movement.sideways_movement_to_left(self.pawns(), pawn[0], pawn[1] - i, self.pawn_to_hit()):
                #             hits.append((pawn[0], pawn[1] - i - 1))
                #         else:
                #             break
                # elif move_type == MOVEMENT_DIAGONAL_RIGHT_DOWN:
                #     for i in range(0, self.width() + 1):
                #         if Movement.diagonal_movement_to_left_up(self.pawns(), pawn[0] - i, pawn[1] - i, self.pawn_to_hit()):
                #             hits.append((pawn[0] - i - 1, pawn[1] - i - 1))
                #         else:
                #             break
                # elif move_type == MOVEMENT_DOWN:
                #     for i in range(0, self.width() + 1):
                #         if Movement.up_movement(self.pawns(), pawn[0] - i, pawn[1], self.pawn_to_hit()):
                #             hits.append((pawn[0] - i - 1, pawn[1]))
                #         else:
                #             break
                # elif move_type == MOVEMENT_DIAGONAL_LEFT_DOWN:
                #     for i in range(0, self.width() + 1):
                #         if Movement.diagonal_movement_to_right_up(self.pawns(), pawn[0] - i, pawn[1] + i, self.pawn_to_hit()):
                #             hits.append((pawn[0] - i - 1, pawn[1] + i + 1))
                #         else:
                #             break
                # elif move_type == MOVEMENT_SIDEWAYS_LEFT:
                #     for i in range(0, self.width() + 1):
                #         if Movement.sideways_movement_to_right(self.pawns(), pawn[0], pawn[1] + i, self.pawn_to_hit()):
                #             hits.append((pawn[0], pawn[1] + i + 1))
                #         else:
                #             break
                # which_hits[(pawn, empty)] = hits
        return which_hits

    def which_hits_by_approach(self):
        """
        :return: dictionary where keys are tuples of pawn's and empty space's co-ordinates and values are co-ordinates
        of opponent's pawns which the pawn can capture by approach by moving to the empty space
        """
        hitting_pawns = self.where_can_hit_by_approach()
        which_hits = {}

        for pawn in hitting_pawns:
            for empty in hitting_pawns[pawn]:
                hits = []
                move_type = Movement.recognize_move(pawn, empty)
                if move_type == MOVEMENT_DIAGONAL_LEFT_UP:
                    for i in range(0, self.width() + 1):
                        if Movement.diagonal_movement_to_left_up(self.pawns(), empty[0] - i, empty[1] - i, self.pawn_to_hit()):
                            hits.append((empty[0] - i - 1, empty[1] - i - 1))
                        else:
                            break
                elif move_type == MOVEMENT_UP:
                    for i in range(0, self.width() + 1):
                        if Movement.up_movement(self.pawns(), empty[0] - i, empty[1], self.pawn_to_hit()):
                            hits.append((empty[0] - i - 1, empty[1]))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_RIGHT_UP:
                    for i in range(0, self.width() + 1):
                        if Movement.diagonal_movement_to_right_up(self.pawns(), empty[0] - i, empty[1] + i, self.pawn_to_hit()):
                            hits.append((empty[0] - i - 1, empty[1] + i + 1))
                        else:
                            break
                elif move_type == MOVEMENT_SIDEWAYS_RIGHT:
                    for i in range(0, self.width() + 1):
                        if Movement.sideways_movement_to_right(self.pawns(), empty[0], empty[1] + i, self.pawn_to_hit()):
                            hits.append((empty[0], empty[1] + i + 1))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_RIGHT_DOWN:
                    for i in range(0, self.width() + 1):
                        if Movement.diagonal_movement_to_right_down(self.pawns(), empty[0] + i, empty[1] + i, self.pawn_to_hit()):
                            hits.append((empty[0] + i + 1, empty[1] + i + 1))
                        else:
                            break
                elif move_type == MOVEMENT_DOWN:
                    for i in range(0, self.width() + 1):
                        if Movement.down_movement(self.pawns(), empty[0] + i, empty[1], self.pawn_to_hit()):
                            hits.append((empty[0] + i + 1, empty[1]))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_LEFT_DOWN:
                    for i in range(0, self.width() + 1):
                        if Movement.diagonal_movement_to_left_down(self.pawns(), empty[0] + i, empty[1] - i, self.pawn_to_hit()):
                            hits.append((empty[0] + i + 1, empty[1] - i - 1))
                        else:
                            break
                elif move_type == MOVEMENT_SIDEWAYS_LEFT:
                    for i in range(0, self.width() + 1):
                        if Movement.sideways_movement_to_left(self.pawns(), empty[0], empty[1] - i, self.pawn_to_hit()):
                            hits.append((empty[0], empty[1] - i - 1))
                        else:
                            break
                which_hits[(pawn, empty)] = hits
        return which_hits

    def if_can_hit_by_approach_and_by_withdrawal(self, pawn, empty):
        """
        :param pawn: co-ordinates of a pawn that player wants to move
        :param empty: co-ordinates of an empty space where player wants to move the pawn
        :return: True if player has a choice to capture opponent's pawns by withdrawal or by approach
        """
        if (pawn, empty) not in self.which_hits_by_withdrawal().keys():
            return False
        if (pawn, empty) not in self.which_hits_by_approach().keys():
            return False
        return True
