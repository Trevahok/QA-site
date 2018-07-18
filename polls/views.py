from django.shortcuts import render
from .models import Faculty
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from .models import Faculty
# Create your views here.
def test(request,department):
    instance =get_list_or_404(Faculty, dept = department)
    instance.sort(key=lambda i: i.post)
    return render(request,'faculty.html',{'f' : instance}) 
