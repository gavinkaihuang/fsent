from fsent import db
from sqlalchemy import ForeignKey

class User(db.Model):
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
    
class Bank(db.Model):
    __tablename__ = "banks"
    id = db.Column(db.Integer, primary_key=True)
    bankname = db.Column(db.String(64), index=True, unique=True)
    icon_url = db.Column(db.String(200))
    note = db.Column(db.String(200))

    def __init__(self, bankname, icon_url, note):
        self.bankname = bankname
        self.icon_url = icon_url
        self.note = note
    

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