from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
        path('<department>/', views.test, name='dept'),
        path('<department>/<pk>/',views.fac_profile,name='fac'),
        path('<department>/<pk>/likes/<direction>/', views.faculty_like, name ='upvote_fac')
        ]
