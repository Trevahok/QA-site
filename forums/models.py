from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    text = models.CharField(blank=False, max_length=1000)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='questions')
    upvotes = models.PositiveSmallIntegerField(default=0)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created','modified', 'upvotes')
    def __str__(self):
        return self.text.title()  + ' by ' + self.user.username.title()


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    text = models.CharField(blank=False, max_length=1000)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    modified = models.DateTimeField(auto_now=True)
    upvotes = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('-created','modified')
    def __str__(self):
        return self.text.title() + ' by ' + self.user.username.title()
