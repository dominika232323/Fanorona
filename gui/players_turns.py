from PySide2.QtCore import QSize
from PySide2.QtWidgets import QDialog, QPushButton

from gui.functor import Functor
from source.board import Board
from source.move import Move
from source.pawns import Pawns
from ui_player_turn import Ui_DialogWIndow


class PlayersTurns(QDialog):
    def __init__(self, turn, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogWIndow()
        self.ui.setupUi(self)
        self._pawns_on_board = turn.pawns()
        self._turn = turn.turn()
        self._pawn_to_hit = turn.pawn_to_hit()
        self._length = turn.length()
        self._width = turn.width()
        self._pawns = Pawns(Board(self._length, self._width))
        self._pawns.set_actual_pawns(self._pawns_on_board)

        self._create_board()

    def _create_board(self):
        self._buttons_dict = {}
        for row in range(0, self._width):
            for column in range(0, self._length):
                self._buttons_dict[(row, column)] = QPushButton()
                self._buttons_dict[(row, column)].setObjectName(f'{row} {column}')
                self._buttons_dict[(row, column)].setMinimumSize(QSize(50, 50))
                self.ui.gridLayout.addWidget(self._buttons_dict[(row, column)], row, column)
        self._set_pawns_on_board()
        self._player_turn()

    def _set_pawns_on_board(self):
        for row_index, row in enumerate(self._pawns_on_board):
            for index, pawn in enumerate(self._pawns_on_board[row_index]):
                self._buttons_dict[(row_index, index)].setStyleSheet(
                    "QPushButton"
                    "{"
                    f"background-color : {pawn};"
                    "}"
                )
                self._buttons_dict[(row_index, index)].setEnabled(True)

    def _highlight_pawns(self, pawns_to_highlight):
        for row_index, row in enumerate(self._pawns_on_board):
            for index, pawn in enumerate(self._pawns_on_board[row_index]):
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

    def _player_turn(self):
        move = Move(self._pawns, self._turn)

        if move.hit.which_can_hit():
            self._highlight_pawns(move.hit.which_can_hit())
            for pawn in move.hit.which_can_hit():
                empties = move.hit.where_can_hit()[pawn]
                self._buttons_dict[pawn].clicked.connect(lambda: self._highlight_pawns(empties))
                self._buttons_dict[pawn].clicked.connect(self._get_pawn_cords_for_players_move)

            for empty in empties:
                self._buttons_dict[empty].clicked.connect(self._get_empty_cords_for_players_move)
                # if move.hit.if_can_hit_by_approach_and_by_withdrawal(self._pawn_cords, self._empty_cords):
                #     self._buttons_dict[empty].clicked.connect(lambda: self._highlight_pawns(move.hit.which_hits_by_withdrawal()[(self._pawn_cords, self._empty_cords)]))
                #     self._buttons_dict[empty].clicked.connect(lambda: self._highlight_pawns(move.hit.which_hits_by_approach()[(self._pawn_cords, self._empty_cords)]))
                self._buttons_dict[empty].clicked.connect(self.close)
        else:
            self._highlight_pawns(move.hit.which_can_move())

    def _get_pawn_cords_for_players_move(self):
        sending_button = self.sender()
        cords = sending_button.objectName()
        self._pawn_cords = self._make_tuple_from_string(cords)

    @staticmethod
    def _make_tuple_from_string(cords_str):
        cords = cords_str.split()
        return int(cords[0]), int(cords[1])

    def _get_empty_cords_for_players_move(self):
        sending_button = self.sender()
        cords = sending_button.objectName()
        self._empty_cords = self._make_tuple_from_string(cords)

    def return_cords(self):
        return self._pawn_cords, self._empty_cords
