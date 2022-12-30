from source.board import Board
from source.pawns import Pawns
from source.move import Move
# from player_turns import (
#     player_turn,
#     computer_random,
#     computer_the_best
# )
from configuration import (
    FIRST_COLOR,
    SECOND_COLOR,
    EMPTY_COLOR,
    OPPONENT_PLAYER,
    OPPONENT_COMPUTER_RANDOM,
    OPPONENT_COMPUTER_BEST
)


def game_progress(board, player_color, opponent_type):
    pawns = Pawns(board)
    first_player, second_player = order_of_players(player_color, opponent_type)

    while pawns.check_for_winner() is False:
        opponent_turn(first_player, FIRST_COLOR)
        opponent_turn(second_player, SECOND_COLOR)


def opponent_turn(opponent, color):
    if opponent == OPPONENT_PLAYER:
        player_turn(color)
    elif opponent == OPPONENT_COMPUTER_RANDOM:
        computer_random(color)
    elif opponent == OPPONENT_COMPUTER_BEST:
        computer_the_best(color)


def order_of_players(player_color, opponent_type):
    if player_color == FIRST_COLOR:
        return OPPONENT_PLAYER, opponent_type
    if player_color == SECOND_COLOR:
        return opponent_type, OPPONENT_PLAYER
