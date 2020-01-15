import base64
from uuid import uuid4

from flask_jwt_extended import create_access_token, get_current_user

from common.auth_utils import platform_user_required
from common.get_valid import ValidCodeImg
from common.utils import json_response
from models import User, Permission, User_Role, Role, Role_Permission
from exts import db
from flask import request, jsonify
import hashlib

from flask_restful import Resource
# from config import redis_0


class Login(Resource):

    def post(self):
        form = request.get_json()
        account=form.get('username')
        pwd=form.get('password')
        # valid_code=kwargs.get('valid_code')
        # uuid=kwargs.get('uuid')
        # code = redis_0.get(f'{uuid}_code')
        # if not code:
        #     return jsonify({'msg':'验证码过期','code':400})
        # if valid_code.upper() != code.upper():
        #     return jsonify({'msg':'验证码错误','code':400})
        is_user = db.session.query(User).filter_by(account = account).first()
        if not is_user:
            return jsonify({'code': 40000,
                            "data": {
                                'msg': '用户不存在'}})
        obj = hashlib.md5(b'str')  # 实例化md5的时候传个参数，这叫加盐
        obj.update(pwd.encode(encoding="utf-8"))
        password = obj.hexdigest()
        user=db.session.query(User).filter(User.account == account, User.pwd == password).first()
        if user:
            access_token = create_access_token(identity = user.uid)
            return jsonify({'code': 20000,
                            "data":{
                                "token": access_token,
                                'msg': '登录成功'}})
        else:
            return jsonify({'code': 40000,
                            "data": {
                                'msg': '账号密码错误'}})


class Register(Resource):
    def post(self):
        form = request.get_json()
        uname = form.get('username')
        pwd = form.get('password')
        is_pwd = form.get('is_password')
        sex = form.get('sex')
        age = form.get('age')
        account = form.get('account')
        user_obj = User.query.filter_by(uname=uname).first()
        if user_obj:
            return jsonify({'msg':'用户名已存在','code':40000})
        if pwd != is_pwd:
            return jsonify({'msg':'两次密码输入不一致','code':40000})
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
            return jsonify({'msg':'注册成功','code':20000})
        except Exception as e:
            db.session.rollback()
            return jsonify({'msg':'注册失败','code':40000})


# class GetValidResource(Resource):
#
#     def get(self):
#         """
#         获取验证码
#         :return:
#         """
#         img = ValidCodeImg()
#         img_data, valid_code = img.getValidCodeImg()
#         base64_data = base64.b64encode(img_data)
#         data = base64_data.decode()
#         uuid = uuid4()
#         print('valid_code:', valid_code)
#         redis_0.set(f'{uuid}_code', valid_code, ex=180)
#         return jsonify({'data': data, 'uuid': uuid})


class HomeRessource(Resource):
    @platform_user_required
    def get(self):
        return jsonify({'code':20000,
                        'data':{
                            "roles":["admin"],
                            "introduction": "I am a super administrator",
                            "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
                            "name": "Super Admin"
                        }})

class LoginOutResouce(Resource):

    def get(self):
        return jsonify({'code': 20000,
                        "data": {'msg': '退出成功'}})