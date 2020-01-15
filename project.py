from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import config
import os
from datetime import timedelta
from exts import db, ma, jwt

from blueprints.login_register.urls import blueprint as login_blueprint
from blueprints.equipment.urls import blueprint as equipment_blueprint
from blueprints.message.urls import blueprint as message_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    from flask_cors import CORS
    CORS(app, supports_credentials=True)
    #设置SECRET_KEY
    app.config['SECRET_KEY'] = os.urandom(24)

    configure_extensions(app)
    register_blueprints(app)
    return app


def configure_extensions(app):
    db.init_app(app) #这步保证db,能够获取到数据配置config信息
    ma.init_app(app)
    jwt.init_app(app)


def register_blueprints(app):
    app.register_blueprint(login_blueprint, url_prefix='/api/user')
    app.register_blueprint(equipment_blueprint, url_prefix='/api/device')
    app.register_blueprint(message_blueprint, url_prefix='/api/message')

app = create_app()

if __name__ == '__main__':
    # 默认为5000端口
    app.run(host='0.0.0.0',debug=True)
    # app.run(port=8000)