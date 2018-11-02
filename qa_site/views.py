from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from forums.models import Question
from blogs.models import Post
from django.db.models import Max
from registration.models import UserProfile
def home(request):
    top_questions = Question.objects.all()[:5]
    top_events = Post.objects.all()[:5]
    return render(request,'home.html' , locals())
