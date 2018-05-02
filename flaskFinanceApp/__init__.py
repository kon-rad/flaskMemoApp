# all the imports
from .flaskFinanceApp import app
import os
from models import Base, User
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
  SQLALCHEMY_DATABASE_URI='sqlite:////tmp/test.db'
  SECRET_KEY='development key',
  USERNAME='admin',
  PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

db = SQLAlchemy(app)