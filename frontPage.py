from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QAction
from ui_index import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # downloads the ui file from the designer and sets it as the window
