# -*- coding: utf-8 -*-

from django.shortcuts import *
from core.models import Prueba
from core.forms import PruebaForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic import  TemplateView, View
from easy_pdf.views import PDFTemplateView
from easy_pdf.rendering import render_to_pdf_response,render_to_pdf

#from wkhtmltopdf.views import PDFTemplateResponse





import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse

def generar_pdf(html):
    # Función para generar el archivo PDF y devolverlo mediante HttpResponse
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))

def detail_Test(request, id_test):
	    dato = get_object_or_404(Prueba, pk=id_test)
	    html = render_to_string('pdf.html', {'pagesize':'A4','dato':dato}, context_instance=RequestContext(request))
	    return generar_pdf(html)


# def create(request):
#     if request.method == 'POST':
#         formularioTest = PruebaForm(request.POST)
#         if formularioTest.is_valid():
#             form = formularioTest.save(commit=False)
#             form.save()
#             messages.add_message(request, messages.INFO, 'Test creado')
#             return render_to_response("inicio.html", RequestContext(request))
#         else:
#             return render_to_response('create.html', {'formularioTest': formularioTest}, context_instance=RequestContext(request))
#     else:
#         formularioTest = PruebaForm()
#         return render_to_response('create.html', {'formularioTest': formularioTest }, context_instance=RequestContext(request))



		

class CreateTest(CreateView):
	template_name = 'create.html'
	form_class = PruebaForm
	success_url = '/'

	def form_valid(self, form):
	    print 'prueba creada'
	    return super(CreateTest, self).form_valid(form)

	def form_invalid(self,form):
		print 'no se pudo crear la prueba'
		return super(CreateTest,self).form_invalid(form)


class ListTest(ListView):
	model = Prueba
	template_name = 'inicio.html'


class DetailTest(DetailView):
	model = Prueba
	template_name = 'detalle.html'

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		return context
	# template='detalle.html'
	# context= {'title': 'Hello World!'}
	# model = Prueba

	# def get(self, request, *args, **kwargs):
	# 	self.context['test'] = self.get_object()

	# 	response = render_to_pdf_response(request=request,
	# 									  template=self.template, 
	# 									  context = self.context ,
	# 									  filename = 'prueba.pdf', 
	# 									  encoding=u'utf-8', 
	# 									  **kwargs)

	# 	response = render_to_pdf(template=self.template, 
	# 							 context = self.context , 
	# 							 encoding=u'utf-8', **kwargs)
		

	# 	response=PDFTemplateResponse(request=request,
 #                                     template=self.template,
 #                                     filename ="prueba.pdf",
 #                                     context=self.context,
 #                                     show_content_in_browser=False,
 #                                     cmd_options={'margin-top': 50,}
 #                                     )
	# 	return response

	
	
	
		

class UpdateTest(UpdateView):
    model = Prueba
    form_class = PruebaForm
    template_name = 'update.html'
    success_url = '/'


class DeleteTest(DeleteView):
	model = Prueba
	template_name = 'delete.html'
	success_url = '/'


class Prue(PDFTemplateView):
	model = Prueba
	template_name = 'detalle.html'
	#pdf_filename = "prueba.pdf" 
	
	def get_context_data(self, **kwargs):
	 	return super(Prue, self).get_context_data(
	 		pagesize="A10",
	 		title="Hola!",
	 		**kwargs
	 		)

class About(TemplateView):
	template_name = 'About.html'
		
		
		