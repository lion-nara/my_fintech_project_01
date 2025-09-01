# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_view(request):
    return HttpResponse("login ok")

def logout_view(request):
    return HttpResponse("logout ok")

def signup_view(request):
    return HttpResponse("signup ok")
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard:home")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})