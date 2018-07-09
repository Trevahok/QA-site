from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    url('login/',auth_views.login,{'template_name':'login.html'},name ='login'),
    path('logout/', auth_views.logout,{'next_page':'login/'},name = 'logout'),
    url('signup/',views.signup,name = 'signup'),
    ]
