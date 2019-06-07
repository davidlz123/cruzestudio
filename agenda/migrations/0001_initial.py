# Generated by Django 2.1.3 on 2019-06-07 12:33

from django.db import migrations, models
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('tipo_contacto', models.IntegerField(blank=True, choices=[(1, 'Cliente'), (2, 'Recurso Humano'), (3, 'Proveedor'), (4, 'Otros')], db_index=True, null=True)),
                ('cargo', models.CharField(blank=True, max_length=255, null=True)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=255, null=True)),
                ('razon_social', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_documento', models.IntegerField(blank=True, choices=[(1, 'Nif'), (2, 'Nie'), (3, 'Cif')], db_index=True, default=1, null=True)),
                ('num_documento', models.CharField(blank=True, max_length=9, null=True)),
                ('fecha_alta', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('telefono', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('dir_calle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Calle')),
                ('dir_numero', models.CharField(blank=True, max_length=255, null=True, verbose_name='Numero')),
                ('dir_piso_puerta', models.CharField(blank=True, max_length=255, null=True, verbose_name='Piso/Puerta')),
                ('cod_postal', models.CharField(blank=True, max_length=5, null=True)),
                ('web_blog', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
                'ordering': ['-created'],
            },
        ),
    ]