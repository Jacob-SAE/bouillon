from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

API_BASE = '/api/v1'

Server = Flask(__name__)
Server.config.from_object('config')
db = SQLAlchemy(Server)

import test.models

db.create_all()
