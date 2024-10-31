from flask import Blueprint,request,jsonify, send_from_directory
from utils import allowed_file, save_securely, classify_image
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
        classified_person = classify_image(os.path.join(Config.UPLOAD_FOLDER,unique_filename))
        event=Event(image=unique_filename,classified_person=classified_person)
        db.session.add(event)
        db.session.commit()
        return jsonify({'classified_person': classified_person}), 201
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