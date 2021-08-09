from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("formulario/", views.formularios),
    path("forms/", views.formulario),
]
