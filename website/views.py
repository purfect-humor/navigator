from django.shortcuts import render
from .models import Station


def index(request):
    stat = Station.objects.get(id=1)
    return render(request, 'website/index.html', locals())
