from django.urls import path

from . import views

urlpatterns = [
    path("dndapp/", views.index, name="index"),
]