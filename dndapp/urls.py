from django.urls import path

from . import views

urlpatterns = [
    path("dndapp/", views.dndapp, name="home"),
    path("dndapp/dice", views.dice, name="dice"),
    path("dndapp/oracolo", views.oracolo, name="oracle"),
    path('oracolo_base/', views.oracolo_base, name='oracolo_base'),
    path('oracolo_migliorato/', views.oracolo_migliorato, name='oracolo_migliorato'),
    path('oracolo_alternativo/', views.oracolo_alternativo, name='oracolo_alternativo'),
]