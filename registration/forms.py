from django.forms import ModelForm
from .models import UserProfile,GENDER_CHOICES
from django import forms

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = [ 'last_activity_ip','user' ]
        fields='__all__'
    gender = forms.CharField(widget=forms.Select,choices=GENDER_CHOICES)

# when size of what is being tracked abt the user increases , switch exclude and fields  
