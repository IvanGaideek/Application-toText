from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PIL.ImageQt import ImageQt
from ui_image_settings import Ui_SettingsImage
from operation_with_settings import get_data_settings, get_data_default_settings, change_in_settings
from process_recognition_image import RecognitionProcessingImage


class SettingsImage(QWidget, Ui_SettingsImage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("""#label_image_before, #label_image_after {padding: 0px;
                                margin: 0px}""")  # style

        # Buttons hide by default
        self.prerrocessing_image_but.setChecked(True)

        data = get_data_settings()

        self.choose_folder_save_but.clicked.connect(self.choose_folder)
        self.turn_off_settings.clicked.connect(self.turn_off_fields)

        # installing the original image
        self.label_image_before.setAlignment(Qt.AlignCenter)
        self.label_image_after.setAlignment(Qt.AlignCenter)
        self.image_path = "Design/image/before_img.jpeg"
        self.init_image_before()

        self.initData(data)

        self.check_to_txt.stateChanged.connect(self.changed_image)
        self.check_gray.stateChanged.connect(lambda: self.changed_image("gray"))
        self.check_bitmap.stateChanged.connect(lambda: self.changed_image("bitmap"))
        self.check_invert.stateChanged.connect(self.changed_image)

        self.comboBox_langs.activated.connect(self.text_changes_language)

        # Dialog buttons box connect
        self.accepting_response.accepted.connect(self.accept)
        self.accepting_response.rejected.connect(self.reject)

    def initData(self, data):
        """Filling in the fields"""
        set_data = data["image_settings"]
        checked_txt = set_data["SAVE_TXT_FILE"]
        self.check_to_txt.setChecked(checked_txt)
        self.lineEdit_folder_path.setText(data["save_path"]["for_image"])

        # create data in the ComboBox
        self.langs_dict = set_data["ALL_LANGS"]
        langs = self.langs_dict.keys()
        self.comboBox_langs.clear()
        self.comboBox_langs.addItems(langs)

        self.input_langs.setText(" ".join(set_data["DEFAULT_LANG"]))
        self.size_SpinBox.setValue(set_data["SIZE_TRANSFORM_IMG"])
        # convert image
        if set_data["CONVERT_IMG"] == "bitmap":
            self.check_gray.setChecked(True)
            self.check_bitmap.setChecked(True)
        elif set_data["CONVERT_IMG"] is None:
            self.check_gray.setChecked(False)
            self.check_bitmap.setChecked(False)
        elif set_data["CONVERT_IMG"] == "gray":
            self.check_gray.setChecked(True)

        self.contract_SpinBox.setValue(set_data["CONTRAST_RATIO"])
        self.check_invert.setChecked(set_data["INVERT_IMG"])  # check_invert

        self.update_image()

    def error_input_langs(self):
        self.error_input.setText("You've entered the languages wrong.")

    def accept(self):
        """Saving the settings"""
        data = get_data_settings()
        set_langs = self.input_langs.text().split()
        if all(lang in data["image_settings"]["ALL_LANGS"].values() for lang in set_langs):
            data["image_settings"]["DEFAULT_LANG"] = set_langs
        else:
            self.error_input_langs()
            return
        data["image_settings"]["SAVE_TXT_FILE"] = self.check_to_txt.isChecked()
        data["image_settings"]["CONTRAST_RATIO"] = self.contract_SpinBox.value()
        data["image_settings"]["SIZE_TRANSFORM_IMG"] = self.size_SpinBox.value()
        data["image_settings"]["CONVERT_IMG"] = "bitmap" if self.check_bitmap.isChecked() else\
            "gray" if self.check_gray.isChecked() else None
        data["image_settings"]["INVERT_IMG"] = self.check_invert.isChecked()
        data["save_path"]["for_image"] = self.lineEdit_folder_path.text()
        change_in_settings(data)
        self.close()

    def reject(self):
        """Button processing Cancel"""
        self.close()

    def turn_off_fields(self):
        data = get_data_default_settings()
        self.initData(data)

    def text_changes_language(self, _):
        """Appending the selected language to a string"""
        lang = self.comboBox_langs.currentText()
        new_text = self.input_langs.text() + " " + self.langs_dict[lang]
        self.input_langs.setText(new_text)

    def changed_image(self, checkbox=None):
        if self.check_bitmap.isChecked() and checkbox == "bitmap":
            self.check_gray.setChecked(True)
        elif not self.check_gray.isChecked() and checkbox == "gray":
            self.check_bitmap.setChecked(False)
        self.update_image()

    def init_image_before(self):
        """Image Preprocessing"""
        pixmap = QPixmap(self.image_path)
        scaled = pixmap.scaled(self.label_image_before.size(), Qt.KeepAspectRatio)  # scaling the image
        self.label_image_before.setPixmap(scaled)

    def choose_folder(self):
        dir = QFileDialog.getExistingDirectory(self,
                                               'Choose Directory')  # create a file dialog box
        self.lineEdit_folder_path.setText(dir)

    def update_image(self):
        """Image Preprocessing"""
        img = RecognitionProcessingImage(self.image_path)
        img = self.transformation_image(img)
        image = ImageQt(img)
        pixmap = QPixmap.fromImage(image)
        scaled = pixmap.scaled(self.label_image_after.size(), Qt.KeepAspectRatio)  # scaling the image
        self.label_image_after.setPixmap(scaled)

    def transformation_image(self, image_object):
        """Converting the image with current settings"""
        image_object.change_size(self.size_SpinBox.value())
        if self.check_bitmap.isChecked():
            image_object.convert_to_gray()
            image_object.change_contrast(self.contract_SpinBox.value())
            image_object.change_threshold()
        elif self.check_gray.isChecked():
            image_object.convert_to_gray()
            image_object.change_contrast(self.contract_SpinBox.value())
        else:
            image_object.change_contrast(self.contract_SpinBox.value())
        if self.check_invert.isChecked():
            image_object.invert_color()
        return image_object.image
