# -*- coding: utf-8 -*-
"""
    Flask Memo
    ~~~~~~

    A memo web application example written with
    Flask and sqlAlchemy.

"""

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from config import Config

#model
from datetime import datetime
import os
from flask_migrate import Migrate

#route
from flask_cors import CORS, cross_origin
from flask import Flask, render_template, url_for, flash, redirect, jsonify

# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config.from_object(Config)


db = SQLAlchemy(app)

def create_app(Config):
    app = FlaskAPI(__name__, instance_relative_config=True)
    cors = CORS(app)
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    return app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    memos = db.relationship('Memo', backref='author', lazy=True)

    # def __repr__(self):
    #     return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Memo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # def __repr__(self):
    #     return f"Memo('{self.title}', '{self.content}')"


memos = [
    {
        'author': 'John Smith',
        'title': 'Memo 1',
        'content': 'First memo content',
        'date_posted': 'April 29, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Memo 2',
        'content': 'Second memo content',
        'date_posted': 'April 29, 2018'
    }
]

def init_db():
    """Initializes the database."""
    app = Flask(__name__)
    db.init_app(app)
    db.create_all()
    return app

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', memos=memos)



@app.route("/memo", methods=['GET', 'POST'])
@cross_origin(origin='*')
def memo():
    return jsonify('hello from server')



@app.route("/empty")
def empty():
    return ('No entries here so far')
