import os 
import face_recognition
import csv
from datetime import datetime
import numpy as np
from werkzeug.utils import secure_filename
import uuid
from config import Config
import cv2

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
# Load known faces
known_faces, known_names = load_known_faces(known_faces_dir)
print(f"Loaded {len(known_faces)} known faces: {', '.join(known_names)}")


def recognize_faces(image_path):
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    name_confidences = {}
    recognized_faces = []

    for face_encoding in face_encodings:
        face_distances = face_recognition.face_distance(known_faces, face_encoding)
        best_match_index = np.argmin(face_distances)

        if face_distances[best_match_index] < 0.6:
            name = known_names[best_match_index]
            confidence = 1 - face_distances[best_match_index]
            name_confidences[name] = max(name_confidences.get(name, 0), confidence)
        else:
            name = "Unknown"
            confidence = 0.0

        label = f"{name} ({confidence:.2f})"
        recognized_faces.append(label)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(image, label, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)
        print(f"Face at ({left}, {top}, {right}, {bottom}): {label}")

    # Save the annotated image to display in the frontend
    annotated_filename = f"annotated_{uuid.uuid4()}_{os.path.basename(image_path)}"
    annotated_image_path = os.path.join(Config.UPLOAD_FOLDER, annotated_filename)
    cv2.imwrite(annotated_image_path, image)

    return annotated_filename, recognized_faces

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS



def save_securely(file):
    filename = secure_filename(file.filename)
    unique_filename = str(uuid.uuid4())+ "_" +filename
    file.save(os.path.join(Config.UPLOAD_FOLDER, unique_filename))
    return unique_filename

