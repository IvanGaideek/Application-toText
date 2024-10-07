from PySide6.QtWidgets import QWidget, QFileDialog

from operation_with_settings import get_data_settings, get_data_default_settings, change_in_settings
from ui_sound_settings import Ui_SettingsSound


class SettingsSound(QWidget, Ui_SettingsSound):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("""#comboBox_langs {margin-left: 85px}""")  # style

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
        set_data = data["sound_settings"]
        checked_txt = set_data["SAVE_TXT_FILE"]
        self.check_to_txt.setChecked(checked_txt)
        self.lineEdit_folder_path.setText(data["save_path"]["for_sound"])

        # create data in the ComboBox for languages
        langs = list(set_data["ALL_LANGS"].keys())
        choose_lang = set_data["DEFAULT_LANG"]
        self.comboBox_langs.clear()
        self.comboBox_langs.addItems(langs)
        self.comboBox_langs.setCurrentIndex(langs.index(choose_lang))

        # create data in the ComboBox for models
        models = list(set_data["ALL_MODELS"].keys())
        choose_model = set_data["DEFAULT_MODEL"]
        self.comboBox_models.clear()
        self.comboBox_models.addItems(models)
        self.comboBox_models.setCurrentIndex(models.index(choose_model))

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
        set_data = data["sound_settings"]
        set_data["SAVE_TXT_FILE"] = self.check_to_txt.isChecked()
        set_data["DEFAULT_LANG"] = self.comboBox_langs.currentText()
        set_data["DEFAULT_MODEL"] = self.comboBox_models.currentText()
        data["save_path"]["for_sound"] = self.lineEdit_folder_path.text()
        change_in_settings(data)
        self.close()

    def reject(self):
        """Button processing Cancel"""
        self.close()
