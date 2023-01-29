from django.urls import path
from . import views

urlpatterns = [
    path('api/music/', views.all_songs),
    path('api/music/<int:pk>/')
]