# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker_app', '0003_auto_20150909_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='id_player',
        ),
        migrations.AddField(
            model_name='player',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='mpr_id',
            field=models.CharField(default=1, unique=True, max_length=3, verbose_name=b'MPR ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='phone',
            field=models.CharField(max_length=10, verbose_name=b'Telefono'),
        ),
    ]
