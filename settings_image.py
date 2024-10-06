from PySide6.QtWidgets import QWidget
from ui_image_settings import Ui_SettingsImage


class SettingsImage(QWidget, Ui_SettingsImage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("""""")
