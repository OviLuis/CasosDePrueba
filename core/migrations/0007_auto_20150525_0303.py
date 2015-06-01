# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150525_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='testAuth',
            field=models.CharField(max_length=100, verbose_name=b'Realizada por'),
        ),
    ]
