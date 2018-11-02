from .models import Post
from django.forms import ModelForm
from django import forms

class BlogForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = [ 'user', 'likes']
        widgets = {
          'description': forms.TextInput()
        }

