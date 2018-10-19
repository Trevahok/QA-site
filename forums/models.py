from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    text = models.CharField( blank =False , max_length = 1000)
    pub_date = models.DateTimeField(auto_created=True )
    user = models.ForeignKey( User, on_delete=models.DO_NOTHING, related_name='questions')
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.CharField( blank= False, max_length=1000)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')