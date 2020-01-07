from flask import Blueprint,render_template,url_for,request,session, jsonify

from blueprints.equipment.views import Exhibition, ServerResource, ServerModifyDelete, \
    ExhibitionReseource, ServerState, ExhibitionAdd, CameraServer

from flask_restful import Api

blueprint=Blueprint('equipment',__name__,url_prefix='',template_folder='',static_folder='')

api = Api(blueprint)


api.add_resource(ServerResource,'/server')  # 服务器<展示、添加>
api.add_resource(ServerModifyDelete,'/server/operate/<string:unique_server_id>')  # 服务器<删除、修改、修改渲染>
api.add_resource(ServerState,'/server/state/<string:unique_server_id>')  # 修改服务器状态接口

api.add_resource(Exhibition,'/camera/<string:unique_server_id>')  # 设备展示
api.add_resource(ExhibitionAdd,'/camera')  # 设备添加
api.add_resource(ExhibitionReseource,'/camera/operate/<string:unique_camera_id>')  # 设备<删除、修改、渲染>
api.add_resource(CameraServer,'/camera/server')  # 设备添加及编辑时,可以选择哪些服务器


