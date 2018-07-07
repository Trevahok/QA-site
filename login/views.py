from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User
# Create your views here.
def login(request):
    if request.method=='GET':
        return render(request,'login/login.html',{'user':''})
    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(pk=username)
        except User.DoesNotExist:
            return render(request,'login/login.html',{'user':''})
        else:
            if user.password==password:
                return render(request,'alwin/home.html',{'user':username})
