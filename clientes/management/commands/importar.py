import csv
from decimal import Decimal as D
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from clientes.models import Provincias, Poblacion


class Command(BaseCommand):
    args = '<import_file_name>'

    def add_arguments(self, parser):
        parser.add_argument(
            '--fileprovincia',
            dest='fileprovincia',
            default=None,
            help='Resource class as dotted path,'
                 'ie: mymodule.resources.MyResource')

        parser.add_argument(
            '--filepoblacion',
            dest='filepoblacion',
            default=None,
            help='Resource class as dotted path,'
                 'ie: mymodule.resources.MyResource')


    def handle(self, *args, **options):
         if options["fileprovincia"]:
             filename = options["fileprovincia"]
             header = False
             linea = 0

             with open(filename) as csvfile:
                 reader = csv.DictReader(csvfile)
                 for row in reader:
                     print(row)
                     kwargs = {
                         "cod_provincia": row["Codigo de la provincia"],
                         "nombre": row["Nombre de la provincia"],
                         "pais": "España",

                     }

                     try:
                         idev = Provincias.objects.create(**kwargs)
                     except IntegrityError as e:
                         if "llave duplicada" in str(e):
                             pass
                         else:
                             print(e)

                     except Exception as e:
                         print(e)
                         print(kwargs)
                         raise e



         elif options["filepoblacion"]:

             filename = options["filepoblacion"]
             header = False
             linea = 0

             with open(filename) as csvfile:
                 reader = csv.DictReader(csvfile)
                 for row in reader:
                     codpoblacion=row["cod poblacion"]
                     codprovincia=row["cod provincia"]
                     kwargs = {
                         "cod_poblacion": row["cod poblacion"],
                         "cod_provincia": row["cod provincia"],
                         "nombre": row["poblacion"],
                         "provincias": obtenerPoblacion(row["cod provincia"]),

                     }

                     try:
                         idpob = Poblacion.objects.get(cod_poblacion=codpoblacion,cod_provincia=codprovincia)
                         print("poblacion exite:")
                         print(idpob)
                     except ObjectDoesNotExist:
                         try:

                             idev = Poblacion.objects.create(**kwargs)
                             print("poblacion creada:")
                             print( idev)
                         except IntegrityError as e:
                             if "llave duplicada" in str(e):
                                 pass
                             else:
                                 print(e)

                         except Exception as e:
                             print(e)
                             print(kwargs)
                             raise e



def obtenerPoblacion(codprovincia):
    try:
        valor=Provincias.objects.get(cod_provincia=codprovincia )
    except ObjectDoesNotExist:
        valor = None

    return valor




