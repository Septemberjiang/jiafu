
from flask import request
from flask_restful import Resource

from blueprints.message.services import alarm_info_add, AlarmSchema, alarm_all
from models import Alarm_info
from common.auth_utils import login_required
from common.utils import json_response
from models import User, Camera, Server, Alarm_info
from exts import db
from flask import request, jsonify, session
from flask_restful import Resource
from common.pagination import paginate
from flask_apispec import use_kwargs
from marshmallow import fields

#查看所有的报警信息
class AlarmMessageAll(Resource):

    def get(self):
        args = request.args
        page = args.get('page', 1)
        size = args.get('size', 10)
        start_time = args.get('start_time')  # 开始时间
        end_time = args.get('end_time')  # 结束时间
        alarm_type = args.get('alarm_type')  # 报警类型
        camera_obj = Alarm_info.query.order_by(Alarm_info.alarm_id.desc())
        if camera_obj:
            data = alarm_all(alarm_type, camera_obj, start_time, end_time, page, size)
            return data
        else:
            return json_response(None, error_message='目前任何摄像头没有报错信息', status=400)


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
        if camera_obj:
            data = alarm_all(alarm_type, camera_obj, start_time, end_time, page, size)
            return data
        else:
            return json_response(None, error_message='该设备下目前没有报错信息', status=400)


class AlarmMessageOperation(Resource):
    def post(self, alarm_id):
        """
        查看某条报警信息的内容
        :param camrea_id:
        :return:
        """
        alarm_obj = Alarm_info.query.filter_by(alarm_id=alarm_id).first()
        alarm_shcema = AlarmSchema(many=True)
        alarm = alarm_shcema.dump(alarm_obj.items)

        return jsonify({'alarm':alarm})

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
