
##GENERAL NOTES

###socket.error: [Errno 48] Address already in use
server already in use
ps -fA | grep python
kill 81651

Find the process using port 8080:

sudo lsof -i:5000

Kill it:

kill -9 XXXX


1. start virtualenv
$ . venv/bin/activate
And if you want to go back to the real world, use the following command:
$ deactivate

to create new virtualenv
$ virtualenv venv

2. install the application ( or try this before step 1 )
pip install --editable .

also checkthis out
pip freeze
pip freeze > requirements.txt

The above installation command assumes that it is run within the projects root directory, flaskr/. The editable flag allows editing source code without having to reinstall the Flask app each time you make changes. The flaskr app is now installed in your virtualenv (see output of pip freeze).

3. create db manual
(venv) $ createdb test_db
(venv) $ createdb flask_api


python flaskMemo
from flaskMemo import db
db.create_all()
from flaskMemo import User, Memo
user_1 = User(username='Corey', email='C@demo.com', password='password')
db.session.add(user_1)
user_2 = User(username='Corey2', email='C2@demo.com', password='password')
db.session.add(user_2)
db.session.commit()
User.query.all()
user = User.query.filter_by(username='Corey').first()
memo_1 = Memo(title='memo1', content='First memo content', user_id=user.id)
memo_2 = Memo(title='memo2', content='First memo content2', user_id=user.id)

db.session.add(memo_1)
db.session.add(memo_2)
db.session.commit()

user.memos
memo = Memo.query.first()
>>> memo
<Memo 1>
>>>
>>> memo.user_id
1
>>> memo.author
<User 1>

db.drop.all()
db.create_all()

4. Run app


export FLASK_APP=flaskMemo
APP_SETTINGS="development"
export FLASK_DEBUG=true
flask run

another way -> 
$ export FLASK_APP="run.py"
$ export APP_SETTINGS="development"
$ export SECRET="a-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"
$ export DATABASE_URL="postgresql://localhost/flask_api"

also can use python run.py


5. Test app
python setup.py test

https://github.com/mitsuhiko/flask-sqlalchemy/issues/98

export FLASK_APP=flaskFinanceApp
export FLASK_DEBUG=true
flask run


###Debugging

if says package is not installed try
import sys
print(sys.path)
this will show you where your available packages are installed.

What's your favorite Flask boilerplate? Why?
https://github.com/realpython/flask-boilerplate
https://github.com/hack4impact/flask-base

 https://github.com/kkinder/GAEStarterKit
https://github.com/sloria/cookiecutter-flask
https://github.com/MaxHalford/Flask-Boilerplate
https://github.com/mjhea0/flask-boilerplate
https://github.com/lassegit/flask-reactjs
https://github.com/hack4impact/flask-base