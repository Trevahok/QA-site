import datetime

class LastIP(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request):
        user = request.user
        if not user.is_authenticated():
            return None
        up = user.get_or_create_profile()
        up.last_activity_ip = request.META['REMOTE_ADDR']
        up.save()
        return None
