# Generated by Django 4.0.1 on 2022-02-06 18:22

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0010_alter_cliente_carro_alter_cliente_estadocivil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estadoCivil',
            field=models.IntegerField(blank=True, choices=[(1, 'Solteiro(a)'), (2, 'Casado(a)'), (3, 'Divorcido(a)'), (4, 'Viuvo(a)'), (5, 'Desquitado(a)'), (6, 'União Estável')], default=1, null=True),
        ),
    ]
