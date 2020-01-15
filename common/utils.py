from exts import db
from flask import jsonify

class GetListResult(object):
    def __init__(self, data, page, error_message, code):
        self.data = data
        self.code = code
        self.error_message = error_message
        if page:
            self.page = {
                'previous_page': page.previous_page,
                'has_previous': page.has_previous,
                'pages': page.pages,
                'total': page.total,
                'next_page': page.next_page,
                'has_next': page.has_next,
            }

def json_response(data: list or dict or None, page=None, error_message=None, code=20000):
    return GetListResult(data, page, error_message, code).__dict__






class GetAllResult(object):
    def __init__(self, obj, total, msg, code):
        self.code = code
        self.data = {
            "total": total,
            "items": obj,
            "msg": msg,
        }


def get_all_response(obj: list or dict or None, total = None, msg=None, code=20000):
    return GetAllResult(obj, total, msg, code).__dict__
