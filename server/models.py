from extensions import db
from datetime import datetime, timedelta
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    image = db.Column(db.String(200), nullable=False)
    classified_person = db.Column(db.String(100), nullable=False)
    annotated_image = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp.isoformat(),
            'image': self.image,
            'classified_person': self.classified_person,
            'annotatedImage': self.annotated_image
        }
