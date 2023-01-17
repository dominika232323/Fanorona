"""
Board dimensions
"""
MIN_BOARD_LENGTH = 3
MIN_BOARD_WIDTH = 3

DEFAULTS_BOARD_LENGTH = 9
DEFAULTS_BOARD_WIDTH = 5

MAX_BOARD_LENGTH = 15
MAX_BOARD_WIDTH = 15

"""
Pawns colors
"""
FIRST_COLOR = '#FFFFFF'
SECOND_COLOR = '#000000'
EMPTY_COLOR = '#DDC683'

"""
Types of moves
"""
MOVEMENT_DIAGONAL_LEFT_UP = 1
MOVEMENT_UP = 2
MOVEMENT_DIAGONAL_RIGHT_UP = 3
MOVEMENT_SIDEWAYS_RIGHT = 4
MOVEMENT_DIAGONAL_RIGHT_DOWN = 5
MOVEMENT_DOWN = 6
MOVEMENT_DIAGONAL_LEFT_DOWN = 7
MOVEMENT_SIDEWAYS_LEFT = 8

"""
Possible choices to capture opponent's pawns
"""
CHOICE_WITHDRAWAL = 'withdrawal'
CHOICE_APPROACH = 'approach'

"""
Types of players and opponents
"""
OPPONENT_PLAYER = 1
OPPONENT_COMPUTER_RANDOM = 2
OPPONENT_COMPUTER_BEST = 3

"""
Information who won the game
"""
FIRST_COLOR_WINNER = 'First player won!'
SECOND_COLOR_WINNER = 'Second player won!'
