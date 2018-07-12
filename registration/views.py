from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
@login_required(login_url='login')
def profile(request):
    if request.method =='POST':
        profile_update_form = UserProfileForm(request.POST)
        if profile_update_form.is_valid():
        # lot more coming soon 
    else:
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'profile.html', {'profile':user_profile})

