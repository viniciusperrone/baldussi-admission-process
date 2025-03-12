from marshmallow import Schema, fields
from bson import ObjectId


class ObjectIdField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if isinstance(value, ObjectId):
            return str(value)
        return None


class AudioSchema(Schema):
    id = ObjectIdField(attribute="_id")
    filename = fields.Str(required=True)
    filepath = fields.Str(required=True)
    transcription_text = fields.Str(required=False, nullable=True)
    status = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
