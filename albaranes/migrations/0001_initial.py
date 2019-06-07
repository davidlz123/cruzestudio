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
            name='Albaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('cod_albaran', models.CharField(blank=True, max_length=30, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Albaran',
                'verbose_name_plural': 'Albaranes',
                'ordering': ['-created'],
            },
        ),
    ]