# -*- coding: utf-8 -*-
import os
import sys

import config
from flask import Flask
from flask import redirect, url_for, abort, render_template, flash
from flask_sqlalchemy import SQLAlchemy

# # SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True
app.config.from_object(config)

# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret string')
path = os.getenv('DATABASE_URL', prefix + os.path.join(app.root_path, app.config['DB_NAME']))
app.config['SQLALCHEMY_DATABASE_URI'] = path
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    # path = os.getenv('DATABASE_URL', prefix + os.path.join(app.root_path, app.config['DB_NAME']))
    return "Hello %s" %path
    # return "Hello  " 

# if __name__ == '__main__':
#     # app.run(host='0.0.0.0',port=5000)
#     app.run()
