from extensions import db
from datetime import datetime

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    image = db.Column(db.String(200), nullable=False)
    classified_person = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp.isoformat(),
            'image': self.image_path,
            'classified_person': self.classified_person
        }