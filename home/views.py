from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser


# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        print("hello i am here")

        # check for correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            print("authenticate success")
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            print("authenticate failed")
            return render(request, 'login.html')


    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("login")

