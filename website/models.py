from django.db import models


class Station(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Line(models.Model):
    TRANSPORT_TYPES = (
        ('BUS', 'Автобус'),
        ('TRAM', 'Трамвай'),
        ('TROLLEY', 'Тролейбус')
    )

    number = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    transport = models.CharField(max_length=7, choices=TRANSPORT_TYPES)
    station = models.ManyToManyField(Station, through='LineStations')


class LineStations(models.Model):
    DIRECTIONS = (
        (True, 'права'),
        (False, 'обратна')
    )

    line = models.ForeignKey(Line)
    station = models.ForeignKey(Station)
    direction = models.BooleanField(choices=DIRECTIONS)
