from PySide2.QtWidgets import QApplication, QMainWindow
from ui_fanorona import Ui_MainWindow


class FanoronaWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def _get_values(self):
        pass


def gui_main():
    app = QApplication()
    window = FanoronaWindow()
    window.show()
    return app.exec_()


gui_main()
