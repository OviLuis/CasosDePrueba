from django.db import models
from django.contrib.auth.models import User

class Prueba(models.Model):
	projectName = models.CharField(max_length = 100, verbose_name = 'Proyecto:' )
	testName  = models.CharField(max_length = 100, verbose_name = 'Caso de prueba')
	testId = models.IntegerField(verbose_name = 'Id prueba')
	testType =	models.CharField(max_length = 50, verbose_name = 'Tipo de Prueba')
	testDate = models.DateField(auto_now = False)
	testAuth = models.CharField(max_length = 100, verbose_name = 'Realizada por')
	testObjective = models.TextField(verbose_name = 'Objetivo de la prueba' )
	testRequirements = models.CharField(max_length = 50, verbose_name = 'Requerimientos')
	"""stage = models.CharField(max_length = 5, verbose_name = 'Paso No') 
	userAction = models.TextField(verbose_name = 'Accion del usuario')
	expectedResult = models.TextField(verbose_name = 'Resultado esperado')
	result = models.TextField(verbose_name = 'Resultado Obtenido')"""
	observations = models.TextField(verbose_name = 'Observaciones')
	CHOICES = (('aprovado','aprovado'), ('rechazado', 'rechazado'))
	veredict =  models.CharField(max_length = 10, choices = CHOICES)
	

	def __unicode__(self):
		return '%s %s' % (self.id, self.testName)


	
		
