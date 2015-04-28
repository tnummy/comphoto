# import numpy as np
# import cv2
import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TESTING = True

ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'SecretKeyForSessionSigning'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED=True
CSRF_SESSION_KEY="somethingimpossibletoguess"

UPLOAD_FOLDER = _basedir+'/static/uploads'
SAVE_FOLDER = _basedir+'/static/results'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'bmp'])