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

    def _get_values(self):
        self._length = int(self.ui.boardLength.value())
        self._width = int(self.ui.boardWidth.value())
        self._opponent = int(self.ui.ChooseOpponent.value())
        self._color = int(self.ui.spinBoxChooseColor.value())
        self._create_board()

    def _create_board(self):
        self.ui.stack.setCurrentIndex(1)
        self._buttons_dict = {}
        for row in range(0, self._width):
            for column in range(0, self._length):
                self._buttons_dict[(row, column)] = QPushButton()
                self._buttons_dict[(row, column)].setMinimumSize(QSize(50, 50))
                self.ui.boardGrid.addWidget(self._buttons_dict[(row, column)], row, column)
        self._board = Board(self._length, self._width)
        self._pawns = Pawns(self._board)
        self._set_pawns_on_board()
        self._game()

    def _set_pawns_on_board(self):
        for row_index, row in enumerate(self._pawns.actual_pawns):
            for index, pawn in enumerate(self._pawns.actual_pawns[row_index]):
                self._buttons_dict[(row_index, index)].setStyleSheet(
                    "QPushButton"
                    "{"
                    f"background-color : {pawn};"
                    "}"
                )
                self._buttons_dict[(row_index, index)].setEnabled(True)

    def _highlight_pawns(self, pawns_to_highlight):
        for row_index, row in enumerate(self._pawns.actual_pawns):
            for index, pawn in enumerate(self._pawns.actual_pawns[row_index]):
                if (row_index, index) in pawns_to_highlight:
                    self._buttons_dict[(row_index, index)].setStyleSheet(
                        "QPushButton"
                        "{"
                        f"background-color : {pawn};"
                        "border-style: outset;"
                        "border-color : yellow;"
                        "border-width: 5px;"
                        "}"
                    )
                    self._buttons_dict[(row_index, index)].setEnabled(True)
                else:
                    self._buttons_dict[(row_index, index)].setEnabled(False)

    def _game(self):
        player_color = FIRST_COLOR if self._color == 1 else SECOND_COLOR
        self._first_player, self._second_player = Game.order_of_players(player_color, self._opponent)

        while self._pawns.check_for_winner() is False:
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
        self._if_move_was_capturing(move)
        self._make_players_move(move)

    def _if_move_was_capturing(self, move):
        if move.was_move_capturing(self._pawn_cords, self._empty_cords):
            self._capturing_move = True
        else:
            self._capturing_move = False

    def _make_players_move(self, move):
        pawns_after_move = move.move_maker(self._pawn_cords, self._empty_cords, self._choice)
        self._pawns.set_actual_pawns(pawns_after_move)
        self._set_pawns_on_board()
        if self._capturing_move:
            self._player_combo(move.turn)

    def _player_combo(self, pawn_color):
        combo = Combo(self._pawns, pawn_color, self._pawn_cords, self._empty_cords)
        if combo.possible_combo():
            self._player_turn(pawn_color, combo.new_pawn)

    def _computer_random(self, pawn_color):
        pawn_cords, empty_cords = Game.get_random_pawn_and_empty_cords(self._pawns, pawn_color)
        choice = Game.get_random_move_choice(self._pawns, pawn_color, pawn_cords, empty_cords)
        move = Move(self._pawns, pawn_color)

        pawns_after_move = move.move_maker(pawn_cords, empty_cords, choice)
        self._pawns.set_actual_pawns(pawns_after_move)
        self._set_pawns_on_board()

        # combo = Combo(self._pawns, pawn_color, pawn_cords, empty_cords)
        # while combo.possible_combo():
        #     move_combo = Move(self._pawns, pawn_color)
        #     combo_empty_cords = choice(combo.find_empty_for_combo())
        #     pawns_after_move = move_combo.move_maker(combo.new_pawn, combo_empty_cords)
        #     self._pawns.set_actual_pawns(pawns_after_move)
        #     self._set_pawns_on_board()
        #     combo = Combo(self._pawns, pawn_color, combo.new_pawn, combo_empty_cords)

    def _computer_best(self, pawn_color):
        pawn_cords, empty_cords = Game.get_best_pawns_and_empty_cords(self._pawns, pawn_color)
        move = Move(self._pawns, pawn_color)

        pawns_after_move = move.move_maker(pawn_cords, empty_cords)
        self._pawns.set_actual_pawns(pawns_after_move)
        self._set_pawns_on_board()

        combo = Combo(self._pawns, pawn_color, pawn_cords, empty_cords)
        while combo.possible_combo():
            move_combo = Move(self._pawns, pawn_color)
            hit_combo = Hit(self._pawns, pawn_color)

            combo_empty_cords_by_withdrawal, len_by_withdrawal = Game.find_best_empty_for_combo(pawn_cords, combo.find_empty_for_combo(), hit_combo.which_hits_by_withdrawal())
            combo_empty_cords_by_approach, len_by_approach = Game.find_best_empty_for_combo(pawn_cords, combo.find_empty_for_combo(), hit_combo.which_hits_by_approach())
            if len_by_withdrawal >= len_by_approach:
                combo_empty_cords = combo_empty_cords_by_withdrawal
            else:
                combo_empty_cords = combo_empty_cords_by_approach

            pawns_after_move = move_combo.move_maker(combo.new_pawn, combo_empty_cords)
            self._pawns.set_actual_pawns(pawns_after_move)
            self._set_pawns_on_board()
            combo = Combo(self._pawns, pawn_color, combo.new_pawn, combo_empty_cords)

    def _game_over(self):
        self.ui.stack.setCurrentIndex(2)
        self.ui.labelWinner.setText(self._pawns.winner_message())
        self.ui.NewGame.clicked.connect(self._setup_game)



def gui_main():
    app = QApplication()
    window = FanoronaWindow()
    window.show()
    return app.exec_()


gui_main()
