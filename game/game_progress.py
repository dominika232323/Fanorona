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


def order_of_players(player_color, opponent_type):
    if player_color == FIRST_COLOR:
        return OPPONENT_PLAYER, opponent_type
    if player_color == SECOND_COLOR:
        return opponent_type, OPPONENT_PLAYER
