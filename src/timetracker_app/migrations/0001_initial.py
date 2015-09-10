# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckPoint',
            fields=[
                ('id', models.IntegerField(verbose_name=b'ID', unique=True, serialize=False, editable=False, primary_key=True)),
                ('place_name', models.CharField(default=True, unique=True, max_length=60, verbose_name=b'Nombre Lugar')),
            ],
            options={
                'verbose_name': 'CheckPoint',
                'verbose_name_plural': 'CheckPoints',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id_player', models.CharField(max_length=6, serialize=False, verbose_name=b'MPR ID', primary_key=True)),
                ('full_name', models.CharField(max_length=200, verbose_name=b'Nombre Completo')),
                ('phone', models.CharField(unique=True, max_length=10, verbose_name=b'Telefono')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
            ],
            options={
                'verbose_name': 'Jugador',
                'verbose_name_plural': 'Jugadores',
            },
        ),
        migrations.CreateModel(
            name='RecordTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_name_id', models.CharField(max_length=1, verbose_name=b'Check Point ID')),
                ('check_in_time', models.TimeField(auto_now=True, verbose_name=b'CheckIn Time')),
                ('mpr_id', models.ForeignKey(to='timetracker_app.Player')),
            ],
            options={
                'verbose_name': 'Tiempo',
                'verbose_name_plural': 'Tiempos',
            },
        ),
    ]
