from datetime import datetime
from bson.objectid import ObjectId

from config.mongo import mongo


class AudioModel:
    collection = mongo.db.audios

    @staticmethod
    def get_audio_by_id(audio_id: str):
        try:
            return AudioModel.collection.find_one({"_id": ObjectId(audio_id)})
        except Exception as e:
            print(f"Erro ao buscar áudio por ID: {e}")
            return None

    @staticmethod
    def create_audio(filename, filepath, transcription, status):
        audio_data = {
            "filename": filename,
            "filepath": filepath,
            "transcription_text": transcription,
            "status": status,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        return AudioModel.collection.insert_one(audio_data)

    @staticmethod
    def get_audio_by_filename(filename):
        return AudioModel.collection.find_one({"filename": filename})

    @staticmethod
    def update_audio_status(filename, status):
        return AudioModel.collection.update_one(
            {"filename": filename},
            {"$set": {"status": status, "updated_at": datetime.utcnow()}}
        )

    @staticmethod
    def list_audios():
        return list(AudioModel.collection.find())
