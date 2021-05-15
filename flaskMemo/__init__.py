
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import app_config
from flask_cors import CORS

from flask_cors import cross_origin
from flask import render_template, redirect, jsonify, request

db = SQLAlchemy()

def create_app(config_name = "development"):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    cors = CORS(app)
    db.init_app(app)


    #    routes
    memos = [
        {
            'title': 'App idea 1',
            'content': 'Instagram for cats'
        },
        {
            'title': 'App idea 2',
            'content': 'Tree identification AI app'
        }
    ]

    @app.route("/")
    @app.route("/home")
    def home():
        return render_template('home.html', memos=memos)

    @app.route("/memos", methods=['GET', 'POST'])
    @cross_origin(origin='*')
    def memo():
        if request.method == "POST":
            title = request.json['title']
            content = request.json['content']
            if title and content:
                memo = Memo(title=title, content=content)
                memo.save()
                response = jsonify({
                    'id': memo.id,
                    'title': memo.title,
                    'content': memo.content
                })
                response.status_code = 201
                return response
        else:
            # GET
            memos = memo.get_all()
            results = []

            for memo in memos:
                obj = {
                    'id': memo.id,
                    'title': memo.title,
                    'content': memo.content
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
        return response



    @app.route("/empty")
    def empty():
        return ('No entries here so far')



    from .models import Memo


    return app

