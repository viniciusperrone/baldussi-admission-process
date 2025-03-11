import os
from datetime import datetime as dt

import openai

from werkzeug.utils import secure_filename
from utils.helpers_files import UPLOAD_FOLDER


openai.api_key = os.getenv("OPENAI_API_KEY")

class AudioSaveService():

    def __init__(self, file) -> None:
        self.file = file
        self.filename = None

    def __generate_security_filename(self):
        self.filename = secure_filename(self.file.filename)

    def __ensure_upload_folder_exists(self):
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

    def save_file_local(self):
        self.__ensure_upload_folder_exists()

        self.__generate_security_filename()

        filepath = os.path.join(UPLOAD_FOLDER, self.filename)

        self.file.save(filepath)

        return filepath

class TranscriptionService:
    def __init__(self, file_path, filename):
        self.file_path = file_path
        self.filename = filename

    def transcribe_audio(self):
        try:
            with open(self.file_path, "rb") as audio_file:
                response = openai.Audio.transcribe("whisper-1", audio_file)

            transcription_text = response["text"]

            transcription_data = {
                "filename": self.filename,
                "transcription": transcription_text,
                "status": "REALIZED",
                "created_at": dt.utcnow()
            }

            return transcription_data

        except Exception as e:
            return None
