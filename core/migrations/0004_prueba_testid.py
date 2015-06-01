# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150524_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='testId',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
