# fsent
flask project

1, checkout venv
on mac
virtualenv --no-site-packages venv

on Linux:
virtualenv venv

or : python3 -m venv test_env

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

5, use gunicorn
pip3 install gunicorn
gunicorn fsent:app
gunicorn -w 4 -b 127.0.0.1:4000 fsent:app

6, use uwsgi
$: uwsgi --http 127.0.0.1:5000 --module fsent:app

#url use head path /fsent
$: uwsgi --http 127.0.0.1:8000 -s /tmp/fsent.sock --manage-script-name --mount /fsent=fsent:app

7, use ini file to restart project
uwsgi --ini uwsgi.ini
uwsgi --reload uwsgi.ini
uwsgi --stop uwsgi.ini

8, use nginx
start: nginx
stop: nginx -s stop

path: /usr/local/etc/nginx

config content like this:
......
server {
    listen 80;
    server_name localhost;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:///tmp/fsent.sock; #read info from socket, wait for uwsgi write info into this socket. set in uwsgi.ini file
    }
}
......


ext: apache is started
try to stop it: sudo apachectl stop

