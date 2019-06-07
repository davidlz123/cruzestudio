# Generated by Django 2.1.3 on 2019-06-07 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profesionales', '0001_initial'),
        ('pedidos', '0001_initial'),
        ('clientes', '0001_initial'),
        ('albaranes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='albaran',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
        ),
        migrations.AddField(
            model_name='albaran',
            name='pedido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.Pedido'),
        ),
        migrations.AddField(
            model_name='albaran',
            name='profesional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profesionales.Profesional'),
        ),
    ]
