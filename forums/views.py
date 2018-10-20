from django.shortcuts import render
from . import models

# Create your views here.

def top_questions(request):
    questions =models.Question.objects.all()
    return render(request, 'question_list.html', context= {'questions': questions})