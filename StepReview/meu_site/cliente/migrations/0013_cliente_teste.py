# Generated by Django 4.0.1 on 2022-02-20 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0012_alter_cliente_cidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='teste',
            field=models.CharField(default='', max_length=10),
        ),
    ]