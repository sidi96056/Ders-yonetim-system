from django import forms
from .models import Odev

class OdevForm(forms.ModelForm):
    class Meta:
        model = Odev
        fields = ['baslik', 'icerik', 'son_tarih']
        widgets = {
            'son_tarih': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'baslik': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ödev adı...'}),
            'icerik': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }