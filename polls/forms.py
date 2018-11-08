from django.forms import ModelForm
from .models import Faculty
from django import forms

class FacultyProfileForm(ModelForm):
    class Meta:
        model = Faculty
        exclude = '__all__'
