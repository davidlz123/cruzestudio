# Generated by Django 2.1.3 on 2019-06-07 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gastos', '0001_initial'),
        ('pedidos', '0001_initial'),
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulopedido',
            name='cod_pedido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.Pedido'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulos.Categoria'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gastos.Proveedor'),
        ),
    ]