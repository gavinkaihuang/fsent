# -*- coding: utf-8 -*-
import os
import sys

import config
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


# # # SQLite URI compatible
# WIN = sys.platform.startswith('win')
# if WIN:
#     prefix = 'sqlite:///'
# else:
#     prefix = 'sqlite:////'

app = Flask(__name__)
app.config.from_object(config)

# 1, use sqlite database
# path = os.getenv('DATABASE_URL', prefix + os.path.join(app.root_path, app.config['DB_NAME']))
# app.config['SQLALCHEMY_DATABASE_URI'] = path

# 2, use mysql database
# 通过修改以下代码来操作不同的SQL比写原生SQL简单很多 --》通过ORM可以实现从底层更改使用的SQL
DB_CONNECT = config.getDBConnectURL(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECT

db = SQLAlchemy(app)


from fsent.users.views import users_blueprint
from fsent.banks.views import banks_blueprint
from fsent.consumers.views import consumers_blueprint
# register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(banks_blueprint)
app.register_blueprint(consumers_blueprint)



# Custom response for 401 Unauthorized errors
@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'code':'401', 'msg': 'Unauthorized access'}), 401


# @app.route('/')
# def index():
#     # path = os.getenv('DATABASE_URL', prefix + os.path.join(app.root_path, app.config['DB_NAME']))
#     return "Hello %s" %path
#     # return "Hello  " 




# from models import User

# @login_manager.user_loader
# def load_user(username):
#     # Load user object from your database or other storage system
#     return User.query.get(username)
