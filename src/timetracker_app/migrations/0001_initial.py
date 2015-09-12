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
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('place_name', models.CharField(max_length=60, verbose_name=b'Nombre Lugar')),
            ],
            options={
                'verbose_name': 'CheckPoint',
                'verbose_name_plural': 'CheckPoints',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('mprid', models.CharField(max_length=3, serialize=False, verbose_name=b'MPR ID', primary_key=True)),
                ('full_name', models.CharField(max_length=200, verbose_name=b'Nombre Completo')),
                ('phone', models.CharField(max_length=10, verbose_name=b'Telefono')),
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
                ('check_in_time', models.DateTimeField(auto_now=True, verbose_name=b'CheckIn Time')),
                ('duration', models.DurationField(null=True, blank=True)),
                ('check_point', models.ForeignKey(to='timetracker_app.CheckPoint')),
                ('player', models.ForeignKey(related_name='record_time', to='timetracker_app.Player')),
            ],
            options={
                'verbose_name': 'Tiempo',
                'verbose_name_plural': 'Tiempos',
            },
        ),
        migrations.AlterUniqueTogether(
            name='recordtime',
            unique_together=set([('player', 'check_point')]),
        ),
    ]
