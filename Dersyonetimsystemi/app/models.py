from django.db import models
from django.utils import timezone

class Odev(models.Model):
    baslik = models.CharField(max_length=200, verbose_name="Ödev Başlığı")
    icerik = models.TextField(verbose_name="Ödev Detayı")
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    son_tarih = models.DateTimeField(verbose_name="Son Teslim Tarihi")
    tamamlandi = models.BooleanField(default=False)

    def __str__(self):
        return self.baslik