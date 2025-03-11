from flask import request, jsonify
import json

from audios.services import AudioSaveService, TranscriptionService

from utils.helpers_files import allowed_file


def upload_file():
    file = request.files.get("file", None)

    if not file or not file.filename:
        return jsonify({"message": "No file provided"}), 400

    if allowed_file(file.filename):
        audio_save_service = AudioSaveService(file)

        filepath = audio_save_service.save_file_local()

        transcription_service = TranscriptionService(filepath)

        transcribe_audio = transcription_service.transcribe_audio()

        if not transcribe_audio:
            return jsonify({"error": "Unable to perform action"}), 400

        return jsonify(json.dumps(transcribe_audio)), 200

    return jsonify({"error": "Invalid file type"}), 400
