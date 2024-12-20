from django.urls import path

from . import views

urlpatterns = [
    path("dndapp/", views.dndapp, name="index"),
]