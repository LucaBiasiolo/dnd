from django.urls import path

from . import views

urlpatterns = [
    path("dndapp/", views.dndapp, name="home"),
    path("dndapp/dice", views.dice, name="dice"),
    path("dndapp/dice/lancia_dadi", views.lancia_dadi, name="lancia_dadi"),
    path("dndapp/oracle", views.oracle, name="oracle"),
    path("dndapp/consult_oracle", views.consult_oracle, name="consult_oracle"),
]