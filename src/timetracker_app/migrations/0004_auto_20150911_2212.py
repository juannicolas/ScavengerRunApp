# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker_app', '0003_recordtime_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordtime',
            name='player',
            field=models.ForeignKey(related_name='record_time', to='timetracker_app.Player'),
        ),
    ]
