
from flask import request
from flask_restful import Resource

from blueprints.message.services import alarm_info_all, alarm_info_add
from models import Alarm_info
from common.auth_utils import login_required
from common.utils import get_list_data
from models import User, Camera, Server, Alarm_info
from exts import db
from flask import request, jsonify, session
from flask_restful import Resource
from common.pagination import paginate
from flask_apispec import use_kwargs
from marshmallow import fields



# 某台摄像机下所有的报警信息,以及查看某条报警信息的内容

class AlarmMessage(Resource):

    def get(self, unique_camera_id):
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
        camera_obj =Alarm_info.query.filter_by(unique_camera_id = unique_camera_id).order_by(Alarm_info.alarm_id.desc())
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


class AlarmMessageOperation(Resource):
    def post(self, alarm_id):
        """
        查看某条报警信息的内容
        :param camrea_id:
        :return:
        """
        alarm_obj = Alarm_info.query.filter_by(alarm_id=alarm_id).first()
        alarm_dict = dict()
        alarm_dict['alarm_content'] = alarm_obj.alarm_content
        alarm_dict['alarm_time'] = str(alarm_obj.alarm_time)
        alarm_dict['face_recognition'] = alarm_obj.face_recognition
        alarm_dict['img_base64'] = alarm_obj.img_base64

        return jsonify({'alarm':alarm_dict})

    def delete(self, alarm_id):
        """
        删除某条报警信息
        """
        alarm_obj = Alarm_info.query.filter_by(alarm_id=alarm_id).first()
        if alarm_obj:
            db.session.delete(alarm_obj)
            db.session.commit()
            return jsonify({'msg':'删除成功', 'code':200})
        else:
            return jsonify({'msg':'匹配信息有误', 'code':400})


# 批量删除报警信息
class AlarmMessageDelete(Resource):

    def delete(self):
        """
        批量删除报警信息
        :return:
        """
        form = request.get_json()
        alarm_list = form.get('alarm_id')
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

    def post(self):
        """
        添加报警信息
        :return:
        """
        alarm = alarm_info_add()
        return alarm
