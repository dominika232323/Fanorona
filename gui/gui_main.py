from PySide2.QtWidgets import QApplication, QMainWindow
from ui_fanorona import Ui_MainWindow


class FanoronaWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stack.setCurrentIndex(0)
        self._setup_game()

    def _setup_game(self):
        self.ui.playButton.clicked.connect(self._get_values)

    def _get_values(self):
        self.length = self.ui.boardLength.value()
        self.width = self.ui.boardWidth.value()
        self.opponent = self.ui.ChooseOpponent.value()
        self.color = self.ui.spinBoxChooseColor.value()


def gui_main():
    app = QApplication()
    window = FanoronaWindow()
    window.show()
    return app.exec_()


gui_main()
