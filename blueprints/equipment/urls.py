from flask import Blueprint,render_template,url_for,request,session, jsonify

from blueprints.equipment.views import Exhibition, ServerResource, ServerModifyDelete, \
    ExhibitionReseource, ServerState, ExhibitionAdd, CameraServer, ExhibitionCamera, CameraStatus, ServerInfoResource, \
    CameraInfo

from flask_restful import Api

blueprint=Blueprint('device',__name__,url_prefix='',template_folder='',static_folder='')

api = Api(blueprint)


api.add_resource(ServerResource,'/server')  # 服务器<展示、添加>
api.add_resource(ServerInfoResource,'/server/<string:unique_server_id>/info')  # 查看单个服务器的详细信息
api.add_resource(ServerModifyDelete,'/server/<string:unique_server_id>')  # 服务器<删除、修改、修改渲染>
api.add_resource(ServerState,'/server/state/<string:unique_server_id>')  # 修改服务器状态接口

api.add_resource(Exhibition,'/camera/server/<string:unique_server_id>')  # 展示某个服务器下所有的设备
api.add_resource(ExhibitionCamera,'/camera/exhibition')  # 所有设备展示
api.add_resource(CameraInfo,'/camera/<string:unique_camera_id>/info')  # 指定设备的详细资料
api.add_resource(ExhibitionAdd,'/camera')  # 设备添加
api.add_resource(ExhibitionReseource,'/camera/<string:unique_camera_id>')  # 设备<删除、修改、渲染>
api.add_resource(CameraStatus,'/camera/state')


api.add_resource(CameraServer,'/camera/server')  # 设备添加及编辑时,可以选择哪些服务器