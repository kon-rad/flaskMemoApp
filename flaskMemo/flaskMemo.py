# -*- coding: utf-8 -*-
"""
    Flask Memo
    ~~~~~~

    A memo web application example written with
    Flask and sqlAlchemy.

"""

from datetime import datetime
import os
from flask import Flask, render_template, url_for, flash, redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.from_object(Config)


db = SQLAlchemy(app)

def init_db():
    """Initializes the database."""
    app = Flask(__name__)
    db.init_app(app)
    db.create_all()
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

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', memos=memos)
    
@app.route("/empty")
def empty():
    return ('No entries here so far')

# def connect_db():
#     """Connects to the specific database."""
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flaskMemo'
#     db = SQLAlchemy(app)
#     return db




# @app.cli.command('initdb')
# def initdb_command():
#     """Creates the database tables."""
#     init_db()
#     print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


# @app.teardown_appcontext
# def close_db(error):
#     """Closes the database again at the end of the request."""
#     if hasattr(g, 'sqlite_db'):
#         g.sqlite_db.close()

