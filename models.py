from sqlalchemy.exc import SQLAlchemyError

from exts import db
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import Column, Integer, \
    VARCHAR
from sqlalchemy.dialects.mysql import TINYINT


class User(db.Model):
    __tablename__ = 'tb_user'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(50), nullable=False)
    sex = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    account = db.Column(db.String(50), nullable=False, unique=True)  # 账号
    pwd = db.Column(db.String(50), nullable=False)


class User_Role(db.Model):
    __tablename__ = 'tb_user_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey('tb_user.uid'), nullable=False)
    rid = db.Column(db.Integer, db.ForeignKey('tb_role.rid'), nullable=False)


class Role(db.Model):
    __tablename__ = 'tb_role'
    rid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=True, unique=True)
    describe = db.Column(db.String(50))
    state = db.Column(db.String(50))



class Role_Permission(db.Model):
    __tablename__ = 'tb_role_permission'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer, db.ForeignKey('tb_role.rid'), nullable=False)
    pid = db.Column(db.Integer, db.ForeignKey('tb_permission.pid'), nullable=False)


class Permission(db.Model):
    __tablename__ = 'tb_permission'
    pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    pname = db.Column(db.String(50))
    url = db.Column(db.String(50))
    parent_id = db.Column(Integer)
    action = db.Column(db.String(50))
    describe = db.Column(db.String(1500))



class Server(db.Model):
    __tablename__='tb_server'
    unique_server_id=db.Column(db.String(50), primary_key=True)
    device_no = db.Column(db.String(50))
    server_name=db.Column(db.String(50))
    server_ip=db.Column(db.String(50))
    province=db.Column(db.String(50))
    city=db.Column(db.String(50))
    county=db.Column(db.String(50))
    company=db.Column(db.String(50))
    server_state=db.Column(db.String(50))
    camera_info = db.relationship('Camera', backref='tb_server', lazy='select')

class Camera(db.Model):
    __tablename__='tb_camera'
    unique_camera_id=db.Column(db.String(50), primary_key=True)
    device_no = db.Column(db.String(50))
    camera_name=db.Column(db.String(50))
    camera_ip=db.Column(db.String(50))
    camera_position=db.Column(db.String(50))
    rtsp_address=db.Column(db.String(50))
    distinguish_wide=db.Column(db.String(50), default=0.6)  # 识别阔值
    check_space = db.Column(db.String(50), default=5)  # 检测间隔
    scene_at_degree = db.Column(db.String(50), default=0.3)  # 场景相识度
    move_check_wide = db.Column(db.String(50), default=1000)  # 移动检测阔值
    equipment_state = db.Column(db.String(50), default=0)  # 设备是否启用
    unique_server_id = db.Column(db.String(50), db.ForeignKey('tb_server.unique_server_id'), nullable=False)


class Alarm_info(db.Model):
    __tablename__='tb_alarm_info'
    alarm_id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    alarm_content = db.Column(db.String(128))  # 报警内容
    alarm_time = db.Column(db.DateTime)
    alarm_type = db.Column(db.String(6))  # 报警类型
    alarm_level = db.Column(db.String(3))  # 报警级别
    alarm_address = db.Column(db.String(150))
    face_recognition = db.Column(db.String(50))  # 人脸识别姓名
    img_base64 = db.Column(db.TEXT)
    unique_camera_id = db.Column(db.String(50), db.ForeignKey('tb_camera.unique_camera_id'), nullable=False)
    img_name = db.Column(db.String(60))
    img_remark = db.Column(db.String(1500))  # 图片备注
    img_url = db.Column(db.String(600))
    video_url = db.Column(db.String(600))
    link_obj = db.Column(db.String(60))  # 事件关联项





