from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from registration.models import UserProfile
def home(request):
    instance = get_object_or_404(UserProfile,user= request.user)
    return(render(request,'home.html',{'details':instance}))
