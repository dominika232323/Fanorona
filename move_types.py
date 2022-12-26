def check_for_max_to_left_or_up(index):
    if index == 0:
        return True
    return False


def check_for_max_to_right_or_down(index, length):
    if index == length-1:
        return True
    return False


def diagonal_movement_to_left_up(pawns, row_index, index, wanted_pawn):
    if check_for_max_to_left_or_up(row_index):
        return False
    if check_for_max_to_left_or_up(index):
        return False
    if pawns[row_index-1][index+1] == wanted_pawn:
        return True
    return False


def up_movement(pawns, row_index, index, wanted_pawn):
    if check_for_max_to_left_or_up(row_index):
        return False
    if pawns[row_index-1][index] == wanted_pawn:
        return True
    return False


def diagonal_movement_to_right_up(pawns, row_index, index, wanted_pawn):
    if check_for_max_to_left_or_up(row_index):
        return False
    if check_for_max_to_right_or_down(index, len(pawns[0])):
        return False
    if pawns[row_index-1][index-1] == wanted_pawn:
        return True
    return False


def sideways_movement_to_right(pawns, row_index, index, wanted_pawn):
    if check_for_max_to_right_or_down(index, len(pawns[0])):
        return False
    if pawns[row_index][index+1] == wanted_pawn:
        return True
    return False


def diagonal_movement_to_right_down(pawns, row_index, index, wanted_pawn):
    if check_for_max_to_right_or_down(row_index, len(pawns)):
        return False
    if check_for_max_to_right_or_down(index, len(pawns[0])):
        return False
    if pawns[row_index+1][index+1] == wanted_pawn:
        return True
    return False


def down_movement(pawns, row_index, index, wanted_pawn):
    if check_for_max_to_right_or_down(row_index, len(pawns)):
        return False
    if pawns[row_index+1][index] == wanted_pawn:
        return True
    return False


def diagonal_movement_to_left_down(pawns, row_index, index, wanted_pawn):
    if check_for_max_to_right_or_down(row_index, len(pawns)):
        return False
    if check_for_max_to_left_or_up(index):
        return False
    if pawns[row_index+1][index-1] == wanted_pawn:
        return True
    return False


def sideways_movement_to_left(pawns, row_index, index, wanted_pawn):
    if check_for_max_to_left_or_up(index):
        return False
    if pawns[row_index][index-1] == wanted_pawn:
        return True
    return False
