from datetime import datetime as dt
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
            "created_at": dt.utcnow(),
            "updated_at": dt.utcnow()
        }
        return AudioModel.collection.insert_one(audio_data)

    @staticmethod
    def updated_audio(audio_id, update_data):
        update_data["updated_at"] = dt.utcnow()

        AudioModel.collection.update_one(
            {"_id": ObjectId(audio_id)},
            {"$set": update_data}
        )

        updated_audio = AudioModel.collection.find_one({"_id": ObjectId(audio_id)})

        return updated_audio

    @staticmethod
    def list_audios():
        return list(AudioModel.collection.find())

    @staticmethod
    def remove_audio(audio_id: str):
        try:
            result = AudioModel.collection.delete_one({"_id": ObjectId(audio_id)})
            if result.deleted_count > 0:
                return True
            else:
                return False
        except Exception as e:
            print(str(e))
            return False
