# Generated by Django 2.2 on 2020-04-25 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogo', '0003_remove_producto_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='nombre',
            field=models.CharField(default='Nombre', max_length=25),
        ),
    ]
