from . import db
from sqlalchemy import ForeignKey
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User {}>'.format(self.username) 
    
    def to_dict(self):
        return {
        'id': self.id,
        'username': self.username,
        'email': self.email
    }
    
class Bank(db.Model):
    __tablename__ = "banks"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    bankname = db.Column(db.String(64), index=True, unique=True)
    icon_url = db.Column(db.String(200))
    note = db.Column(db.String(200))

    def __init__(self, code, bankname, icon_url, note):
        self.code = code
        self.bankname = bankname
        self.icon_url = icon_url
        self.note = note

    def to_dict(self):
        return {
            'id': self.id,
            'code': self.code,
            'bankname': self.bankname,
            'icon_url': self.icon_url,
            'note': self.note
        }

    

class Consume(db.Model):
    __tablename__ = "consumes"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    bank_id = db.Column(db.Integer, ForeignKey('banks.id'), nullable=True)
    price = db.Column(db.Numeric, nullable=False)
    account_date = db.Column(db.DateTime, nullable=True)
    finish_date = db.Column(db.DateTime, nullable=True)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    note = db.Column(db.String(200))
    # author_id = db.Column(db.Integer, ForeignKey('users.id'))


    def to_dict(self):
        return {
        'id': self.id,
        'user_id': self.user_id,
        'bank_id': self.bank_id,
        'price': self.price,
        'account_date': self.account_date,
        'finish_date': self.finish_date,
        'month': self.month,
        'year': self.year,
        'note': self.note
    }