from flask_script import Manager
from app import app
from exts import db

from flask_migrate import Migrate,MigrateCommand

#需要把映射到数据库中的模型导入到manage.py中
from models import User
from models import Uer_Role
from models import Role
from models import Role_Limit
from models import Limit
from models import Server
from models import Camera
from models import Alarm_info

manager=Manager(app)

#用来绑定app到flask-migrate的
Migrate(app,db)
#添加Migrate的所有子命令到db下
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()