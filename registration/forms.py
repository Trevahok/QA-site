from django.forms import ModelForm
from .models import UserProfile

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = [ 'last_login_ip' ]
        fields= '__all__'

