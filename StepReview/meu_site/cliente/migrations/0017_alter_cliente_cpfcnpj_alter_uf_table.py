# Generated by Django 4.0.1 on 2022-02-27 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0016_cliente_cidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpfcnpj',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterModelTable(
            name='uf',
            table='uf',
        ),
    ]
