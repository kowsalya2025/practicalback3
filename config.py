import os

class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///students.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'kowsalyacse1992@gmail.com'  
    MAIL_PASSWORD = 'mljunabrnedeunpx'  
