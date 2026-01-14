from django.urls import path
from . import views

urlpatterns = [
    path('lesson/', views.lesson_view, name='lesson'),
    path('odev-sil/<int:odev_id>/', views.odev_sil, name='odev_sil'),
]