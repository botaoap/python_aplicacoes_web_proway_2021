# Generated by Django 4.0.1 on 2022-01-30 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_cidade_uf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
