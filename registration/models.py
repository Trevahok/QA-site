from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    ''' A model for user profile page that stores all the specifics. '''
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be a valid number. ")

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email_id = models.EmailField()
    ph_no = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    reg_date = models.DateField(blank = False)
    last_login = models.DateTimeField()
    last_activity_ip = models.GenericIPAddressField()

    def __str__(self):
        return self.user.username
