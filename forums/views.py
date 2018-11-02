from django.shortcuts import render
from .models import Question,Answer
from .forms import QuestionForm, AnswerForm
# Create your views here.

def top_questions(request):
    questions =Question.objects.all()
    form = QuestionForm(request.POST or None)
    answer_form = AnswerForm(request.POST or None)

    if form.is_valid():
        temp = form.save(commit=False)
        temp.user = request.user
        temp.save()
    return render(request, 'question_list.html', context= {'questions': questions, 'form': form, 'answer_form': answer_form , })