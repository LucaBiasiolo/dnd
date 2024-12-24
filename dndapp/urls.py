from django.urls import path

from . import views

urlpatterns = [
    path("dndapp/", views.dndapp, name="home"),
    path("dndapp/dice", views.dice, name="dice"),
    path("dndapp/dice/lancia_dadi", views.lancia_dadi, name="lancia_dadi"),
    path("dndapp/oracle", views.oracle, name="oracle"),
    path("dndapp/oracle/oracolo_base/", views.oracolo_base, name='oracolo_base'),
    path("dndapp/oracle/oracolo_migliorato/", views.oracolo_migliorato, name='oracolo_migliorato'),
    path("dndapp/oracle/oracolo_alternativo/", views.oracolo_alternativo, name='oracolo_alternativo'),
]