
from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('usuarios_sem_entrada/', views.usuarios_sem_entrada, name='listagem_usuarios_sem_entrada')

]
