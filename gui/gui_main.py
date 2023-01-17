import time
from random import choice

from PySide2.QtCore import QSize, QEventLoop
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from gui.game import Game
from gui.players_turns import PlayersTurns
from source.board import Board
from source.combo import Combo
from source.configuration import (
    FIRST_COLOR,
    SECOND_COLOR,
    OPPONENT_PLAYER,
    OPPONENT_COMPUTER_RANDOM,
    OPPONENT_COMPUTER_BEST
)
from source.hit import Hit
from source.move import Move
from source.pawns import Pawns
from source.turn import Turn
from ui_fanorona import Ui_MainWindow


class FanoronaWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stack.setCurrentIndex(0)
        self._setup_game()

    def _setup_game(self):
        self.ui.stack.setCurrentIndex(0)
        self.ui.playButton.clicked.connect(self._get_values)
        self._play_game = True

    def _get_values(self):
        self._length = int(self.ui.boardLength.value())
        self._width = int(self.ui.boardWidth.value())
        self._opponent = int(self.ui.ChooseOpponent.value())
        self._color = int(self.ui.spinBoxChooseColor.value())
        self._create_board()

    def _create_board(self):
        self.ui.stack.setCurrentIndex(1)
        self._board = Board(self._length, self._width)
        self._pawns = Pawns(self._board)
        self._game()

    def _game(self):
        player_color = FIRST_COLOR if self._color == 1 else SECOND_COLOR
        self._first_player, self._second_player = Game.order_of_players(player_color, self._opponent)

        while self._pawns.check_for_winner() is False and self._play_game is True:
            self._make_turn(self._first_player, FIRST_COLOR)
            if self._pawns.check_for_winner() is False:
                self._make_turn(self._second_player, SECOND_COLOR)

        self._game_over()

    def _make_turn(self, player, color):
        if player == OPPONENT_PLAYER:
            self._player_turn(color)
        elif player == OPPONENT_COMPUTER_RANDOM:
            self._computer_random(color)
        elif player == OPPONENT_COMPUTER_BEST:
            self._computer_best(color)

    def _player_turn(self, pawn_color, previous_pawn_cords=None):
        window = PlayersTurns(Turn(self._pawns, pawn_color), previous_pawn_cords)
        window.exec_()
        self._pawn_cords, self._empty_cords, self._choice = window.return_cords()
        move = Move(self._pawns, pawn_color)
        self._if_move_was_capturing(move, self._pawn_cords, self._empty_cords)
        self._make_players_move(move)

    def _make_players_move(self, move):
        pawns_after_move = move.move_maker(self._pawn_cords, self._empty_cords, self._choice)
        self._pawns.set_actual_pawns(pawns_after_move)
        if self._capturing_move:
            self._player_combo(move.turn)

    def _player_combo(self, pawn_color):
        combo = Combo(self._pawns, pawn_color, self._pawn_cords, self._empty_cords)
        if combo.possible_combo():
            self._player_turn(pawn_color, combo.new_pawn)

    def _computer_random(self, pawn_color):
        time.sleep(0.2)
        pawn_cords, empty_cords = Game.get_random_pawn_and_empty_cords(self._pawns, pawn_color)
        move_choice = Game.get_random_move_choice(self._pawns, pawn_color, pawn_cords, empty_cords)
        move = Move(self._pawns, pawn_color)
        self._if_move_was_capturing(move, pawn_cords, empty_cords)

        pawns_after_move = move.move_maker(pawn_cords, empty_cords, move_choice)
        self._pawns.set_actual_pawns(pawns_after_move)

        if self._capturing_move:
            self._computer_random_combo(move, pawn_cords, empty_cords)

    def _computer_random_combo(self, move, pawn_cords, empty_cords):
        combo = Combo(self._pawns, move.turn, pawn_cords, empty_cords)
        while combo.possible_combo():
            empty_cords = choice(combo.find_empty_for_combo())
            move_choice = Game.get_random_move_choice(self._pawns, move.turn, combo.new_pawn, empty_cords)

            pawns_after_move = move.move_maker(combo.new_pawn, empty_cords, move_choice)
            self._pawns.set_actual_pawns(pawns_after_move)
            combo = Combo(self._pawns, move.turn, combo.new_pawn, empty_cords)

    def _computer_best(self, pawn_color):
        time.sleep(0.2)
        pawn_cords, empty_cords = Game.get_best_pawns_and_empty_cords(self._pawns, pawn_color)
        move_choice = Game.find_best_choice(self._pawns, pawn_color, pawn_cords, empty_cords)
        move = Move(self._pawns, pawn_color)
        self._if_move_was_capturing(move, pawn_cords, empty_cords)

        pawns_after_move = move.move_maker(pawn_cords, empty_cords, move_choice)
        self._pawns.set_actual_pawns(pawns_after_move)

        if self._capturing_move:
            self._computer_best_combo(move, pawn_cords, empty_cords)

    def _computer_best_combo(self, move, pawn_cords, empty_cords):
        combo = Combo(self._pawns, move.turn, pawn_cords, empty_cords)
        while combo.possible_combo():
            empty_cords = Game.get_best_empty_for_combo(combo, combo.new_pawn)
            move_choice = Game.find_best_choice(self._pawns, move.turn, pawn_cords, empty_cords)

            pawns_after_move = move.move_maker(combo.new_pawn, empty_cords, move_choice)
            self._pawns.set_actual_pawns(pawns_after_move)
            combo = Combo(self._pawns, move.turn, combo.new_pawn, empty_cords)

    def _if_move_was_capturing(self, move, pawn_cords, empty_cords):
        if move.was_move_capturing(pawn_cords, empty_cords):
            self._capturing_move = True
        else:
            self._capturing_move = False

    def _game_over(self):
        self.ui.stack.setCurrentIndex(2)
        self.ui.labelWinner.setText(self._pawns.winner_message())
        self.ui.NewGame.clicked.connect(self._setup_game)
        self._play_game = False
