from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse



def home(request):
    return render(request,"base.html")

#def base(request):
    return render(request,"base.html")

def calendar_view(request):
    return render(request,"calendar.html")

def live_lesson_view(request):
    return render(request,"live_lesson.html")

def lesson_view(request):
    return render(request,"lesson.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def subscribe(request):
    return render(request,"subscribe.html")

def paid(request):
    return render(request,"paid.html")

def paid1(request):
    return render(request,"paid1.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def profile(request):
    return render(request,"profile.html")

@login_required
def profile_view(request):
    if request.method == "POST":
        messages.success(request, "Ayarlarınız başarıyla güncellendi.")
        return redirect('profile')
        
    return render(request, "profile.html")


@login_required
def subscribe_view(request):
    return render(request, 'subscribe.html')


