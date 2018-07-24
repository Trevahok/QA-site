from polls.models import dept_choices_list
from registration.models import UserProfile
def faculties_var(request):
    return {'schools':dept_choices_list}
def user_var(request):
    if request.user.is_authenticated:
        instance = UserProfile.objects.get(user= request.user)
    return {'details':instance}