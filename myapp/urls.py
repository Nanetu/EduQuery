from django.contrib import admin
from django.urls import path, include

from myapp import views
from .view import auth

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', auth.signup, name='signup'),
    path('login', auth.login, name='login'),
    path('logout', auth.logout, name='logout'),
    #path('upload', upload, name='upload'),
    #path('concepts', concepts, name='concepts'),
    #path('quiz', quiz, name='quiz'),

]