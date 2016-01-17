from django.shortcuts import render
from .models import Station
from random import randint
from django.http import JsonResponse


def index(request):
    #stat = Station.objects.get(id=randint(1, 1000))
    return render(request, 'website/index.html', locals())


def getStationById(request, id):
    stat = Station.objects.get(id=id)
    return JsonResponse({
        'number': stat.number,
        'name': stat.name,
        'latitude': stat.latitude,
        'longitude': stat.longitude,
    })
