# Generated by Django 2.2 on 2020-04-25 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Catalogo', '0004_producto_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='Sin nombre', max_length=40)),
                ('ingresos', models.BigIntegerField()),
                ('direccion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('cedula_cliente', models.CharField(default='NA', max_length=12)),
                ('inicio', models.DateField(auto_now=True)),
                ('total', models.IntegerField(default=0)),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.Tienda')),
            ],
        ),
        migrations.CreateModel(
            name='Recordatorio',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(default='Sin nombre', max_length=40)),
                ('deuda', models.IntegerField(default=0)),
                ('venta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Tienda.Venta')),
            ],
        ),
        migrations.CreateModel(
            name='Producto_venta',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('cantidad', models.PositiveSmallIntegerField(default=0)),
                ('subtotal', models.IntegerField(default=0)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Catalogo.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Producto_inventario',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('cantidad', models.PositiveSmallIntegerField(default=0)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Catalogo.Producto')),
            ],
        ),
    ]