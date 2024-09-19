import os

from PIL.ImageQt import ImageQt
from PIL import Image
from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QFileDialog
from auxiliary_funcs import check_file_extension, wrap_text, read_file, clear_result
from threads import RecognitionThreadImage, RecognitionThreadSound, RecognitionThreadPDF
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

        # Connecting buttons to functions recognitions
        self.but_recognition_image.clicked.connect(self.recognition_images_files)
        self.but_recognition_sound.clicked.connect(self.recognition_sound_files)
        self.but_recognition_pdf.clicked.connect(self.recognition_pdf_files)

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
        self.set_types_and_func_file_for_widget = {0: ("*.png *.jpeg *.jpg *.webp *.bmp *.gif *.svg",
                                                       self.placement_image),
                                                   1: ("*.mp3 *.wav", self.load_sound),
                                                   2: ("*.pdf", self.load_pdf)}

        # Instantiating list names files of recognitions
        self.recognitions_images = []
        self.recognitions_sounds = []
        self.recognitions_pdfs = []
        self.recognitions_files_name = {0: self.recognitions_images, 1: self.recognitions_sounds,
                                        2: self.recognitions_pdfs}

    def load_page_inf(self, plain_text_edit, radio_but_ru, radio_but_en, prefix_name_fie):
        """Loads the widget (components) information page"""
        name_file = prefix_name_fie
        if radio_but_ru.isChecked():
            name_file += "ru.txt"
        else:
            name_file += "en.txt"
        full_name_file = dir_for_info + name_file
        read_file(plain_text_edit, full_name_file)
        # Reaction to radio buttons
        radio_but_ru.clicked.connect(lambda: read_file(plain_text_edit, dir_for_info + prefix_name_fie + "ru.txt"))
        radio_but_en.clicked.connect(lambda: read_file(plain_text_edit, dir_for_info + prefix_name_fie + "en.txt"))

    @QtCore.Slot()
    def load_file(self):
        """Opens a one file dialog box"""
        clear_result(self.result)
        widget_in_stack = self.stackedWidget.currentIndex()  # get the index of the current widget
        self.clear_files(widget_in_stack)
        file_type = self.set_types_and_func_file_for_widget[widget_in_stack][0]
        file = QFileDialog.getOpenFileName(self, "Choose File", ":/", file_type)
        way_to_file = file[0]
        if way_to_file != "":
            self.set_types_and_func_file_for_widget[widget_in_stack][1](way_to_file)  # call the function
            self.recognitions_files_name[widget_in_stack].append(way_to_file)  # add the name of the file to the list

    @QtCore.Slot()
    def load_dir(self):
        clear_result(self.result)
        widget_in_stack = self.stackedWidget.currentIndex()  # get the index of the current widget
        self.clear_files(widget_in_stack)
        dir = QFileDialog.getExistingDirectory(self,
                                               'Choose Directory')  # create a file dialog box
        if dir:
            for root, dirs, files in os.walk(dir):
                for file in files:
                    # check if the file has a valid extension
                    if check_file_extension(file,
                                         self.set_types_and_func_file_for_widget[self.stackedWidget.currentIndex()][0]):
                        self.recognitions_files_name[widget_in_stack].append(root + "/" + file)  # add the name of the file to the list
        # call the function for the first file
        if self.recognitions_files_name[widget_in_stack]:
            path = self.recognitions_files_name[widget_in_stack][0].split("/")[-2]
            first_file_path = self.recognitions_files_name[widget_in_stack][0]
            self.set_types_and_func_file_for_widget[widget_in_stack][1](first_file_path)

    @QtCore.Slot()
    def recognition_images_files(self):
        """Recognition of all chosen images in a separate thread."""
        if not self.recognitions_images:
            self.result.setText("There are no images!")
            return  # If there are no images, do nothing

        self.but_recognition_image.setEnabled(False)  # Disable the button "Recognition of images"
        self.recognition_thread_img = RecognitionThreadImage(self.recognitions_images)
        self.recognition_thread_img.finished_one_rec_signal.connect(self.update_ui_after_recognition)
        self.recognition_thread_img.all_finished_signal.connect(self.finish_proccess_rec_images)  # end recognition
        self.recognition_thread_img.start()  # Launch the thread
        self.counter_images = 0

    @QtCore.Slot(str, Image.Image)
    def update_ui_after_recognition(self, result_text, image):
        """Update UI after recognition is finished."""
        self.text_edit_image.setPlainText(result_text)
        self.placement_image(image)  # Update Image in the UI
        self.counter_images += 1
        self.result.setText(f"Image recognition {self.counter_images} / {len(self.recognitions_images)} ...")

    def finish_proccess_rec_images(self):
        self.result.setText(f"Image recognition is finished!({self.counter_images} images)")
        self.recognition_thread_img.quit()  # closing the thread
        self.but_recognition_image.setEnabled(True)  # Enable the button "Recognition of images"

    @QtCore.Slot()
    def recognition_sound_files(self):
        """Recognition of all chosen sounds files in a separate thread."""
        if not self.recognitions_sounds:
            self.result.setText("There are no sounds!")
            return  # If there are no sounds, do nothing

        self.but_recognition_sound.setEnabled(False)  # Disable the button "Recognition of sounds"
        self.recognition_thread_audio = RecognitionThreadSound(self.recognitions_sounds)
        self.recognition_thread_audio.finished_signal.connect(self.update_ui_after_recognition_sound)
        self.recognition_thread_audio.start()  # Launch the thread

    @QtCore.Slot(str)
    def update_ui_after_recognition_sound(self, result_text):
        """Update UI after recognition is finished."""
        self.text_edit_sound.setPlainText(result_text)
        self.result.setText("Sound recognition is finished!")  # Update result text
        self.recognition_thread_audio.quit()  # closing the thread
        self.but_recognition_sound.setEnabled(True)  # Enable the button "Recognition of sounds"

    @QtCore.Slot(str)
    def recognition_pdf_files(self):
        """Recognition of all chosen PDF files in a separate thread."""
        if not self.recognitions_pdfs:
            self.result.setText("There are no PDFs!")
            return  # If there are no PDFs, do nothing

        self.but_recognition_pdf.setEnabled(False)  # Disable the button "Recognition of PDFs"
        self.recognition_thread_pdf = RecognitionThreadPDF(self.recognitions_pdfs)
        self.recognition_thread_pdf.finished_signal.connect(self.update_ui_after_recognition_pdf)
        self.recognition_thread_pdf.start()  # Launch the thread

    @QtCore.Slot(str)
    def update_ui_after_recognition_pdf(self, result_text):
        """Update UI after recognition is finished."""
        self.text_edit_pdf.setPlainText(result_text)
        self.result.setText("PDF recognition is finished!")  # Update result text
        self.recognition_thread_pdf.quit()  # closing the thread
        self.but_recognition_pdf.setEnabled(True)  # Enable the button "Recognition of PDFs"

    def clear_files(self, widget_in_stack):
        del self.recognitions_files_name[widget_in_stack][:]  # delete all items in the list

    def placement_image(self, image):
        """Placing the image in the label"""
        if type(image) == str:
            pixmap = QPixmap(image)
        else:
            image = ImageQt(image)
            pixmap = QPixmap.fromImage(image)
        scaled = pixmap.scaled(self.label_image.size(), QtCore.Qt.KeepAspectRatio)  # scaling the image
        self.label_image.setPixmap(scaled)

    def load_sound(self, path):
        self.label_select_audio_file.setText(path.split("/")[-1])  # change the text (name file) in the label
        wrap_text(self.label_select_audio_file)

    def load_pdf(self, path):
        self.label_select_pdf_file.setText(path.split("/")[-1])  # change the text (name file or directory) in the label
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
