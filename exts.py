from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()#注意没有传app对象过来，此时的db无法获取数据库的配置config信息

