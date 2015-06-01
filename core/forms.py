from django.forms import ModelForm
from django import forms
from .models import Prueba


class PruebaForm(ModelForm):
	class Meta:
		model = Prueba
		fields = ['projectName','testName','testId','testType','testDate','testAuth','testObjective','testRequirements','observations','veredict']

	def __init__(self, *args, **kwargs):        
            super(PruebaForm,self).__init__()


		
					
	
		