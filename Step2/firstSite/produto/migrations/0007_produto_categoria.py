# Generated by Django 4.0.1 on 2022-01-30 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0006_alter_categoria_nome_alter_categoria_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='produto.categoria'),
            preserve_default=False,
        ),
    ]
