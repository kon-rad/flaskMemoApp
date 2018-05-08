from flask_cors import cross_origin
from flask import render_template, redirect, jsonify, request
from models import User, Memo
from flaskMemo import app


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