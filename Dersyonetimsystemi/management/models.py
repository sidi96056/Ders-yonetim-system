from django.db import models
from django.contrib.auth.models import User

class DersProgrami(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tarih = models.DateField(null=True, blank=True)
    gun = models.CharField(max_length=20)
    saat = models.TimeField()
    ders_adi = models.CharField(max_length=100)
    renk = models.CharField(max_length=7, default="#3b82f6")

    def __str__(self):
        return f"{self.ders_adi} - {self.gun}"