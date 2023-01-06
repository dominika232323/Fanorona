from PySide2.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton

from source.board import Board
from source.pawns import Pawns
from ui_fanorona import Ui_MainWindow


class FanoronaWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stack.setCurrentIndex(0)
        self._setup_game()

    def _setup_game(self):
        # self.ui.boardLength.valueChanged.connect(self._get_values())
        # self.ui.boardWidth.valueChanged.connect(self._get_values())
        # self.ui.ChooseOpponent.valueChanged.connect(self._get_values())
        # self.ui.spinBoxChooseColor.valueChanged.connect(self._get_values())
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
                self.ui.boardGrid.addWidget(self._buttons_dict[(row, column)], row, column)
        self._set_pawns_on_board(Pawns(Board(self._length, self._width)))

    def _set_pawns_on_board(self, pawns):
        for row_index, row in enumerate(pawns.actual_pawns):
            for index, pawn in enumerate(pawns.actual_pawns[row_index]):
                self._buttons_dict[(row_index, index)].setStyleSheet(
                    "QPushButton"
                    "{"
                    f"background-color : {pawn};"
                    "}"
                )


def gui_main():
    app = QApplication()
    window = FanoronaWindow()
    window.show()
    return app.exec_()


gui_main()
