from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flasgger import swag_from

from transcriptions.models import TranscriptionModel
from transcriptions.schemas import TranscriptionSchema

from audios.services import AudioSaveService, TranscriptionService

from utils.helpers_files import allowed_file


@swag_from({
    'tags': ['Upload de Áudio'],
    'summary': 'Upload de arquivo de áudio e transcrição',
    'description': 'Aqui fazermos upload do arquivo e transcrevemos com a API da OpenAI e salvamos no banco Mongo',
    'parameters': [
        {
            'name': 'file',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': 'Arquivo de áudio para transcrição'
        }
    ],
    'responses': {
        201: {'description': 'Audio sent and transcribed successfully'},
        400: {'description': 'Invalid file or no file uploaded'},
        401: {'description': 'Missing Token'},
        500: {'description': 'Internal server error'},
    }
})
@jwt_required()
def upload_file():
    file = request.files.get("file", None)

    if not file or not file.filename:
        return jsonify({"message": "No file provided"}), 400

    if allowed_file(file.filename):
        audio_save_service = AudioSaveService(file)
        transcription_schema = TranscriptionSchema()

        data_file = audio_save_service.save_file_local()

        filename = data_file["filename"]
        filepath = data_file["filepath"]

        transcription_service = TranscriptionService(filepath, filename)

        transcribed_audio = transcription_service.transcribe_audio()

        transcription = TranscriptionModel.create_transcription(
            filename=transcribed_audio["filename"],
            filepath=transcribed_audio["filepath"],
            transcription=transcribed_audio["transcription"],
            status=transcribed_audio["status"]
        )

        inserted_id = transcription.inserted_id

        saved_transcription = TranscriptionModel.get_transcription_by_id(inserted_id)

        return jsonify(transcription_schema.dump(saved_transcription)), 201

    return jsonify({"error": "Invalid file type"}), 400
