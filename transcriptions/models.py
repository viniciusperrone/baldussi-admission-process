from datetime import datetime as dt
from bson.objectid import ObjectId

from config.mongo import mongo


class TranscriptionModel:
    collection = mongo.db.transcriptions

    @staticmethod
    def get_transcription_by_id(transcription_id: str):
        try:
            return TranscriptionModel.collection.find_one({"_id": ObjectId(transcription_id)})
        except Exception as e:
            print(f"Erro ao buscar áudio por ID: {e}")
            return None

    @staticmethod
    def create_transcription(filename, filepath, transcription, status):
        transcription_data = {
            "filename": filename,
            "filepath": filepath,
            "transcription_text": transcription,
            "status": status,
            "created_at": dt.utcnow(),
            "updated_at": dt.utcnow()
        }
        return TranscriptionModel.collection.insert_one(transcription_data)

    @staticmethod
    def updated_transcription(transcription_id, update_data):
        setattr(update_data, "updated_at", dt.utcnow())

        return TranscriptionModel.collection.update_one(
            {"_id": ObjectId(transcription_id)},
            {"$set": update_data}
        )

    @staticmethod
    def list_transcriptions():
        return list(TranscriptionModel.collection.find())

    @staticmethod
    def remove_transcription(transcription_id: str):
        try:
            result = TranscriptionModel.collection.delete_one({"_id": ObjectId(transcription_id)})
            if result.deleted_count > 0:
                return True
            else:
                return False
        except Exception as e:
            print(str(e))
            return False
