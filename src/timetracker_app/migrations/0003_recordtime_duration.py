# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker_app', '0002_auto_20150911_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordtime',
            name='duration',
            field=models.DurationField(null=True, blank=True),
        ),
    ]
