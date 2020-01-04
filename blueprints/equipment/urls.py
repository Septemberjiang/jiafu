from flask import Blueprint,render_template,url_for,request,session, jsonify

from blueprints.equipment.views import Exhibition, ServerResource, AlarmMessage, ServerModifyDelete, \
    ExhibitionReseource, AlarmMessageDelete, AlarmMessageResource
from models import User
from exts import db
from flask_restful import Api

blueprint=Blueprint('equipment',__name__,url_prefix='',template_folder='',static_folder='')

api = Api(blueprint)

api.add_resource(Exhibition,'/exhibition/<int:unique_server_id>')  # 设备展示
api.add_resource(ExhibitionReseource,'/exhibition/operation')  # 设备<增加、删除、修改>
api.add_resource(ServerResource,'/server')  # 服务器<展示、添加>
api.add_resource(ServerModifyDelete,'/server/modify/out')  # 服务器<删除、修改、修改渲染>
api.add_resource(AlarmMessage,'/alarm/message/<int:camrea_id>')  # 报警信息页
api.add_resource(AlarmMessageDelete,'/alarm/message/all')  # 批量删除报警信息
api.add_resource(AlarmMessageResource,'/alarm/message')  # 添加报警信息

# api.add_resource(Register, '/register')  # 注册模块
