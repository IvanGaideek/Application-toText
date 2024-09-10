import whisper


class RecognitionProcessingSound:
    def __init__(self, audio_path):
        self.audio_path = audio_path
        self.lang = None  # Language
        self.name_model = "base"

    @property
    def recognize_text(self):
        model = whisper.load_model("base")
        result = model.transcribe(self.audio_path, language=self.lang)  # Transcribe audio file with language
        return result["text"]  # recognized text
