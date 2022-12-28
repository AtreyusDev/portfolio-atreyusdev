from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('projects/', views.proyectos, name='proyectos')
]