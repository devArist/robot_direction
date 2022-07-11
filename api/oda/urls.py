from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='devant'),
    path('devant/', views.devant, name='devant'),
    path('arriere/', views.arriere, name='arriere'),
    path('gauche/', views.gauche, name='gauche'),
    path('droite/', views.droite, name='droite'),
    path('stop/', views.stop, name='stop'),
]