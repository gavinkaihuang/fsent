# -*- coding: utf-8 -*-
import os
import sys

import config
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(config)

DB_CONNECT = config.getDBConnectURL(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECT
db = SQLAlchemy(app)

# from fsent.users.views import users_blueprint
# from fsent.banks.views import banks_blueprint
# from fsent.consumers.views import consumers_blueprint
# # register our blueprints
# app.register_blueprint(users_blueprint)
# app.register_blueprint(banks_blueprint)
# app.register_blueprint(consumers_blueprint)


from fsent.ai.views import ai_blueprint
app.register_blueprint(ai_blueprint)

# Custom response for 401 Unauthorized errors
@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'code':'401', 'msg': 'Unauthorized access'}), 401
