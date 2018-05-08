# -*- coding: utf-8 -*-
"""
    Flask Memo
    ~~~~~~

    A memo web application example written with
    Flask and sqlAlchemy.

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config)

db = SQLAlchemy(app)

def init_db():
    """Initializes the database."""
    app = Flask(__name__)
    db.init_app(app)
    db.create_all()
    return app

import routes