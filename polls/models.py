from django.db import models

# Create your models here.

class Faculty(models.Model):
    class Meta:
        verbose_name_plural = 'Faculties'

    dept_choices = (
            ('sas','School of Advanced Sciences'),
            ('scse','School of Computing Science and Engineering'),
            ('select', 'School of Electrical Engineering '),
            ('sense','School of Electronics Engineering'),
            ('smbs','School of Mechanical and Building Sciences'),
            ('vitbs', 'VIT Business School'),
            ('vitsol', 'VIT School of Law'),
            ('vfit','VIT Fashion Institute of Technology')
            )

    star_choices = (
            (1, 'one'),
            (2, 'two'),
            (3,'three'),
            (4, 'four'),
            (5, 'five'),
            )
    pic = models.ImageField(upload_to='media',blank=True)
    name = models.CharField(default = '', max_length=50)
    post = models.CharField(default = '' , max_length=50)     # postiton like sr.professor or associate prof. etc.
    dept = models.CharField(default = '' , max_length=7, choices=dept_choices)
    likes = models.PositiveSmallIntegerField(default =0 )
    dislikes = models.PositiveSmallIntegerField(default=0)
    rating = models.PositiveSmallIntegerField(default = 0 , choices= star_choices)


    def __str__(self):
        return self.name
