from PySide6 import QtCore
from PIL import Image

from process_recognition_image import RecognitionProcessingImage
from process_recognition_pdf import RecognitionProcessingPDF
from process_recognition_sound import RecognitionProcessingSound


class RecognitionThreadImage(QtCore.QThread):
    finished_one_rec_signal = QtCore.Signal(str, Image.Image)  # A signal for transmitting the results of each image
    all_finished_signal = QtCore.Signal()

    def __init__(self, image_paths):
        super().__init__()
        self.image_paths = image_paths

    def run(self):
        result_text = ""

        for path in self.image_paths:
            image = RecognitionProcessingImage(path)
            result_text += image.recognize_text  # Result text
            result_text += "\n----------Separator-----------\n"
            picture_image = image.before_image
            self.finished_one_rec_signal.emit(result_text, picture_image)  # Signal that the thread is finished

        self.all_finished_signal.emit()  # Signal that the thread is finished


class RecognitionThreadSound(QtCore.QThread):
    finished_signal = QtCore.Signal(str, list)

    def __init__(self, audio_paths):
        super().__init__()
        self.audio_paths = audio_paths  # List of paths to audio files

    def run(self):
        result_text = ""
        all_errors = []
        for path in self.audio_paths:
            text, errors = RecognitionProcessingSound(path).recognize_text
            all_errors = errors + all_errors
            result_text += text
            result_text += "\n----------Separator-----------\n"
        self.finished_signal.emit(result_text, all_errors)  # Signal that the thread is finished


class RecognitionThreadPDF(QtCore.QThread):
    finished_signal = QtCore.Signal(str, list)

    def __init__(self, pdf_paths):
        super().__init__()
        self.pdf_paths = pdf_paths  # List of paths to PDF files

    def run(self):
        result_text = ""
        all_errors = []
        for path in self.pdf_paths:
            text, errors = RecognitionProcessingPDF(path).recognize
            all_errors = errors + all_errors
            result_text += text
            result_text += "\n----------Separator-----------\n"
        self.finished_signal.emit(result_text, all_errors)  # Signal that the thread is finished
