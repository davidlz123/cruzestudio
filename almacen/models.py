import os
from django.db import models
from django_extensions.db.models import TimeStampedModel
from gastos.models import GrupoGasto, Proveedor
from datetime import datetime
import django.utils.timezone
from django import forms

GENERAL = 1
REDUCIDO = 2
SUPER = 3

IVA = (
    (GENERAL, 'Iva General (21%)'),
    (REDUCIDO, 'Iva Reducido (10%)'),
    (SUPER, 'Iva Superreducido (4%)'),
)


class Almacen(TimeStampedModel):
    descripcion = models.CharField(max_length=255, verbose_name="Descripción")
    cod_prov = models.CharField(max_length=255, blank=True, null=True, verbose_name="Código proveedor")
    cod_sust = models.CharField(max_length=255, blank=True, null=True, verbose_name="Código sustitución")
    proveedor = models.ForeignKey(Proveedor, blank=True, null=True, db_index=True, on_delete=models.CASCADE)
    notas = models.TextField(blank=True, null=True)
    stock = models.CharField(max_length=255, blank=True, null=True, verbose_name="Stock")
    precio = models.CharField(max_length=8, blank=True, null=True)
    iva = models.IntegerField(default=GENERAL, choices=IVA, db_index=True, null=True, blank=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Almacen"
        verbose_name_plural = "Almacen"
        ordering = ['-created']
