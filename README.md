# fsent
flask project

1, checkout venv
on mac
virtualenv --no-site-packages venv

on Linux:
virtualenv venv

source venv/bin/active


2, install requirements
pip3 install -r requirements.txt


3, change database
use mysql:
vi config.py

use sqlite:

4, create tables
cd project_root_folder
python3 db_creater.py

