# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recordtime',
            old_name='place_name',
            new_name='check_point',
        ),
        migrations.RenameField(
            model_name='recordtime',
            old_name='mprid',
            new_name='player',
        ),
        migrations.AlterField(
            model_name='checkpoint',
            name='id',
            field=models.IntegerField(unique=True, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='checkpoint',
            name='place_name',
            field=models.CharField(max_length=60, verbose_name=b'Nombre Lugar'),
        ),
        migrations.AlterField(
            model_name='recordtime',
            name='check_in_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'CheckIn Time'),
        ),
        migrations.AlterUniqueTogether(
            name='recordtime',
            unique_together=set([('player', 'check_point')]),
        ),
    ]
