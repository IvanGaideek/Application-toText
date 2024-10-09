from PySide6.QtWidgets import QWidget, QFileDialog

from operation_with_settings import get_data_settings, get_data_default_settings, change_in_settings
from ui_pdf_settings import Ui_SettingsPDF


class SettingsPDF(QWidget, Ui_SettingsPDF):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("""""")  # style

        data = get_data_settings()
        self.initData(data)

        # connect to buttons
        self.choose_folder_save_but.clicked.connect(self.choose_folder)
        self.turn_off_settings.clicked.connect(self.turn_off_fields)

        # Dialog buttons box connect
        self.accepting_response.accepted.connect(self.accept)
        self.accepting_response.rejected.connect(self.reject)

    def initData(self, data):
        """Filling in the fields"""
        set_data = data["pdf_settings"]
        checked_txt = set_data["SAVE_TXT_FILE"]
        self.check_to_txt.setChecked(checked_txt)
        checked_WORD = set_data["SAVE_WORD_FILE"]
        self.check_to_WORD.setChecked(checked_WORD)
        checked_image = set_data["SAVE_IMAGES"]
        self.check_to_images.setChecked(checked_image)
        checked_table = set_data["SAVE_TABLES"]
        self.check_to_tables.setChecked(checked_table)
        self.lineEdit_folder_path.setText(data["save_path"]["for_pdf"])

    def choose_folder(self):
        dir = QFileDialog.getExistingDirectory(self,
                                               'Choose Directory')  # create a file dialog box
        self.lineEdit_folder_path.setText(dir)

    def turn_off_fields(self):
        data = get_data_default_settings()
        self.initData(data)

    def accept(self):
        """Saving the settings"""
        data = get_data_settings()
        set_data = data["pdf_settings"]
        set_data["SAVE_TXT_FILE"] = self.check_to_txt.isChecked()
        set_data["SAVE_WORD_FILE"] = self.check_to_WORD.isChecked()
        set_data["SAVE_IMAGES"] = self.check_to_images.isChecked()
        set_data["SAVE_TABLES"] = self.check_to_tables.isChecked()
        data["save_path"]["for_pdf"] = self.lineEdit_folder_path.text()
        change_in_settings(data)
        self.close()

    def reject(self):
        """Button processing Cancel"""
        self.close()

