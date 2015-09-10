# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker_app', '0002_auto_20150909_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkpoint',
            name='place_name',
            field=models.CharField(unique=True, max_length=60, verbose_name=b'Nombre Lugar'),
        ),
    ]
