from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import config
import os
from datetime import timedelta

from blueprints.login_register.urls import blueprint as login_blueprint
from blueprints.equipment.urls import blueprint as equipment_blueprint

app = Flask(__name__)
from flask_cors import CORS
CORS(app, supports_credentials=True)
#设置SECRET_KEY
app.config['SECRET_KEY'] = os.urandom(24)
# 5.设置session的有效期方式2【指session可以往后活多长时间】
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)


app.config.from_object(config)

from exts import db
db.init_app(app) #这步保证db,能够获取到数据配置config信息

app.register_blueprint(login_blueprint)
app.register_blueprint(equipment_blueprint)


if __name__ == '__main__':
    # 默认为5000端口
    app.run(host='0.0.0.0',debug=True)
    # app.run(port=8000)