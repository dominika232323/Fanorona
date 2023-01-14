from PySide2.QtCore import QSize
from PySide2.QtWidgets import QDialog, QPushButton
from source.board import Board
from source.move import Move
from source.pawns import Pawns
from ui_player_turn import Ui_DialogWIndow
from source.configuration import (
    CHOICE_WITHDRAWAL,
    CHOICE_APPROACH
)


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
        self.move = Move(self._pawns, self._turn)

        if self.move.hit.which_can_hit():
            self._choose_pawn_for_move(self.move.hit.which_can_hit())
        else:
            self._choose_pawn_for_move(self.move.hit.which_can_move())

    def _choose_pawn_for_move(self, from_where):
        self._highlight_pawns(from_where)
        for pawn in from_where:
            self._buttons_dict[pawn].clicked.connect(self._get_pawn_cords_for_players_move)

    def _get_pawn_cords_for_players_move(self):
        sending_button = self.sender()
        cords = sending_button.objectName()
        self._pawn_cords = self._make_tuple_with_cords_from_button_name(cords)
        self._highlight_empty_pawns()

    def _highlight_empty_pawns(self):
        if self._pawn_cords in self.move.hit.which_can_hit():
            self._empties = self.move.hit.where_can_hit()[self._pawn_cords]
        else:
            self._empties = self.move.hit.where_can_move()[self._pawn_cords]
        self._highlight_pawns(self._empties)
        self._choose_empty_place_for_move()

    def _choose_empty_place_for_move(self):
        for empty in self._empties:
            self._buttons_dict[empty].clicked.connect(self._get_empty_cords_for_players_move)

    def _get_empty_cords_for_players_move(self):
        sending_button = self.sender()
        cords = sending_button.objectName()
        self._empty_cords = self._make_tuple_with_cords_from_button_name(cords)
        self._choose_group_to_capture()

    def _choose_group_to_capture(self):
        if self.move.hit.if_can_hit_by_approach_and_by_withdrawal(self._pawn_cords, self._empty_cords):
            self._group_by_withdrawal = self.move.hit.which_hits_by_withdrawal()[(self._pawn_cords, self._empty_cords)]
            self._group_by_approach = self.move.hit.which_hits_by_approach()[(self._pawn_cords, self._empty_cords)]
            self._highlight_pawns(self._group_by_withdrawal)
            self._highlight_pawns(self._group_by_approach)

            pawns_to_capture = self._group_by_approach + self._group_by_withdrawal
            for pawn in pawns_to_capture:
                self._buttons_dict[pawn].clicked.connect(self._get_players_choice_to_capture)
                self._buttons_dict[pawn].clicked.connect(self.close)
        else:
            self._choice = None
            self.close()

    def _get_players_choice_to_capture(self):
        chosen_button = self.sender()
        cords = chosen_button.objectName()
        chosen_pawn = self._make_tuple_with_cords_from_button_name(cords)
        if chosen_pawn in self._group_by_withdrawal:
            self._choice = CHOICE_WITHDRAWAL
        else:
            self._choice = CHOICE_APPROACH

    @staticmethod
    def _make_tuple_with_cords_from_button_name(cords_str):
        cords = cords_str.split()
        return int(cords[0]), int(cords[1])

    def return_cords(self):
        return self._pawn_cords, self._empty_cords, self._choice
