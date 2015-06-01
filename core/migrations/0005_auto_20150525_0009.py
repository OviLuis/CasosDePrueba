# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_prueba_testid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='testId',
            field=models.IntegerField(max_length=4, verbose_name=b'ID'),
        ),
    ]
