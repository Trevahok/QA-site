import datetime

class LastSeen(object):

    def process_request(self, request):
        user = request.user
        if not user.is_authenticated(): return None  
        up = user.get_profile()
        up.last_login_on = datetime.now()
        up.last_activity_ip = request.META['REMOTE_ADDR']
        up.save()
        return None