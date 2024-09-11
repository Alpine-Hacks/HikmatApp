import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'your_secret_key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database/hikmat.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
