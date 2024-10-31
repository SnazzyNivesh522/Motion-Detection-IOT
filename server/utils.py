import os
import numpy as np
from tensorflow.keras.preprocessing import image
import pickle
from config import Config
from werkzeug.utils import secure_filename
import uuid
import tensorflow as tf

model_binary = tf.keras.models.load_model('model_binary.keras')
with open('class_indices_binary.pkl', 'rb') as f:
    class_indices_binary = pickle.load(f)

class_labels_binary = {v: k for k, v in class_indices_binary.items()}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def preprocess_image(img_path):
    img=image.load_img(img_path, target_size=(512,512))
    image_array=image.img_to_array(img)
    image_array=image_array/255.0
    image_array=np.expand_dims(image_array,0)
    return image_array

def save_securely(file):
    filename = secure_filename(file.filename)
    unique_filename = str(uuid.uuid4())+ "_" +filename
    file.save(os.path.join(Config.UPLOAD_FOLDER, unique_filename))
    return unique_filename

def predict_image(model, img_array):
    prediction = model.predict(img_array)
    return prediction

def classify_image(image_path):
    img=preprocess_image(image_path)
    prediction=predict_image(model_binary, img)
    print(prediction)
    if prediction[0] < 0.5:
        predicted_class = class_labels_binary[0]
    else:
        predicted_class = class_labels_binary[1]
    print(f"Predicted class: {predicted_class}")
    print(f"Probability: {prediction[0][0]:.4f}")
    return predicted_class
