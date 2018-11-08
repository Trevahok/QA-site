from django.shortcuts import render
from .models import Faculty
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404,get_object_or_404
from .models import Faculty, Like
from .forms import FacultyProfileForm
# Create your views here.
def test(request,department='scse'):
    instance =get_list_or_404(Faculty, dept = department)
    instance.sort(key=lambda i: i.post)
    return render(request,'faculty.html',{'f' : instance,'len':len(instance)}) 
def fac_profile(request,department,pk):
    instance = get_object_or_404(Faculty,dept=department,id= pk)
    profile_update_form = FacultyProfileForm(request.POST or None,request.FILES or None,instance=instance)
    if profile_update_form.is_valid():
        profile_update_form.save()
    likes = 0
    for like in Like.objects.filter(faculty=Faculty.objects.get(id=pk)):
        likes += like.direction
    return render(request, 'faculty_profile.html', {'rating':profile_update_form,'profile':instance,'likes':likes})

def faculty_like(request, department, pk, direction):
    print(direction, pk , request.user)
    try:
        new_like= Like.objects.get(user=request.user, faculty_id=pk)
        new_like.direction = direction
        new_like.save()
    except Like.DoesNotExist:
        new_like, created = Like.objects.create(user=request.user , faculty_id=pk , direction= int(direction))
        new_like.save()
    likes = 0
    for like in Like.objects.filter(faculty=Faculty.objects.get(id=pk)):
        likes += like.direction
    return JsonResponse({'message': 'successfully liked/disliked!', 'likes':likes})

