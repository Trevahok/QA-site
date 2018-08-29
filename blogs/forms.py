from .models import Post
from django.forms import ModelForm

class BlogForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = [ 'user', 'likes']
