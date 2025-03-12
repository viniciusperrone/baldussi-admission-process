from flask import Blueprint

from audios.controllers import list_transcriptions, detail_transcription, update_transcription, delete_transcription


transcriptions_blueprint = Blueprint('transcriptions', __name__)

transcriptions_blueprint.add_url_rule('/transcriptions/list', view_func=list_transcriptions, methods=['GET'])
transcriptions_blueprint.add_url_rule('/transcriptions/<string:transcription_id>/', view_func=detail_transcription, methods=['GET'])
transcriptions_blueprint.add_url_rule('/transcriptions/<string:transcription_id>/', view_func=update_transcription, methods=['PUT'])
transcriptions_blueprint.add_url_rule('/transcriptions/<string:transcription_id>/', view_func=delete_transcription, methods=['DELETE'])
