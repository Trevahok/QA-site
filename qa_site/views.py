from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from registration.models import UserProfile
def home(request):
    if request.user.is_authenticated:
        instance = UserProfile.objects.get(user= request.user)
        return(render(request,'home.html',{'details':instance}))
    return(render(request,'home.html',{}))
