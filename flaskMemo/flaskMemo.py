# -*- coding: utf-8 -*-
"""
    Flask Memo
    ~~~~~~

    A memo web application example written with
    Flask and sqlAlchemy.

"""

from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_object(Config)

db = SQLAlchemy(app)

from flaskMemo import routes