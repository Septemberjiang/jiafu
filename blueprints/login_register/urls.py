from flask import Blueprint,render_template,url_for,request,session, jsonify

from blueprints.login_register.views import Login, Register, HomeRessource, LoginOutResouce
from models import User
from exts import db
from flask_restful import Api

blueprint=Blueprint('user',__name__,url_prefix='',template_folder='',static_folder='')

api = Api(blueprint)

api.add_resource(Login, '/login')  # 登录模块
api.add_resource(Register, '/register')  # 注册模块
# api.add_resource(GetValidResource, '/valid')  # 获取验证码

# 首页
api.add_resource(HomeRessource, '/info')
api.add_resource(LoginOutResouce, '/logout')

