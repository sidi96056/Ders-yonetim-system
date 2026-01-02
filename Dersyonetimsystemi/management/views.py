from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DersProgrami

def live_lesson_view(request):
    return render(request,"live_lesson.html")

@login_required
def calendar_view(request):
    if request.method == "POST":
        tarih = request.POST.get('tarih')
        gun = request.POST.get('gun')
        saat = request.POST.get('saat')
        ders_adi = request.POST.get('ders_adi')
        renk = request.POST.get('renk')
        
        DersProgrami.objects.create(
            user=request.user,
            tarih=tarih,
            gun=gun,
            saat=saat,
            ders_adi=ders_adi,
            renk=renk
        )
        return redirect('calendar')

    dersler = DersProgrami.objects.filter(user=request.user).order_by('saat')
    return render(request, 'calendar.html', {'dersler': dersler})

@login_required
def ders_sil(request, id):
    ders = get_object_or_404(DersProgrami, id=id, user=request.user)
    ders.delete()
    return redirect('calendar')
