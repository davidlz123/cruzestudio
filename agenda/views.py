from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import ContactoForm
from .models import Contacto



class ListadoContactos(ListView):
    model = Contacto
    template_name = 'listado_contactos.html'
    context_object_name ='contactos'

class DetalleContacto(DetailView):
    model = Contacto
    template_name = 'detalle_contacto.html'

class ModificarContacto(UpdateView):
    model = Contacto
    template_name = 'modificar_contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('agenda:listado_contactos')

class NuevoContacto(CreateView):
    model = Contacto
    template_name = 'nuevo_contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('agenda:listado_contactos')

class EliminarContacto(DeleteView):
    model = Contacto
    template_name = 'contacto_eliminar.html'
    success_url = reverse_lazy('agenda:listado_contactos')



