# -*- coding: utf-8 -*-
import os
import sys

import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# # SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config.from_object(config)

# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret string')
path = os.getenv('DATABASE_URL', prefix + os.path.join(app.root_path, app.config['DB_NAME']))
app.config['SQLALCHEMY_DATABASE_URI'] = path
db = SQLAlchemy(app)


from fsent.users.views import users_blueprint
from fsent.banks.views import banks_blueprint
# register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(banks_blueprint)


@app.route('/')
def index():
    # path = os.getenv('DATABASE_URL', prefix + os.path.join(app.root_path, app.config['DB_NAME']))
    return "Hello %s" %path
    # return "Hello  " 




# from models import User

# @login_manager.user_loader
# def load_user(username):
#     # Load user object from your database or other storage system
#     return User.query.get(username)
