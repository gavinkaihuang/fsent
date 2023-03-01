# -*- coding: utf-8 -*-
import os
import sys

ENV = 'development'

SECRET_KEY = 'mysecretkey'

DB_NAME = 'sqlite_sent.db'

# SQLALCHEMY_DATABASE_URI = 'sqlite:///myapp.db'

SQLALCHEMY_TRACK_MODIFICATIONS = 'False'

USE_DB = 3  #1 USE mysql local, 2 USE mysql , 2 USE SQLITE

DEBUG = True

# HOSTNAME = ""
# PORT = 3306
# USERNAME = ""
# PASSWORD = ""
# DATABASE = ""
# DATABASE = ""

# # SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

# MySQL所在主机名
#Nas config
def initNasMysql():
   HOSTNAME = "192.168.2.214"
   PORT = 3306
   USERNAME = "root"
   PASSWORD = "commonuse"
   DATABASE = "datacheck"
   DATABASE = "fsentdb"
   return f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

#macbook config
def initLocalMysql():
    HOSTNAME = "localhost"
    PORT = 3306
    USERNAME = "root"
    PASSWORD = "123456"
    DATABASE = "datacheck"
    return f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

def initSQLite(app):
    path = os.getenv('DATABASE_URL', prefix + os.path.join(app.root_path, app.config['DB_NAME']))
    return path

def getDBConnectURL(app):   
    if USE_DB == 1:
        print('use local mysql')
        return initLocalMysql()
    elif USE_DB == 2:
        print('use nas mysql')
        return initNasMysql()
    else:
        print('use sqlite')
        return initSQLite(app)
    # return f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

#初始化数据库配置
# getDBConnectURL()
# 通过修改以下代码来操作不同的SQL比写原生SQL简单很多 --》通过ORM可以实现从底层更改使用的SQL
# SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"


         

# HOSTNAME = "192.168.2.214"
# HOSTNAME = "192.168.2.214"
#HOSTNAME = "localhost"
# MySQL监听的端口号，默认3306
# PORT = 3306
# # 连接MySQL的用户名，自己设置
# USERNAME = "root"
# # 连接MySQL的密码，自己设置
# # PASSWORD = "commonuse"
# PASSWORD = "123456"
# PASSWORD = "commonuse"
# #PASSWORD = "123456"
# # MySQL上创建的数据库名称
# # DATABASE = "fsentdb"
# DATABASE = "datacheck"
# DATABASE = "fsentdb"
#DATABASE = "datacheck"
