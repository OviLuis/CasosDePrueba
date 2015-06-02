# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150602_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='expectedResult',
            field=models.CharField(max_length=100, verbose_name=b'Resultado esperado'),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='result',
            field=models.CharField(max_length=100, verbose_name=b'Resultado Obtenido'),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='userAction',
            field=models.CharField(max_length=100, verbose_name=b'Accion del usuario'),
        ),
    ]
