# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150525_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='veredict',
            field=models.CharField(max_length=10, choices=[(b'aprovado', b'aprovado'), (b'rechazado', b'rechazado')]),
        ),
    ]
