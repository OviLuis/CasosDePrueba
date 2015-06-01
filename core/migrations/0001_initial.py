# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('projectName', models.CharField(max_length=100, verbose_name=b'Proyecto:')),
                ('testName', models.CharField(max_length=100, verbose_name=b'Caso de prueba')),
                ('testType', models.CharField(max_length=50, verbose_name=b'Tipo de Prueba')),
                ('testDate', models.DateTimeField()),
                ('testAuth', models.CharField(max_length=50, verbose_name=b'Realizada por')),
                ('testObjective', models.TextField(verbose_name=b'Objetivo de la prueba')),
                ('stage', models.CharField(max_length=5, verbose_name=b'Paso No')),
                ('userAction', models.TextField(verbose_name=b'Accion del usuario')),
                ('expectedResult', models.TextField(verbose_name=b'Resultado esperado')),
                ('result', models.TextField(verbose_name=b'Resultado Obtenido')),
                ('observations', models.TextField(verbose_name=b'Observaciones')),
                ('veredict', models.CharField(max_length=10, choices=[(b'1', b'aprovado'), (b'2', b'rechazado')])),
            ],
        ),
    ]
