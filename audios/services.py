import os
from datetime import datetime as dt

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

from werkzeug.utils import secure_filename
from utils.helpers_files import UPLOAD_FOLDER


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

        return {
            "filename": self.filename,
            "filepath": filepath
        }

class TranscriptionService:
    def __init__(self, filepath, filename):
        self.filepath = filepath
        self.filename = filename

    def transcribe_audio(self):
        try:
            audio_file = open(self.filepath, "rb")

            response = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )

            transcription_text = response.text

            transcription_data = {
                "filename": self.filename,
                "filepath": self.filepath,
                "transcription": transcription_text,
                "status": "DONE",
                "created_at": dt.utcnow().isoformat()
            }

            return transcription_data

        except Exception as e:
            transcription_data = {
                "filename": self.filename,
                "filepath": self.filepath,
                "transcription": None,
                "status": "FAILED",
            }

            return transcription_data
