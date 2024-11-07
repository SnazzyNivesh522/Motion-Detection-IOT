import os 
import face_recognition
import csv
from datetime import datetime
import numpy as np
from werkzeug.utils import secure_filename
import uuid
from config import Config

def load_known_faces(directory):
    known_faces = []
    known_names = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image = face_recognition.load_image_file(os.path.join(directory, filename))
            encodings = face_recognition.face_encodings(image)
            if encodings:
                encoding = encodings[0]
                known_faces.append(encoding)
                known_names.append(os.path.splitext(filename)[0])
            else:
                print(f"No face found in {filename}. Skipping.")
    return known_faces, known_names

known_faces_dir = 'Training_images'
known_faces, known_names = [], []
if os.path.exists(known_faces_dir):
    known_faces, known_names = load_known_faces(known_faces_dir)

attendance_file = 'attendance.csv'
def mark_attendance(name, attendance_file):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    if not os.path.isfile(attendance_file):
        with open(attendance_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Date", "Time"])

    with open(attendance_file, 'r+', newline='') as f:
        reader = csv.reader(f)
        existing_entries = [row[0] for row in list(reader)]
        if name not in existing_entries:
            writer = csv.writer(f)
            writer.writerow([name, date, time])

def recognize_faces(image_path):
    # Load the uploaded image
    image = face_recognition.load_image_file(image_path)

    # Detect faces and get encodings
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    recognized_names = []

    for face_encoding in face_encodings:
        face_distances = face_recognition.face_distance(known_faces, face_encoding)
        best_match_index = np.argmin(face_distances)

        if face_distances[best_match_index] < 0.6:
            name = known_names[best_match_index]
            recognized_names.append(name)
            mark_attendance(name, attendance_file)
        else:
            recognized_names.append("Unknown")

    return recognized_names



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS



def save_securely(file):
    filename = secure_filename(file.filename)
    unique_filename = str(uuid.uuid4())+ "_" +filename
    file.save(os.path.join(Config.UPLOAD_FOLDER, unique_filename))
    return unique_filename

