"""cruzestudio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.views.static import serve
from . import views

urlpatterns = [

    url('gastos/', include('gastos.urls', namespace='gastos')),
    url('clientes/', include('clientes.urls', namespace='clientes')),
    url('almacen/', include('almacen.urls', namespace='almacen')),
    url('profesionales/', include('profesionales.urls', namespace='profesionales')),
    url('agenda/', include('agenda.urls', namespace='agenda')),
    url('articulos/', include('articulos.urls', namespace='articulos')),
    url('pedidos/', include('pedidos.urls', namespace='pedidos')),
    url('albaranes/', include('albaranes.urls', namespace='albaranes')),
    path('admin/', admin.site.urls),
    url(r'^login/', auth_views.LoginView.as_view(), {'template_name': 'templates/login.html'},name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'template_name': 'templates/logged_out.html'},name='logout'),
    url(r'^', views.index),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)