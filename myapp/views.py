from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User 
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def home(request):
    return render (request, "myapp/index.html")

    
