from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager


db=SQLAlchemy()#注意没有传app对象过来，此时的db无法获取数据库的配置config信息
ma = Marshmallow()
jwt = JWTManager()
