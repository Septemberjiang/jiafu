from flask import request, jsonify
from exts import db

from models import Camera, Alarm_info


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

def alarm_info_add():
    form = request.get_json()
    alarm_content = form.get('alarm_content')
    alarm_time = form.get('alarm_time')
    alarm_type = form.get('alarm_type')
    alarm_level = form.get('alarm_level')
    alarm_address = form.get('alarm_address')
    face_recognition = form.get('face_recognition')
    img_base64 = form.get('img_base64')
    unique_camera_id = form.get('unique_camera_id')
    img_name = form.get('img_name')
    img_remark = form.get('img_remark')
    img_url = form.get('img_url')
    video_url = form.get('video_url')
    link_obj = form.get('link_obj')
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