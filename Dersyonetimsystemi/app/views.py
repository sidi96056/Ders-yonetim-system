from django.shortcuts import render, redirect, get_object_or_404
from .models import Odev
from .forms import OdevForm

def lesson_view(request):
    # Ödev Ekleme İşlemi
    if request.method == 'POST':
        form = OdevForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lesson')
    else:
        form = OdevForm()

    odevler = Odev.objects.all().order_by('son_tarih')
    return render(request, "lesson.html", {'form': form, 'odevler': odevler})

# Ödev Silme İşlemi
def odev_sil(request, odev_id):
    odev = Odev.objects.get(id=odev_id)
    odev.delete()
    return redirect('lesson')