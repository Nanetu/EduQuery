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

def signup(request):
        if request.method =="POST":
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname'] 
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            myuser = User.objects.create_user(username, email, password1)
            myuser.first_name = fname
            myuser.last_name = lname

            myuser.save()
            messages.success(request, "Your account has been successfully created")

            return redirect('login')

        return render (request, "myapp/signup.html")
def login(request):
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password1']

            user = authenticate(email=email, password=password)

            if user is not None:
                 login(request, user)
                 fname = user.first_name
                 return render(request, "myapp/index.html", {'fname':fname})
            else:
                 messages.error(request, "Bad Credentials")
                 return redirect('home')
        return render (request, "myapp/login.html")
def logout(request):
        logout(request)
        messages.success(request, "Logged out successfully")
        return redirect('home')
    

class homepage(View):
    def get(self, request):
        return
    def post(self, request):
        return
    
