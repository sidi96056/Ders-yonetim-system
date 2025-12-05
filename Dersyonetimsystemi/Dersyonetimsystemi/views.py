from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request,"base.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return redirect(request,"register.html")
