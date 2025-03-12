from marshmallow import Schema, fields, validate
from bson import ObjectId


CHOICES_STATUS = (
    ('PENDING', 'PENDING'),
    ('FAILED', 'FAILED'),
    ('DONE', 'DONE'),
)

class ObjectIdField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if isinstance(value, ObjectId):
            return str(value)
        return None


class TranscriptionSchema(Schema):
    id = ObjectIdField(attribute="_id")
    filename = fields.Str(required=True)
    filepath = fields.Str(required=True)
    transcription_text = fields.Str(required=False, nullable=True)
    status = fields.Str(required=True, validate=validate.OneOf([choice[0] for choice in CHOICES_STATUS]))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
