from source.pawns import Pawns
from players_turns import (
    player_turn,
    computer_random,
    computer_best
)
from source.configuration import (
    FIRST_COLOR,
    SECOND_COLOR,
    OPPONENT_PLAYER,
    OPPONENT_COMPUTER_RANDOM,
    OPPONENT_COMPUTER_BEST
)


def game_progress(board, player_color, opponent_type):
    pawns = Pawns(board)
    first_player, second_player = order_of_players(player_color, opponent_type)

    while pawns.check_for_winner() is False:
        make_turn(first_player, pawns, FIRST_COLOR)
        make_turn(second_player, pawns, SECOND_COLOR)


def make_turn(player, pawns, color):
    if player == OPPONENT_PLAYER:
        player_turn(pawns, color)
    elif player == OPPONENT_COMPUTER_RANDOM:
        computer_random(pawns, color)
    elif player == OPPONENT_COMPUTER_BEST:
        computer_best(pawns, color)


def order_of_players(player_color, opponent_type):
    if player_color == FIRST_COLOR:
        return OPPONENT_PLAYER, opponent_type
    if player_color == SECOND_COLOR:
        return opponent_type, OPPONENT_PLAYER
