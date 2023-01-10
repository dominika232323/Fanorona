from source.configuration import (
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
    def __init__(self, pawns, turn):
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
        Returns a list of co-ordinates of pawns that can move, because they have an empty space near them.
        """
        result_pawns = []
        for index_row, row in enumerate(self.pawns()):
            for index, pawn in enumerate(row):
                if pawn == self.turn():
                    if self._can_move(index, index_row):
                        result_pawns.append((index_row, index))
        return result_pawns

    def _can_move(self, index, index_row):
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
        which = self.which_can_move()
        where = {}

        for indexes in which:
            where_for_pawn = []
            tab_of_movements = [
                (Movement.diagonal_movement_to_left_up(self.pawns(), indexes[0], indexes[1], EMPTY_COLOR), -1, -1),
                (Movement.up_movement(self.pawns(), indexes[0], indexes[1], EMPTY_COLOR), -1, 0),
                (Movement.diagonal_movement_to_right_up(self.pawns(), indexes[0], indexes[1], EMPTY_COLOR), -1, 1),
                (Movement.sideways_movement_to_right(self.pawns(), indexes[0], indexes[1], EMPTY_COLOR), 0, 1),
                (Movement.diagonal_movement_to_right_down(self.pawns(), indexes[0], indexes[1], EMPTY_COLOR), 1, 1),
                (Movement.down_movement(self.pawns(), indexes[0], indexes[1], EMPTY_COLOR), 1, 0),
                (Movement.diagonal_movement_to_left_down(self.pawns(), indexes[0], indexes[1], EMPTY_COLOR), 1, -1),
                (Movement.sideways_movement_to_left(self.pawns(), indexes[0], indexes[1], EMPTY_COLOR), 0, -1),
            ]
            for movement in tab_of_movements:
                if movement[0]:
                    where_for_pawn.append((indexes[0] + movement[1], indexes[1] + movement[2]))
            where[indexes] = where_for_pawn

        return where

    def which_can_hit(self):
        which = []
        which_withdrawal = self.which_can_hit_by_withdrawal()
        for element in which_withdrawal:
            which.append(element)

        which_approach = self.which_can_hit_by_approach()
        for element in which_approach:
            which.append(element)

        return [] if not which else set(which)

    def which_can_hit_by_approach(self):
        moving_pawns = self.where_can_move()
        which = []

        for pawn in moving_pawns:
            for empty in moving_pawns[pawn]:
                if self._check_by_approach(pawn, empty, pawn) is not None:
                    which.append(self._check_by_approach(pawn, empty, pawn))

        return [] if not which else set(which)

    def _check_by_approach(self, pawn, empty, what_append):
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

        for type, approach in zip(self._movement_types, movement_by_approach):
            if type == move_type and approach:
                return what_append
        return None

    def which_can_hit_by_withdrawal(self):
        moving_pawns = self.where_can_move()
        which = []

        for pawn in moving_pawns:
            for empty in moving_pawns[pawn]:
                if self._check_by_withdrawal(pawn, empty, pawn) is not None:
                    which.append(self._check_by_withdrawal(pawn, empty, pawn))
        return [] if not which else set(which)

    def _check_by_withdrawal(self, pawn, empty, what_append):
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

        for type, withdrawal in zip(self._movement_types, movement_by_withdrawal):
            if type == move_type and withdrawal:
                return what_append
        return None

    def where_can_hit(self):
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

    def which_hits(self):
        # dic = {[(pawns cords), (empty cords)]: [cords of each pawn that hits]}
        pass

    def which_hits_by_withdrawal(self):
        hitting_pawns = self.where_can_hit_by_withdrawal()
        which_hits = {}

        for pawn in hitting_pawns:
            for empty in hitting_pawns[pawn]:
                hits = []
                move_type = Movement.recognize_move(pawn, empty)
                if move_type == MOVEMENT_DIAGONAL_LEFT_UP:
                    for i in range(0, self.width() + 1):
                        if Movement.diagonal_movement_to_right_down(self.pawns(), pawn[0] + i, pawn[1] + i, self.pawn_to_hit()):
                            hits.append((pawn[0] + i + 1, pawn[1] + i + 1))
                        else:
                            break
                elif move_type == MOVEMENT_UP:
                    for i in range(0, self.width() + 1):
                        if Movement.down_movement(self.pawns(), pawn[0] + i, pawn[1], self.pawn_to_hit()):
                            hits.append((pawn[0] + i + 1, pawn[1]))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_RIGHT_UP:
                    for i in range(0, self.width() + 1):
                        if Movement.diagonal_movement_to_left_down(self.pawns(), pawn[0] + i, pawn[1] - i, self.pawn_to_hit()):
                            hits.append((pawn[0] + i + 1, pawn[1] - i - 1))
                        else:
                            break
                elif move_type == MOVEMENT_SIDEWAYS_RIGHT:
                    for i in range(0, self.width() + 1):
                        if Movement.sideways_movement_to_left(self.pawns(), pawn[0], pawn[1] - i, self.pawn_to_hit()):
                            hits.append((pawn[0], pawn[1] - i - 1))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_RIGHT_DOWN:
                    for i in range(0, self.width() + 1):
                        if Movement.diagonal_movement_to_left_up(self.pawns(), pawn[0] - i, pawn[1] - i, self.pawn_to_hit()):
                            hits.append((pawn[0] - i - 1, pawn[1] - i - 1))
                        else:
                            break
                elif move_type == MOVEMENT_DOWN:
                    for i in range(0, self.width() + 1):
                        if Movement.up_movement(self.pawns(), pawn[0] - i, pawn[1], self.pawn_to_hit()):
                            hits.append((pawn[0] - i - 1, pawn[1]))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_LEFT_DOWN:
                    for i in range(0, self.width() + 1):
                        if Movement.diagonal_movement_to_right_up(self.pawns(), pawn[0] - i, pawn[1] + i, self.pawn_to_hit()):
                            hits.append((pawn[0] - i - 1, pawn[1] + i + 1))
                        else:
                            break
                elif move_type == MOVEMENT_SIDEWAYS_LEFT:
                    for i in range(0, self.width() + 1):
                        if Movement.sideways_movement_to_right(self.pawns(), pawn[0], pawn[1] + i, self.pawn_to_hit()):
                            hits.append((pawn[0], pawn[1] + i + 1))
                        else:
                            break
                which_hits[(pawn, empty)] = hits
        return which_hits

    def which_hits_by_approach(self):
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
        if (pawn, empty) not in self.which_hits_by_withdrawal().keys():
            return False
        if (pawn, empty) not in self.which_hits_by_approach().keys():
            return False
        return True
