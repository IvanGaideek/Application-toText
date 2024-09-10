from PySide6 import QtCore

from process_recognition_image import RecognitionProcessingImage
from process_recognition_sound import RecognitionProcessingSound


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


class RecognitionThreadSound(QtCore.QThread):
    finished_signal = QtCore.Signal(str)

    def __init__(self, audio_paths):
        super().__init__()
        self.audio_paths = audio_paths  # List of paths to audio files

    def run(self):
        result_text = ""
        for path in self.audio_paths:
            result_text += RecognitionProcessingSound(path).recognize_text
            result_text += "\n----------Separator-----------\n"
        self.finished_signal.emit(result_text)  # Signal that the thread is finished
