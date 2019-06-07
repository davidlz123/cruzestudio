import os
from django.db import models
from django_extensions.db.models import TimeStampedModel
from clientes.models import Cliente,Poblacion,Provincias
from datetime import datetime
import django.utils.timezone
from django import forms


NIF= 1
NIE= 2
CIF= 3

TIPODOCUMENTO= (
    (NIF,'Nif'),
    (NIE,'Nie'),
    (CIF,'Cif')
)


CLIENTE = 1
RECURSOHUMANO = 2
PROVEEDOR = 3
OTROS = 4

TIPOCONTACTO = (
    (CLIENTE,'Cliente'),
    (RECURSOHUMANO,'Recurso Humano'),
    (PROVEEDOR,'Proveedor'),
    (OTROS,'Otros'),
)

class Contacto(TimeStampedModel):

    tipo_contacto = models.IntegerField(choices= TIPOCONTACTO, db_index=True, null=True, blank=True)
    cargo = models.CharField(max_length=255, null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    apellidos = models.CharField(max_length=255,null=True, blank=True)
    razon_social = models.CharField(max_length=255,null=True, blank=True)
    tipo_documento = models.IntegerField(default=NIF, choices=TIPODOCUMENTO, db_index=True, null=True, blank=True)
    num_documento = models.CharField(max_length=9, null=True, blank=True)
    fecha_alta = models.DateField(default= django.utils.timezone.now, null=True, blank=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    dir_calle = models.CharField(max_length=255, verbose_name='Calle', null=True, blank=True)
    dir_numero = models.CharField(max_length=255, verbose_name='Numero', null=True, blank=True)
    dir_piso_puerta = models.CharField(max_length=255, verbose_name='Piso/Puerta', null=True, blank=True)
    poblacion = models.ForeignKey(Poblacion, db_index=True, on_delete=models.CASCADE, null=True, blank=True)
    provincias = models.ForeignKey(Provincias, db_index=True, on_delete=models.CASCADE, null=True, blank=True)
    cod_postal = models.CharField(max_length=5,null=True, blank=True)
    web_blog = models.CharField(max_length=255, null=True, blank=True)


    def tipo_contacto_display(self):
        return '%s' % (self.get_tipo_contacto_display())

    def tipo_documento_display(self):
        return '%s' % (self.get_tipo_documento_display())

    def __str__(self):
        return "{} - {}".format(self.nombre, self.apellidos)


    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['-created']