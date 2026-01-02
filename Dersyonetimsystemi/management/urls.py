from django.urls import path
from . import views

urlpatterns = [
    path('calender/', views.calendar_view, name='calendar'),
    path('calender/sil/<int:id>/', views.ders_sil, name='ders_sil'),
    path('live_lesson/', views.live_lesson_view, name='live_lesson'),
]