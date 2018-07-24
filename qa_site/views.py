from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from registration.models import UserProfile
from polls.models import dept_choices_list
def home(request):
    if request.user.is_authenticated:
        return(render(request,'home.html'))
    return(render(request,'home.html'))