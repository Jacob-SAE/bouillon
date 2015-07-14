import os

DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'test.db')
DATABASE_CONNECT_OPTIONS = {}
THREADS_PER_PAGE = 8
CSRF_ENABLED = True
CSRF_SESSION_KEY = 'thisisabadsecretchangeme'
SECRET_KEY = 'changeme'
