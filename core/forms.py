from django.forms import ModelForm
from django import forms
from .models import Prueba


class PruebaForm(ModelForm):
	projectName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Nombre del proyecto'}))
	testName  = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Nombre de Prueba'}))
	testId = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Id prueba'}))
	testType =	forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Tipo de prueba ej: funcional, automatica etc.'}))
	testDate = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Fecha aaaa/mm/dd'}))
	testAuth = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Autor'}))
	testObjective = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Objetivo de la prueba'}))
	testRequirements = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Requerimientos'}))
	userAction = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Accion del usuario'}))
	expectedResult = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Resultado esperado'}))
	result = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'Resultado obtenido'}))
	observations = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder': 'observaciones'}))

	class Meta:
		model = Prueba
		fields = ['projectName','testName','testId','testType','testDate','testAuth','testObjective','testRequirements','userAction','expectedResult','result','observations', 'calificacion']

	def __init__(self, *args, **kwargs):        
            super(PruebaForm,self).__init__()




		
					
	
		