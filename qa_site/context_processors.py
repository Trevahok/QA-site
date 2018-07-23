from polls.models import dept_choices_list
def faculties_var(request):
    return {'schools':dept_choices_list}