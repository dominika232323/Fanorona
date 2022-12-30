from game.game_progress import (
    game_progress,
    opponent_turn,
    order_of_players
)
from configuration import (
    FIRST_COLOR,
    SECOND_COLOR,
    EMPTY_COLOR,
    OPPONENT_PLAYER,
    OPPONENT_COMPUTER_RANDOM,
    OPPONENT_COMPUTER_BEST
)


# ----------------------------------------- order_of_players()


def test_order_of_players():
    assert order_of_players(FIRST_COLOR, OPPONENT_COMPUTER_RANDOM) == (OPPONENT_PLAYER, OPPONENT_COMPUTER_RANDOM)
    assert order_of_players(SECOND_COLOR, OPPONENT_COMPUTER_BEST) == (OPPONENT_COMPUTER_BEST, OPPONENT_PLAYER)
    assert order_of_players(SECOND_COLOR, OPPONENT_PLAYER) == (OPPONENT_PLAYER, OPPONENT_PLAYER)
