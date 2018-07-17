from django.shortcuts import render
from .models import Faculty
from django.http import HttpResponse
# Create your views here.
def test(request):
    return render(request,'faculty.html') 
