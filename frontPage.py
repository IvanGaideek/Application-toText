from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QAction
from ui_index import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # downloads the ui file from the designer and sets it as the window

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
