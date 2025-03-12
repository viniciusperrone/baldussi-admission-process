from mongoengine import Document, StringField, DateTimeField
from datetime import datetime


CHOICES_STATUS = (
    ('DONE', 'DONE'),
    ('PENDING', 'PENDING'),
    ('FAILED', 'FAILED')
)

class AudioModel(Document):
    filename = StringField(required=True)
    file_url = StringField(required=True)
    transcription_text = StringField(required=False)
    status = StringField(required=True, choices=CHOICES_STATUS)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'indexes': [
            'filename',
            'status',
            {'fields': ['$transcription_text']}
        ]
    }
