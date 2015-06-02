# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150601_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='observations',
            field=models.CharField(max_length=100, verbose_name=b'Observaciones'),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='testObjective',
            field=models.CharField(max_length=100, verbose_name=b'Objetivo de la prueba'),
        ),
    ]
