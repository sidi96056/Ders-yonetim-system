from django import forms
from .models import UserSchedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = UserSchedule
        fields = ['ders_adi', 'gun', 'baslangic_saati', 'bitis_saati', 'renk']
        widgets = {
            'ders_adi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dersin Adı'}),
            'gun': forms.Select(attrs={'class': 'form-select'}),
            'baslangic_saati': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'bitis_saati': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'renk': forms.TextInput(attrs={'class': 'form-control', 'type': 'color', 'style': 'height: 45px;'}),
        }