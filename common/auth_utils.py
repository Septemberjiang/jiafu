from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from flask import jsonify
from functools import wraps
from models import User, Role, User_Role, Permission, Role_Permission
from exts import db, jwt


def platform_user_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()  # 校验是否携带了token, 如果没有携带token 则会抛出异常
        user = User.query.filter_by(uid = get_jwt_identity()).first()
        if not user:
            return jsonify({"msg": "无权限访问", 'code': 400})
        return fn(*args, **kwargs)
    return wrapper


# 和get_current_user() 方法有关(类似重写, 是这个方法能拿到登录时存入的值)
@jwt.user_loader_callback_loader
def user_loader_callback(identity):
    return User.query.get(identity)


# def role_permission_required(url_name=''):
#     def wrapper(func):
#         def f(*args, **kwargs):
#             verify_jwt_in_request()
#             user = User.query.filter_by(uid = get_jwt_identity()).first()
#             if not user:
#                 return jsonify({'msg': "无用户信息或者该管理员账号已停用", 'code': 400})
#             ret = func(*args, **kwargs)
#             # if user.uid== 1:
#             #     return ret
#             role_obj = db.session.query(User_Role).filter(User_Role.uid == user.uid,
#                                                                  Role.rid == User_Role.rid,
#                                                                  Role_Permission.rid == Role.rid,
#                                                                  Role_Permission.pid == Permission.pid,
#                                                                  ).filter(Permission.pname == url_name).all()
#             if not role_obj:
#                 return jsonify({"msg": "该用户没有角色权限访问", 'code': 401})
#
#             return ret
#
#         return f
#
#     return wrapper
