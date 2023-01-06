from PySide2.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton
from ui_fanorona import Ui_MainWindow


class FanoronaWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stack.setCurrentIndex(0)
        self._setup_game()

    def _setup_game(self):
        self.ui.boardLength.valueChanged.connect(self._get_values())
        self.ui.boardWidth.valueChanged.connect(self._get_values())
        self.ui.ChooseOpponent.valueChanged.connect(self._get_values())
        self.ui.spinBoxChooseColor.valueChanged.connect(self._get_values())
        self.ui.playButton.clicked.connect(self._create_board)

    def _get_values(self):
        self._length = int(self.ui.boardLength.value())
        self._width = int(self.ui.boardWidth.value())
        self._opponent = int(self.ui.ChooseOpponent.value())
        self._color = int(self.ui.spinBoxChooseColor.value())

    def _create_board(self):
        self.ui.stack.setCurrentIndex(1)
        # self.ui.boardGrid.addWidget(QPushButton())
        for row in range(0, self._width):
            for column in range(0, self._length):
                self.ui.boardGrid.addWidget(QPushButton(), row, column)




def gui_main():
    app = QApplication()
    window = FanoronaWindow()
    window.show()
    return app.exec_()


gui_main()
