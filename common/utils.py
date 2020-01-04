class GetListResult(object):
    def __init__(self, data, page, error_message, status):
        self.data = data
        self.status = status
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
def get_list_data(data: list or dict or None, page=None, error_message=None, status=200):
    return GetListResult(data, page, error_message, status).__dict__