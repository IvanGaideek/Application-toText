import os

from PySide6 import QtCore
from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QMainWindow, QFileDialog
from auxiliary_funcs import check_file_extension, wrap_text
from ui_index import Ui_MainWindow

dir_for_info = "docs/"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # downloads the ui file from the designer and sets it as the window
        self.setWindowTitle("toText")

        # Buttons hide by default
        self.frame_2.setHidden(True)
        self.but_information.setChecked(True)

        # Connecting buttons to page
        self.but_rimage.clicked.connect(self.switch_to_rimage_page)
        self.but_rsound.clicked.connect(self.switch_to_rsound_page)
        self.but_pdf.clicked.connect(self.switch_to_pdf_page)
        self.but_guide.clicked.connect(self.switch_to_guide_page)
        self.but_developer.clicked.connect(self.switch_to_developer_page)
        self.but_technologies.clicked.connect(self.switch_to_technologies_page)

        self.but_exit.clicked.connect(self.exit_or_close)

        # Instantiating information pages
        components_for_pages = [(self.plainTextEdit_guide, self.radbut_ru1, self.radbut_en1, "guide_"),
                                (self.plainTextEdit_developer, self.radbut_ru2, self.radbut_en2, "developer_"),
                                (self.plainTextEdit_technologies, self.radbut_ru3, self.radbut_en3, "techs_")]
        for set_components in components_for_pages:
            self.load_page_inf(*set_components)

        # Connecting menu actions
        actions = {self.choice_file: self.load_file,
                   self.choice_dir: self.load_dir}  # Dictionary: key = action, value = function
        for act in actions:
            act.triggered.connect(actions[act])
        self.set_types_and_func_file_for_widget = {0: ("*.png *.jpeg *.jpg *.webp *.bmp *.gif *.svg", self.placement_image),
                                                   1: ("*.mp3 *.wav", self.load_sound),
                                                   2: ("*.pdf", self.load_pdf)}

    def load_page_inf(self, plain_text_edit, radio_but_ru, radio_but_en, prefix_name_fie):
        """Loads the widget (components) information page"""
        name_file = prefix_name_fie
        if radio_but_ru.isChecked():
            name_file += "ru.txt"
        else:
            name_file += "en.txt"
        with open(dir_for_info + name_file, "r", encoding="utf-8") as file:
            plain_text_edit.setPlainText(file.read())  # read the file

    @QtCore.Slot()
    def load_file(self):
        """Opens a one file dialog box"""
        widget_in_stack = self.stackedWidget.currentIndex()  # get the index of the current widget
        file_type = self.set_types_and_func_file_for_widget[widget_in_stack][0]
        file = QFileDialog.getOpenFileName(self, "Choose File", ":/", file_type)
        way_to_file = file[0]
        self.set_types_and_func_file_for_widget[widget_in_stack][1](way_to_file)  # call the function

    @QtCore.Slot()
    def load_dir(self):
        dir = QFileDialog.getExistingDirectory(self,
                                               'Choose Directory')  # create a file dialog box
        if dir:
            for root, dirs, files in os.walk(dir):
                for file in files:
                    # check if the file has a valid extension
                    if check_file_extension(file,
                                         self.set_types_and_func_file_for_widget[self.stackedWidget.currentIndex()][0]):
                        print("yes")

    def placement_image(self, path):
        """Placing the image in the label"""
        self.pixmap = QPixmap(path)
        scaled = self.pixmap.scaled(self.label_image.size(), QtCore.Qt.KeepAspectRatio)  # scaling the image
        self.label_image.setPixmap(scaled)

    def load_sound(self, path):
        self.label_select_audio_file.setText(path.split("/")[-1])  # change the text (name file) in the label
        wrap_text(self.label_select_audio_file)

    def load_pdf(self, path):
        self.label_select_pdf_file.setText(path.split("/")[-1])  # change the text (name file) in the label
        wrap_text(self.label_select_pdf_file)

    def switch_to_rimage_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_rsound_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_pdf_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_guide_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_developer_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_technologies_page(self):
        self.stackedWidget.setCurrentIndex(5)

    def exit_or_close(self):
        """Closes the application"""
        self.close()
