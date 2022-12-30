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
    MOVEMENT_SIDEWAYS_LEFT,
    CHOICE_WITHDRAWL,
    CHOICE_APPROACH
)
from source.move_types import (
    diagonal_movement_to_left_up,
    up_movement,
    diagonal_movement_to_right_up,
    sideways_movement_to_right,
    diagonal_movement_to_right_down,
    down_movement,
    diagonal_movement_to_left_down,
    sideways_movement_to_left,
)


class Move():
    def __init__(self, pawns, turn):
        self._validate(pawns, turn)
        self._pawns = pawns.actual_pawns
        self._turn = turn
        self._pawn_to_hit = FIRST_COLOR if turn == SECOND_COLOR else SECOND_COLOR
        self._length = pawns.board_length
        self._width = pawns.board_width

    @staticmethod
    def _validate(pawns, turn):
        if not isinstance(pawns, Pawns):
            raise TypeError
        if turn != FIRST_COLOR and turn != SECOND_COLOR:
            raise ValueError('This type of pawn does not exist.')

    @property
    def pawns(self):
        return self._pawns

    @property
    def turn(self):
        return self._turn

    @property
    def pawn_to_hit(self):
        return self._pawn_to_hit

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    def which_can_move(self):
        """
        Returns a list of co-ordinates of pawns that can move, because they have an empty space near them.
        """
        result_pawns = []
        for index_row, row in enumerate(self._pawns):
            for index, pawn in enumerate(row):
                if pawn == self._turn:
                    if diagonal_movement_to_left_up(self._pawns, index_row, index, EMPTY_COLOR):
                        result_pawns.append((index_row, index))
                    elif up_movement(self._pawns, index_row, index, EMPTY_COLOR):
                        result_pawns.append((index_row, index))
                    elif diagonal_movement_to_right_up(self._pawns, index_row, index, EMPTY_COLOR):
                        result_pawns.append((index_row, index))
                    elif sideways_movement_to_right(self._pawns, index_row, index, EMPTY_COLOR):
                        result_pawns.append((index_row, index))
                    elif diagonal_movement_to_right_down(self._pawns, index_row, index, EMPTY_COLOR):
                        result_pawns.append((index_row, index))
                    elif down_movement(self._pawns, index_row, index, EMPTY_COLOR):
                        result_pawns.append((index_row, index))
                    elif diagonal_movement_to_left_down(self._pawns, index_row, index, EMPTY_COLOR):
                        result_pawns.append((index_row, index))
                    elif sideways_movement_to_left(self._pawns, index_row, index, EMPTY_COLOR):
                        result_pawns.append((index_row, index))
        return result_pawns

    def where_can_move(self):
        which = self.which_can_move()
        where = {}

        for indexs in which:
            where_for_pawn = []
            if diagonal_movement_to_left_up(self._pawns, indexs[0], indexs[1], EMPTY_COLOR):
                where_for_pawn.append((indexs[0]-1, indexs[1]-1))
            if up_movement(self._pawns, indexs[0], indexs[1], EMPTY_COLOR):
                where_for_pawn.append((indexs[0]-1, indexs[1]))
            if diagonal_movement_to_right_up(self._pawns, indexs[0], indexs[1], EMPTY_COLOR):
                where_for_pawn.append((indexs[0]-1, indexs[1]+1))
            if sideways_movement_to_right(self._pawns, indexs[0], indexs[1], EMPTY_COLOR):
                where_for_pawn.append((indexs[0], indexs[1]+1))
            if diagonal_movement_to_right_down(self._pawns, indexs[0], indexs[1], EMPTY_COLOR):
                where_for_pawn.append((indexs[0]+1, indexs[1]+1))
            if down_movement(self._pawns, indexs[0], indexs[1], EMPTY_COLOR):
                where_for_pawn.append((indexs[0]+1, indexs[1]))
            if diagonal_movement_to_left_down(self._pawns, indexs[0], indexs[1], EMPTY_COLOR):
                where_for_pawn.append((indexs[0]+1, indexs[1]-1))
            if sideways_movement_to_left(self._pawns, indexs[0], indexs[1], EMPTY_COLOR):
                where_for_pawn.append((indexs[0], indexs[1]-1))
            where[indexs] = where_for_pawn
        return where

    def which_can_hit(self):
        which = []
        which_withdrawl = self.which_can_hit_by_withdrawal()
        for element in which_withdrawl:
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
        move_type = self.recognize_move(pawn, empty)
        if move_type == MOVEMENT_DIAGONAL_LEFT_UP and diagonal_movement_to_left_up(self._pawns, empty[0], empty[1], self._pawn_to_hit):
            return what_append
        if move_type == MOVEMENT_UP and up_movement(self._pawns, empty[0], empty[1], self._pawn_to_hit):
            return what_append
        if move_type == MOVEMENT_DIAGONAL_RIGHT_UP and diagonal_movement_to_right_up(self._pawns, empty[0], empty[1], self._pawn_to_hit):
            return what_append
        if move_type == MOVEMENT_SIDEWAYS_RIGTH and sideways_movement_to_right(self._pawns, empty[0], empty[1], self._pawn_to_hit):
            return what_append
        if move_type == MOVEMENT_DIAGONAL_RIGTH_DOWN and diagonal_movement_to_right_down(self._pawns, empty[0], empty[1], self._pawn_to_hit):
            return what_append
        if move_type == MOVEMENT_DOWN and down_movement(self._pawns, empty[0], empty[1], self._pawn_to_hit):
            return what_append
        if move_type == MOVEMENT_DIAGONAL_LEFT_DOWN and diagonal_movement_to_left_down(self._pawns, empty[0], empty[1], self._pawn_to_hit):
            return what_append
        if move_type == MOVEMENT_SIDEWAYS_LEFT and sideways_movement_to_left(self._pawns, empty[0], empty[1], self._pawn_to_hit):
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
        move_type = self.recognize_move(pawn, empty)
        if move_type == MOVEMENT_DIAGONAL_LEFT_UP and diagonal_movement_to_right_down(self._pawns, pawn[0], pawn[1], self._pawn_to_hit):
            return what_append
        if move_type == MOVEMENT_UP and down_movement(self._pawns, pawn[0], pawn[1], self._pawn_to_hit):
            return what_append
        if move_type == MOVEMENT_DIAGONAL_RIGHT_UP and diagonal_movement_to_left_down(self._pawns, pawn[0], pawn[1], self._pawn_to_hit):
            return what_append
        if move_type == MOVEMENT_SIDEWAYS_RIGTH and sideways_movement_to_left(self._pawns, pawn[0], pawn[1], self._pawn_to_hit):
            return what_append
        if move_type == MOVEMENT_DIAGONAL_RIGTH_DOWN and diagonal_movement_to_left_up(self._pawns, pawn[0], pawn[1], self._pawn_to_hit):
            return what_append
        if move_type == MOVEMENT_DOWN and up_movement(self._pawns, pawn[0], pawn[1], self._pawn_to_hit):
            return what_append
        if move_type == MOVEMENT_DIAGONAL_LEFT_DOWN and diagonal_movement_to_right_up(self._pawns, pawn[0], pawn[1], self._pawn_to_hit):
            return what_append
        if move_type == MOVEMENT_SIDEWAYS_LEFT and sideways_movement_to_right(self._pawns, pawn[0], pawn[1], self._pawn_to_hit):
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
                move_type = self.recognize_move(pawn, empty)
                if move_type == MOVEMENT_DIAGONAL_LEFT_UP:
                    for i in range(0, self._width+1):
                        if diagonal_movement_to_right_down(self._pawns, pawn[0]+i, pawn[1]+i, self._pawn_to_hit):
                            hits.append((pawn[0]+i+1, pawn[1]+i+1))
                        else:
                            break
                elif move_type == MOVEMENT_UP:
                    for i in range(0, self._width+1):
                        if down_movement(self._pawns, pawn[0]+i, pawn[1], self._pawn_to_hit):
                            hits.append((pawn[0]+i+1, pawn[1]))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_RIGHT_UP:
                    for i in range(0, self._width+1):
                        if diagonal_movement_to_left_down(self._pawns, pawn[0]+i, pawn[1]-i, self._pawn_to_hit):
                            hits.append((pawn[0]+i+1, pawn[1]-i-1))
                        else:
                            break
                elif move_type == MOVEMENT_SIDEWAYS_RIGTH:
                    for i in range(0, self._width+1):
                        if sideways_movement_to_left(self._pawns, pawn[0], pawn[1]-i, self._pawn_to_hit):
                            hits.append((pawn[0], pawn[1]-i-1))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_RIGTH_DOWN:
                    for i in range(0, self._width+1):
                        if diagonal_movement_to_left_up(self._pawns, pawn[0]-i, pawn[1]-i, self._pawn_to_hit):
                            hits.append((pawn[0]-i-1, pawn[1]-i-1))
                        else:
                            break
                elif move_type == MOVEMENT_DOWN:
                    for i in range(0, self._width+1):
                        if up_movement(self._pawns, pawn[0]-i, pawn[1], self._pawn_to_hit):
                            hits.append((pawn[0]-i-1, pawn[1]))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_LEFT_DOWN:
                    for i in range(0, self._width+1):
                        if diagonal_movement_to_right_up(self._pawns, pawn[0]-i, pawn[1]+i, self._pawn_to_hit):
                            hits.append((pawn[0]-i-1, pawn[1]+i+1))
                        else:
                            break
                elif move_type == MOVEMENT_SIDEWAYS_LEFT:
                    for i in range(0, self._width+1):
                        if sideways_movement_to_right(self._pawns, pawn[0], pawn[1]+i, self._pawn_to_hit):
                            hits.append((pawn[0], pawn[1]+i+1))
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
                move_type = self.recognize_move(pawn, empty)
                if move_type == MOVEMENT_DIAGONAL_LEFT_UP:
                    for i in range(0, self._width+1):
                        if diagonal_movement_to_left_up(self._pawns, empty[0]-i, empty[1]-i, self._pawn_to_hit):
                            hits.append((empty[0]-i-1, empty[1]-i-1))
                        else:
                            break
                elif move_type == MOVEMENT_UP:
                    for i in range(0, self._width+1):
                        if up_movement(self._pawns, empty[0]-i, empty[1], self._pawn_to_hit):
                            hits.append((empty[0]-i-1, empty[1]))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_RIGHT_UP:
                    for i in range(0, self._width+1):
                        if diagonal_movement_to_right_up(self._pawns, empty[0]-i, empty[1]+i, self._pawn_to_hit):
                            hits.append((empty[0]-i-1, empty[1]+i+1))
                        else:
                            break
                elif move_type == MOVEMENT_SIDEWAYS_RIGTH:
                    for i in range(0, self._width+1):
                        if sideways_movement_to_right(self._pawns, empty[0], empty[1]+i, self._pawn_to_hit):
                            hits.append((empty[0], empty[1]+i+1))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_RIGTH_DOWN:
                    for i in range(0, self._width+1):
                        if diagonal_movement_to_right_down(self._pawns, empty[0]+i, empty[1]+i, self._pawn_to_hit):
                            hits.append((empty[0]+i+1, empty[1]+i+1))
                        else:
                            break
                elif move_type == MOVEMENT_DOWN:
                    for i in range(0, self._width+1):
                        if down_movement(self._pawns, empty[0]+i, empty[1], self._pawn_to_hit):
                            hits.append((empty[0]+i+1, empty[1]))
                        else:
                            break
                elif move_type == MOVEMENT_DIAGONAL_LEFT_DOWN:
                    for i in range(0, self._width+1):
                        if diagonal_movement_to_left_down(self._pawns, empty[0]+i, empty[1]-i, self._pawn_to_hit):
                            hits.append((empty[0]+i+1, empty[1]-i-1))
                        else:
                            break
                elif move_type == MOVEMENT_SIDEWAYS_LEFT:
                    for i in range(0, self._width+1):
                        if sideways_movement_to_left(self._pawns, empty[0], empty[1]-i, self._pawn_to_hit):
                            hits.append((empty[0], empty[1]-i-1))
                        else:
                            break
                which_hits[(pawn, empty)] = hits
        return which_hits

    def possible_combo(self, previous_move_type):
        # sprawdza czy mozna zrobic kombo
        pass

    def move_without_hits(self, pawn, empty):
        pawns_after_move = self.copy_pawns()
        pawns_after_move[pawn[0]][pawn[1]] = EMPTY_COLOR
        pawns_after_move[empty[0]][empty[1]] = self._turn
        return pawns_after_move

    def move_with_hits(self, pawn, empty):
        withdrawal = self.which_hits_by_withdrawl()
        approach = self.which_hits_by_approach()

        if (pawn, empty) in withdrawal and (pawn, empty) in approach:
            choice = self.choose_move_with_hits()
            if choice == CHOICE_WITHDRAWL:
                dead_pawns = withdrawal[(pawn, empty)]
            if choice == CHOICE_APPROACH:
                dead_pawns = approach[(pawn, empty)]
        elif (pawn, empty) in withdrawal:
            dead_pawns = withdrawal[(pawn, empty)]
        elif (pawn, empty) in approach:
            dead_pawns = approach[(pawn, empty)]

        return self.move_with_hits_kill_pawns(pawn, empty, dead_pawns)

    def choose_move_with_hits(self, pawn, empty, chosen_group):
        group_withdrawal = self.which_hits_by_withdrawl()[(pawn, empty)]
        group_approach = self.which_hits_by_approach()[(pawn, empty)]
        if chosen_group == group_withdrawal:
            return CHOICE_WITHDRAWL
        elif chosen_group == group_approach:
            return CHOICE_APPROACH
        else:
            raise MoveError('You cannot choose this group of pawns')

    def move_with_hits_kill_pawns(self, pawn, empty, dead_pawns):
        pawns_after_move = self.move_without_hits(pawn, empty)

        for dead in dead_pawns:
            pawns_after_move[dead[0]][dead[1]] = EMPTY_COLOR
        
        return pawns_after_move

    def move_maker(self, pawn, empty):
        self._validate_move_maker(empty, pawn)

        if not self.which_can_hit():
            return self.move_without_hits(pawn, empty)
        else:
            return self.move_with_hits(pawn, empty)

    def _validate_move_maker(self, empty, pawn):
        if pawn not in self.which_can_move():
            raise MoveError('This pawn cannot move')
        if empty not in self.where_can_move()[pawn]:
            raise MoveError('This pawn cannot move here')
        if pawn not in self.which_can_hit():
            raise MoveError('This pawn does not have any hits')
        if empty not in self.where_can_hit()[pawn]:
            raise MoveError('This pawn does not have any hits here')

    @staticmethod
    def recognize_move(pawn, where_moves):
        if where_moves[0] < pawn[0]:
            if where_moves[1] < pawn[1]:
                return MOVEMENT_DIAGONAL_LEFT_UP
            if where_moves[1] == pawn[1]:
                return MOVEMENT_UP
            if where_moves[1] > pawn[1]:
                return MOVEMENT_DIAGONAL_RIGHT_UP
        if where_moves[0] == pawn[0]:
            if where_moves[1] < pawn[1]:
                return MOVEMENT_SIDEWAYS_LEFT
            if where_moves[1] > pawn[1]:
                return MOVEMENT_SIDEWAYS_RIGTH
        if where_moves[0] > pawn[0]:
            if where_moves[1] < pawn[1]:
                return MOVEMENT_DIAGONAL_LEFT_DOWN
            if where_moves[1] == pawn[1]:
                return MOVEMENT_DOWN
            if where_moves[1] > pawn[1]:
                return MOVEMENT_DIAGONAL_RIGTH_DOWN

    def copy_pawns(self):
        pawns_after_move = []

        for row in self._pawns:
            row_after_move = []
            for pawn in row:
                row_after_move.append(pawn)
            pawns_after_move.append(row_after_move)
        
        return pawns_after_move


class MoveError(Exception):
    pass
