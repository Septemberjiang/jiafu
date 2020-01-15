import datetime

import redis

HOSETNAME = '47.93.246.49'
PORT = '3306'
DATABASE = 'jiafu'
USERNAME = 'root'
PASSWORD = '950429'

DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?'.format(username=USERNAME, password=PASSWORD,
                                                                            host=HOSETNAME, port=PORT, db=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
# SQLALCHEMY_TRACK_MODIFICATTONS=False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

redis_0= redis.StrictRedis(host="127.0.0.1", port=6379, db=2)


ACCESS_EXPIRES = datetime.timedelta(days=7)
REFRESH_EXPIRES = datetime.timedelta(days=30)

JWT_SECRET_KEY = 'flask-jwt-secret'
JWT_ACCESS_TOKEN_EXPIRES = False
JWT_REFRESH_TOKEN_EXPIRES = False

JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
