import uuid

from exts import db
from models import Server, Camera
from flask import jsonify, request


def camrea_all(camrea_obj):
    """
    某个服务器下的所有设备信息
    :param camrea_obj:
    :return:
    """
    camrea = list()
    for i in camrea_obj:
        camrea_dict = dict()
        camrea_dict['unique_camera_id'] = i.unique_camera_id
        camrea_dict['camera_name'] = i.camera_name
        camrea_dict['device_no'] = i.device_no
        camrea_dict['camera_ip'] = i.camera_ip
        camrea_dict['camera_position'] = i.camera_position
        camrea_dict['rtsp_address'] = i.rtsp_address
        camrea_dict['distinguish_wide'] = i.distinguish_wide
        camrea_dict['check_space'] = i.check_space
        camrea_dict['scene_at_degree'] = i.scene_at_degree
        camrea_dict['move_check_wide'] = i.move_check_wide
        camrea_dict['equipment_state'] = i.equipment_state
        camrea_dict['camera_state'] = i.camera_state
        camrea.append(camrea_dict)
    return camrea

def camrea_add(unique_camera_id, method=None):
    """
    摄像头的添加以及修改 \
    method= add 则是再进行添加
    :param kwargs:
    :param method:
    :return:
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
    camera_state = form.get('camera_state')
    server = Server.query.filter_by(unique_server_id=unique_server_id).first()
    if not server:
        return jsonify({'msg':f'不存在标识码为{unique_server_id}的服务器', 'code':400})
    try:
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
        camera_obj.camera_state = camera_state
        db.session.add(camera_obj)
        db.session.commit()
        content = '添加' if method=='add' else '修改'
        return jsonify({"msg": f"摄像头设备{content}成功", "unique_camera_id":unique_camera_id,'code': 200})
    except Exception as e:
        db.session.rollback()
        content = '添加' if method == 'add' else '修改'
        return jsonify({"msg":f"摄像头设备未{content}成功", 'code':400})

def server_all(server_obj):
    """
    展示所有的服务器信息
    :param server_obj:
    :return:
    """
    server_list = list()
    for s in server_obj:
        server_dict = dict()
        server_dict['unique_server_id'] = s.unique_server_id
        server_dict['server_name'] = s.server_name
        server_dict['device_no'] = s.device_no
        server_dict['server_ip'] = s.server_ip
        server_dict['province'] = s.province
        server_dict['city'] = s.city
        server_dict['county'] = s.county
        server_dict['company'] = s.company
        server_dict['device_no'] = s.device_no
        server_dict['server_state'] = s.server_state
        server_list.append(server_dict)
    return server_list

def server_add():
    """
    添加服务器
    :param kwargs:
    :return:
    """
    form = request.get_json()
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
        server_obj = Server()
        server_obj.unique_server_id=unique_server_id
        server_obj.server_name=server_name
        server_obj.device_no=device_no
        server_obj.server_ip=server_ip
        server_obj.province=province
        server_obj.city=city
        server_obj.county=county
        server_obj.company=company
        server_obj.server_state=server_state
        db.session.add(server_obj)
        db.session.commit()
        return jsonify({'msg':'服务器添加成功', 'unique_server_id':unique_server_id,'code':200})
    except:
        db.session.rollback()
        return jsonify({'msg':'服务器添加失败', 'code':400})

def server_modify_delete(unique_server_id, name=None):
    """
    删除服务器,修改服务器信息, 修改服务器信息数据回响
    :param unique_server_id:
    :param name:
    :param kwargs:
    :return:
    """

    # unique_server_id = form.get('unique_server_id')
    if not unique_server_id:
        return jsonify({'msg':'没有传唯一标识码', 'code':400})
    server = Server.query.filter_by(unique_server_id=unique_server_id).first()
    if not server:
        return jsonify({'msg': f'没有标识码为{unique_server_id}的服务器', 'code': 400})
    if name == 'out':
        camera = Camera.query.filter_by(unique_server_id=unique_server_id).all()
        if camera:
            return jsonify({'msg':f'标识码为{unique_server_id}的服务器下有相关摄像头,无法删除','code':400})
        try:
            db.session.delete(server)
            db.session.commit()
            return jsonify({'msg':f'标识码为{unique_server_id}的服务器删除成功','code':200})
        except:
            db.session.rollback()
            return jsonify({'msg':f'标识码为{unique_server_id}的服务器删除出错','code':400})
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
            server.server_name=server_name
            server.server_ip=server_ip
            server.province=province
            server.device_no=device_no
            server.city=city
            server.county=county
            server.company=company
            server.server_state=server_state
            db.session.add(server)
            db.session.commit()
            return jsonify({'msg':f"标识码为{unique_server_id}的服务器修改成功",'code':200})
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({'msg':f'标识码为{unique_server_id}的服务器修改出错','code':400})
    if name == 'rendering':
        server_dict = dict()
        server_dict['unique_server_id']=server.unique_server_id
        server_dict['server_name']=server.server_name
        server_dict['device_no']=server.device_no
        server_dict['server_ip']=server.server_ip
        server_dict['province']=server.province
        server_dict['city']=server.city
        server_dict['county']=server.county
        server_dict['company']=server.company
        server_dict['server_state']=server.server_state
        return jsonify({'server':server_dict})


