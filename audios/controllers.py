from flask import request, jsonify
import json

from audios.models import AudioModel
from audios.schemas import AudioSchema
from audios.services import AudioSaveService, TranscriptionService

from utils.helpers_files import allowed_file


def upload_file():
    file = request.files.get("file", None)

    if not file or not file.filename:
        return jsonify({"message": "No file provided"}), 400

    if allowed_file(file.filename):
        audio_save_service = AudioSaveService(file)
        audio_schema = AudioSchema()

        data_file = audio_save_service.save_file_local()

        filename = data_file["filename"]
        filepath = data_file["filepath"]

        transcription_service = TranscriptionService(filepath, filename)

        transcribed_audio = transcription_service.transcribe_audio()

        inserted_audio = AudioModel.create_audio(
            filename=transcribed_audio["filename"],
            filepath=transcribed_audio["filepath"],
            transcription=transcribed_audio["transcription"],
            status=transcribed_audio["status"]
        )

        inserted_id = inserted_audio.inserted_id

        saved_audio = AudioModel.get_audio_by_id(inserted_id)

        return jsonify(audio_schema.dump(saved_audio)), 201

    return jsonify({"error": "Invalid file type"}), 400
