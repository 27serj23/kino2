from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.films_list, name='films_list'),
    path('add_film/', views.add_film, name='add_film'),
]