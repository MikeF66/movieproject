from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_film/', views.add_film, name='add_film'),
    path('film/<int:film_id>/', views.film_detail, name='film_detail'),
]