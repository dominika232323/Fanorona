from PySide2.QtWidgets import QApplication

from gui.gui_main import FanoronaWindow
from gui import ui_fanorona, ui_player_turn
import sys


def main():
    app = QApplication()
    window = FanoronaWindow()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    main()
