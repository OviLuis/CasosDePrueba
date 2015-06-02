# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150601_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prueba',
            old_name='veredict',
            new_name='calificacion',
        ),
    ]
