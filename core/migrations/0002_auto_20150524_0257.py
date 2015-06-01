# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prueba',
            name='expectedResult',
        ),
        migrations.RemoveField(
            model_name='prueba',
            name='result',
        ),
        migrations.RemoveField(
            model_name='prueba',
            name='stage',
        ),
        migrations.RemoveField(
            model_name='prueba',
            name='userAction',
        ),
    ]
