# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('number', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=100)),
                ('transport', models.CharField(max_length=7, choices=[('BUS', 'Автобус'), ('TRAM', 'Трамвай'), ('TROLLEY', 'Тролейбус')])),
            ],
        ),
        migrations.CreateModel(
            name='LineStations',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('direction', models.BooleanField(choices=[(True, 'права'), (False, 'обратна')])),
                ('line', models.ForeignKey(to='website.Line')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='linestations',
            name='station',
            field=models.ForeignKey(to='website.Station'),
        ),
        migrations.AddField(
            model_name='line',
            name='station',
            field=models.ManyToManyField(through='website.LineStations', to='website.Station'),
        ),
    ]
