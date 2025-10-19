import os

class Config:
    # Security
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    
    # Database configuration (defaulting to a local SQLite database)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///pearlbox.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Email configuration (for order notifications)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'jk0000000908@gmail.com'
    MAIL_PASSWORD = 'Nk29411492'
    MAIL_DEFAULT_SENDER = 'jk0000000908@gmail.com'
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL') or 'admin@pearlbox.com'
    
    # Upload folder for product images
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'images')
