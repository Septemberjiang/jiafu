from flask import Blueprint,render_template,url_for,request,session, jsonify

from blueprints.message.views import AlarmMessage, AlarmMessageDelete, AlarmMessageResource, AlarmMessageOperation, \
    AlarmMessageAll

from flask_restful import Api

blueprint=Blueprint('message',__name__,url_prefix='',template_folder='',static_folder='')

api = Api(blueprint)

api.add_resource(AlarmMessage,'/alarm/<string:unique_camera_id>')  # 报警信息页
api.add_resource(AlarmMessageAll,'/alarm/exhibition')  # 报警信息页
api.add_resource(AlarmMessageOperation,'/alarm/operate/<int:alarm_id>')  # 报警信息的查看以及删除
api.add_resource(AlarmMessageDelete,'/alarm/all')  # 批量删除报警信息

api.add_resource(AlarmMessageResource,'/alarm/far')  # 添加报警信息
