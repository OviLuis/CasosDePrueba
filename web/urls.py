from django.conf.urls import patterns, url

from .views import *


urlpatterns = (
    # ... 
    url(r'^$', ListTest.as_view(), name='inicio'),
    url(r'^detail/(?P<pk>[\w-]+)$', DetailTest.as_view(), name='detalle'),
    #url(r'^detail/(?P<id_test>\d+)$', 'web.views.detail_Test', name='pdf'),
    url(r'^create/$', CreateTest.as_view(), name='crearPrueba'),
    url(r'^update/(?P<pk>[\w-]+)$', UpdateTest.as_view(), name='actualizar'),
    url(r'^delete/(?P<pk>[\w-]+)$', DeleteTest.as_view(), name='borrar'),
    
    url(r'^prueba/$', Prue.as_view(), name='prueba'),
    url(r'^pdf/(?P<id_test>\d+)$', 'web.views.detail_Test', name='pdf'),
    )