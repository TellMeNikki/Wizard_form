from django.shortcuts import render, HttpResponse
from .models import Wizard


def index(request):
    context = {"saludo": "Hola"}
    return render(request, "index.html", context)


def formularios(request):
    wizards = Wizard.objects.all()
    context = {"wizards": wizards, "saludo": "probando wizards"}
    return render(request, "home.html", context)


def formulario(request):
    name_form = request.POST["nombre"]
    house_form = request.POST["casa"]
    pet_form = request.POST["mascota"]
    year_form = request.POST["año"]

    Wizard.objects.create(
        name=name_form, house=house_form, pet=pet_form, year=year_form
    )
    wizards = Wizard.objects.all()
    context = {"wizards": wizards, "saludo": "probando wizards"}
    return render(request, "home.html", context)
