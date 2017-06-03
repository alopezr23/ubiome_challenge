import os


_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = os.environ.get('DEBUG')
use_reloader = True

SECRET_KEY = os.environ.get('SECRET_KEY')
MONGODB_URI = os.environ.get('MONGODB_URL')
DATABASE_CONNECT_OPTIONS = os.environ.get('DATABASE_CONNECT_OPTIONS')

del os
