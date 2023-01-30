from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.all_songs),
    path('music/<int:pk>/', views.song_details),
]