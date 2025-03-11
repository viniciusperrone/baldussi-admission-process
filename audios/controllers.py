from flask import request, jsonify

from audios.services import AudioSaveService

from utils.helpers_files import allowed_file


def upload_file():
    file = request.files.get("file", None)

    if not file or not file.filename:
        return jsonify({"message": "No file provided"}), 400

    if allowed_file(file.filename):
        audio_save_service = AudioSaveService(file)

        filepath = audio_save_service.save_file_local()

        return jsonify({"path": filepath}), 200

    return jsonify({"error": "Invalid file type"}), 400
