from flask import request, jsonify

from common.pagination import paginate
from common.utils import json_response
from exts import db, ma

from models import Camera, Alarm_info

class AlarmSchema(ma.ModelSchema):

    class Meta():
        model = Alarm_info


def alarm_all(alarm_type, camera_obj, start_time, end_time, page, size):
    if alarm_type:
        """
        筛选报警类型
        """
        camera_obj = camera_obj.filter(Alarm_info.alarm_type == alarm_type)
    if start_time and end_time:
        """
        筛选时间
        """
        camera_obj = camera_obj.filter(end_time >= Alarm_info.alarm_time, Alarm_info.alarm_time >= start_time)
    if camera_obj:
        page_result = paginate(camera_obj, int(page), int(size))
        alarm_shcema = AlarmSchema(many=True)
        alarm = alarm_shcema.dump(page_result.items)
        result_data = json_response(alarm, page_result)
        return result_data


def alarm_info_add():
    form = request.get_json()
    alarm_content = form.get('alarm_content')
    alarm_time = form.get('alarm_time')
    face_recognition = form.get('face_recognition')
    img_base64 = form.get('img_base64')
    unique_camera_id = form.get('unique_camera_id')
    camera = Camera.query.filter_by(unique_camera_id=unique_camera_id).first()
    if not camera:
       return jsonify({'msg':f"并未找到相关{unique_camera_id}的摄像头设备", 'code':400})
    try:
        alarm = Alarm_info()
        alarm.alarm_content=alarm_content
        alarm.alarm_time=alarm_time
        alarm.face_recognition=face_recognition
        alarm.img_base64=img_base64
        alarm.unique_camera_id=unique_camera_id
        db.session.add(alarm)
        db.session.commit()
        return jsonify({'msg':'报警信息添加成功', 'code':200})
    except:
        db.session.rollback()
        return jsonify({'msg':'报警信息添加失败', 'code':400})