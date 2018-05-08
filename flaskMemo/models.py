
#model
from datetime import datetime
import os
from flaskMemo import db


class Memo(db.Model):
    """This class represents the Memo table."""

    __tablename__ = 'memo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, title):
        """initialize with title."""
        self.title = title

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Memo.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Memo: {}>".format(self.title)

    @staticmethod
    def generate_fake(count=100, **kwargs):
        """Generate a number of fake memos for testing."""
        from sqlalchemy.exc import IntegrityError
        from random import seed, choice
        from faker import Faker

        fake = Faker()

        seed()
        for i in range(count):
            m = Memo(
                title=fake.lorem(),
                content=fake.text(),
                **kwargs)
            db.session.add(m)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()



class User(db.Model):
    """This class represents the User table."""

    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    memos = db.relationship('Memo', backref='author', lazy=True)

    def __init__(self, username):
        """initialize with username."""
        self.username = username

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<User: {}>".format(self.name)

    @staticmethod
    def generate_fake(count=100, **kwargs):
        """Generate a number of fake users for testing."""
        from sqlalchemy.exc import IntegrityError
        from random import seed, choice
        from faker import Faker

        fake = Faker()

        seed()
        for i in range(count):
            u = User(
                username=fake.first_name(),
                email=fake.email(),
                password='password',
                **kwargs)
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

    def __repr__(self):
        return '<User \'%s\'>' % self.full_name()
