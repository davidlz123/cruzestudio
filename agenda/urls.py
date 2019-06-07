from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import ListadoContactos, ModificarContacto, DetalleContacto, EliminarContacto, NuevoContacto


app_name = 'agenda'

urlpatterns = [

    url(r'^listado_contactos/$', ListadoContactos.as_view(), name="listado_contactos"),
    url(r'^detalle_contacto/(?P<pk>.+)/$', DetalleContacto.as_view(), name="detalle_contacto"),
    url(r'^modificar_contacto/(?P<pk>.+)/$', ModificarContacto.as_view(), name="modificar_contacto"),
    url(r'^nuevo_contacto/', NuevoContacto.as_view(), name="nuevo_contacto"),
    url(r'^contacto/(?P<pk>[0-9]+)/delete/$', EliminarContacto.as_view(), name="contacto_eliminar"),
]