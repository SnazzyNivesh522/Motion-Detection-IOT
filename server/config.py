import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER=os.getenv('UPLOAD_FOLDER')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    FRONTEND_URL = os.getenv('FRONTEND_URL')
    
