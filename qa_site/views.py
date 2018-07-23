from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from registration.models import UserProfile
from polls.models import dept_choices_list
def home(request):
    if request.user.is_authenticated:
        instance = UserProfile.objects.get(user= request.user)
        return(render(request,'home.html',{'details':instance}))
    return(render(request,'home.html'))