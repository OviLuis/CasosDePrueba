# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150602_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='expectedResult',
            field=models.CharField(default=b'hola', max_length=100, verbose_name=b'Resultado esperado'),
        ),
        migrations.AddField(
            model_name='prueba',
            name='result',
            field=models.CharField(default=b'hola', max_length=100, verbose_name=b'Resultado Obtenido'),
        ),
        migrations.AddField(
            model_name='prueba',
            name='userAction',
            field=models.CharField(default=b'hola', max_length=100, verbose_name=b'Accion del usuario'),
        ),
    ]
