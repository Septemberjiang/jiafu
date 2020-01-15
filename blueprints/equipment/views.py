from common.auth_utils import platform_user_required
from common.utils import json_response, get_all_response
from models import Camera, Server
from exts import db
from flask import request, jsonify
from flask_restful import Resource
from blueprints.equipment.services import server_add, server_modify_delete, \
    camrea_add, ServerSchema, CameraSchema, camera_exhibition
from common.pagination import paginate



#查看所有的设备
class ExhibitionCamera(Resource):
    # decorators = [platform_user_required]

    def get(self):
        """
        查看所有的设备
        :return:
        """
        data = camera_exhibition(None)
        return data


class CameraInfo(Resource):
    def get(self, unique_camera_id):
        camera = Camera.query.filter_by(unique_camera_id=unique_camera_id).first()
        if camera:
            camera_schema = CameraSchema()
            camera_dict = camera_schema.dump(camera)
            return get_all_response(camera_dict, msg = "成功")
        else:
            return get_all_response(None, msg = "没有查到该设备的详情信息", code = 40000)

# 查看某台服务器下的所有摄像头
class Exhibition(Resource):
    def get(self, unique_server_id):
        """
        查看某台服务器下的所有摄像头
        :param unique_server_id:
        :return:
        """
        data = camera_exhibition(unique_server_id)
        return data


#摄像头的添加
class ExhibitionAdd(Resource):

    def post(self):
        """
        某台服务器下添加摄像头
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
            return get_all_response(None, msg="摄像头信息不匹配", code=40000)
        camera_schema = CameraSchema()
        camera_dict = camera_schema.dump(camera)
        return get_all_response(camera_dict, code=20000)

    def delete(self, unique_camera_id):
        camera = Camera.query.filter_by(unique_camera_id=unique_camera_id).first()
        if camera:
            try:
                db.session.delete(camera)
                db.session.commit()
                return get_all_response(None,msg="删除成功", code=20000)
            except:
                db.session.rollback()
                return get_all_response(None,msg="删除出错", code=40000)
        else:
            return get_all_response(None, msg="没有匹配到该信息", code=40000)

    def put(self, unique_camera_id):
        camera = camrea_add(unique_camera_id)
        return camera


class CameraStatus(Resource):

    def post(self):
        form = request.get_json()
        unique_camera_id = form.get('unique_camera_id')
        state = form.get('state')
        camera = Camera.query.filter_by(unique_camera_id=unique_camera_id).first()
        if camera:
            camera.equipment_state=state
            db.session.add(camera)
            db.session.commit()
            return get_all_response(None, msg="状态修改成功", code=20000)
        else:
            db.session.rollback()
            return get_all_response(None, msg="状态修改失败", code=40000)


# 查看所有的服务器以及添加服务器
class ServerResource(Resource):
    def get(self):
        """
        查看所有的服务器
        :return:
        """
        # form = request.args
        # server = form.get('server_name')
        server_obj = Server.query.order_by(Server.create_time.desc()).all()
        # if server:
        #     server_obj = server_obj.filter(Server.server_name.like("%{}%".format(server)))
        if server_obj:
            server = ServerSchema(many=True)
            server_data = server.dump(server_obj)
            return get_all_response(server_data, total=len(server_obj), msg='展示成功')
        else:
            return get_all_response(None, code=40000, msg='目前没有服务器')

    def post(self):
        """
        添加服务器
        :return:
        """
        server = server_add()
        return server


#查看单挑服务器的信息
class ServerInfoResource(Resource):
    def get(self, unique_server_id):
        server_obj = Server.query.filter_by(unique_server_id=unique_server_id).first()
        server = ServerSchema()
        server_data = server.dump(server_obj)
        return jsonify({'code': 20000,
                        "data": {
                            "items": server_data,
                            'msg': '展示成功'
                        }})


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
