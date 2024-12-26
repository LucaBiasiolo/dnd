from django.urls import path

from . import views

urlpatterns = [
    path("dndapp/", views.dndapp, name="home"),
    path("dndapp/dice", views.dice, name="dice"),
    path("dndapp/dice/throw_dice", views.throw_dice, name="throw_dice"),
    path("dndapp/oracle", views.oracle, name="oracle"),
    path("dndapp/consult_oracle", views.consult_oracle, name="consult_oracle"),
]