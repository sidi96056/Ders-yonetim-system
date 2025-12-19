from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse



def home(request):
    return render(request,"base.html")


def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def subscribe(request):
    return render(request,"subscribe.html")

def paid(request):
    return render(request,"paid.html")
