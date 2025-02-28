from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login

def signup(request):
        if request.method =="POST":
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname'] 
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            user = User.objects.get(email=email)
            if user is not None:
                  messages.error(request, "Email already exists")
                  return redirect(login)
            elif password1 != password2:
                  messages.error(request, "Passwords do not match")
                  return render(request, "myapp/signup.html")

            myuser = User.objects.create_user(username, email, password1)
            myuser.first_name = fname
            myuser.last_name = lname

            myuser.save()
            messages.success(request, "Your account has been successfully created")

            return redirect('login')

        return render (request, "myapp/signup.html")
def login(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password1']

            user = User.objects.get(username=username)

            user = authenticate(username=username, password=password)

            if user is not None:
                 auth_login(request, user)
                 fname = user.first_name
                 return render(request, "myapp/dashboard.html", {'fname':fname})
            else:
                 messages.error(request, "Bad Credentials")
                 return redirect('home')
        return render (request, "myapp/login.html")

        
def logout(request):
        logout(request)
        messages.success(request, "Logged out successfully")
        return redirect('home')
