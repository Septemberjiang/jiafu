from exts import db
from models import Server, Camera, Alarm_info
from flask import jsonify


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

def camrea_add(kwargs, method=None):
    """
    摄像头的添加以及修改 \
    method= add 则是再进行添加
    :param kwargs:
    :param method:
    :return:
    """
    unique_camera_id = kwargs.get('unique_camera_id')
    camera_name = kwargs.get('camera_name')
    camera_ip = kwargs.get('camera_ip')
    camera_position = kwargs.get('camera_position')
    rtsp_address = kwargs.get('rtsp_address')
    distinguish_wide = kwargs.get('distinguish_wide')
    check_space = kwargs.get('check_space')
    scene_at_degree = kwargs.get('scene_at_degree')
    move_check_wide = kwargs.get('move_check_wide')
    equipment_state = kwargs.get('equipment_state')
    unique_server_id = kwargs.get('unique_server_id')
    camera_state = kwargs.get('camera_state')
    if method == 'add':
        camrea = Camera.query.filter_by(unique_camera_id=unique_camera_id, unique_server_id=unique_server_id).first()
        if camrea:
            return jsonify({'msg':f'标识码为{unique_server_id}的服务器下已存在{unique_camera_id}摄像头','code':400})
    server = Server.query.filter_by(unique_server_id=unique_server_id).first()
    if not server:
        return jsonify({'msg':f'不存在标识码为{unique_server_id}的服务器', 'code':400})
    try:
        camera_obj = Camera.query.filter_by(unique_camera_id=unique_camera_id).first()
        if method == 'add':
            camera_obj = Camera()
            camera_obj.unique_camera_id = unique_camera_id
        camera_obj.camera_name = camera_name
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
        return jsonify({"msg": f"标识码为{unique_camera_id}的摄像头设备{content}成功", 'code': 200})
    except Exception as e:
        db.session.rollback()
        content = '添加' if method == 'add' else '修改'
        return jsonify({"msg":f"标识码为{unique_camera_id}的摄像头设备未{content}成功", 'code':400})

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
        server_dict['server_ip'] = s.server_ip
        server_dict['province'] = s.province
        server_dict['city'] = s.city
        server_dict['county'] = s.county
        server_dict['company'] = s.company
        server_dict['server_state'] = s.server_state
        server_list.append(server_dict)
    return server_list

def server_add(kwargs):
    """
    添加服务器
    :param kwargs:
    :return:
    """
    unique_server_id = kwargs.get('unique_server_id')
    server_name = kwargs.get('server_name')
    server_ip = kwargs.get('server_ip')
    province = kwargs.get('province')
    city = kwargs.get('city')
    county = kwargs.get('county')
    company = kwargs.get('company')
    server_state = kwargs.get('server_state')
    server = Server.query.filter_by(unique_server_id=unique_server_id).first()
    if server:
        return jsonify({'msg':'服务器标识码重复,请重新输入','code':400})
    try:
        server_obj = Server()
        server_obj.unique_server_id=unique_server_id
        server_obj.server_name=server_name
        server_obj.server_ip=server_ip
        server_obj.province=province
        server_obj.city=city
        server_obj.county=county
        server_obj.company=company
        server_obj.server_state=server_state
        db.session.add(server_obj)
        db.session.commit()
        return jsonify({'msg':'服务器添加成功','code':200})
    except:
        db.session.rollback()
        return jsonify({'msg':'服务器添加失败','code':400})

def server_modify_delete(name=None, kwargs=None):
    """
    删除服务器,修改服务器信息, 修改服务器信息数据回响
    :param unique_server_id:
    :param name:
    :param kwargs:
    :return:
    """
    unique_server_id = kwargs.get('unique_server_id')
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
        server_name = kwargs.get('server_name')
        server_ip = kwargs.get('server_ip')
        province = kwargs.get('province')
        city = kwargs.get('city')
        county = kwargs.get('county')
        company = kwargs.get('company')
        server_state = kwargs.get('server_state')
        try:
            server.unique_server_id=unique_server_id
            server.server_name=server_name
            server.server_ip=server_ip
            server.province=province
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
        server_dict['server_ip']=server.server_ip
        server_dict['province']=server.province
        server_dict['city']=server.city
        server_dict['county']=server.county
        server_dict['company']=server.company
        server_dict['server_state']=server.server_state
        return jsonify({'server':server_dict})

def alarm_info_all(alarm_obj):
    """
    某个设备里面的报警信息
    :return:
    """
    alarm_list = list()
    for a in alarm_obj:
        alarm_dict = dict()
        alarm_dict['alarm_id'] = a.alarm_id
        alarm_dict['alarm_content'] = a.alarm_content
        alarm_dict['alarm_time'] = str(a.alarm_time)
        alarm_list.append(alarm_dict)
    return alarm_list

def alarm_info_add(kwargs):
    alarm_content = kwargs.get('alarm_content')
    alarm_time = kwargs.get('alarm_time')
    alarm_type = kwargs.get('alarm_type')
    alarm_level = kwargs.get('alarm_level')
    alarm_address = kwargs.get('alarm_address')
    face_recognition = kwargs.get('face_recognition')
    img_base64 = kwargs.get('img_base64')
    unique_camera_id = kwargs.get('unique_camera_id')
    img_name = kwargs.get('img_name')
    img_remark = kwargs.get('img_remark')
    img_url = kwargs.get('img_url')
    video_url = kwargs.get('video_url')
    link_obj = kwargs.get('link_obj')
    camera = Camera.query.filter_by(unique_camera_id=unique_camera_id).first()
    if not camera:
       return jsonify({'msg':f"并未找到相关{unique_camera_id}的摄像头设备", 'code':400})
    try:
        alarm = Alarm_info()
        alarm.alarm_content=alarm_content
        alarm.alarm_time=alarm_time
        alarm.alarm_type=alarm_type
        alarm.alarm_level=alarm_level
        alarm.alarm_address=alarm_address
        alarm.face_recognition=face_recognition
        alarm.img_base64=img_base64
        alarm.unique_camera_id=unique_camera_id
        alarm.img_name=img_name
        alarm.img_remark=img_remark
        alarm.img_url=img_url
        alarm.video_url=video_url
        alarm.link_obj=link_obj
        db.session.add(alarm)
        db.session.commit()
        return jsonify({'msg':'报警信息添加成功', 'code':200})
    except:
        db.session.rollback()
        return jsonify({'msg':'报警信息添加失败', 'code':400})
