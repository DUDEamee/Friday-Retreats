from django.shortcuts import render
from .models import Data

# Create your views here.


def Home(request):
    Place = Data.objects.all()
    context = {"place": Place}
    return render(request, "base/home.html",context)


def About(request):
    
    return render(request, "base/about.html",)


def Place(request):
    Place = Data.objects.all()
    context = {"place": Place}
    return render(request, "base/place.html", context)
