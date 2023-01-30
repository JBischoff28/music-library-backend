from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_songs),
    path('<int:pk>/', views.song_details),
]