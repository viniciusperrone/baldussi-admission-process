from flask import request, jsonify
from bson.objectid import ObjectId

from config.mongo import mongo

from transcriptions.models import TranscriptionModel
from transcriptions.schemas import TranscriptionSchema


def list_transcriptions():
    transcriptions = TranscriptionModel.list_transcriptions()
    transcriptions_schema = TranscriptionSchema(many=True)

    return jsonify(transcriptions_schema.dump(transcriptions)), 200

def detail_transcription(transcription_id):
    transcription = TranscriptionModel.get_transcription_by_id(transcription_id)
    transcription_schema = TranscriptionSchema()

    if not transcription:
        return jsonify({"message": "Doesn't match transcription with given id"}), 404

    return jsonify(transcription_schema.dump(transcription)), 200

def update_transcription(transcription_id):
    transcription = TranscriptionModel.get_transcription_by_id(transcription_id)
    transcription_schema = TranscriptionSchema(partial=True)

    data = request.get_json()

    if not transcription:
        return jsonify({"message": "Doesn't match transcription with given id"}), 404


    try:
        TranscriptionModel.updated_transcription(transcription_id, data)

        updated_transcription = TranscriptionModel.get_transcription_by_id(transcription_id)

        return jsonify(transcription_schema.dump(updated_transcription)), 200

    except Exception as e:
        return jsonify({"message": "Internal Server Error", "error": str(e)}), 500

def delete_transcription(transcription_id):
    transcription = TranscriptionModel.get_transcription_by_id(transcription_id)

    if not transcription:
        return jsonify({"message": "Doesn't match transcription with given id"}), 404

    try:
        TranscriptionModel.collection.delete_one({"_id": ObjectId(transcription_id)})

        return jsonify({"message": "Transcript deleted successfully"}), 201

    except Exception as e:
        return jsonify({"message": "Internal Server Error"}), 201


def search_transcriptions_by_query():
    query = request.args.get("query", None)

    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    results = list(mongo.db.transcriptions.find({"$text": {"$search": query}}))

    return jsonify({"results": results}), 200
