import os

from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QFileDialog
from ui_index import Ui_MainWindow


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

        # Connecting menu actions
        actions = {self.choice_file: self.load_file,
                   self.choice_dir: self.load_dir}  # Dictionary: key = action, value = function
        for act in actions:
            act.triggered.connect(actions[act])

    @QtCore.Slot()
    def load_file(self):
        """Opens a one file dialog box"""
        files = QFileDialog.getOpenFileName(self, "Choose File", None, "Images (*.png *.xpm *.jpg)")
        print(files)

    @QtCore.Slot()
    def load_dir(self):
        dir = QFileDialog.getExistingDirectory(self,
                                               'Choose Directory')  # create a file dialog box
        if dir:
            for file_name in os.listdir(dir):

                # Check if the file is an image
                if file_name.endswith('.png') or file_name.endswith('jpeg'):
                    print("Yes")

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
