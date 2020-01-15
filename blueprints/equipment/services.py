import uuid

from common.pagination import paginate
from common.utils import json_response, get_all_response
from exts import db, ma
from models import Server, Camera
from flask import jsonify, request
import datetime

class ServerSchema(ma.ModelSchema):

    class Meta:
        model = Server
        fields = ('unique_server_id', 'device_no', 'server_name', 'server_ip', 'province', 'city',
                  'county', 'company', 'server_state', 'create_time')


class CameraSchema(ma.ModelSchema):

    class Meta:
        model = Camera
        fields = ('unique_camera_id', 'camera_name', 'device_no', 'camera_ip', 'camera_position',
                  'rtsp_address', 'distinguish_wide', 'check_space', 'scene_at_degree', 'move_check_wide',
                  'equipment_state', 'unique_server_id', 'create_time')


def camera_exhibition(unique_server_id):
    args = request.args
    camera = args.get('camera')
    if unique_server_id:
        camrea_obj = Camera.query.filter_by(unique_server_id=unique_server_id).order_by(Camera.create_time.desc())
    else:
        camrea_obj = Camera.query.order_by(Camera.create_time.desc())
    if camera:
        """
        筛选摄像头名称
        """
        camrea_obj = camrea_obj.filter(Camera.camera_name.like("%{}%".format(camera)))
    if camrea_obj:
        camera_schema = CameraSchema(many=True)
        camera = camera_schema.dump(camrea_obj.all())
        result_data = get_all_response(camera, code = 20000, msg = "成功")
        return result_data
    else:
        return get_all_response(None, msg = "目前没有设备", code = 40000)


def camrea_add(unique_camera_id, method=None):
    """
    摄像头的添加以及修改 \
    method= add 则是再进行添加
    """
    form = request.get_json()
    camera_name = form.get('camera_name')
    device_no = form.get('device_no')
    camera_ip = form.get('camera_ip')
    camera_position = form.get('camera_position')
    rtsp_address = form.get('rtsp_address')
    distinguish_wide = form.get('distinguish_wide')
    check_space = form.get('check_space')
    scene_at_degree = form.get('scene_at_degree')
    move_check_wide = form.get('move_check_wide')
    equipment_state = form.get('equipment_state')
    unique_server_id = form.get('unique_server_id')
    server = Server.query.filter_by(unique_server_id=unique_server_id).first()
    if not server:
        return get_all_response(None, msg="不存在该服务器", code=40000)
    try:
        now = datetime.datetime.now()
        strf = now.strftime('%Y-%m-%d %H:%M:%S')
        unique_camera = None
        if unique_camera_id:
            camera_obj = Camera.query.filter_by(unique_camera_id=unique_camera_id).first()
        if method == 'add':
            uid = str(uuid.uuid1())
            unique_camera = ''.join(uid.split('-'))
            camera_obj = Camera()
            camera_obj.unique_camera_id = unique_camera
        camera_obj.camera_name = camera_name
        camera_obj.device_no = device_no
        camera_obj.camera_ip = camera_ip
        camera_obj.camera_position = camera_position
        camera_obj.rtsp_address = rtsp_address
        camera_obj.distinguish_wide = distinguish_wide
        camera_obj.check_space = check_space
        camera_obj.scene_at_degree = scene_at_degree
        camera_obj.move_check_wide = move_check_wide
        camera_obj.equipment_state = equipment_state
        camera_obj.unique_server_id = unique_server_id
        camera_obj.create_time = strf
        db.session.add(camera_obj)
        db.session.commit()
        return jsonify({'code': 20000,
                        "data": {
                            "unique_camera_id": unique_camera,
                            'msg': '成功'}})
    except Exception as e:
        db.session.rollback()
        return get_all_response(None, msg="失败", code=40000)


def server_add():
    """
    添加服务器
    :param kwargs:
    :return:
    """
    form = request.get_json()
    if not form:
        return jsonify({'code': 40000,
                        "data": {
                            'msg': '没有数据'}})
    server_name = form.get('server_name')
    device_no = form.get('device_no')
    server_ip = form.get('server_ip')
    province = form.get('province')
    city = form.get('city')
    county = form.get('county')
    company = form.get('company')
    server_state = form.get('server_state')
    uid = str(uuid.uuid1())
    unique_server_id = ''.join(uid.split('-'))
    try:
        now = datetime.datetime.now()
        strf = now.strftime('%Y-%m-%d %H:%M:%S')
        server_obj = Server()
        server_obj.unique_server_id = unique_server_id
        server_obj.server_name = server_name
        server_obj.device_no = device_no
        server_obj.server_ip = server_ip
        server_obj.province = province
        server_obj.city = city
        server_obj.county = county
        server_obj.company = company
        server_obj.server_state = server_state
        server_obj.create_time = strf
        db.session.add(server_obj)
        db.session.commit()
        return jsonify({'code': 20000,
                        "data": {
                            "unique_server_id": unique_server_id,
                            'msg': '服务器添加成功'}})
    except Exception as e:
        db.session.rollback()
        return get_all_response(None, msg="服务器添加失败", code=40000)


def server_modify_delete(unique_server_id, name=None):
    """
    删除服务器,修改服务器信息, 修改服务器信息数据回响
    """
    if not unique_server_id:
        return get_all_response(None, msg="没有传唯一标识码", code=40000)
    server = Server.query.filter_by(unique_server_id=unique_server_id).first()
    if not server:
        return get_all_response(None, msg="没有该服务器", code=40000)
    if name == 'out':
        camera = Camera.query.filter_by(unique_server_id=unique_server_id).all()
        if camera:
            return get_all_response(None, msg="该服务器下有相关摄像头,无法删除", code=40000)
        try:
            db.session.delete(server)
            db.session.commit()
            return get_all_response(None, msg="删除成功", code=20000)
        except:
            db.session.rollback()
            return get_all_response(None, msg="删除时出错", code=40000)
    if name == 'modify':
        form = request.get_json()
        server_name = form.get('server_name')
        server_ip = form.get('server_ip')
        device_no = form.get('device_no')
        province = form.get('province')
        city = form.get('city')
        county = form.get('county')
        company = form.get('company')
        server_state = form.get('server_state')
        try:
            server.server_name = server_name
            server.server_ip = server_ip
            server.province = province
            server.device_no = device_no
            server.city = city
            server.county = county
            server.company = company
            server.server_state = server_state
            db.session.add(server)
            db.session.commit()
            return get_all_response(None, msg="修改成功", code=20000)
        except:
            db.session.rollback()
            return get_all_response(None, msg="修改出错", code=40000)

    if name == 'rendering':
        server_dict = dict()
        server_dict['unique_server_id'] = server.unique_server_id
        server_dict['server_name'] = server.server_name
        server_dict['device_no'] = server.device_no
        server_dict['server_ip'] = server.server_ip
        server_dict['province'] = server.province
        server_dict['city'] = server.city
        server_dict['county'] = server.county
        server_dict['company'] = server.company
        server_dict['server_state'] = server.server_state
        # return jsonify({'server': server_dict}
        return get_all_response(server_dict, msg="成功", code=40000)
