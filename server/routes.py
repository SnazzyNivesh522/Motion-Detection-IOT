from flask import Blueprint,request,jsonify, send_from_directory
from utils import allowed_file,save_securely,recognize_faces
import os
from config import Config
from models import Event
from extensions import db

routes_blueprint=Blueprint('routes', __name__)

@routes_blueprint.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    if file and allowed_file(file.filename):
        unique_filename = save_securely(file)
        uploaded_image_path = os.path.join(Config.UPLOAD_FOLDER, unique_filename)

        # Perform face recognition
        recognized_faces = recognize_faces(uploaded_image_path)

        # Save event in the database
        event = Event(image=unique_filename, classified_person=", ".join(recognized_faces))
        db.session.add(event)
        db.session.commit()

        return jsonify({'recognized_faces': recognized_faces}), 201
    else:
        return jsonify({'error': 'Allowed file types are png, jpg, jpeg'}), 400

@routes_blueprint.route('/events', methods=['GET'])
def get_events():
    events = Event.query.order_by(Event.timestamp.desc()).all()
    events_data = [event.to_dict() for event in events]
    return jsonify(events_data), 200

@routes_blueprint.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get(event_id)
    if event is None:
        return jsonify({'error': 'Event not found'}), 404
    return jsonify(event.to_dict()), 200

@routes_blueprint.route('/image/<filename>', methods=['GET'])
def get_image(filename):
    return send_from_directory(Config.UPLOAD_FOLDER, filename)