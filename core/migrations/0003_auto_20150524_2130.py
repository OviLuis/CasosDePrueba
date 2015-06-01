# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150524_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='testRequirements',
            field=models.CharField(default=datetime.datetime(2015, 5, 24, 21, 30, 2, 567972, tzinfo=utc), max_length=50, verbose_name=b'Requerimientos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prueba',
            name='testAuth',
            field=models.CharField(max_length=100, verbose_name=b'Realizada por'),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='testDate',
            field=models.DateField(),
        ),
    ]
