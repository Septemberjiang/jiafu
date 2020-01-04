import base64
from uuid import uuid4

from common.auth_utils import login_required
from common.get_valid import ValidCodeImg
from models import User
from exts import db
from flask import request, jsonify, session
import hashlib
from flask_apispec import use_kwargs
from marshmallow import fields

from flask_restful import Resource
from config import redis_0


class Login(Resource):
    @use_kwargs({
        'username': fields.String(required=True),
        'password': fields.String(required=True),
        # 'valid_code': fields.String(required=True),
        # 'uuid': fields.String(required=True),
    })
    def post(self, **kwargs):
        uname=kwargs.get('username')
        pwd=kwargs.get('password')
        # valid_code=kwargs.get('valid_code')
        # uuid=kwargs.get('uuid')
        # code = redis_0.get(f'{uuid}_code')
        # if not code:
        #     return jsonify({'msg':'验证码过期','code':400})
        # if valid_code.upper() != code.upper():
        #     return jsonify({'msg':'验证码错误','code':400})
        is_user = db.session.query(User).filter_by(uname=uname).first()
        if not is_user:
            return jsonify({'msg':"用户不存在",'cod e':400})
        obj = hashlib.md5(b'str')  # 实例化md5的时候传个参数，这叫加盐
        obj.update(pwd.encode(encoding="utf-8"))
        password = obj.hexdigest()
        user=db.session.query(User).filter(User.uname==uname,User.pwd==password).first()
        if user:
            session['user_id'] = user.uid
            session.permanent = True
            return jsonify({'msg': '登录成功', 'code': 200})
        else:
            return jsonify({'msg':'账号密码错误', 'code':200})

    def get(self):
        session.clear()
        return jsonify({'msg':"退出登录", 'code':200})


class Register(Resource):
    @use_kwargs({
        'username': fields.String(required=True),
        'password': fields.String(required=True),
        'is_password': fields.String(required=True),
        'sex': fields.String(required=True),
        'age': fields.Integer(required=True),
        'account': fields.String(required=True)})
    # @login_require
    def post(self,**kwargs):
        uname = kwargs.get('username')
        pwd = kwargs.get('password')
        is_pwd = kwargs.get('is_password')
        sex = kwargs.get('sex')
        age = kwargs.get('age')
        account = kwargs.get('account')
        user_obj = User.query.filter_by(uname=uname).first()
        if user_obj:
            return jsonify({'msg':'用户名已存在','code':400})
        if pwd != is_pwd:
            return jsonify({'msg':'两次密码输入不一致','code':400})
        try:
            obj = hashlib.md5(b'str')  # 实例化md5的时候可以给传个参数，这叫加盐
            obj.update(pwd.encode(encoding="utf-8"))
            password = obj.hexdigest()
            user = User()
            user.uname=uname
            user.pwd=password
            user.account=account
            user.age=age
            user.sex=sex
            db.session.add(user)
            db.session.commit()
            return jsonify({'msg':'注册成功','code':200})
        except:
            db.session.rollback()
            return jsonify({'msg':'注册失败','code':400})


class GetValidResource(Resource):

    def get(self):
        """
        获取验证码
        :return:
        """
        img = ValidCodeImg()
        img_data, valid_code = img.getValidCodeImg()
        base64_data = base64.b64encode(img_data)
        data = base64_data.decode()
        uuid = uuid4()
        print('valid_code:', valid_code)
        redis_0.set(f'{uuid}_code', valid_code, ex=180)
        return jsonify({'data': data, 'uuid': uuid})
