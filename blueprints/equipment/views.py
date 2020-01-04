from common.auth_utils import login_required
from common.utils import get_list_data
from models import User, Camera, Server, Alarm_info
from exts import db
from flask import request, jsonify, session
from flask_restful import Resource
from blueprints.equipment.services import camrea_all, server_all, alarm_info_all, server_add, server_modify_delete, \
    camrea_add, alarm_info_add
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

# 摄像头的增加、删除、编辑、编辑时的数据回响
class ExhibitionReseource(Resource):
    @use_kwargs({
        'unique_camera_id': fields.String(required=False),
    })
    def get(self, **kwargs):
        """
        摄像头信息修改渲染
        :return:
        """
        camera = Camera.query.filter_by(unique_camera_id=kwargs.get('unique_camera_id')).first()
        if not camera:
            return jsonify({'msg':'摄像头信息不匹配', 'code':400})
        camera_dict = dict()
        camera_dict['unique_camera_id'] = camera.unique_camera_id
        camera_dict['camera_name'] = camera.camera_name
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
        return jsonify({"camera":camera_dict})

    @use_kwargs({
        'unique_camera_id': fields.String(required=False),
    })
    def delete(self, **kwargs):
        camera = Camera.query.filter_by(unique_camera_id=kwargs.get('unique_camera_id')).first()
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


    @use_kwargs({
        'unique_camera_id': fields.String(required=False),
        'camera_name': fields.String(required=False),
        'camera_ip': fields.String(required=False),
        'camera_position': fields.String(required=False),
        'rtsp_address': fields.String(required=False),
        'distinguish_wide': fields.String(required=False),
        'check_space': fields.String(required=False),
        'scene_at_degree': fields.String(required=False),
        'move_check_wide': fields.String(required=False),
        'equipment_state': fields.String(required=False),
        'unique_server_id': fields.String(required=False),
        'camera_state': fields.String(required=False),
    })
    def post(self, **kwargs):
        """
        某台服务器下添加摄像头
        :param unique_server_id:
        :param kwargs:
        :return:
        """
        camrea = camrea_add(kwargs, method='add')
        return camrea

    @use_kwargs({
        'unique_camera_id': fields.String(required=False),
        'camera_name': fields.String(required=False),
        'camera_ip': fields.String(required=False),
        'camera_position': fields.String(required=False),
        'rtsp_address': fields.String(required=False),
        'distinguish_wide': fields.String(required=False),
        'check_space': fields.String(required=False),
        'scene_at_degree': fields.String(required=False),
        'move_check_wide': fields.String(required=False),
        'equipment_state': fields.String(required=False),
        'unique_server_id': fields.String(required=False),
        'camera_state': fields.String(required=False),
    })
    def put(self, **kwargs):
        camera = camrea_add(kwargs)
        return camera


# 查看所有的服务器以及添加服务器
class ServerResource(Resource):
    def get(self):
        """
        查看所有的服务器
        :return:
        """
        args = request.args
        page = args.get('page', 1)
        size = args.get('size', 10)
        server = args.get('server_name')
        server_obj = Server.query
        if server:
            server_obj = server_obj.filter(Server.server_name.like("%{}%".format(server)))
        if server_obj:
            page_result =paginate(server_obj,int(page),int(size))
            server = server_all(page_result.items)
            result_data = get_list_data(server, page_result)
            return result_data
        else:
            return get_list_data(None, error_message="目前没有服务器", status=400)

    @use_kwargs({
        'unique_server_id': fields.String(required=True),
        'server_name': fields.String(required=False),
        'server_ip': fields.String(required=False),
        'province': fields.String(required=False),
        'city': fields.String(required=False),
        'county': fields.String(required=False),
        'company': fields.String(required=False),
        'server_state': fields.String(required=False)
    })
    def post(self, **kwargs):
        """
        添加服务器
        :param kwargs:
        :return:
        """
        server = server_add(kwargs)
        return server


# 服务器删除、编辑、编辑数据回响
class ServerModifyDelete(Resource):
    @use_kwargs({
        'unique_server_id': fields.String(required=True)})
    def delete(self, **kwargs):
        """
        删除某台服务器,如果这台服务器下有摄像头,则无法删除
        :param unique_server_id:
        :return:
        """
        server  = server_modify_delete(name="out", kwargs=kwargs)
        return server

    @use_kwargs({
        'unique_server_id': fields.String(required=True)})
    def get(self, **kwargs):
        """
        编辑某台服务器时的数据回响
        :param unique_server_id:
        :return:
        """
        server = server_modify_delete(name="rendering", kwargs=kwargs)
        return server

    @use_kwargs({
        'unique_server_id': fields.String(required=True),
        'server_name': fields.String(required=False),
        'server_ip': fields.String(required=False),
        'province': fields.String(required=False),
        'city': fields.String(required=False),
        'county': fields.String(required=False),
        'company': fields.String(required=False),
        'server_state': fields.String(required=False)
    })
    def put(self, **kwargs):
        """
        编辑某台服务器
        :param unique_server_id:
        :param kwargs:
        :return:
        """
        server = server_modify_delete(name="modify", kwargs=kwargs)
        return server


# 某台摄像机下所有的报警信息,以及查看某条报警信息的内容
class AlarmMessage(Resource):

    def get(self, camrea_id):
        """
        查看某台摄像机下所有的报警信息
        :param camrea_id:
        :return:
        """
        args = request.args
        page = args.get('page', 1)
        size = args.get('size', 10)
        start_time = args.get('start_time')  # 开始时间
        end_time = args.get('end_time')  # 结束时间
        alarm_type = args.get('alarm_type')  #报警类型
        camera_obj =Alarm_info.query.filter_by(unique_camera_id = camrea_id).order_by(Alarm_info.alarm_id.desc())
        if alarm_type:
            """
            筛选报警类型
            """
            camera_obj = camera_obj.filter(Alarm_info.alarm_type==alarm_type)
        if start_time and end_time:
            """
            筛选时间
            """
            camera_obj = camera_obj.filter(end_time >= Alarm_info.alarm_time,Alarm_info.alarm_time >= start_time)
        if camera_obj:
            page_result = paginate(camera_obj, int(page), int(size))
            alarm = alarm_info_all(page_result.items)
            result_data = get_list_data(alarm, page_result)
            return result_data
        else:
            return get_list_data(None, error_message='该设备下目前没有报错信息', status=400)

    def post(self, camrea_id):
        """
        查看某条报警信息的内容
        :param camrea_id:
        :return:
        """
        alarm_obj = Alarm_info.query.filter_by(alarm_id=camrea_id).first()
        alarm_dict = dict()
        alarm_dict['alarm_content'] = alarm_obj.alarm_content
        alarm_dict['alarm_time'] = str(alarm_obj.alarm_time)
        alarm_dict['face_recognition'] = alarm_obj.face_recognition
        alarm_dict['img_base64'] = alarm_obj.img_base64

        return jsonify({'alarm':alarm_dict})

    def delete(self, camrea_id):
        """
        删除某条报警信息
        """
        alarm_obj = Alarm_info.query.filter_by(alarm_id=camrea_id).first()
        if alarm_obj:
            db.session.delete(alarm_obj)
            db.session.commit()
            return jsonify({'msg':'删除成功', 'code':200})
        else:
            return jsonify({'msg':'匹配信息有误', 'code':400})


# 批量删除报警信息
class AlarmMessageDelete(Resource):
    @use_kwargs({
        'alarm_id': fields.List(cls_or_instance=fields.Integer(), required=True)
    })
    def delete(self, **kwargs):
        """
        批量删除报警信息
        :return:
        """
        alarm_list = kwargs.get('alarm_id')
        if alarm_list == []:
            return jsonify({'msg':'并未选择要删除的报警信息', 'code':400})
        for a in alarm_list:
            alarm_obj = Alarm_info.query.filter_by(alarm_id=a).first()
            if alarm_obj:
                try:
                    db.session.delete(alarm_obj)
                    db.session.commit()
                except:
                    db.session.rollback()
                    return jsonify({'msg':f'编码为{a}的报警信息删除失败', 'code':400})
        return jsonify({'msg':'批量删除成功', 'code':200})


# 报警信息的添加
class AlarmMessageResource(Resource):
    @use_kwargs({
        'alarm_content': fields.String(required=False),
        'alarm_time': fields.DateTime(required=False),
        'alarm_type': fields.String(required=False),
        'alarm_level': fields.String(required=False),
        'alarm_address': fields.String(required=False),
        'face_recognition': fields.String(required=False),
        'img_base64': fields.String(required=False),
        'unique_camera_id': fields.String(required=False),
        'img_name': fields.String(required=False),
        'img_remark': fields.String(required=False),
        'img_url': fields.String(required=False),
        'video_url': fields.String(required=False),
        'link_obj': fields.String(required=False),
    })
    def post(self, **kwargs):
        """
        添加报警信息
        :return:
        """
        alarm = alarm_info_add(kwargs)
        return alarm
