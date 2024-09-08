from PySide6 import QtCore
from PIL import Image

from process_recognition_image import RecognitionProcessingImage


class RecognitionThread(QtCore.QThread):
    finished_signal = QtCore.Signal(str, list)  # in list: Image.Image

    def __init__(self, image_paths):
        super().__init__()
        self.image_paths = image_paths

    def run(self):
        result_text = ""
        final_images = []

        for path in self.image_paths:
            image = RecognitionProcessingImage(path)
            result_text += image.recognize_text  # Result text
            result_text += "\n----------Separator-----------\n"
            final_images.append(image.before_image)  # Updated image after recognition

        self.finished_signal.emit(result_text, final_images)  # Signal that the thread is finished
