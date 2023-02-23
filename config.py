# -*- coding: utf-8 -*-

ENV = 'development'

DEBUG = True

SECRET_KEY = 'mysecretkey'

DB_NAME = 'sqlite_sent.db'

# SQLALCHEMY_DATABASE_URI = 'sqlite:///myapp.db'

SQLALCHEMY_TRACK_MODIFICATIONS = 'False'


# MySQL所在主机名
# HOSTNAME = "192.168.2.214"
HOSTNAME = "localhost"
# MySQL监听的端口号，默认3306
PORT = 3306
# 连接MySQL的用户名，自己设置
USERNAME = "root"
# 连接MySQL的密码，自己设置
# PASSWORD = "commonuse"
PASSWORD = "123456"
# MySQL上创建的数据库名称
# DATABASE = "fsentdb"
DATABASE = "datacheck"
# 通过修改以下代码来操作不同的SQL比写原生SQL简单很多 --》通过ORM可以实现从底层更改使用的SQL
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"