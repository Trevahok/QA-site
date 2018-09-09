from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
def get_sentinel_user():
    return User.objects.get_or_create(username='deleted_user')[0]
class Post(models.Model):
    type_choices = ( ('i', 'informal') , ('f', 'formal'))
    user = models.ForeignKey(User, on_delete = models.SET(get_sentinel_user))
    event_name = models.CharField(max_length = 40, blank = True)
    description = models.TextField(max_length = 150)
    likes = models.PositiveSmallIntegerField(default = 0)
    pub_date = models.DateTimeField(auto_now_add = True)
    venue = models.CharField(max_length = 40 , blank =False)
    timings = models.DateTimeField( blank = False, default=timezone.now)
    duration = models.DurationField(default = timedelta(hours=1))
    type = models.CharField(choices = type_choices, max_length=1, blank=False,default = 'i')

    def __str__(self):
        return self.event_name
