from django.shortcuts import render
from .models import Station
from random import randint


def index(request):
    stat = Station.objects.get(id=randint(1, 1000))
    return render(request, 'website/index.html', locals())
