import os
import whisper
from auxiliary_funcs import get_current_time
from operation_with_settings import get_data_settings


class RecognitionProcessingSound:
    def __init__(self, audio_path):
        self.audio_path = audio_path

        # Open and read the JSON (settings) file
        data = get_data_settings()

        self.values_setting = data["sound_settings"]
        self.lang = self.values_setting["ALL_LANGS"][self.values_setting["DEFAULT_LANG"]]  # Language (one, str)
        self.name_model = self.values_setting["ALL_MODELS"][self.values_setting["DEFAULT_MODEL"]]
        self.save_path = data["save_path"]["for_sound"]
        self.name_file = self.audio_path.split(".")[0].split("/")[-1]
        self.errors = []  # List of errors (time, str)

    def convert_to_TXT(self, text):
        """Converts the audio file to .txt format."""
        if os.path.isdir(self.save_path):  # Check if the directory exists
            with open(self.save_path + self.name_file + ".txt", "w", encoding="utf-8") as file:
                file.write(text)
        else:
            self.errors.append((get_current_time(), "This directory is for saving .txt does not exist!"))

    @property
    def recognize_text(self):
        """Main function to recognize text in the audio file"""
        text = self.get_text()
        if self.values_setting["SAVE_TXT_FILE"]:
            self.convert_to_TXT(text)
        return text, self.errors

    def get_text(self):
        model = whisper.load_model(self.name_model)
        result = model.transcribe(self.audio_path, language=self.lang)  # Transcribe audio file with language
        return result["text"]  # recognized text
