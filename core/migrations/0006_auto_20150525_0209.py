# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150525_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='testAuth',
            field=models.ForeignKey(verbose_name=b'Realizada por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='testId',
            field=models.IntegerField(verbose_name=b'Id prueba'),
        ),
    ]
