from django.urls import path

from . import views

urlpatterns = [
    path("dndapp/", views.dndapp, name="home"),
    path("dndapp/dice", views.dice, name="dice"),
    path("dndapp/oracle", views.oracle, name="oracle")
]