from common.auth_utils import login_required
from common.utils import get_list_data
from models import User, Camera, Server, Alarm_info
from exts import db
from flask import request, jsonify, session
from flask_restful import Resource
from blueprints.equipment.services import camrea_all, server_all,  server_add, server_modify_delete, \
    camrea_add
from common.pagination import paginate
from flask_apispec import use_kwargs
from marshmallow import fields

# 查看某台服务器下的所有摄像头
class Exhibition(Resource):
    def get(self, unique_server_id):
        """
        查看某台服务器下的所有摄像头
        :param server_id:
        :return:
        """
        args = request.args
        page = args.get('page', 1)
        size = args.get('size',10)
        camera = args.get('camera')
        camrea_obj = Camera.query.filter_by(unique_server_id=unique_server_id)
        if camera:
            """
            筛选摄像头名称
            """
            camrea_obj = camrea_obj.filter(Camera.camera_name.like("%{}%".format(camera)))
        if camrea_obj:
            page_result = paginate(camrea_obj, int(page), int(size))
            camrea_list =camrea_all(page_result.items)
            result_data = get_list_data(camrea_list, page_result)
            return result_data
        else:
            return get_list_data(None, error_message="该服务器下目前没有设备", status=400)


#摄像头的添加
class ExhibitionAdd(Resource):

    def post(self):
        """
        某台服务器下添加摄像头
        :param unique_server_id:
        :param kwargs:
        :return:
        """
        camrea = camrea_add(None, method='add')
        return camrea




# 摄像头的删除、编辑、编辑渲染
class ExhibitionReseource(Resource):

    def get(self, unique_camera_id):
        """
        摄像头信息修改渲染
        :return:
        """
        camera = Camera.query.filter_by(unique_camera_id=unique_camera_id).first()
        if not camera:
            return jsonify({'msg': '摄像头信息不匹配', 'code': 400})
        camera_dict = dict()
        camera_dict['unique_camera_id'] = camera.unique_camera_id
        camera_dict['camera_name'] = camera.camera_name
        camera_dict['device_no'] = camera.device_no
        camera_dict['camera_ip'] = camera.camera_ip
        camera_dict['camera_position'] = camera.camera_position
        camera_dict['rtsp_address'] = camera.rtsp_address
        camera_dict['distinguish_wide'] = camera.distinguish_wide
        camera_dict['check_space'] = camera.check_space
        camera_dict['scene_at_degree'] = camera.scene_at_degree
        camera_dict['move_check_wide'] = camera.move_check_wide
        camera_dict['equipment_state'] = camera.equipment_state
        camera_dict['unique_server_id'] = camera.unique_server_id
        camera_dict['camera_state'] = camera.camera_state
        return jsonify({"camera": camera_dict})

    def delete(self, unique_camera_id):
        camera = Camera.query.filter_by(unique_camera_id=unique_camera_id).first()
        if camera:
            try:
                db.session.delete(camera)
                db.session.commit()
                return jsonify({'msg':"删除成功",'code':200})
            except:
                db.session.rollback()
                return jsonify({'msg':'删除出错', 'code':400})
        else:
            return jsonify({'msg':"没有匹配到该信息", 'code':400})

    def put(self, unique_camera_id):
        camera = camrea_add(unique_camera_id)
        return camera


# 查看所有的服务器以及添加服务器
class ServerResource(Resource):
    def get(self):
        """
        查看所有的服务器
        :return:
        """
        # form = request.get_json()
        # page = form.get('page', 1)
        # size = form.get('size', 10)
        # server = form.get('server_name')
        server_obj = Server.query
        # if server:
        #     server_obj = server_obj.filter(Server.server_name.like("%{}%".format(server)))
        if server_obj:
            # page_result =paginate(server_obj,int(page),int(size))
            # server = server_all(page_result.items)
            server = server_all(server_obj)
            # result_data = get_list_data(server, page_result)
            result_data = get_list_data(server, status=200)
            return result_data
        else:
            return get_list_data(None, error_message="目前没有服务器", status=400)

    def post(self):
        """
        添加服务器
        :param kwargs:
        :return:
        """
        server = server_add()
        return server


# 服务器删除、编辑、编辑数据回响
class ServerModifyDelete(Resource):
    def delete(self, unique_server_id):
        """
        删除某台服务器,如果这台服务器下有摄像头,则无法删除
        :param unique_server_id:
        :return:
        """
        server  = server_modify_delete(unique_server_id, name="out")
        return server


    def get(self, unique_server_id):
        """
        编辑某台服务器时的数据回响
        :param unique_server_id:
        :return:
        """
        server = server_modify_delete(unique_server_id, name="rendering")
        return server


    def put(self, unique_server_id):
        """
        编辑某台服务器
        :param unique_server_id:
        :param kwargs:
        :return:
        """
        server = server_modify_delete(unique_server_id, name="modify")
        # server = server_modify_delete(name="modify")
        return server


#服务器状态的修改-后后
class ServerState(Resource):

    def post(self, unique_server_id):
        form = request.get_json()
        state = form.get('state')
        server = Server.query.filter_by(unique_server_id=unique_server_id).first()
        if server:
            try:
                server.server_state = state
                db.session.add(server)
                db.session.commit()
                return jsonify({'msg':'修改状态成功', 'code':200})
            except:
                db.session.rollback()
                return jsonify({'msg':'修改状态失败', 'code':400})
        else:
            return jsonify({'msg':'并无该服务器', 'code':400})


#设备添加时都可以选择哪些服务器
class CameraServer(Resource):

    def get(self):
        server = Server.query.all()
        server_list = []
        for s in server:
            server_dict = dict()
            server_dict['unique_server_id'] = s.unique_server_id
            server_dict['device_no'] = s.device_no
            server_list.append(server_dict)
        return jsonify({'server':server_list})






