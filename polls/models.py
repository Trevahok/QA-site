from django.db import models
from django.contrib.auth.models import User
# Create your models here.
dept_choices = (
            ('sas','School of Advanced Sciences'),
            ('scse','School of Computing Science and Engineering'),
            # ('select', 'School of Electrical Engineering '),
            # ('sense','School of Electronics Engineering'),
            # ('smbs','School of Mechanical and Building Sciences'),
            # ('vitbs', 'VIT Business School'),
            # ('vitsol', 'VIT School of Law'),
            # ('vfit','VIT Fashion Institute of Technology')
            )
dept_choices_list=[x[0].upper for x in dept_choices]
class Faculty(models.Model):
    class Meta:
        verbose_name_plural = 'Faculties'
    star_choices = (
            (1, 'one'),
            (2, 'two'),
            (3,'three'),
            (4, 'four'),
            (5, 'five'),
            )
    campus_choices= (
            ('v', 'vellore'),
            ('c', 'chennai'),
            )
    dp = models.ImageField(upload_to='facultydps',blank=True)
    name = models.CharField(default = '', max_length=50)
    post = models.CharField(default = '' , max_length=50)     # postiton like sr.professor or associate prof. etc.
    dept = models.CharField(default = '' , max_length=7, choices=dept_choices)
    campus = models.CharField(max_length=1,blank=False, choices= campus_choices,default='c')
    def __str__(self):
        return self.name

class Like(models.Model):
    direction_choices=(
        (1, 'like'),
        (0 , 'dislike')
    )
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    faculty = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    direction = models.SmallIntegerField(choices=direction_choices)
    def __str__(self):
        return str(user.username) + ',' + str(faculty)

  