# Generated by Django 4.0.1 on 2022-02-06 17:36

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_remove_cliente_cidadenatal_cliente_cidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='', max_length=1),
            preserve_default=False,
        ),
    ]
